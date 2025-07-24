#!/bin/bash

touch /var/log/mail.log /var/log/mail.err

# Inicia syslog (Postfix e Dovecot usam)
service rsyslog start

# Inicia Postfix
service postfix start

# Inicia Dovecot
dovecot

# Mantém o container vivo com log visível
tail -F /var/log/mail.log