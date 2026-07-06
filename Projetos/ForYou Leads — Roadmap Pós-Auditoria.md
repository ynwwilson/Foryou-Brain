---
projeto: ForYou Leads — Roadmap completo
status: Fases 1-5 CONCLUÍDAS + Sistema de Ofertas + Gerenciador de Campanhas (deployados em produção). Roadmap original 100% entregue.
criado: 2026-05-18
atualizado: 2026-05-22
tags: [projeto, forYou-code, leads, roadmap, anti-detection, instagram, automacao, multi-user, completo]
relacionado: "[[Pipeline de Leads ForYou]]"
---

# ForYou Leads — Roadmap Pós-Auditoria (em Fases)

> Resultado da auditoria completa realizada em 18-05-2026. 55 melhorias identificadas, organizadas em 5 fases ordenadas por **risco de perda imediata → reliability → UX → inteligência → escala**.

---

## 🎯 Status em 20/05/2026

| Fase | Tema | Status |
|------|------|--------|
| 0 | Baseline | ✅ Pré-auditoria |
| 1 | 🔴 Sobrevivência IG | ✅ CONCLUÍDA (5 commits, 19-20/05) |
| 2 | 🟠 Reliability + Segurança | ✅ CONCLUÍDA (5+1 commits, 19-20/05). Sentry e Test Send deferred por escolha do user |
| 3 | 🟢 UX & Operacional | ✅ CONCLUÍDA (5 commits, 19-20/05) |
| 4 | 🟣 Inteligência & Métricas | ✅ CONCLUÍDA (5 commits, 19-20/05). LTV/Churn simplificado (venda única) |
| 5 | 🔵 Multi-vendedor (Adaptive-Ember) | ✅ CONCLUÍDA — código (8 commits, 20/05). Migration 019, backfill 142 leads, deploy prod, Marco/Eduardo no DB + webhooks. Falta TeamViewer worker setup. Plano: `C:\Users\ynwwi\.claude\plans\sim-bright-codd.md` |

**Validações reais:**
- 1º DM real entregue pra @jessica.montelari (texto + vídeo, 20/05)
- Backup Neon validado (14 tabelas, 173 rows, 339 KB)
- IG snapshot inicial: 1744 followers @ynwwilson

**Detalhes da implementação:** [[2026-05-20 01h00 encerramento]]

---

## 🚀 Pós-roadmap (22/05/2026)

Roadmap original 100% entregue. Duas evoluções grandes além dele, deployadas em produção:

### Sistema de Ofertas (multi-produto)
O produto vendido deixou de ser hardcoded e virou um **catálogo configurável** (`offers`). Cada oferta carrega público-alvo, preço, case, pitch, orientações e CTAs — e a IA monta as mensagens a partir disso. Tela `/admin/ofertas` pra gerir, `OfferCombobox` na campanha, métricas por oferta. Migration 021. Permite vender IA de Atendimento, App, etc., não só sites.

### Gerenciador de Campanhas (estilo Ads Manager)
A campanha virou a **unidade de trabalho completa** — captura + envio + oferta + criativo + ritmo. Estados rascunho→pausada→ativa, lista com métricas ao vivo, builder em seções, painel da campanha com "Enviar agora" e feed do job. O `/enviar` foi absorvido. Migration 022. Worker respeita ritmo por campanha.

### Corte de redundância
`/enviar` removido · `/hoje`+`/respostas` → `/atendimento` · `/metricas`+ROI Nichos em abas. Menu de 12 → 9 itens.

**Detalhes:** [[2026-05-22 00h37 - ForYou Leads — Ofertas + Gerenciador de Campanhas]]

---

---

## 🧭 Context

Sistema [[Pipeline de Leads ForYou|ForYou Leads]] está operacional mandando DMs reais. Auditoria revelou que apesar da camada base funcionar, há **riscos imediatos** de:

- Banimento da conta IG (worker não detecta "Action Blocked"; CTA do vídeo é hardcoded igual pra todo mundo)
- Poluição de dados (webhook ManyChat sem auth/HMAC)
- Perda total (sem backup do Neon)
- Falhas silenciosas (sem audit log, sem Sentry)

O usuário **enfatizou que variação de mensagem é prioridade absoluta**. CTA hardcoded em `lib/claude.ts:77` é idêntica em todos os DMs → padrão fácil de detectar pelo Instagram.

---

## 📊 Visão de fases (overview)

| Fase | Tema | Tempo | Risco se NÃO fizer |
|------|------|-------|---------------------|
| 0 | ✅ Baseline atual | já feito | — |
| 1 | 🔴 Sobrevivência IG | 1 semana | Conta banida em semanas |
| 2 | 🟠 Reliability/Segurança | 1 semana | Bugs invisíveis, perda de dados |
| 3 | 🟢 UX/Operacional | 1 semana | Fricção alta no dia-a-dia |
| 4 | 🟣 Inteligência/Métricas | 1-2 semanas | Decisões cegas, sem ROI |
| 5 | 🔵 Escala | 2-4 semanas | Limitação ao crescimento |

---

## ✅ Fase 0 — Baseline atual (já implementado)

- Captura automática (Apify + Claude → DB)
- Pipeline / Hoje / Pipeline kanban
- Lead card com mensagem, score, tags, notas, snooze
- Bulk actions, filtros client-side, kanban
- Sistema de envio (send_jobs, /enviar UI, worker AdsPower)
- Worker com features robustas:
  - typeHumanInPage via JS injetado
  - findInput scoring inteligente
  - expandMiniChat 3 estratégias + Vision fallback
  - clickSendButton estrito + Vision fallback
  - ensureInThread (recovery)
  - dismissPopups estrito (`text-is`)
  - accept-check no input de vídeo
  - Detecção de envio real (poll DOM por `<video>`)
  - CSP bypass + file picker intercept
  - HTTP server local pra vídeos > 50MB
  - Auto-cleanup jobs órfãos
- Vídeos locais (sync via worker)
- Crons (apify, morning brief, followup, cleanup)
- Webhook ManyChat (inbound → status update + hot keywords)
- Mensagem `msg_unified` única por lead (Claude)
- Auto-snooze 3 dias após envio

---

## 🔴 Fase 1 — CRÍTICO: Sobrevivência da conta IG

### 1.1 Variação de mensagem (anti-detection #1) ⚡ PRIORIDADE MÁXIMA

**Por quê**: CTA hardcoded em `lib/claude.ts:77` é idêntica em todos os DMs. IG detecta padrão e flagga conta como spam.

**Como**:
- Modificar `SYSTEM_ANALYZE` em `lib/claude.ts` pra Claude gerar `msg_unified` com instruções de variação:
  - **Saudação rotativa**: "Oii", "Olá", "Boa tarde", "Oi"
  - **Estrutura de pitch pode variar ordem** (pain-first vs autoridade-first)
  - **CTA**: lista de 8-10 variações no prompt, Claude escolhe 1 baseado em hash do username (consistente mas distribuído)
- Variações da CTA do vídeo (exemplos):
  - "Vou te mandar agora um vídeo do site do Dr. Eder Paula..."
  - "Te envio logo um exemplo: vídeo do site que entregamos pro Dr. Eder Paula..."
  - "Vou compartilhar um vídeo aqui do site do Dr. Eder (nutrólogo) que entregamos..."
  - "Logo te mando o vídeo do site do Dr. Eder Paula — pra você ver a qualidade..."
- Adicionar campo `cta_seed` no Claude prompt (recebe hash do username) pra escolha determinística mas distribuída

**Files**: `lib/claude.ts`

---

### 1.2 Rotação de vídeos

**Por quê**: Mesmo MP4 sendo enviado N vezes = fingerprint detectável. IG hasheia uploads.

**Como**:
- Worker escolhe vídeo aleatório do pool (permite múltiplos `is_default=true`)
- Migration 009: remove unique-like behavior do `is_default`
- Worker recebe vídeo via `hash(ig_username) % video_count` ou random

**Files**: `sql/009_multi_default_videos.sql`, `scripts/worker-adspower.mjs`, `lib/send-queue.ts`, `components/videos-client.tsx`

---

### 1.3 Detecção de bloqueio do IG

**Por quê**: Worker continua mandando mesmo após IG sinalizar "Action Blocked". Banimento escala.

**Como**:
- Função `detectIGBlock(p)` no worker: após cada DM, checa DOM por:
  - "Action Blocked"
  - "Try Again Later"
  - "verify it's you"
  - "We restrict certain activity"
- Se detectar: pausa worker por 24h (state em DB), aborta job atual, notifica Telegram com print
- Tabela `worker_state` com `paused_until`

**Files**: `scripts/worker-adspower.mjs`, `sql/010_worker_state.sql`, `lib/telegram.ts`

---

### 1.4 Warm-up de conta antes do batch

**Por quê**: Conta logada que dispara 15 DMs em sequência = padrão obviamente bot.

**Como**: Antes do primeiro DM de um job, worker faz 3-5 min de "atividade humana":
- Navega pro feed (`/`)
- Scroll random
- Like em 1-2 posts (de quem já segue, não leads)
- Hover em 1-2 stories
- Função `warmUpAccount(p)`, chamada uma vez no início de `processJob`

**Files**: `scripts/worker-adspower.mjs`

---

### 1.5 Janela horária + timing humanizado

**Por quê**: DMs às 3am = bot óbvio. Intervalo idêntico (3-8min) também é padrão.

**Como**:
- Worker rejeita iniciar `processJob` fora da janela 9h-19h BR local
- Distribuir 15 DMs por 6-8h (não 2h compactas)
- 1 em cada 10 DMs: pausa de 30-60min ("almoço")
- Sábado: meia carga. Domingo: pula

**Files**: `scripts/worker-adspower.mjs`, `app/api/send/start/route.ts`

---

### 1.6 HMAC no webhook ManyChat

**Por quê**: Qualquer um pode hitar `/api/manychat/inbound` e poluir DB com leads/mensagens falsas.

**Como**:
- Adicionar `MANYCHAT_WEBHOOK_SECRET` em env
- Validar header `X-Manychat-Signature` (HMAC SHA256 do body)
- Se falhar: 401, não processa
- Configurar ManyChat pra enviar a signature

**Files**: `app/api/manychat/inbound/route.ts`, `lib/env.ts`

---

### 1.7 Backup automático do Neon

**Por quê**: Neon free tier = sem backup garantido. Banco morre = perde tudo.

**Como**:
- Cron novo: 1x/semana (domingo 4h) executa `pg_dump` lógico via Neon API
- Salva no Vercel Blob com retenção 4 semanas
- Notifica Telegram do sucesso/falha

**Files**: `app/api/cron/backup/route.ts`, `vercel.json`

---

## 🟠 Fase 2 — Reliability + Segurança

### 2.1 Audit log de status changes
**Por quê**: Hoje status muda sem rastro. Conversion drop = mistério.
**Como**: Tabela `lead_status_changes` (lead_id, old, new, source[user/webhook/cron/worker], at, reason). Insert em cada lugar que muda status.
**Files**: `sql/011_audit_log.sql`, status endpoints e webhook

### 2.2 Rate limiting em endpoints sensíveis
**Por quê**: Spam de `/api/auth/start` = Telegram lotado.
**Como**: `@upstash/ratelimit` (free tier) ou implementação em memória. Limits: auth/start 5/min/IP, manychat/inbound 60/min/IP.

### 2.3 Idempotency no webhook
**Por quê**: ManyChat às vezes reenvia mesmo evento → duplica no banco.
**Como**: Hash(username + message + timestamp arredondado) → tabela `webhook_dedup` TTL 24h.
**Files**: `sql/012_webhook_dedup.sql`, `app/api/manychat/inbound/route.ts`

### 2.4 Test send pra si mesmo
**Por quê**: Toda mudança no worker queima nome real. Precisa de "DM pra mim".
**Como**: Lead especial com `ig_username` = conta secundária do Wilson. Botão "Enviar teste" em `/enviar`.
**Files**: `components/send-controller.tsx`, `app/api/send/start/route.ts`

### 2.5 Migrations versionadas
**Por quê**: Esquecer SQL no Neon → bug em prod.
**Como**: Script `scripts/migrate.mjs` lê `sql/*.sql` em ordem, marca aplicadas em `_migrations`. Comando `npm run migrate`.
**Files**: `scripts/migrate.mjs`, `sql/000_migrations_meta.sql`, `package.json`

### 2.6 Health check da conta IG
**Por quê**: Account silenciosamente restrito = você não sabe.
**Como**: Cron diário 8h: worker navega pro próprio perfil, lê followers/posts, compara com snapshot. Queda >5% = alerta.
**Files**: `scripts/worker-adspower.mjs` (modo health), `app/api/cron/account-health/route.ts`, `sql/013_account_health.sql`

### 2.7 Sentry pra erros
**Por quê**: Erros em prod hoje vão pra console.log que ninguém vê.
**Como**: `@sentry/nextjs` integrado. Free tier 5k events/mês.

### 2.8 CRON_SECRET por scope
**Por quê**: 1 secret pra tudo = vazou, perdeu tudo.
**Como**: `CRON_APIFY_SECRET`, `CRON_WORKER_SECRET`, `CRON_BACKUP_SECRET`, `CRON_BRIEF_SECRET`.
**Files**: `lib/env.ts`, todos `app/api/cron/*/route.ts`

---

## 🟢 Fase 3 — UX & Operacional

### 3.1 Histórico completo de conversa
Hoje só inbound salva. Worker insere outbound em `lead_messages` source='worker'. UI mostra timeline merged.

### 3.2 Search global na sidebar
Input busca em `ig_username`, `ig_full_name`, tags, notes. Endpoint `/api/leads/search`.

### 3.3 Filtros persistentes na URL
`useSearchParams` em `leads-grid.tsx`. URL fica `?niche=Derma&city=BH&score=70`.

### 3.4 Date range em /metricas
Date picker. Query SQL `WHERE date BETWEEN`.

### 3.5 Templates de resposta rápida
Tabela `reply_templates`. Botão dropdown em `/lead/[id]`, click copia.

### 3.6 View dedicada de "respostas pendentes"
Rota `/respostas` lista `status='respondeu'` por `last_inbound_at DESC`. Badge na sidebar.

### 3.7 Export CSV
Endpoint `/api/leads/export.csv` com query opcional. Botão "Exportar" no Pipeline.

### 3.8 Pipeline com drag-and-drop
`@dnd-kit/core`. Arrastar entre colunas.

---

## 🟣 Fase 4 — Inteligência & Métricas

### 4.1 Revenue tracking + ROI por hashtag
Campo `revenue_brl` em leads. Modal ao virar `cliente`. Métricas mostram R$ por hashtag.

### 4.2 A/B test framework de copy
Tabela `copy_variants`. Worker rotaciona. Métricas por variant.

### 4.3 Análise de sentimento (Claude)
No webhook inbound, classifica resposta como 😊/😐/😣. UI mostra ícone.

### 4.4 Predição de score (auto-tune)
Cron semanal analisa convertidos vs descartados, ajusta pesos do score.

### 4.5 LTV + Churn de clientes
Tabela `client_revenue_log`. Status `cliente_ativo` / `cliente_churn`. LTV médio nas métricas.

---

## 🔵 Fase 5 — Escala (futuro)

### 5.1 Multi-conta IG
Tabela `ig_accounts`. `send_jobs.account_id`. Worker abre profile dinâmico.

### 5.2 Multi-vendedor
Leads atribuídos a `assigned_user_id`. Métricas e comissões por pessoa.

### 5.3 Multi-worker (load balance)
Workers se registram em `worker_pool`. Claim com lock. Permite VPS + residencial.

### 5.4 API pública
REST com OAuth. Documentação Swagger. Integra com Hubspot/Pipedrive.

### 5.5 Mobile refinement
Audit completo no mobile. Drawer pra filtros. PWA install.

### 5.6 Tests + CI/CD
Playwright E2E. GitHub Actions com typecheck + test. Staging Neon.

---

## 🧪 Verification por Fase

**Fase 1**:
- Mandar 5 DMs de teste, verificar via hash que mensagens são diferentes
- Forçar bloqueio (30+ DMs seguidos sem espera) → confirmar que detector pausa worker
- Restaurar backup local → todas tabelas/dados intactos
- Tentar hitar webhook sem HMAC → 401

**Fase 2**:
- Mudar status manualmente, conferir entry em `lead_status_changes`
- Spam `/api/auth/start` → após 5 req, bloqueio
- Worker manda DM, conferir `lead_messages` outbound registrado
- Sentry recebe erro intencional

**Fase 3**:
- Search "Maria" mostra todas Marias
- Filtrar Pipeline, copiar URL, abrir em incognito → mesmos filtros
- Métricas filtradas pra mês passado mostra dados diferentes
- CSV abre no Excel corretamente

**Fase 4**:
- Fechar 1 lead como cliente, marcar revenue. Métricas mostram ROI por hashtag.
- Resposta com "preço" → sentiment positivo. "Não tenho interesse" → negativo.

**Fase 5**:
- Criar 2 IG accounts no AdsPower, atribuir 1 lead a cada, conferir worker abre o profile certo

---

## 🔄 Dependências entre fases

- **Fase 1** é independente — pode começar imediatamente
- **Fase 2** depende de Fase 1 (HMAC) e migrations versionadas (necessário antes)
- **Fase 3** depende de Fase 2.5 (migrations versionadas) pra mover rápido
- **Fase 4** depende de Fase 2.1 (audit log) pra ter dados de análise
- **Fase 5** pressupõe tudo anterior

---

## ⚡ Ordem recomendada de execução

| Quando | O quê |
|--------|-------|
| **Hoje/amanhã** | 1.1 (variação) + 1.3 (detecção de bloqueio) + 1.6 (HMAC webhook) |
| **Esta semana** | Resto da Fase 1 |
| **Semana 2** | Fase 2 completa |
| **Semanas 3-4** | Fase 3 cherry-picking conforme dor |
| **Mês 2** | Fase 4 (quando ja tiver dados suficientes pra ROI) |
| **Mês 3+** | Fase 5 conforme escala |

---

## 📁 Files de referência

- **Plan file**: `C:\Users\ynwwi\.claude-nova\plans\eager-wondering-nygaard.md` (working file)
- **Projeto principal**: `~/Projects/foryou-leads/`
- **Nota mãe**: [[Pipeline de Leads ForYou]]

---

> Roadmap criado em 18-05-2026 após sessão de auditoria completa com Claude Sonnet 4.6. Cada item tem files identificados e verification plan. Pronto pra execução sequencial.
