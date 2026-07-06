---
data: 2026-05-29
tipo: implementação
projeto: ForYou Leads — Envio automático + Ads Manager (sem terminal)
status: ENTREGUE — PR #5 mergeado, em produção
---

# 2026-05-29 — ForYou Leads: envio automático + worker sempre-on

> Mata a dependência de rodar o worker no terminal e torna o envio automático (modelo Gerenciador de Anúncios). 6 commits na branch `feat/auto-dispatch` → **PR #5**. Build + typecheck limpos, migration 023 aplicada em prod.

## Dor que resolveu
Wilson tinha que abrir o terminal e rodar `node scripts/worker-adspower.mjs` pra qualquer envio funcionar. E o app era confuso (ativar, enviar, buscar lead). Pediu controle absoluto num app simples/minimalista, **sem textos de instrução**.

## Decisões (travadas com o Wilson)
- DM de IG não tem API → worker continua local, mas vira **serviço pm2 sempre-on** (sobe no boot). Captura (Apify) já era automática na nuvem.
- **Envio automático**: toggle ativa/pausada que não some com métricas; envia dentro da janela + teto + intervalo. Sem botão manual.
- Checkbox **"reativar amanhã no mesmo horário"** — senão roda só hoje.
- Criação de campanha com controle absoluto (nicho, hashtags, **faixa de seguidores**, oferta, vídeo, templates, ritmo).
- **Templates por oferta**: 3 variações; a IA personaliza por lead; editar manual ou "aprimorar com IA".
- Multi-canal (WhatsApp/Reddit/freelas) = **fora de escopo**, fase futura.

## O que foi feito
- **Migration 023**: campaigns (follower_count_min/max, auto_repeat_daily, active_date), users.worker_last_seen_at, offers.templates (+ backfill 3 templates de site).
- **Fase 1 — worker sempre-on**: `ecosystem.config.cjs`, `npm run worker:install` (pm2 + boot), heartbeat `/api/worker/ping`, pill online/offline (`worker-status.tsx`) na sidebar.
- **Fase 2 — auto-dispatch**: `lib/dispatch.ts` cria lote por campanha ativa (janela+teto+intervalo); poll do worker dispara quando ocioso. Toggle seta `active_date`. Removido envio manual + `/enviar`.
- **Fase 3 — templates**: `lib/claude.ts` modo-templates (personaliza o template hash-selecionado), `improveTemplate` + `/api/offers/improve-template`, UI de 3 templates + "aprimorar com IA" em Ofertas.
- **Fase 4 — builder**: faixa de seguidores (cron Apify lê da campanha), checkbox repetir amanhã, preview de templates da oferta.
- **Fase 5 — painel**: toggle Ativar/Pausar focal + pill worker, métricas sempre visíveis, bloco agenda (fatos), envio ao vivo só quando o worker manda. Sem instruções.

## Estado
- **PR #5 mergeado em main** (29/05) → deploy Vercel disparado. github.com/ynwwilson/foryou-leads/pull/5
- **Pós-merge (1x)**: rodar `npm run worker:install` na máquina do worker (sobe no boot do Windows + marcar AdsPower pra abrir no boot).

## Próximos / futuro
- Multi-canal por API: WhatsApp Cloud API (número novo), Reddit, plataformas de freela — rodam 100% nuvem, sem worker local. A arquitetura oferta→template→campanha→dispatch já fica pronta pra ganhar "canal" como dimensão.

Relacionado: [[Pipeline de Leads ForYou]], [[2026-05-22 01h15 - ForYou Leads — Phase 5 Frontend Redesign]]
