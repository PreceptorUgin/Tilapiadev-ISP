# Projeto ISP-Infra

Infraestrutura de provedor de serviços de internet (ISP) usando microsserviços Docker.

## Descrição
Este projeto acadêmico, para a disciplina Administração de Sistemas Abertos (ASA), visa criar um ambiente completo de ISP com:

- **DNS** (Bind9)
- **Serviço de E-mail** (Postfix + Dovecot)
- **Proxy Reverso** (Apache)
- **Portal** estático (Nginx)
- **Webmail** (Roundcube)

Além dos serviços para os clientes com:
-- Cliente 1:

- **Hotsite**
- **Portal**
- **Proxy Reverso Secundário** (Nginx)
- **Sign-in**

-- Cliente 2 & 3:

- **CMS** (Wordpress)
- **Portal**
- **Proxy** (Nginx)

O trabalho é organizado em 4 sprints ao longo de 8 semanas, seguindo Scrum e PMBoK.

## Estrutura do Repositório
```
ISP-Infra/
├── Clients/              # Microsserviços de clientes
│   ├── Client01/
│   │   ├── Hotsite/
│   │   ├── Portal/
│   │   ├── Proxy/
│   │   └── Sign/
│   ├── Client02/
│   │   ├── CMS/ 
│   │   ├── Portal/
│   │   └── Proxy/
│   └── Client03/
│       ├── CMS/
│       ├── Portal/
│       └── Proxy/
├── DNS/                  # Servidor DNS (Bind9)
├── mail/                 # Servidor de e-mail (Postfix + Dovecot)
├── proxy/                # Apache Reverse Proxy principal
├── portal/               # Portal principal do ISP
├── webmail/              # Roundcube
├── compose.yaml          # Orquestração principal
└── script.py             # Utilitários e automação
```

## Como Começar

1. **Pré-requisitos**
   - Docker >= 20.10
   - Docker Compose >= 1.29
   - Git
   - Python3
2. **Clone o repositório**
   ```bash
   git clone https://github.com/PreceptorUgin/Tilapiadev-ISP
   cd Tilapiadev-ISP
   ```
3. **Subir serviços**
   ```bash
   chmod +x ./script.py
   python3 ./script.py
   ```
   ```powershell
   python script.py
   ```
Em caso de erro entre em contato em:
[juliocaynaaguiar@gmail.com](mailto:juliocaynaaguiar@gmail.com)

---
*Este README será atualizado conforme o projeto avança.*
