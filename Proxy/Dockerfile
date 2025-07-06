FROM alpine:latest

RUN apk update && apk add apache2

RUN apk update && apk add --no-cache \
    apache2 \
    apache2-utils \
    apache2-proxy

RUN mkdir -p /run/apache2

COPY reverse-proxy.conf /etc/apache2/conf.d/reverse-proxy.conf
COPY index.html /var/www/localhost/htdocs/index.html
COPY style.css /var/www/localhost/htdocs/style.css
COPY peixao.jpg /var/www/localhost/htdocs/peixao.jpg
COPY world.webp /var/www/localhost/htdocs/world.webp

EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]