FROM ubuntu:latest

RUN apt update -y
RUN apt install bind9 dnsutils -y
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/cache/bind
RUN mkdir -p /run/named
RUN chown bind:bind /var/cache/bind
RUN chown bind:bind /run/named

COPY named.conf.local /etc/bind/
COPY db.asa.br /etc/bind/

RUN chown bind:bind /etc/bind/named.conf.local
RUN chown bind:bind /etc/bind/db.asa.br
RUN chmod 644 /etc/bind/named.conf.local
RUN chmod 644 /etc/bind/db.asa.br

EXPOSE 53/tcp
EXPOSE 53/udp

CMD ["/usr/sbin/named", "-g", "-c", "/etc/bind/named.conf", "-u", "bind"]