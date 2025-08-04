# 📝 Ata da Reunião - Sprint 2

**Data da Reunião:** 2025-07-14
**Sprint:** 2 – Infraestrutura do Cliente 1
**Participantes:**

* Júlio
* Heyson
* Magno (Lider da Sprint)

---

## 🎯 Objetivos da Sprint 2

* Criar a infraestrutura isolada para o Cliente 1
* Configurar rede Docker separada e proxy
* Garantir isolamento, segurança e criptografia para Cliente 1
* Registrar artefatos de gerenciamento (planejamento e ata)

---

## 📌 Tarefas Definidas

| Tarefa                                                              | Responsável | Status       |
| ------------------------------------------------------------------- | ----------- | ------------ |
| Definir e criar rede Docker para Cliente 1 (`cliente1_network`)     | Heyson      | Conluído     |
| Configurar zona DNS para Cliente 1 no Bind9 do provedor             | Júlio       | Concluído    |
| Criar serviço de e-mail (Postfix/Dovecot) para Cliente 1            | Júlio       | Concluído    |
| Configurar proxy reverso (Nginx) no container do cliente            | Júlio       | Concluído    |
| Desenvolver portal estático do Cliente 1 (`/portal`)                | Heyson      | Concluído    |
| Criar hotsite estático do Cliente 1 (`/hotsite`)                    | Magno       | Concluído    |
| Integrar serviço de assinatura (Sign) na rede Cliente 1             | Heyson      | Concluído    |
| Escrever planejamento da sprint e atas de reunião                   | Magno       | Concluído    |

---

## 🔄 Discussões e Decisões

* A rede isolada `cliente1_net` garante que containers de Cliente 1 não vejam outros clientes
* O DNS do provedor (`172.25.0.2`) será usado pelos containers do Cliente 1
* Será usado Nginx como proxy reverso no Cliente 1, roteando `/portal`, `/hotsite` e `/sign`
* E-mails do Cliente 1 terão certificados TLS (STARTTLS) configurados no Postfix/Dovecot

---

## 🚧 Bloqueios e Riscos

* Definição das variáveis de ambiente e credenciais para o serviço de assinatura
* Integração do Zone file do Cliente 1 no Bind9 do provedor sem impactar zona principal
* Obtenção e aplicação de certificados SSL (autoassinado temporário na Sprint 2)

---

## 📆 Prazos

* Início da Sprint: 07/07/2025
* Fim da Sprint: 21/07/2025
* Próxima reunião de checkpoint: 21/07/2025

---

**Observação Final:** A Sprint 2 concentra-se em dar ao Cliente 1 sua infraestrutura completa e isolada, preparando terreno para replicação nas sprints seguintes.
