---
tipo: tecnico
tags: [foryoucode, conteudo, infinity-content, arquitetura, cloudflare, telegram, webhook]
atualizado: 2026-05-26
---

# Infinity Content — arquitetura técnica

> Documento de referência técnica do Worker. Endpoints, deploy, secrets, como debugar. Atualizado após a refatoração de 2026-05-23 (polling → webhook).

## Stack

| Camada | Tecnologia |
|---|---|
| Runtime | Cloudflare Workers |
| Banco | Cloudflare D1 (SQLite) |
| Cron | Cloudflare Cron Trigger — 1 trigger só, 4x/dia |
| LLM | Anthropic (primário) · OpenAI (fallback) |
| Bot | Telegram Bot API · `@infinitycontent_bot` |
| Sinal de clique | **Webhook do Telegram** (não getUpdates) |

Worker URL: **https://infinitycontent.ynwwilson.workers.dev**
Código: `C:\Users\ynwwi\Projetos\infinitycontent`
Repo: github.com/ynwwilson/infinitycontent (privado)

## Endpoints

Todos exigem `?key=$RUN_KEY` exceto `/health`. O webhook autentica via mesma key na querystring.

| Endpoint | Método | Função |
|---|---|---|
| `/health` | GET | Status, sem auth |
| `/run` | GET | Dispara ciclo de extração agora. `?dry=1` simula sem postar |
| `/telegram-webhook` | POST | Telegram POSTa updates aqui (cliques, reações, replies) |
| `/setup-webhook` | GET | Registra (uma vez) o webhook do Telegram apontando pra esse Worker |
| `/post-button` | GET | Posta no canal a mensagem com o botão fixo "🔄 Gerar Temas Agora". Rodar 1x e fixar a mensagem. Retorna o `message_id` |
| `/nuke-cards` | GET | Apaga cards pendentes do canal + marca todos como `rejected` no DB |

## Secrets (no Cloudflare)

| Nome | Função |
|---|---|
| `ANTHROPIC_API_KEY` | LLM primário |
| `OPENAI_API_KEY` | LLM fallback |
| `GITHUB_PAT` | Aumenta rate limit da busca no GitHub |
| `TELEGRAM_BOT_TOKEN` | Token do `@infinitycontent_bot` |
| `TELEGRAM_CHANNEL_ID` | ID do canal "Infinity Content" |
| `RUN_KEY` | Senha das chamadas administrativas |
| `PRODUCTHUNT_TOKEN` | Developer token (read-only) da Product Hunt — fonte de ferramentas com tração |

**Var (não secret):** `WORKER_URL = "https://infinitycontent.ynwwilson.workers.dev"` no `wrangler.toml`. Usada pelo `/setup-webhook` pra registrar o webhook do Telegram.

## Schema D1

Tabelas: `items`, `dossies`, `feedback`, `state`.

Colunas relevantes da `items`:
- `id` (UUID) — usado como `callback_data` do botão
- `status` — `new|approved|carded|generating|delivered|rejected`
- `card_message_id` — `message_id` da mensagem do card no Telegram (usado pra deletar)
- `tag` — `perecivel|estavel|rumor`
- `topic` — slug do assunto, dedup entre ciclos

Coluna adicionada em 2026-05-23:
```sql
ALTER TABLE items ADD COLUMN card_message_id INTEGER
```

## Crons

`wrangler.toml` (CRON DESLIGADO desde 2026-05-27 — geração 100% sob demanda via botão):
```toml
[triggers]
# crons = ["0 3,9,15,21 * * *"]   # antigo: 4x/dia. Descomentar pra reativar.
crons = []
```

O cron foi desligado: agora os temas só são buscados quando você toca no botão **"🔄 Gerar Temas Agora"** (mensagem fixa no canal, `message_id=225`). O clique chega via webhook como `callback_data = "__RUN__"` → dispara `runExtractionCycle()`. Cliques de dossiê/feedback continuam em tempo real via webhook.

## Como funciona o webhook

1. `/setup-webhook?key=...` chama o endpoint `setWebhook` do Telegram, registrando o Worker como destino.
2. Quando alguém clica no botão de um card, o Telegram POSTa em `/telegram-webhook?key=...` com o `Update` (callback_query).
3. Worker processa imediatamente, gera o dossiê via LLM, posta no canal.
4. `answerCallback` responde o clique (tira o spinner do Telegram).

Mesmo fluxo serve pra:
- Reações 👍/👎 nos dossiês → vira sinal de feedback (gravado/pulado)
- Respostas de texto a um dossie (ex: "gravado", "pulado") → mesmo loop

## Por que webhook e não polling

O código original usava `getUpdates` em cron de 5 min. Não funcionava: **canais do Telegram não entregam `callback_query` via `getUpdates`** quando o bot é admin do canal. O cron rodava em loop sem nunca pegar clique nenhum.

Webhook resolve porque o Telegram empurra os updates pro Worker, contornando o problema do polling.

## Operação — comandos úteis

Pré-requisito: `cd C:\Users\ynwwi\Projetos\infinitycontent`

**Deploy:**
```powershell
npx wrangler deploy
```

**Trocar a RUN_KEY (sem deixar lixo no paste):**
```powershell
$key = "<sua-key-32-chars>"
[System.IO.File]::WriteAllText("$env:TEMP\rk.txt", $key)
Get-Content "$env:TEMP\rk.txt" -Raw -Encoding UTF8 | npx wrangler secret put RUN_KEY
Remove-Item "$env:TEMP\rk.txt"
```

**Gerar key aleatória:**
```powershell
-join ((48..57) + (65..90) + (97..122) | Get-Random -Count 32 | ForEach-Object {[char]$_})
```

**Disparos manuais (PowerShell, com `$key` já setado):**
```powershell
Invoke-RestMethod "https://infinitycontent.ynwwilson.workers.dev/setup-webhook?key=$key"
Invoke-RestMethod "https://infinitycontent.ynwwilson.workers.dev/run?key=$key"
Invoke-RestMethod "https://infinitycontent.ynwwilson.workers.dev/nuke-cards?key=$key"
```

**Rodar SQL no D1 remoto:**
```powershell
npx wrangler d1 execute infinitycontent --remote --command "<sql>"
```

**Ver logs em tempo real:**
```powershell
npx wrangler tail
```

## Limites de produção (em `src/cycle.ts`)

```ts
const CARDS_PER_CYCLE = 20;       // teto duro de seguranca por ciclo
const STABLE_PER_CYCLE = 1;       // skill/plugin/metodo/prompt: 1 por ciclo
const URGENT_DAILY_CAP = 10;      // perecivel/rumor: 10/dia (rolling 24h)
```

Rolling 24h conta `items` com `status IN ('carded','generating','delivered')` e `tag IN ('perecivel','rumor')` dos últimos 86_400_000 ms.

## Histórico de mudanças

### 2026-05-27 — Geração sob demanda (botão) + cron desligado + controle de custo

Motivo: queria disparar a busca na hora que quisesse (sem cron) E o custo de API estava alto (~R$150/mês projetado), puxado pelo cron classificando ~90 itens com IA 4x/dia.

- **Cron desligado** (`wrangler.toml`: `crons = []`). Geração 100% manual. Linha antiga comentada — reativar é trivial.
- **Botão fixo "🔄 Gerar Temas Agora"** no canal (`message_id=225`, fixar). Clique → webhook recebe `callback_data="__RUN__"` → `runExtractionCycle(env, false, true)`. Em `cycle.ts` (`handleTelegramUpdate`) e `telegram.ts` (`sendRunButton`).
- **Clique = 5 cards, sem tetos** (`CARDS_PER_CLICK = 5`). O parâmetro novo `manual` em `runExtractionCycle` ignora `URGENT_DAILY_CAP` e `STABLE_PER_CYCLE` (esses só valem pro cron, se reativado). Seleção/postagem extraídas pros helpers `selectCardable(target, manual)` e `postCards()`.
- **Atalho de custo (backlog-first):** em clique manual, se o backlog já tem ≥5 cards prontos, posta direto **sem coletar nem classificar** → zero chamada de IA. Só busca conteúdo novo (e gasta LLM, ~US$0,10) quando o backlog esvazia; esse refetch classifica até 90 e reabastece o buffer pra ~18 cliques grátis. Cliques rápidos "paginam" o backlog de graça. Validado: 2 cliques seguidos = `backlog-hit cards=5` cada, sem IA.
- **Novo endpoint `/post-button`** (`index.ts`) — posta a mensagem do botão. Rodar 1x. `/run` agora também usa `manual=true`.
- **Webhook responde 200 imediato** + trabalho em background via `ctx.waitUntil` — evita disparo duplo pelo retry do Telegram.
- **RUN_KEY rotacionada** (antiga não recuperável — secret write-only via arquivo temp). Nova key no gerenciador de secrets do Mestre; webhook re-registrado. **Não versionar a key no vault.**
- **Custo pós-mudança:** baseline zero (sem cron). Por clique: quase sempre grátis (backlog). Refetch ocasional ~US$0,10 amortizado. Gasto real = dossiês que você pedir (Sonnet + web search ≤5 ≈ US$0,10–0,15 cada). Bem abaixo de R$150/mês.
- Deploy: Version `0b20ba17`.

**Feedback por botão (Version `e5a830b9`)** — reação 👍/👎 emoji **não funciona em canal** (Telegram entrega reação de canal como `message_reaction_count` anônimo, não `message_reaction`). Confirmado: feedback table estava vazia mesmo após múltiplos 👍. Solução: dossiê agora sai com botões inline `[👍 Gravei] [👎 Pulei]` na última mensagem. callback_data `fbg:<id>` / `fbp:<id>` → handler em `cycle.ts` chama `feedbackForItem()` → `recordFeedback()`. Mesmo caminho de webhook do botão "Gerar Temas" e "Gerar dossiê" (comprovadamente funciona). Dossiês antigos ficam sem botão; só novos pegam.

### 2026-05-26 — Reforma de fontes + motor de corroboração

Motivo: conteúdo entregue estava ruim (skills obscuras que ninguém usa, lançamentos não apareciam). Diagnóstico achou DOIS problemas: (1) fontes/critérios errados, (2) **Anthropic e OpenAI sem crédito** — a classificação estava em fallback "aprova tudo", então nada era filtrado de verdade.

- **Fontes novas** (em `src/`):
  - `youtube.ts` — RSS gratuito por canal (oficiais + criadores); resolve `@handle→channelId` e cacheia no `state`
  - `bluesky.ts` — API pública (sem auth), contas verificadas: simonwillison, emollick, swyx, mattwolfe, elevenlabs.io, karpathy
  - `producthunt.ts` — GraphQL, top do dia filtrado por tópico AI + votos mínimos (tração real)
  - RSS de jornalismo em `sources.ts`: **The Decoder, TechCrunch AI, VentureBeat AI** (cobrem lançamento de qualquer empresa)
  - Scrape expandido: Mistral, ElevenLabs (best-effort; empresas sem RSS — xAI/Perplexity dão 403)
- **Skills/MCPs reescrito** (`githubSkills`): matou a busca `created:>14d` (pescava lixo sem tração). Agora `stars:>80-200 pushed:>30-45d` = ferramenta estabelecida e viva.
- **Motor de corroboração** (`cycle.ts` + coluna `corroboration` em `items`): conta fontes distintas por tópico (lote atual + DB recente via `recentTopicSources`). 3+ fontes = HOT → boost de score (`+8` por fonte, teto 4) + etiqueta "🔥 ALTA REPERCUSSÃO" no card. Afunda single-source obscuro.
- **Pré-filtro heurístico** (`pipeline.ts` `looksLikeJunk`): corta ruído óbvio (release de manutenção, título só-versão) antes do LLM. Conservador.
- **Classificador tunado**: penaliza ferramenta obscura sem tração (score < 50).
- **Janela de dedup** (`usedTopics`): rolling 14d em vez de all-time (desdobramento novo de tema antigo pode voltar).
- **`MAX_NEW_PER_CYCLE`**: 45 → 90 (mais fontes; Workers Paid aguenta).
- **Infra**: conta migrada pra **Workers Paid ($5/mês)** — remove o teto de 50 subrequests/execução.
- **Twitter**: ficou pra Fase 2 (precisa conta descartável + RSSHub auto-hospedado; rotas de Twitter do RSSHub hoje exigem `auth_token`).

Validação (dry-run pós-recarga): coletados=263, aprovados=39/90 (filtro rejeitando 57%), 6 cards. Filtro cortando corretamente fotos de natureza, notícia corporativa, marketing, opinião.

### 2026-05-23 — Refatoração crítica

- **Bug corrigido**: clicar em "Gerar dossiê" não fazia nada (callback_query de canais não chega via `getUpdates`)
- **Polling → webhook**: removido cron de 5 min, removida função `runPickCycle`, removida `getTelegramUpdates`
- **Novos endpoints**: `/telegram-webhook`, `/setup-webhook`, `/nuke-cards`
- **Schema**: adicionada coluna `card_message_id` na tabela `items`
- **Limites por categoria**: separação entre perecível/rumor (10/dia rolling) e estável (1/ciclo)
- **Worker URL fixa** em `wrangler.toml` como `WORKER_URL`

## Pegadinhas conhecidas

- **Bot precisa ser admin do canal** pra que cliques/reações cheguem ao webhook
- **Webhook e getUpdates são mutuamente exclusivos** — se chamar `getUpdates` enquanto webhook está ativo, retorna 409
- **`wrangler secret put` via prompt pode pegar lixo do clipboard** — use pipe via arquivo temporário (ver comandos acima)
- **`callback_data` tem limite de 64 bytes** — UUID v4 (36 chars) cabe folgado
- **Dossiê sai com latência de ~30s** após clique — gargalo é o LLM com busca web, não a infra
- **LLM sem crédito = classificação aprova TUDO como estável.** Quando Anthropic E OpenAI falham (sem saldo), `classifyChunk` cai no `fallbackClass()` que retorna `approve`/`estavel`. Sintoma: `aprovados=N/N` (100%) e só 1 card/ciclo. NÃO é bug de código — é billing. Recarregar crédito na Anthropic resolve.
- **`wrangler secret put` via pipe do PowerShell injeta `\n`/BOM no secret** → auth quebra com 401 (RUN_KEY) ou 400/credit-like. Setar via redirecionamento de arquivo com bytes exatos: `cmd /c "wrangler.cmd secret put NOME < arquivo.txt"` (arquivo escrito com `[IO.File]::WriteAllText`, sem newline).

## Links

- [[Infinity Content]] — visão funcional/de produto
- [[Infinity Content - reforma 2026-05-26 (log completo)]] — log passo a passo desta reforma
- [[Conteúdo José]]
- [[Regras de hook roteiro e tom para conteudo da ForYou Code]]
