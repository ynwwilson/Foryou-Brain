---
data: 2026-05-20
sessao: ForYou Leads — Fases 1-4 completas + primeiro envio real + plano Multi-vendedor
projeto: "[[Pipeline de Leads ForYou]]"
tags: [foryou, leads, automacao, instagram, multi-user, fase-1, fase-2, fase-3, fase-4, claude-haiku, neon, vercel, sentry, telegram, apify, manychat]
duracao: ~9h (sessão extensa 19/05 23h → 20/05 01h)
participantes: Wilson + Claude
---

# ForYou Leads — Maratona completa: do diagnóstico Fase 1 ao primeiro DM real entregue

> Sessão monstro. Saímos de "Fase 1 do roadmap não começada" e chegamos em "Fases 1, 2, 3, 4 completas + 20 commits em produção + primeiro envio real testado + plano Multi-vendedor pronto pra implementar". Documentação completa abaixo de cada decisão, bug, fix, deploy.

---

## 🎯 Estado no início vs estado no fim

### Início da sessão (19/05 ~22h):
- Roadmap Pós-Auditoria escrito (Fase 1 a 5, 55 melhorias) mas **nenhuma fase implementada**
- 142 leads no DB
- 1 user (Wilson)
- 1 vídeo na biblioteca local (Dr Eder 19mn)
- Worker AdsPower funcionando em estado pré-auditoria

### Fim da sessão (20/05 ~01h):
- ✅ **Fases 1, 2, 3, 4 totalmente implementadas e em produção**
- ✅ **20+ commits pushed pra main**
- ✅ **8 migrations aplicadas (sql/011-018)**
- ✅ **Primeiro DM real entregue** pra `@jessica.montelari` com texto + vídeo
- ✅ **Plano absurdamente completo Multi-vendedor (Marco + Eduardo)** escrito em `C:\Users\ynwwi\.claude\plans\vamos-para-a-fase-adaptive-ember.md` (20 seções, ~1000 linhas)
- ✅ **Sistema rodando autônomo** com 8 crons agendados no Vercel
- ✅ **Bugs identificados e corrigidos no caminho** (10+ fixes durante implementação)
- ⚠ Sentry deferred (escolha do user)
- ⚠ Test send deferred (Wilson não tem conta secundária)

---

## 📦 FASE 1 — Sobrevivência IG (5 commits)

### 1.1 Variação de mensagem (anti-detection #1) 🔴
- **Problema:** CTA hardcoded em `lib/claude.ts` linha 77 — todos DMs terminavam igual. IG detecta padrão.
- **Solução:** `hashUsername()` (djb2) + 8 CTAs + 4 saudações em SYSTEM_ANALYZE. `cta_index = hashUsername(username) % 8`. Após 12h BR força "Boa tarde".
- **Validação:** regenerou 5 leads, conferiu via SQL que cada um tem CTA diferente.

### 1.2 Rotação de vídeos
- **Migration 009**: `videos.in_rotation`, `send_jobs.use_video_pool`
- Worker escolhe vídeo por `hash(ig_username) % pool_size`
- UI: botão `+ Rotação` em `/videos` + checkbox "Usar pool" em `/enviar`
- **Estado:** Wilson tem só 1 vídeo (Dr Eder), não usa pool ainda. Funcionalidade pronta pra quando tiver +1 vídeo.

### 1.3 Detecção de bloqueio IG
- **Migration 010**: tabela `worker_state` (singleton, paused_until, block_count)
- Função `detectIGBlock(page)` no worker varre DOM por 9 padrões ("Action Blocked", "Try Again Later", "verify it's you", etc)
- Endpoint `/api/cron/send/block` pausa worker 24h + notifica Telegram 🚨
- Worker checa `paused_until` em cada poll → dorme se pausado

### 1.4 Warm-up de conta
- Função `warmUpAccount(page)` antes do 1º DM:
  - Navega pro feed
  - 4-6 scrolls aleatórios
  - 1-2 likes leves (sem desfazer)
  - Total 3-5 min de atividade
- Flag `WARMUP_ENABLED` pra desligar em testes

### 1.5 Janela horária + timing humanizado
- **Inicial:** Seg-Sex 9h-19h, Sáb 9h-14h, Dom bloqueado
- **Iterado pra:** Seg-Sex 7h-00h, Sáb 7h-00h, Dom bloqueado
- **Final (escolha Wilson):** Domingo bloqueado, demais dias 24h livre
- Lunch pause aleatório: 10% chance de +30-60min entre DMs

### 1.6 HMAC webhook ManyChat
- Env: `MANYCHAT_WEBHOOK_SECRET`, `MANYCHAT_HMAC_ENFORCE=false` (soft mode)
- Validação `crypto.timingSafeEqual` no header `X-Manychat-Signature`
- **Estado:** Soft mode ativo. Enforce não ligado (Wilson não configurou header no ManyChat ainda)
- Doc: `brain/manychat-hmac-setup.md`

### 1.7 Backup automático Neon → Vercel Blob
- **Problema crítico inicial:** `pg_dump` não roda em Vercel serverless
- **Solução:** dump JSON via `information_schema` por tabela
- **Bug grande no caminho:** `access:"public"` falhou — Blob store é "Private" por default em v2.4
- **Fix:** `access:"private"` + `allowOverwrite:true`
- Endpoint `/api/cron/backup` (Domingo 7h UTC = 4h BR)
- Health-check public: `/api/cron/backup/health` (debug rápido)
- **Validado:** 14 tabelas dumpadas, 173 rows, 339 KB, 15s. Telegram recebeu ✅

**Commits Fase 1:** `2076a49`, `e63335e`, `0a42990`, `6f43120`, `00ce63e`

---

## 🟠 FASE 2 — Reliability + Segurança (5+1 commits)

### 2.1 Audit log de status changes
- **Migration 011**: tabela `lead_status_changes` (lead_id, old, new, source, reason, changed_at)
- Helper `lib/leads.ts` `updateLeadStatus()` (preparado pra futuro refactor)
- 7 call sites adicionaram audit INSERT inline (manychat/inbound, leads/[id]/status, leads/[id]/sent, leads/bulk, cron/cleanup, cron/followup, admin/regenerate)
- Falha de audit nunca derruba operação principal (try/catch)

### 2.2 Rate limiting via Neon (sem Upstash)
- **Decisão importante:** user pediu sem dependência externa nova. Implementado via Postgres.
- **Migration 012**: tabela `rate_limit_events (bucket_key, created_at)`
- `lib/ratelimit.ts`: `checkRateLimit({ key, limit, windowSec })` faz SELECT count + INSERT
- Fail-open em erro de DB (prioriza disponibilidade)
- Aplicado em 4 endpoints:
  - `/api/auth/start` — 5/min/IP
  - `/api/auth/verify` — 5/min/IP
  - `/api/send/start` — 30/min/IP
  - `/api/manychat/inbound` — 60/min/IP
- Cleanup diário no cron/cleanup (DELETE > 24h)

### 2.3 Idempotency webhook ManyChat
- **Migration 013**: tabela `webhook_dedup` (service, dedup_hash PK, created_at)
- Hash SHA256(ig + msg + minute) com janela 1min
- INSERT com `ON CONFLICT` retorna `{ duplicate: true }` se já existe
- Cleanup diário > 24h

### 2.4 Test send pra si mesmo
- Endpoint `/api/send/test` (cria lead "test" + job force=true)
- Botão "📧 Enviar teste" em `/enviar`
- Env: `TEST_LEAD_IG_USERNAME`
- **Estado:** Pulado — Wilson não tem conta secundária pra testar. Botão dá erro amigável "config não setada"

### 2.5 Migrations versionadas
- Script `scripts/migrate.mjs` lê `sql/*.sql` ordenado, checksum SHA256
- **Bug no caminho:** primeira versão skipava statement inteiro que começa com `--` (comentário). Fix: pula só se TODAS as linhas forem comentários.
- Self-bootstrap: cria `_migrations` + seed das 010 antigas se não existir
- Command: `npm run migrate`
- Doc: `brain/migrations.md`

### 2.6 Health check IG via Apify
- **Migration 014**: tabela `ig_account_snapshots`
- Endpoint `/api/cron/account-health` reusa `runProfileScrape` do Apify
- Env: `IG_OWN_USERNAME=ynwwilson`
- Compara follower count vs snapshot anterior → alerta Telegram se queda > 5%
- Schedule: diário 11h UTC (8h BR)
- **Validado:** 1º snapshot capturado — 1744 followers, 449 following, 1 post

### 2.7 Sentry
- **Status:** ⚠ PULADO por escolha do user (não criou conta sentry.io)
- Código instalado mas `SENTRY_DSN` ausente → fica disabled
- Pra ativar futuro: criar projeto sentry.io, setar `SENTRY_DSN` + `NEXT_PUBLIC_SENTRY_DSN`, redeploy
- Doc: `brain/sentry-setup.md`

### 2.8 CRON_SECRET por scope
- 5 secrets gerados: `CRON_APIFY_SECRET`, `CRON_BRIEF_SECRET`, `CRON_WORKER_SECRET`, `CRON_BACKUP_SECRET`, `CRON_CLEANUP_SECRET`
- Fallback inteligente em `lib/env.ts`: se scoped ausente, usa `CRON_SECRET` global
- 11 cron routes refatoradas pra usar scoped
- Worker (`scripts/worker-adspower.mjs`): lê `CRON_WORKER_SECRET || CRON_SECRET`

### + Setup automatizado (script extra)
- **Bug enorme antes:** o setup manual exigia 6 passos manuais. Wilson teve dificuldade.
- **Solução:** `npm run setup:fase2` orquestra tudo:
  1. Confere `vercel whoami`
  2. `vercel env pull --environment=production` automático
  3. Roda migrations
  4. Gera 5 CRON_*_SECRETs aleatórios
  5. Pede 2 inputs (TEST_LEAD, IG_OWN_USERNAME) via readline
  6. `vercel env add` pra cada (production + preview)
  7. Atualiza `.env.local` com `CRON_WORKER_SECRET`
- **Bug no caminho:** Vercel marca envs como "Sensitive Encrypted" — não conseguimos revelar via dashboard. Solução foi salvar localmente no `.env.local`
- Doc: `brain/setup-fase2.md`

**Commits Fase 2:** `183b1a5`, `0326dd5`, `2b31989`, `34bc4b8`, `1111943` + setup auto

---

## 🟢 FASE 3 — UX & Operacional (5 commits)

### 3.1 Histórico unificado de conversa
- **Bug crítico antes:** worker NUNCA registrava DMs enviados em `lead_messages`. Só ManyChat inbound aparecia. Histórico em `/lead/[id]` ficava enviesado.
- **Migration 015**: amplia `lead_messages.source CHECK` pra incluir 'worker'
- Endpoint `/api/leads/[id]/log-outbound` (auth `CRON_WORKER_SECRET`)
- Worker chama após cada DM enviado com sucesso
- Não bloqueia worker — try/catch silencioso

### 3.2 Search global na sidebar
- Endpoint `/api/leads/search?q=termo` (auth currentUser, LIMIT 20)
- Busca em `ig_username`, `ig_full_name`, `tags[]`, `notes` (case-insensitive)
- `<SearchBox />` no topo da sidebar:
  - Debounce 250ms
  - Atalho global "/" foca input
  - Esc fecha
  - Click → router.push(`/lead/[id]`)

### 3.3 Filtros persistentes na URL
- `components/leads-grid.tsx`: useState → `useSearchParams` + `router.replace()`
- 4 filtros migrados: niche, city, tag, min_score
- Botão "📋 Copiar link filtrado" — copia URL com filtros pra clipboard

### 3.4 Date range em /metricas
- `components/metricas-controls.tsx` (client) com 2 date inputs + presets ("7d", "30d", "Este mês", "Mês passado")
- `app/metricas/page.tsx` lê searchParams `from`/`to`
- Default: últimos 30 dias
- Validação `isValidDate` anti-SQL injection

### 3.5 Quick Replies via Claude
- Decisão: em vez de templates estáticos, Claude sugere 3 respostas contextuais
- `lib/claude.ts`: `suggestQuickReplies()` com SYSTEM_QUICK_REPLIES
- Endpoint `/api/leads/[id]/suggest-replies` (auth currentUser)
- `components/quick-replies.tsx` (client): botão "✨ Sugerir" → 3 cards com Copiar + Marcar enviada
- Token count footer

### 3.6 View dedicada de "respostas pendentes"
- `/respostas/page.tsx` (server) filtra `status IN (respondeu, quente)` ordenado quente primeiro
- Empty state amigável
- **Badge dinâmico na sidebar**: link `/respostas` com count em rosa
- Endpoint `/api/leads/pending-count` (auth currentUser)
- Refresh a cada 60s via useEffect

### 3.7 Export CSV
- Endpoint `/api/leads/export?status=&niche=&city=&tag=&min_score=` (auth currentUser)
- RFC 4180 escape + BOM UTF-8 (Excel não bagunça acentos)
- LIMIT 5000 rows
- Filename `leads_YYYYMMDD.csv`
- Botão "📥 CSV" no leads-grid (reusa filtros ativos como query params)

### 3.8 Pipeline com drag-and-drop
- Lib: `@dnd-kit/core` + `@dnd-kit/sortable` + `@dnd-kit/utilities`
- `components/pipeline-board.tsx` refatorado:
  - `<DndContext>` com PointerSensor (distance:6px) + TouchSensor (delay:200ms)
  - Cada coluna `useDroppable`
  - Cada card `useDraggable`
  - Optimistic + rollback se fetch falha
  - DragOverlay com sombra
  - Dropdown "Mudar ▾" mantido como fallback (acessibilidade + mobile sem touch)

**Commits Fase 3:** Worker outbound, Search+Respostas+Export, URL filters+Date range, Quick replies, Drag-drop

---

## 🟣 FASE 4 — Inteligência & Métricas (5 commits)

### 4.1 Revenue tracking + ROI por hashtag (+4.5 simplificado)
- **Migration 016**: `leads.revenue_brl`, `leads.hashtag_origem`, `leads.post_url`
- Apify route captura hashtag origem (match contra hashtags rotacionadas da campanha) + post URL
- Endpoint `/api/leads/[id]/revenue` (auth currentUser): UPDATE status='cliente' + revenue_brl
- `components/revenue-modal.tsx`: modal pequeno com R$ input + presets 1500/1800/2000 + botão "Pular"
- `lead-card.tsx` intercepta `updateStatus('cliente')` → abre modal antes
- `/metricas` painel "🏷 Por hashtag (ROI)" com revenue total + R$/lead

### 4.2 A/B test refinado por CTA index
- **Decisão importante:** em vez de reativar V1/V2/V3 legacy, mede 8 CTAs reais da Fase 1.1
- **Migration 017**: `leads.cta_index`, `leads.saudacao_index`
- `analyzeProfile` injeta cta_index/saudacao_index no JSON parseado
- Apify INSERT inclui essas colunas
- `lib/abtest.ts`: nova `recomputeCtaStats()` calcula por cta_index 0-7
- Persiste em `ab_test_state` com chaves `cta_0` a `cta_7`
- `/metricas` painel "🎯 Por CTA (8 variações)"

### 4.3 Sentimento via Claude
- `lib/claude.ts`: `classifySentiment(text)` com SYSTEM_SENTIMENT
- Retorna `{ sentiment: 'positivo'|'neutro'|'negativo', confidence, reason }`
- `/api/manychat/inbound`: classificação **fire-and-forget** após INSERT
  - Não bloqueia response do webhook
  - UPDATE `lead_messages.metadata` com `{ sentiment, confidence, sentiment_reason }`
- UI `/lead/[id]`: emoji ao lado de cada mensagem inbound
  - 😊 positivo (verde, conf≥0.6)
  - 😐 neutro (cinza, conf≥0.6)
  - 😣 negativo (vermelho, conf≥0.6)
  - ⚪ baixa confiança

### 4.4 Score insights via Telegram (modo "sugerir só")
- **Decisão:** auto-tune autônomo iria aprender padrões errados com volume baixo (142 leads, poucos clientes). Modo sugerir é mais seguro.
- **Migration 018**: tabela `score_predictions` (snapshot do score + outcome quando lead termina)
- Apify route faz INSERT snapshot junto com lead
- `/api/leads/[id]/status` UPDATE outcome quando vira cliente/descartado/respondeu
- `/api/leads/[id]/revenue` UPDATE outcome='cliente'
- Endpoint `/api/cron/score-insights` (sexta 17h BR):
  - Se < 30 outcomes: pula com Telegram "esperando volume"
  - Buckets de score (0-29, 30-49, 50-69, 70-100)
  - Top 5 hashtags por conversão
  - Top 3 CTAs
  - Sugestão automática textual heurística
- `lib/telegram.ts`: `notifyScoreInsights()`

### 4.5 LTV/Churn simplificado
- ForYou Code é venda única (R$ 1.500-2.000) — não tem recorrência
- Implementado dentro de 4.1 (só `revenue_brl`)
- Métricas mostram revenue total + R$/lead por hashtag/cidade/nicho
- Pra Fase 5+: adicionar `client_revenue_log` se virar SaaS

### ★ Weekly Digest sexta 18h BR
- Endpoint `/api/cron/weekly-digest` (sexta 21h UTC)
- Coleta paralela últimos 7 dias:
  - Leads novos, DMs enviadas, respondidos, quentes, clientes, revenue total
  - Sentimento (positivo/neutro/negativo) das respostas com conf≥0.6
  - Top 5 hashtags por revenue
  - IG account delta (followers ganhos/perdidos)
  - Backup status
- `lib/telegram.ts`: `notifyWeeklyDigest()` formata HTML rico
- Link "Ver métricas completas" no fim
- **Testado manual:** chegou no Telegram com "12/05 → 19/05, 142 novos, 2 enviadas..."

**Commits Fase 4:** Revenue+hashtag, Sentimento, A/B CTA, Score insights, Weekly Digest

---

## 🐛 Bugs corrigidos durante a maratona

| # | Bug | Causa | Fix |
|---|-----|-------|-----|
| 1 | `vercel env pull` puxava development | Default do CLI | `--environment=production` explícito |
| 2 | Vercel envs "Sensitive Encrypted" não revelam | Default em v2 | Salvar `.env.production.local` localmente |
| 3 | Worker não lê `.env.local` automaticamente | Script Node puro | Adicionar `loadEnvLocal()` no topo |
| 4 | Migration script skipava statements com `--` no topo | `trimmed.startsWith("--")` pulava tudo | Checar TODAS as linhas, pular só se TUDO for comentário |
| 5 | `@vercel/blob` v2 `access:"public"` falhava em store private | Blob criado como Private | `access:"private"` |
| 6 | `@vercel/blob` 2ª execução do dia falhava por blob duplicado | Sem `allowOverwrite` | `allowOverwrite:true` |
| 7 | Regenerate endpoint não persistia msg_unified | UPDATE não incluía a coluna | Adicionar `msg_unified = ${a.msg_unified}` |
| 8 | Regenerate só pegava leads sem msg_v1 (não pegava sem msg_unified) | Filtro restrito | Adicionar OR msg_unified IS NULL + flag `force=true` |
| 9 | UI lead/[id] não mostrava msg_unified | Component só renderizava V1/V2/V3 | Adicionar bloco rosa destacado no topo |
| 10 | `clickMessageButton` retornava true silenciosamente | Algum dos 12 seletores pegava elemento errado (menu lateral, etc) | Reordenar seletores (header primeiro) + `miniChatVisible()` verifica pós-click + Vision fallback |
| 11 | Vídeo "confirmation" 8s era timeout muito curto | Vídeos grandes (19MB) demoram renderizar thumb | 20s + seletores ampliados + benefício da dúvida (não throw, log warning) |
| 12 | Worker rodou pela 1ª vez mas Sync vídeos falhou 401 | `.env.local` não carregava no Node script | Função `loadEnvLocal()` adicionada |
| 13 | `/api/cron/send/cleanup` recusava user-agent vercel-cron | Endpoint estrito (worker-only) | Wilson usou secret direto via PowerShell |
| 14 | PowerShell quebrava comandos longos em linhas | Default | Sempre orientar uma linha só, ou usar Git Bash |

---

## 🚀 Estado final em produção

### Crons agendados no Vercel
| Cron | Schedule | Função |
|------|----------|--------|
| `/api/cron/apify` | 9h30 BR diário | Captura leads + score_predictions |
| `/api/cron/morning-brief` | 10h BR diário | Brief manhã |
| `/api/cron/followup` | 11h BR diário | Follow-up 72h |
| `/api/cron/cleanup` | 8h BR seg | Cleanup leads mortos + rate_limit + webhook_dedup |
| `/api/cron/backup` | 4h BR dom | Backup Neon → Vercel Blob |
| `/api/cron/account-health` | 8h BR diário | Snapshot IG do Wilson |
| `/api/cron/score-insights` | 17h BR sex | Insights de score (Telegram) |
| `/api/cron/weekly-digest` | 18h BR sex | Digest semanal (Telegram) |

### Env vars no Vercel (production)
- DATABASE_URL ✅
- APIFY_TOKEN, APIFY_HASHTAG_TASK_ID, APIFY_PROFILE_TASK_ID ✅
- ANTHROPIC_API_KEY, ANTHROPIC_MODEL=claude-haiku-4-5-20251001 ✅
- TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID ✅
- MANYCHAT_API_TOKEN, MANYCHAT_WEBHOOK_SECRET, MANYCHAT_HMAC_ENFORCE=false ✅
- CRON_SECRET (legacy global) + 5 scoped ✅
- BLOB_READ_WRITE_TOKEN ✅
- IG_OWN_USERNAME=ynwwilson ✅
- SENTRY_DSN ⚠ (pulado)
- TEST_LEAD_IG_USERNAME ⚠ (pulado — sem conta secundária)

### Migrations aplicadas (sql/_migrations)
001 → 018 todas ✅ (14 originais + 5 da fase 1-2 + 3 da fase 4)

### Worker local
- Wilson PC com AdsPower profile `k1cn2qmx`
- `.env.local` com `CRON_WORKER_SECRET=ab3bc2d004c5ce8aabd06417a7c25d70ec4ef9cb82f82fbe4b6b139162f6ae6f`
- 1 vídeo na pasta `scripts/videos/` (Dr Eder 19mn)

---

## ✅ Validação real de produção

### Primeiro DM real enviado
- Lead: `@jessica.montelari` (Harmonização Facial SP)
- Texto entregue: "Oii Jéssica, vi seu perfil e seu trabalho com harmonização de lábios em SP é muito profissional, conteúdo consistente. Sem site próprio você acaba perdendo pacientes que pesquisam no Google e caem em quem aparece primeiro. A gente faz site profissional pra saúde/estética entre R$1.500 e R$2.000, entrega em 7 dias. Vou te mandar agora um vídeo do site do Dr. Eder Paula (nutrólogo) que entregamos pra você ver a qualidade que conseguimos pra você."
- Vídeo entregue: Dr Eder 19mn.mp4 (19.3 MB)
- Status: lead vira 'enviado', registrado em `lead_status_changes` (source='worker'), registrado em `lead_messages` (direction='outbound', source='worker', com metadata variant+video_sent+video_name)
- Worker logou "vídeo NÃO confirmado" mas vídeo CHEGOU (falso negativo). Fix aplicado depois (20s polling + benefício da dúvida)

### Backup testado
- Manual `curl /api/cron/backup` → 14 tabelas, 173 rows, 339 KB, Telegram ✅

### Account health testado
- Manual `curl /api/cron/account-health` → @ynwwilson 1744 followers capturado

### Weekly Digest testado
- Manual `curl /api/cron/weekly-digest` → Telegram com números da semana ✅

---

## 🔮 Próxima fase planejada: Multi-vendedor

**Documento completo:** `C:\Users\ynwwi\.claude\plans\vamos-para-a-fase-adaptive-ember.md` (20 seções, 1000 linhas)

### Decisões já tomadas
- ✅ Distribuição via campanhas (cada campanha tem `assigned_to_user_id`)
- ✅ UI privacy: "Meus" default, admin Wilson tem toggle "Ver todos"
- ✅ Repo privado + GitHub collaborators
- ✅ OTP login via bot do user (precisa `/start` antes)
- ✅ Apify cron: 5 hashtags × N campanhas (cabe no timeout 5min Vercel)
- ✅ Cada user com bot Telegram próprio
- ✅ Cada user com AdsPower profile próprio
- ✅ Cada user com conta IG dedicada
- ✅ Worker per-PC (Marco no Mac M4, Eduardo no Windows)

### Escopo final (8 commits previstos)
1. Migration 019 (multi_user) + types
2. Backend helpers (lib/users.ts, /api/auth/whoami) + telegram per-user
3. UI admin (criar users + campaigns)
4. Telegram webhook multi-bot + ManyChat per-user
5. Worker per-user + endpoints filtering
6. UI privacy (Meus vs Todos)
7. Apify per-campaign + crons per-user
8. Setup script + docs onboarding (Mac + Windows)

### Marco e Eduardo precisam providenciar ANTES do onboarding
- Conta IG dedicada NOVA (1 semana aquecimento manual)
- AdsPower instalado + profile criado + IG logado
- Bot Telegram via @BotFather (token + chat_id após /start)
- Node 20+ + Git
- Username GitHub (pra adicionar como collaborator)

### Wilson tem que coletar de cada um (matriz no §8.2 do plano)
- Email + Nome + GitHub username
- IG dedicado (@)
- AdsPower profile ID
- Bot Telegram username + token + chat_id

### Gates de validação (do plano)
- **Gate 1:** Wilson testa pós-migration que sistema dele continua funcionando 100%
- **Gate 2:** Marco/Eduardo entregam os 8 itens cada
- **Gate 3:** Wilson confirma que ambos receberam credenciais
- **Gate 4:** Cada parceiro completa envio de teste antes de subir volume

---

## 📝 3 perguntas pendentes pro Wilson (do plano §19)

1. **Migration 019** — applicar antes ou depois dos commits? (Recomendação: antes do commit 4)
2. **OTP de login** — bot do user (precisa /start antes) OU bot global (sempre funciona)? (Recomendação: bot do user)
3. **Apify cron timeout** — aceita 5 hashtags × 3 campanhas (15 batches em 5min)? (Recomendação: sim)

---

## 🎯 Próximos passos absurdos pendentes

1. Wilson **revisa o plano Multi-vendedor com calma**
2. Responde as 3 perguntas pendentes
3. Dá **"GO"** pra implementação
4. Claude implementa 8 commits sequenciais (~3-4h)
5. Wilson valida regressão (§15.1)
6. Wilson coleta info dos parceiros (§8.2)
7. Wilson cria contas Marco e Eduardo no `/admin/users`
8. Wilson adiciona ambos como collaborators no GitHub
9. Marco faz setup no Mac M4 (doc onboarding-marco-mac.md)
10. Eduardo faz setup no Windows (doc onboarding-eduardo-windows.md)
11. Cada um faz envio de teste (Gate 4)
12. Operação trio começa

---

## 🔥 Riscos remanescentes (não-críticos)

| Risco | Mitigação |
|------|-----------|
| Wilson esquecer backfill `UPDATE leads SET assigned_to = wilson` | Plan file destaca isso 3x |
| Marco/Eduardo iniciarem com conta IG virgem (banimento rápido) | Doc força 1 semana aquecimento manual ANTES |
| Score predictions misturadas após Marco/Eduardo entrarem | Adiar separação por user pra Fase 5+ |
| HMAC ManyChat continua em soft mode | Não bloqueia operação. Wilson liga quando quiser |
| Sentry deferred | Sem captura de erros em prod. Pode ativar quando criar conta |
| 1 vídeo só na biblioteca | Rotação funciona mas sem variar arquivo. Ideal: 2-3 versões do mesmo vídeo |

---

## 💡 Coisas pra lembrar (lições aprendidas)

1. **Vercel envs Sensitive** não saem em `env pull` quando setadas via `vercel env add`. Pra debug futuro: gerar secret e salvar no `.env.local` local antes de submetter no Vercel.
2. **Worker é Node puro** — sempre precisa loadEnvLocal no topo.
3. **Migrations idempotentes** salvaram a pele várias vezes. Sempre `IF NOT EXISTS`, `ADD COLUMN IF NOT EXISTS`.
4. **@vercel/blob v2** requer `access:private` se store é Private + `allowOverwrite` pra reruns.
5. **clickMessageButton no IG** muda toda semana. Vision fallback é essencial.
6. **PowerShell Windows** quebra comandos longos. Recomendar Git Bash pro Eduardo.
7. **Score insights modo "sugerir"** evita overfitting com volume baixo.
8. **Warm-up de 3-5 min** parece travado mas é normal. Doc deve avisar.
9. **Vídeo confirmation timeout 8s é curto demais** — vídeos grandes precisam de mais tempo. 20s + benefício da dúvida.
10. **Repo deve ficar privado** com collaborators (não público). Secrets em commits antigos podem vazar.

---

## 🔗 Links e referências

- **App produção:** https://foryou-leads.vercel.app
- **GitHub:** https://github.com/ynwwilson/foryou-leads (privado)
- **Vercel project:** yngomesmarco-hues-projects/foryou-leads
- **Neon project:** neondb (Wilson)
- **Plan file Multi-vendedor:** `C:\Users\ynwwi\.claude\plans\vamos-para-a-fase-adaptive-ember.md`
- **Documentação no repo:**
  - `brain/manychat-hmac-setup.md`
  - `brain/backup-neon-restore.md`
  - `brain/migrations.md`
  - `brain/sentry-setup.md`
  - `brain/setup-fase2.md`
- **Notas Obsidian relacionadas:**
  - [[Pipeline de Leads ForYou]] (nota mãe — atualizada nesta sessão)
  - [[ForYou Leads — Roadmap Pós-Auditoria]] (marcada Fases 1-4 como ✅)
  - [[2026-05-18 22h00 - ForYou Leads sistema completo + auditoria + roadmap]] (sessão anterior)

---

## 📊 Métricas da sessão

| Métrica | Valor |
|---------|-------|
| Duração | ~9h |
| Fases completas | 4 de 5 (Fase 5 reformulada como Multi-vendedor) |
| Commits | 20+ (Fases 1-4 + bug fixes + setup auto) |
| Migrations aplicadas | 8 (011-018) |
| Bugs corrigidos | 14 |
| Endpoints novos | 13+ |
| UI components novos | 6 (revenue-modal, quick-replies, metricas-controls, SearchBox+PendingBadge embed, etc) |
| Funções Claude novas | 3 (suggestQuickReplies, classifySentiment, +cta_index injection no analyzeProfile) |
| Crons novos | 3 (account-health, score-insights, weekly-digest) |
| DMs reais entregues | 1 (@jessica.montelari, texto + vídeo) |
| Dependências npm novas | 2 (@dnd-kit, @sentry/nextjs) |
| Tempo estimado economia futura | Incalculável — operação saiu de "Wilson manualmente" pra "sistema autônomo com 8 crons + relatórios Telegram automáticos" |

---

> **Sessão encerrada às ~01h de 20/05/2026.** Wilson disse "agora só amanha, por enquanto o ultimo teste passou 100%". Próximo retorno: revisar plano Multi-vendedor + dar GO pra implementação.
