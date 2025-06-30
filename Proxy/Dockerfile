FROM httpd:latest

RUN chown -R daemon:daemon /usr/local/apache2/logs

COPY httpd-proxy.conf /usr/local/apache2/conf/httpd.conf

EXPOSE 80