FROM ubuntu:latest

# Instalação do BIND9 e limpeza
RUN apt-get update -y && \
    apt-get install -y bind9 dnsutils && \
    rm -rf /var/lib/apt/lists/*

# Criação de diretórios e ajustes de permissão
RUN mkdir -p /var/cache/bind /run/named && \
    chown -R bind:bind /var/cache/bind /run/named

# Cópia dos arquivos de configuração
COPY ./bind9 /etc/bind/

# Ajuste de permissões
RUN chown -R bind:bind /etc/bind && \
    chmod 644 /etc/bind/named.conf.local \
              /etc/bind/db.asa.isp \
              /etc/bind/db.bacalhau.asa.isp \
              /etc/bind/db.piaba.asa.isp \
              /etc/bind/db.tilapia.asa.isp  # Nome corrigido

# Exposição de portas
EXPOSE 53/tcp
EXPOSE 53/udp

# Comando de inicialização
CMD ["/usr/sbin/named", "-g", "-c", "/etc/bind/named.conf", "-u", "bind"]