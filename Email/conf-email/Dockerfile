FROM ubuntu:latest

RUN apt update -y
RUN apt upgrade -y

RUN apt install postfix dovecot-imapd dovecot-pop3d telnet -y

# Copia configs do Postfix
COPY ./postfix/main.cf /etc/postfix/main.cf
COPY ./postfix/master.cf /etc/postfix/master.cf

# Copia o nome de dominio do postfix
COPY ./postfix/mailname /etc/mailname

# Copia configs do Dovecot
COPY ./dovecot/* /etc/dovecot/conf.d

# Copia o entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Cria usuário local
RUN useradd -m testuser
RUN echo "testuser:testpass" | chpasswd

RUN useradd -m tinybox
RUN echo "tinybox:tinypass" | chpasswd

EXPOSE 25/tcp 143/tcp

CMD ["/entrypoint.sh"]