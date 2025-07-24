FROM php:8.2-apache

# Instalação de dependências e extensões PHP
RUN apt-get update && apt-get install -y \
    unzip wget libpng-dev libjpeg62-turbo-dev libfreetype6-dev libicu-dev libonig-dev libxml2-dev \
 && docker-php-ext-configure gd --with-freetype --with-jpeg \
 && docker-php-ext-install pdo pdo_mysql intl mbstring xml gd \
 && rm -rf /var/lib/apt/lists/*

# Definindo diretório de trabalho
WORKDIR /var/www/html

# Versão do Roundcube
ENV ROUNDCUBE_VERSION=1.6.6

# Baixar, extrair e limpar Roundcube
RUN wget https://github.com/roundcube/roundcubemail/releases/download/${ROUNDCUBE_VERSION}/roundcubemail-${ROUNDCUBE_VERSION}-complete.tar.gz \
 && tar xzf roundcubemail-${ROUNDCUBE_VERSION}-complete.tar.gz --strip-components=1 \
 && rm roundcubemail-${ROUNDCUBE_VERSION}-complete.tar.gz

# Criar diretórios necessários e ajustar permissões
RUN mkdir -p temp logs \
 && chown -R www-data:www-data temp logs

# Configurar ServerName para evitar warning Apache
RUN echo "ServerName webmail.asa.isp" >> /etc/apache2/apache2.conf

# Copiar arquivo de configuração customizado do Roundcube
RUN rm -rf /var/www/html/config/config.inc.php
RUN mkdir -p /var/www/html/config
COPY ./config/config.inc.php /var/www/html/config/

# Expor porta 80 para HTTP
EXPOSE 80