---
type: credentials
project: Totus Cenografia IA
sensitive: true
tags: [credentials, totus]
---

# Credenciais & Acessos

> ⚠️ **Arquivo sensível.** Não compartilhar fora do vault.

## 1. Painel administrativo Totus

| Campo | Valor |
|---|---|
| URL | https://totus-cenografia-ia.vercel.app |
| Email | guilherme@totus.com |
| Senha | `Totus@2026!` |
| Auth backend | JWT (gerado pelo `/api/auth/login`) |

> Nota: este é o login do PAINEL TOTUS. Diferente do Chatwoot (abaixo).

## 2. Chatwoot CRM

| Campo | Valor |
|---|---|
| URL | https://atendimento.totuscenografia.com.br |
| Email | guilherme@totuscenografia.com.br |
| Senha | `Totus@Cenografia#2026!` |
| Account ID | 1 |
| Inbox ID | 1 (nome: "Totus IA", channel API) |
| User API Token | `pWGdmnFhVrZJCfa914FXFxLm` |
| Tipo | Self-hosted Docker no VPS Hostgr |
| Versão | chatwoot/chatwoot:latest |

> ⚠️ Existe uma segunda conta `guilhermepcamargo@gmail.com` que foi criada acidentalmente. Ver [[08 - Pendências e Próximos Passos]].

## 3. VPS Hostgr (Brasil/Campinas)

| Campo | Valor |
|---|---|
| IP | `76.13.166.51` |
| SSH | `ssh root@76.13.166.51` |
| Senha root | `REy9LxN7fajG7.JK&t8B` |
| Sistema | Ubuntu 22.04 LTS |
| Specs | KVM 2 — 2 CPU, 8GB RAM, 100GB disco |
| Hostname | srv1554152.hstgr.cloud |
| Validade plano | 2026-06-18 |

> ⚠️ Este VPS também roda o **Chatwoot do Rodrigo (Concretize)** em `/opt/concretize/`. **Não tocar nesses containers/configs.**

## 4. Vercel

| Campo | Valor |
|---|---|
| Conta | yngomesmarco-hue@... (team `yngomesmarco-hues-projects`) |
| Token | `[REDACTED-VERCEL]` |
| Team ID | `team_uZU2DYDtmcTe4QYFnquE3EqJ` |
| Project ID | `prj_1uOKfMMIOdCcjePb4PMgGWHAbnLZ` |
| Project URL | https://vercel.com/yngomesmarco-hues-projects/totus-cenografia-ia |

## 5. GitHub

| Campo | Valor |
|---|---|
| User | ynwwilson |
| Repo | https://github.com/ynwwilson/totus-cenografia-ia |
| Visibilidade | Privado |
| PAT | `[REDACTED-GITHUB]` |
| Repo ID | 1242536912 |
| Branch produção | main (auto-deploy Vercel) |

## 6. Neon PostgreSQL

| Campo | Valor |
|---|---|
| Connection string | `postgresql://neondb_owner:npg_jQC7Ylp5iZdz@ep-shiny-cell-ac9qba4n-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require` |
| User | neondb_owner |
| Password | `npg_jQC7Ylp5iZdz` |
| Host | ep-shiny-cell-ac9qba4n-pooler.sa-east-1.aws.neon.tech |
| Database | neondb |
| Schema Totus | `totus.*` (isolado de outros projetos) |
| Console | https://console.neon.tech |

> ⚠️ Este Neon é COMPARTILHADO com o projeto **ForYou Leads** (schema `public.*`). Schema `totus.*` é nosso.

## 7. Anthropic API

| Campo | Valor |
|---|---|
| API Key | `[REDACTED-ANTHROPIC]` |
| Modelo usado | `claude-sonnet-4-6` |
| Console | https://console.anthropic.com |

## 8. Upstash Redis (compartilhado com Rodrigo)

| Campo | Valor |
|---|---|
| REST URL | `https://precious-flea-91141.upstash.io` |
| REST Token | `gQAAAAAAAWQFAAIncDIwZDM2Zjc3OGI4Mjg0NGIwOTExMmE4NmJjNjcwMzAwYnAyOTExNDE` |
| Prefixo das keys Totus | `totus:` |
| Console | https://console.upstash.com |

> ⚠️ Esse Redis também é usado pelo Rodrigo (Concretize) com prefixo `concretize:`. Compartilhado, sem custo extra.

## 9. Cloudflare

| Campo | Valor |
|---|---|
| API Token | `[REDACTED-CLOUDFLARE]` |
| Zone Totus | `totuscenografia.com.br` |
| Zone ID | `17c89f9ee2f60ba8779fb7ecb8fa8c92` |
| Account ID | `64f87e0d24c915cc2dbd50376712a030` |
| DNS atendimento | A record `atendimento` → `76.13.166.51` (proxy OFF, TTL auto) |

## 10. CRON_SECRET

| Campo | Valor |
|---|---|
| Secret | `ab206e0d72339e2e575b...` (64 chars hex - completo está no Vercel env vars) |
| Endpoint | `POST /api/cron/follow-up` |
| Header | `Authorization: Bearer ${CRON_SECRET}` |
| Schedule | `0 13,18 * * 1-5` (13h e 18h, seg-sex) |

## 11. JWT do Painel

| Campo | Valor |
|---|---|
| Secret | (configurado no Vercel como `JWT_SECRET`, 96 chars hex) |
| Algoritmo | HS256 |
| Validade | 7 dias |
| Storage cliente | `localStorage.totus_token` |

## 12. Secrets do Chatwoot (Postgres/Redis internos do container)

Salvos em `/opt/chatwoot-totus/.env` no VPS:

| Var | Valor |
|---|---|
| POSTGRES_PASSWORD | `1GOGU2p4exvrdsZIasI5nsaAN5pL7REs` |
| REDIS_PASSWORD | `qn8n8WCCXU2ccVhSUxwRdQ` |
| SECRET_KEY_BASE | `8c3fef5dd2a0be467718e5186620d5779072b3b447d00992e6bda1dcb2a1dec0fc3a3e90904a3f7e39d09bb9b22c48e1641ca2ff007deaed943d40d59d9cf3a6` |

## 13. Domínios

- `totuscenografia.com.br` — site institucional (Lovable, IP `216.198.79.1`)
- `www.totuscenografia.com.br` — Vercel
- `atendimento.totuscenografia.com.br` — Chatwoot self-hosted (este projeto)
- Email Google Workspace ativo
