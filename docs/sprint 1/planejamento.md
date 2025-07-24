# 📌 Planejamento da Sprint 1

**Sprint:** 1 - Infraestrutura do Provedor
**Período:** 30/06/2025 a 07/07/2025

---

## 🎯 Objetivo Geral

Implementar toda a infraestrutura base do provedor, incluindo os serviços principais (DNS, e-mail, proxy reverso, portal e webmail), além da organização do projeto e documentação inicial.

---

## ✅ Metas da Sprint 1

### 📁 Organização do Projeto

* Criar o repositório no GitHub
* Definir estrutura de diretórios por serviço e por sprint
* Criar quadro Kanban e labels no GitHub Projects
* Criar branches: `dev`, `DNS`, `Email`, `Proxy`, `Portal`, `Webmail`
* Atualizar o `README.md` com estrutura e instruções iniciais

### 🧠 Artefatos de Gerenciamento

* `docs/cronograma.md`: Visão geral das 4 sprints
* `docs/sprint1/planejamento.md`: Este planejamento
* `docs/sprint1/ata.md`: Ata da reunião inicial

### 🌐 DNS (Bind9)

* Criar arquivos:

  * `named.conf`
  * `named.conf.options`
  * `named.conf.local`
  * Zonas direta e reversa (`db.isp.local`, `db.0.168.192.in-addr.arpa`)
* Configurar Bind9 em container Docker
* Validar resolução de nomes via `dig` e `ping`

### 📬 E-mail (Postfix + Dovecot)

* Estruturar diretórios `mail/postfix/` e `mail/dovecot/`
* Criar `main.cf` (Postfix) e `dovecot.conf`
* Adicionar usuários locais e testes de envio/recebimento
* Configurar SMTP/IMAP em `docker-compose.yml`

### 🔁 Proxy Reverso (Apache)

* Criar estrutura `proxy/apache/`
* Adicionar VirtualHosts para `portal.isp.local` e `webmail.isp.local`
* Configurar redirecionamento HTTP sem SSL
* Testes de acesso aos serviços

### 🖥️ Portal estático

* Criar pasta `portal/` com página HTML básica
* Servir o portal pelo Apache ou container dedicado

### 📬 Webmail (Roundcube/RainLoop)

* Escolher ferramenta e configurar container básico
* Conectar com serviço de e-mail do provedor

### ⚙️ Integração e Validação

* Adicionar todos os serviços no `docker-compose.yml`
* Subir ambiente com `docker-compose up -d`
* Validar funcionamento integrado dos serviços

---

## 👥 Responsabilidades

| Nome   | Tarefa Principal                      |
| ------ | ------------------------------------- |
| Indefinido | Repositório, DNS e documentação geral |
| Indefinido | E-mail e Webmail                      |
| Indefinido | Proxy reverso e Portal estático       |

---

## 🧱 Entregas Esperadas

* Infraestrutura completa do provedor ISP funcional
* DNS, E-mail, Proxy, Portal e Webmail integrados
* Repositório com estrutura e documentação atualizada
* Artefatos de gerenciamento concluídos

---

## 📎 Referências

* Documentação oficial do Bind9, Postfix, Dovecot, Apache
* PDF do enunciado (Projeto ASA)

---

**Observação:** Esta sprint define a fundação técnica e organizacional de todo o projeto. Tudo precisa estar estável para permitir o avanço dos clientes nas próximas sprints.
