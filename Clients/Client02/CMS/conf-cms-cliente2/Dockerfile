FROM wordpress:php8.2-apache

# Instala utilitários
RUN apt-get update && \
    apt-get install -y less curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Baixa e desembrulha o core do WordPress durante o build
RUN curl -fsSL https://wordpress.org/latest.tar.gz -o /tmp/wordpress.tar.gz && \
    mkdir -p /var/www/html && \
    tar --strip-components=1 -xzf /tmp/wordpress.tar.gz -C /var/www/html && \
    rm /tmp/wordpress.tar.gz

# Instala WP-CLI
RUN curl -fsSL https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar -o /usr/local/bin/wp && \
    chmod +x /usr/local/bin/wp

# Copia configuração da rede multisite
COPY ./wp-conf/wp-config.php /var/www/html/wp-config.php
COPY ./wp-conf/.htaccess /var/www/html/.htaccess

# Copia entrypoint
COPY ./wp-conf/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Suprime aviso de FQDN
RUN echo "ServerName bacalhau.asa.isp" >> /etc/apache2/apache2.conf

# Garantir permissões
RUN chown -R www-data:www-data /var/www/html

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["apache2-foreground"]
