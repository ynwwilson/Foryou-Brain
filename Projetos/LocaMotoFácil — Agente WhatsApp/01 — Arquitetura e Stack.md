---
projeto: LocaMotoFácil — Agente WhatsApp
nota: Arquitetura e Stack
---

# Arquitetura e Stack

## Visão geral do fluxo
```
WhatsApp (cliente)
   │  mensagem
   ▼
Meta Cloud API ──webhook──▶ GATEWAY (Cloudflare Worker + Durable Object)
                                │  debounce 8s, junta mensagens (batching)
                                │  POST /api/brain/process (shared secret)
                                ▼
                           BRAIN (Next.js na Vercel) ── orquestra o turno:
                             ingest mídia → entende → LLM (OpenAI→Anthropic)
                             → style-filter → envia resposta → Meta → cliente
                                │
                                ▼
                           SUPABASE (Postgres + pgvector + Storage + Auth + RLS)
```

## Monorepo (`C:\Users\ynwwi\Projects\whatsapp-ai-agent`)
npm workspaces, branch `build-b`. 3 pacotes:
- **`packages/core`** — toklit puro, portável Node/Workers. LLM router, prompts, whatsapp client/parse/verify, payments/extract, media/video, memory, usage, alerts, db/supabase, **sgrlock/client**, agent/actions. ~99 testes (vitest).
- **`apps/gateway`** — Cloudflare Worker + `ConversationDO` (Durable Object): recebe webhook, valida assinatura, debounce, exactly-once, encaminha pro brain. Também repassa delivery-status e template-status pro brain.
- **`apps/panel`** — Next.js 16 (App Router, `proxy.ts` = middleware). Tem o **Brain** (`/api/brain/process`, `/api/brain/event`, `/api/cron/proactive`) + o **painel CRM** (todas as telas).

## Stack
- **WhatsApp**: Meta Cloud API oficial, single-tenant (1 número). Webhook + X-Hub-Signature-256. Janela 24h + templates.
- **LLM**: OpenAI primário (gpt-4o chat/visão, gpt-4o-transcribe STT, tts, embeddings) + Anthropic fallback (claude-sonnet-4-5) via `LlmRouter`. Groq Whisper = failover de STT.
- **Banco**: Supabase (Postgres, pgvector 1536 = text-embedding-3-small, Storage pra mídia, Auth pros donos, RLS single-owner via tabela `panel_users`).
- **Gateway**: Cloudflare Worker + Durable Object (debounce + inflight exactly-once + alarm). Ordena buffer por timestamp.
- **Painel**: Next 16 + React 19, **CSS Modules** (sem Tailwind), design system próprio "Revolut Dark laranja". Fontes Inter/JetBrains Mono via next/font.
- **Validação**: zod nas server actions e nos parsers.

## Tabelas Supabase (migrations 0001–0008)
- `contacts` (wa_id, name, profile jsonb, ai_paused, opt_in, last_inbound_at)
- `messages` (in/out, type, body, transcription, media_id, wa_message_id, status)
- `media` (recebida, storage_path, transcription, extracted jsonb)
- `media_library` (assets que a IA envia, por id)
- `memory_facts` (pgvector) + `conversation_summaries` (resumo rolante + watermark) + `re_embed_queue`
- `payments` (payer, **recipient**, amount, status, confidence, ...)
- `templates` + `proactive_jobs` (reengajamento)
- `usage_events` (custo) + `error_log` (observabilidade) + `settings` (singleton id=1: global_pause, banned_phrases, hard_cap_usd, ...)
- `panel_users` (allowlist RLS) + `risk_checks` (SGRLock)

## Padrões importantes do código
- **AgentTurn** (zod, `packages/core/src/agent/actions.ts`): a IA emite ações estruturadas — `text`, `voice`, `send_media`, `escalate`, `pause`, **`risk_check`** + memoryFacts + summaryUpdate + profileUpdate. O orchestrator executa.
- **style-filter** (`prompts/style-filter.ts`): mata travessão/clichê de IA, deterministicamente.
- **system prompt** (`prompts/system.ts`) + **knowledge** (`business/locamoto.md` embarcado em build via `gen-knowledge.mjs` → `knowledge.generated.ts`).
- **Orchestrator** (`apps/panel/lib/orchestrator.ts`): ingest → think → execute, com idempotência, rate-limit, safe-bridge (nunca expõe erro).
