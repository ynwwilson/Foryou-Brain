---
project: Totus Cenografia IA
date: 2026-05-18
status: production-ready (sem WhatsApp plugado ainda)
owner: Guilherme
tags: [totus, ia-atendimento, chatwoot, vercel, neon]
---

# Totus Cenografia IA — Overview

Sistema de IA de atendimento WhatsApp para a **Totus Cenografia** (Guilherme), inspirado na arquitetura do Rodrigo (Concretize). Stack moderna, infraestrutura própria, painel administrativo completo + CRM integrado.

## Resumo executivo

- **9 fases entregues** (A–G), do MVP inicial à plataforma com Chatwoot + BATCH_WINDOW
- **Sistema no ar** mas **WhatsApp não plugado** ainda (decisão do Guilherme — usar Meta API depois)
- IA é Claude Sonnet 4.6 com 37 seções de persona (Manual Mestre da Totus)
- Inbox unificado em Chatwoot self-hosted no domínio próprio

## URLs principais

| Recurso | URL |
|---|---|
| Painel administrativo | https://totus-cenografia-ia.vercel.app |
| Chatwoot CRM | https://atendimento.totuscenografia.com.br |
| API health | https://totus-cenografia-ia.vercel.app/api/health/full |
| GitHub | https://github.com/ynwwilson/totus-cenografia-ia |
| Vercel project | https://vercel.com/yngomesmarco-hues-projects/totus-cenografia-ia |

## Arquitetura em 1 linha

```
WhatsApp → Webhook → BATCH_WINDOW 10s (Upstash) → Claude → Guardrails → Neon + Chatwoot
```

## Diferenciais vs MVP

Comparado à proposta inicial:
- ✅ Auth JWT (era painel aberto)
- ✅ Lead memory estruturada (era JSONB genérico)
- ✅ Catálogo de produtos com CRUD + mídia
- ✅ Fila de aprovações funcional (era placeholder)
- ✅ Versionamento da IA com rollback
- ✅ Toggle global + por conversa + business hours
- ✅ Real-time UX (polling 4s + toasts)
- ✅ Recharts no dashboard com KPIs comparativos
- ✅ Lead profile com 4 tabs (memória/conversas/objeções/follow-ups)
- ✅ Health checks reais (Neon/Anthropic/Redis/Chatwoot)
- ✅ Meta API stub pronto + Evolution fallback
- ✅ **Chatwoot self-hosted próprio** (https://atendimento.totuscenografia.com.br)
- ✅ **Upstash Redis** com BATCH_WINDOW 10s, locks, deduplicação, rate limit
- ✅ **Guardrails de aparência humana** (zero emojis, sem clichês, fatiamento)
- ✅ **Cron follow-up 48h** → fila de aprovação

## Navegação nesta pasta

- [[01 - Credenciais e Acessos]] — TODOS logins, senhas, tokens
- [[02 - Infraestrutura]] — VPS, Vercel, Neon, Cloudflare, Upstash
- [[03 - Arquitetura]] — diagramas e fluxo completo
- [[04 - Backend API]] — endpoints, arquivos Python
- [[05 - Frontend Painel]] — páginas Next.js
- [[06 - Chatwoot Self-hosted]] — como acessar e manter
- [[07 - Comandos e Scripts]] — deploy, migrations, debug, SSH
- [[08 - Pendências e Próximos Passos]] — bugs conhecidos, WhatsApp pendente

## Referência cruzada

- [[IA de Atendimento Rodrigo]] — projeto base de referência (Concretize)
- [[ForYou Code]] — empresa

## Atualizacao 2026-05-22

- Fonte correta do codigo: `C:\Users\ynwwi\Projects\totus-cenografia-ia`.
- Repo legado `C:\Users\ynwwi\Projects\totus-ai-concierge` nao deve ser usado como fonte de verdade.
- Producao verificada: painel Vercel HTTP 200, Chatwoot HTTP 200, `/api/health/full` com `status: ok`.
- Health em 2026-05-22: Neon ok, Anthropic ok, Redis ok, Chatwoot ok, Meta WhatsApp `meta_configured=false`, Evolution `evolution_configured=true`, OpenAI `not_configured`.
- Estado real: plataforma pronta/online, mas WhatsApp Meta ainda nao plugado para conversa real.
- Nota de retomada completa: [[09 - Retomada 2026-05-22 - Status completo e memoria]].
- Alerta de seguranca: antes de entregar/compartilhar, rotacionar senhas/tokens e remover token embutido do Git remote local.
