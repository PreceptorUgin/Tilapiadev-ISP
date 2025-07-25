# Projeto ISP-Infra

Infraestrutura de provedor de serviços de internet (ISP) usando microsserviços Docker.

## Descrição
Este projeto acadêmico, para a disciplina Administração de Sistemas Abertos (ASA), visa criar um ambiente completo de ISP com:

- **DNS** (Bind9)
- **Serviço de E-mail** (Postfix + Dovecot)
- **Proxy Reverso** (Apache)
- **Portal** estático (Nginx)
- **Webmail** (Roundcube)

O trabalho é organizado em 4 sprints ao longo de 8 semanas, seguindo Scrum e PMBoK.

## Estrutura do Repositório
```
ISP-Infra/
├── dns/                  # Configurações Bind9
├── mail/                 # Postfix e Dovecot
├── proxy/                # Apache Reverse Proxy
├── portal/               # Site estático do ISP
├── webmail/              # Interface Webmail
├── clients/              # Microsserviços dos clientes
├── docs/                 # Documentação por sprint e cronograma
├── .env.example                  # Variáveis de ambiente
└── docker-compose.yml    # Serviços do provedor
```

## Como Começar

1. **Pré-requisitos**
   - Docker >= 20.10
   - Docker Compose >= 1.29
   - Git
2. **Clone o repositório**
   ```bash
   git clone https://github.com/seu_usuario/ISP-Infra.git
   cd ISP-Infra
   ```
3. **Subir serviços básicos**
   ```bash
   docker-compose up -d dns mail proxy portal webmail
   ```
4. **Verificar logs**
   ```bash
   docker-compose logs -f
   ```

---
*Este README será atualizado conforme o projeto avança.*
