---
type: infrastructure
project: Totus Cenografia IA
tags: [infra, totus]
---

# Infraestrutura

Mapa completo dos serviços em produção.

## Camadas

```
┌─────────────────────────────────────────────────────────┐
│  Cloudflare (DNS)                                       │
│  atendimento.totuscenografia.com.br → 76.13.166.51      │
└────────────────────────┬────────────────────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │                                 │
   ┌────▼─────┐                    ┌──────▼──────┐
   │ Vercel   │                    │ VPS Hostgr  │
   │ (Painel  │                    │ (Chatwoot)  │
   │  + API)  │                    │             │
   └────┬─────┘                    └──────┬──────┘
        │                                 │
        └──┬───────────────┬──────────────┘
           │               │
      ┌────▼────┐    ┌─────▼─────┐
      │ Neon    │    │ Upstash   │
      │ Postgres│    │ Redis     │
      └─────────┘    └───────────┘
           │
      ┌────▼──────────┐
      │ Anthropic API │
      │ Claude        │
      └───────────────┘
```

## 1. Vercel (Frontend + Backend API)

- **Frontend**: Next.js 14 + React 18 + Tailwind + Recharts + React Query + Sonner
- **Backend**: FastAPI Python serverless em `/api/index.py`
- **Build**: ~30s, bundle ~250MB (limite de função Vercel — substituímos SDK Anthropic por HTTP direto)
- **Deploy**: auto via push em `main` no GitHub
- **Crons**: `/api/cron/follow-up` rodando `0 13,18 * * 1-5`
- **17 env vars** configuradas (ver [[01 - Credenciais e Acessos]])

## 2. VPS Hostgr (Chatwoot)

**Localização**: Brasil — Campinas
**IP público**: `76.13.166.51`

### Dois Chatwoots no mesmo VPS

#### Concretize (Rodrigo) — `/opt/concretize/`
- Containers: `concretize-chatwoot-*`
- Domínio: provavelmente `aiagentconcretize.com.br`
- ⚠️ Status atual: `concretize-chatwoot-web-1` em loop de restart (avisar Rodrigo)
- **NÃO TOCAR**

#### Totus (este projeto) — `/opt/chatwoot-totus/`
- Containers: `totus-chatwoot-web` (3001), `totus-chatwoot-sidekiq`, `totus-chatwoot-redis` (6380), `totus-chatwoot-db` (5433)
- Domínio: `atendimento.totuscenografia.com.br`
- Postgres, Redis, storage_data isolados em volumes próprios
- Network Docker `totus-chatwoot_totus`

### Nginx vhosts

| Vhost | Arquivo | Aponta para |
|---|---|---|
| concretize | `/etc/nginx/sites-enabled/concretize` | Rodrigo (não mexer) |
| totus | `/etc/nginx/sites-enabled/totus` | `127.0.0.1:3001` |

### SSL Let's Encrypt

- `/etc/letsencrypt/live/atendimento.totuscenografia.com.br/fullchain.pem`
- Renovação automática (certbot timer)
- Válido até 2026-08-16

## 3. Neon PostgreSQL

- Region: `sa-east-1` (São Paulo)
- **Compartilhado**: 2 projetos no mesmo banco
  - `public.*` → ForYou Leads (não tocar)
  - `totus.*` → Este projeto

### Tabelas no schema `totus.*` (13)

```
ai_brain_drafts         1 linha   (rascunho atual da IA)
ai_brain_versions       1 linha   (v1 ativa)
ai_settings             1 linha   (config global)
analytics_events        0 linhas  (futuro)
conversations           5 linhas  (testes)
follow_ups              0 linhas  (fila aprovação)
leads                   4 linhas  (testes)
messages                16 linhas (histórico)
objections_log          0 linhas  (futuro)
products                9 linhas  (9 padrões Totus seed)
sessions                0 linhas  (auth)
users                   1 linha   (guilherme@totus.com)
whatsapp_instance       1 linha   (legado, status)
```

## 4. Upstash Redis

- Self-hosted serverless (compartilhado com Rodrigo)
- Prefixo de chaves: `totus:*` (isola do `concretize:*`)
- Padrões de chave:
  - `totus:msgs:{phone}` — fila batch
  - `totus:lock:{phone}` — lock por telefone (TTL 60s)
  - `totus:dedup:{messageId}` — dedup (TTL 60s)
  - `totus:rate:{phone}` — rate limit (TTL 60s, max 10/min)
  - `totus:outgoing:{hash}` — echo blocking (TTL 300s)

## 5. Cloudflare DNS

Zone `totuscenografia.com.br` (já existente antes do projeto):

| Tipo | Nome | Valor | Proxy |
|---|---|---|---|
| A | atendimento | 76.13.166.51 | ❌ off |
| A | (raiz) | 216.198.79.1 | (Lovable site) |
| CNAME | www | vercel-dns | (site Vercel) |
| MX | (raiz) | Google Workspace | — |
| TXT | _dmarc | DMARC config | — |
| TXT | _lovable | verificação Lovable | — |

> ⚠️ NÃO ligar proxy do `atendimento` (Cloudflare) — Let's Encrypt usa HTTP-01 challenge que precisa do IP direto.

## 6. Anthropic

- Modelo único: `claude-sonnet-4-6`
- Sem fallback configurado (futuro: Gemini ou OpenAI como fallback)
- ~5-10s por chamada
- Substituímos o SDK por HTTP direto (`api/_anthropic.py`) para reduzir bundle Vercel

## Custos mensais estimados

| Serviço | Custo |
|---|---|
| Vercel | $0 (free tier) |
| Neon | $0 (free, compartilhado) |
| Anthropic | pay-as-you-go (~$5-30/mês com uso moderado) |
| Upstash | $0 (compartilhado pago pelo Rodrigo) |
| Cloudflare | $0 |
| VPS Hostgr | já pago, anual |
| **Total** | **~$5-30/mês** |
