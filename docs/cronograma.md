# 📅 Cronograma do Projeto ISP-Infra

Este documento apresenta a divisão detalhada do projeto em 4 sprints ao longo de 8 semanas, conforme metodologia Scrum.

---

## 🟩 Sprint 1 – Infraestrutura do Provedor (Semana 1 e 2)

**Objetivo:** Montar a base de serviços do ISP e estruturar a gestão do projeto.

**Entregas:**

* **Gerencial:**

  * Quadro Kanban único com labels por sprint
  * Ata da reunião inicial (`docs/sprint1/ata.md`)
  * Planejamento da Sprint 1 (`docs/sprint1/planejamento.md`)
  * `docs/cronograma.md` atualizado
* **DNS:**

  * `named.conf`, `named.conf.options`, `named.conf.local`
  * Zona direta `db.isp.local` e reversa `db.0.168.192.in-addr.arpa`
  * Container Bind9 em `docker-compose.yml`
  * Testes com `dig` e `ping` entre containers
* **E-mail:**

  * Estrutura de diretórios `mail/postfix/` e `mail/dovecot/`
  * Configs básicas de Postfix e Dovecot
  * Dockerfile e `docker-compose.yml` para SMTP/IMAP
  * Teste de envio/recebimento local
* **Proxy Reverso (Apache):**

  * Estrutura `proxy/apache/` e VirtualHosts iniciais
  * `docker-compose.yml` para Apache Reverse Proxy sem SSL
  * Teste de redirecionamento HTTP
* **Portal & Webmail:**

  * `portal/` estático servido por Apache
  * Container Webmail básico (Roundcube/RainLoop)
  * Testes de acesso local

---

## 🟨 Sprint 2 – Cliente 1 (Semana 3 e 4)

**Objetivo:** Implantar e validar a infraestrutura isolada do Cliente 1.

**Entregas:**

* **Rede e DNS:**

  * Rede Docker `cliente1_net`
  * Zona `cliente1.isp.local` (direta e reversa)
* **E-mail Cliente 1:**

  * Configuração de Postfix/Dovecot em `mail/cliente1/`
  * `docker-compose.yml` e testes de mail externo
* **Proxy & Portal Cliente 1:**

  * VirtualHosts Apache para portal.cliente1.isp.local e webmail.cliente1.isp.local
  * Containers de proxy e portal via `docker-compose.yml`
  * Testes de acesso HTTP/HTTPS básico
* **Documentação:**

  * `docs/sprint2/planejamento.md`
  * `docs/sprint2/ata.md`
  * Atualização do README com instruções do Cliente 1

---

## 🟧 Sprint 3 – Clientes 2 e 3 + SSL (Semana 5 e 6)

**Objetivo:** Replicar serviços para Clientes 2 e 3 e habilitar SSL/TLS.

**Entregas:**

* **Rede e DNS:**

  * Redes `cliente2_net`, `cliente3_net`
  * Zonas `cliente2.isp.local`, `cliente3.isp.local`
* **E-mail Clientes 2/3:**

  * Configuração de Postfix/Dovecot em `mail/cliente2/` e `mail/cliente3/`
  * Testes de mail entre clientes
* **Proxy & Portais:**

  * VirtualHosts Apache com SSL para todos domínios
  * Containers configurados com Let’s Encrypt (staging)
  * Testes de HTTPS e redirecionamento
* **Automação SSL:**

  * Certbot container e renovação automática
* **Documentação:**

  * `docs/sprint3/planejamento.md`
  * `docs/sprint3/ata.md`
  * Relatório técnico parcial (métricas de HTTPS)

---

## 🟥 Sprint 4 – Testes, Documentação e Apresentação Final (Semana 7 e 8)

**Objetivo:** Validar, automatizar e apresentar todo o ambiente do provedor e clientes.

**Entregas:**

* **Testes automatizados:**

  * Scripts para DNS, e-mail e proxy (GitHub Actions)
* **Métricas e relatórios:**

  * Latência DNS, disponibilidade de serviços
  * Relatório final com gráficos e conclusões
* **Manual de implantação:**

  * Vídeo passo a passo (deploy completo)
* **CI/CD:**

  * Documentação do pipeline de testes e deploy
* **Apresentação final:**

  * Slides com overview, desafios, demo
  * Agendamento de demo ao vivo

---

> **Observação:** Em todas as sprints mantenha planejamento, ata de reunião e registro de tarefas no Kanban.
