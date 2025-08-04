#!/bin/bash
set -euo pipefail

# DEBUG=1 ativa trace dos comandos para diagnóstico
[ "${DEBUG:-0}" != "0" ] && set -x

# ---------- Validações iniciais ----------
: "${WORDPRESS_DB_HOST:?WORDPRESS_DB_HOST não definido}"
: "${WORDPRESS_DB_USER:?WORDPRESS_DB_USER não definido}"
: "${WORDPRESS_DB_PASSWORD:?WORDPRESS_DB_PASSWORD não definido}"
: "${WORDPRESS_DB_NAME:?WORDPRESS_DB_NAME não definido}"

# ---------- Configuráveis via ambiente ----------
BASE_DOMAIN="${WORDPRESS_BASE_DOMAIN:-wp.bacalhau.asa.isp}"
ADMIN_USER="${WORDPRESS_ADMIN_USER:-admin}"
ADMIN_PASS="${WORDPRESS_ADMIN_PASSWORD:-admin123}"
ADMIN_EMAIL="${WORDPRESS_ADMIN_EMAIL:-admin@${BASE_DOMAIN}}"
SITE_TITLE="${WORDPRESS_SITE_TITLE:-Rede Bacalhau}"
WP_PATH="/var/www/html"

# ---------- WP-CLI com memória aumentada ----------
WP_CLI=(php -d memory_limit=512M /usr/local/bin/wp --path="${WP_PATH}" --allow-root)

echo "Esperando MariaDB em ${WORDPRESS_DB_HOST}..."

# ---------- Função de checagem de banco via PHP ----------
check_db() {
  php -r '
    $hostEnv = getenv("WORDPRESS_DB_HOST");
    $parts = explode(":", $hostEnv);
    $host = $parts[0];
    $port = $parts[1] ?? 3306;
    $mysqli = @new mysqli($host, getenv("WORDPRESS_DB_USER"), getenv("WORDPRESS_DB_PASSWORD"), getenv("WORDPRESS_DB_NAME"), $port);
    if ($mysqli->connect_errno) exit(1);
    exit(0);
  '
}

until check_db; do
  echo "Ainda não disponível, aguardando..."
  sleep 2
done

echo "Banco disponível."

# ---------- Permissões e preparação ----------
chown -R www-data:www-data "${WP_PATH}"
cd "${WP_PATH}"

# ---------- Garante que o core do WordPress existe ----------
if [ ! -f "${WP_PATH}/wp-load.php" ]; then
  echo "WordPress core ausente. Fazendo download..."
  "${WP_CLI[@]}" core download
fi

# ---------- Garante wp-config.php (opcional: cria se não existir) ----------
if [ ! -f wp-config.php ]; then
  echo "Gerando wp-config.php a partir das variáveis de ambiente..."
  "${WP_CLI[@]}" config create \
    --dbname="${WORDPRESS_DB_NAME}" \
    --dbuser="${WORDPRESS_DB_USER}" \
    --dbpass="${WORDPRESS_DB_PASSWORD}" \
    --dbhost="${WORDPRESS_DB_HOST}" \
    --skip-check
  # Note: você pode injetar salts dinamicamente se quiser
fi

# ---------- Instalação e ativação da rede multisite ----------
if ! "${WP_CLI[@]}" core is-installed --url="${BASE_DOMAIN}" >/dev/null 2>&1; then
  echo "Instalando WordPress base em ${BASE_DOMAIN}..."
  "${WP_CLI[@]}" core install \
    --url="${BASE_DOMAIN}" \
    --title="${SITE_TITLE}" \
    --admin_user="${ADMIN_USER}" \
    --admin_password="${ADMIN_PASS}" \
    --admin_email="${ADMIN_EMAIL}" \
    --skip-email

  echo "Ativando Multisite com subdomínios..."
  "${WP_CLI[@]}" core multisite-install \
    --url="${BASE_DOMAIN}" \
    --title="${SITE_TITLE}" \
    --admin_user="${ADMIN_USER}" \
    --admin_password="${ADMIN_PASS}" \
    --admin_email="${ADMIN_EMAIL}" \
    --subdomains \
    --skip-email
else
  echo "WordPress já instalado."
  # opcional: verificar se Multisite está ativo
fi

# ---------- Delegar ao entrypoint original para subir o Apache ----------
exec docker-entrypoint.sh "$@"
