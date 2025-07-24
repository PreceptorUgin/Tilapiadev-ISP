# 📝 Ata da Reunião - Sprint 1

**Data da Reunião:** 2025-06-30
**Sprint:** 1 - Infraestrutura do Provedor
**Participantes:**

* Júlio (Líder da Sprint)
* Heyson
* Magno

---

## 🎯 Objetivos da Sprint 1

* Estabelecer toda a infraestrutura do provedor ISP
* Organizar o repositório e os diretórios por microserviço
* Configurar os serviços DNS, E-mail, Proxy Reverso, Portal e Webmail
* Criar artefatos de gerenciamento (planejamento, ata, cronograma)
* Integrar os serviços em um ambiente Docker único

---

## 📌 Tarefas Definidas

| Tarefa                                           | Responsável | Status       |
| ------------------------------------------------ | ----------- | ------------ |
| Criar estrutura de repositório                   | Heyson      | Concluído    |
| Configurar servidor DNS (Bind9)                  | Heyson      | Concluído    |
| Estruturar serviço de e-mail (Postfix + Dovecot) | Júlio      | Não inciada  |
| Configurar proxy reverso (Apache)                | Magno      | Não iniciada |
| Criar página do portal                           | Heyson      | Não iniciada |
| Configurar webmail (Roundcube/RainLoop)          | Júlio     | Não iniciada |
| Escrever planejamento e ata da sprint            | Heyson      | Concluído    |
| Atualizar README e cronograma                    | Heyson      | Concluído    |

---

## 🔄 Discussões e Decisões

* Cada serviço será desenvolvido em uma branch separada (DNS, Email, Proxy, etc.)
* Será usada uma única rede Docker externa chamada `isp_net`
* As labels das issues representarão as sprints
* O projeto seguirá integração contínua na branch `dev` e entrega final na `main`

---

## 🚧 Bloqueios e Riscos

* Definição final do cliente webmail ainda em avaliação (Roundcube ou RainLoop)
* Tempo estimado para integração de todos os containers pode variar dependendo dos testes

---

## 📆 Prazos

* Início da Sprint: 30/06/2025
* Fim da Sprint: 07/07/2025
* Próxima reunião de checkpoint: 07/07/2025

---

**Observação Final:** A Sprint 1 tem caráter estrutural. A conclusão total da infraestrutura do provedor é essencial para o sucesso das sprints seguintes (clientes 1, 2 e 3).
