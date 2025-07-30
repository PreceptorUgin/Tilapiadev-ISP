FROM wordpress:php8.2-apache

# Copia configurações personalizadas para dentro do container
COPY ./wp-conf/wp-config.php /var/www/html/wp-config.php
COPY ./wp-conf/.htaccess /var/www/html/.htaccess

# Corrige permissões
RUN chown -R www-data:www-data /var/www/html
