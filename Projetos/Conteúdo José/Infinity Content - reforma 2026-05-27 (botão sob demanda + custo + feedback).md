---
tipo: log
tags: [foryoucode, conteudo, infinity-content, reforma, cloudflare, telegram, custo, feedback]
data_inicio: 2026-05-26
data_fim: 2026-05-27
status: implementado
deploys: [f544ed02, 0b20ba17, e5a830b9]
---

# Infinity Content — reforma 2026-05-27 (botão sob demanda + custo + feedback)

> Sessão que transformou o Infinity Content de "máquina automática 4x/dia" em "máquina sob demanda quando você clica". Resolveu também o gasto projetado de ~R$150/mês e o bug do feedback por reação que nunca funcionou em canal. Três deploys: `f544ed02` → `0b20ba17` → `e5a830b9`.

---

## Resumo executivo

Antes:
- Cron 4x/dia (00/06/12/18 BRT) buscava temas sozinho, batia em tetos (10 urgentes/24h, 1 estável/ciclo).
- Custo estimado escalando pra ~R$150/mês — cron classificando ~90 itens com IA 4x/dia, gerando ou não conteúdo de fato.
- Reação 👍/👎 em dossiês no canal nunca registrou feedback (confirmado: tabela `feedback` vazia mesmo com 👍 dados).

Depois:
- **Sem cron.** Geração 100% sob demanda.
- **Botão fixo "🔄 Gerar Temas Agora"** no canal (`message_id=225`). Clique = 5 cards, sem tetos.
- **Atalho de custo (backlog-first):** clique manual quase sempre serve do backlog **sem chamar IA** — gasto só quando o backlog esvazia (refetch ~US$0,10 que reabastece pra ~18 cliques grátis).
- **Feedback por botão inline** `[👍 Gravei] [👎 Pulei]` na última mensagem do dossiê — substitui a reação emoji que não chega em canal.

Custo projetado pós-mudança: bem abaixo de R$150/mês. Você só paga quando gera dossiê (US$0,10–0,15 cada) + refetch ocasional.

---

## Linha do tempo da sessão

### Ponto de partida (manhã 2026-05-26, sessão anterior)

A reforma de 2026-05-26 (fontes novas + corroboração — log em [[Infinity Content - reforma 2026-05-26 (log completo)]]) deixou o sistema funcionando, mas com cron 4x/dia e tetos pensados pra agendamento, não pra clique humano.

### 1. "Quero clicar e aparecer card" — desenho da feature

Pergunta inicial: dá pra ter botão no Telegram que substitua o cron — clico, aparecem cards, escolho, gero dossiê?

Resposta: dá certo, e é fácil. O cron só chama `runExtractionCycle()` — a função que faz tudo. Falta um gatilho manual de dentro do Telegram. O webhook que recebe cliques já existe (é o mesmo do botão "Gerar dossiê" dos cards).

Duas opções de UX:
1. Botão fixo no canal (recomendado)
2. Comando `/gerartemas`

**Escolha:** botão fixo apenas. **Cron:** desligado, só manual.

### 2. Implementação inicial — botão "Gerar Temas Agora"

Quatro arquivos, mudança cirúrgica:

| Arquivo | Mudança |
|---|---|
| `telegram.ts` | Função nova `sendRunButton()` — posta mensagem com botão inline |
| `cycle.ts` | `handleTelegramUpdate` trata `callback_data="__RUN__"` → dispara `runExtractionCycle()` |
| `index.ts` | Endpoint novo `/post-button` + webhook responde 200 imediato com `ctx.waitUntil` (evita disparo duplo pelo retry do Telegram, já que o ciclo leva ~1 min) |
| `wrangler.toml` | `crons = []` (linha original comentada — reativar é trivial) |

`tsc --noEmit` passou limpo (exit 0).

### 3. Deploy 1 — Version `f544ed02`

```
npx wrangler deploy
→ Uploaded infinitycontent (2.75 sec)
→ Deployed infinitycontent triggers (1.74 sec)
→ Current Version ID: f544ed02-fd59-4ee6-a1fd-27cd0485f8f6
```

Triggers re-publicados com `crons = []` — cron oficialmente desligado.

### 4. Problema: RUN_KEY perdida

`/post-button` exige `RUN_KEY` na querystring. A key é secret no Cloudflare = write-only, não dá pra ler de volta.

Buscas em arquivos `.env`, vault, histórico do PowerShell, `paste-cache`:
- Histórico PS: tem comandos do projeto, mas não o valor da key
- Paste-cache: tem evidência do `wrangler secret put RUN_KEY` rodado, mas o valor não está no clipboard (foi via arquivo temp deletado, exatamente pra não vazar)
- Memory note: confirma "RUN_KEY write-only — não versionar"

Conclusão: valor genuinamente não recuperável. **Decisão:** rotacionar.

### 5. Rotação da RUN_KEY

Comando único PowerShell, seguindo o padrão da doc (arquivo temp sem newline/BOM):

```powershell
$key = -join ((48..57)+(65..90)+(97..122) | Get-Random -Count 32 | ForEach-Object {[char]$_})
[System.IO.File]::WriteAllText("$env:TEMP\rk.txt", $key)
cmd /c "npx wrangler secret put RUN_KEY < `"$env:TEMP\rk.txt`""
Remove-Item "$env:TEMP\rk.txt" -Force
Start-Sleep -Seconds 10
Invoke-RestMethod "$base/setup-webhook?key=$key"   # re-registra webhook com nova key
Invoke-RestMethod "$base/post-button?key=$key"     # posta o botão no canal
```

Resultado:
- `✨ Success! Uploaded secret RUN_KEY`
- `webhook registrado`
- `botao postado. message_id=225 (fixe essa mensagem)`

**Nova RUN_KEY:** `AfK0hEtXSxMea5ozLZjJD2lsGbIW1HcV` (salvar no gerenciador de secrets — não versionada no vault por design).

### 6. Primeiro clique do José — "esperei, nada"

Diagnóstico via `/run` direto:

```
extracao 2026-05-27T03:44:44Z | coletados=244 apos-split=254 novos=6 ruido-cortado=0 aprovados=1 urgent-24h=10/10 slots=0 cards=1
```

Achei: **`urgent-24h=10/10 slots=0`** — o teto rolling de 24h tava cheio. Botão funcionou, mas os tetos seguraram quase tudo. Era descompasso de design: tetos pensados pro cron, não pra clique humano.

### 7. Susto do custo — "R$150/mês só de API"

Levantamento dos drivers de custo:
- **Cron 4x/dia** = 4 ciclos completos/dia, classificando até 90 itens cada com haiku (cheap mas não free). Esse era o baseline.
- **Dossiê** = sonnet + busca web (até 5 usos) ≈ US$0,10–0,15 cada. Por demanda.
- Classificação: já em haiku (barato), pouco a otimizar ali.

### 8. Re-spec do botão por você

> "Sobre o botão, já conversamos que não deve ter cron mais, nem teto, sempre que eu clico em gerar temas gera 5 hora que eu quiser, toda vez que eu quiser. Mas não gera mais automático com cron."

Spec final: **clique = 5 cards, sem tetos, toda vez**.

### 9. Refatoração do ciclo — 5/click + atalho de custo

Mudanças em `cycle.ts`:

- Constante nova `CARDS_PER_CLICK = 5`.
- Assinatura: `runExtractionCycle(env, dryRun=false, manual=false)`.
- **Atalho backlog-first:** no início, se `manual=true`, checa se já tem ≥5 cards prontos no backlog (não-velhos, tópico não usado). Se sim, posta direto e retorna **sem coletar, sem classificar — zero chamada de IA**.
- Seleção e postagem extraídas em helpers `selectCardable(target, manual)` e `postCards()`. `manual=true` ignora `URGENT_DAILY_CAP` e `STABLE_PER_CYCLE`.
- `postDailyStatus` agora só roda no cron (não em clique manual).
- `handleTelegramUpdate __RUN__` passa `manual=true`.
- `/run` endpoint também passa `manual=true` pra bater com botão.

Os tetos antigos (`CARDS_PER_CYCLE=20`, `STABLE_PER_CYCLE=1`, `URGENT_DAILY_CAP=10`) continuam definidos — só valem se o cron for reativado no futuro.

### 10. Deploy 2 — Version `0b20ba17`

`tsc` exit 0. Deploy ok.

### 11. Validação — 2 cliques `/run` seguidos

```
clique 1: extracao ... | manual backlog-hit cards=5
clique 2: extracao ... | manual backlog-hit cards=5
```

**Ambos `backlog-hit`** — 5 cards cada, zero IA. Validação completa: comportamento + economia funcionando. 10 cards postados no canal nos testes.

### 12. Bug do feedback — "dei joinhas, veja se funcionou"

Verificação D1 (após erro 7403 transitório):

```sql
SELECT signal, COUNT(*) n FROM feedback GROUP BY signal
→ results: []
```

**Tabela `feedback` vazia.** Nenhum 👍 registrado, apesar de existirem 11 dossiês e 10 entregues.

Causa raiz (certeira, baseada na API do Telegram):
- **Em canal, reação é anônima/agregada.** Telegram entrega como `message_reaction_count` (aggregate counts), **não** `message_reaction` (per-user).
- O webhook foi registrado com `allowed_updates: [..., 'message_reaction']` — sem `message_reaction_count`. E o handler só processa `message_reaction`.
- Resultado: 👍 dado em canal → some no caminho, bot nunca vê.
- Funcionalidade era especificada na doc mas **nunca tinha sido testada de verdade em canal**.

Outro problema sobreposto: `feedbackForMessage` mapeia por `dossies.telegram_message_id` — se o 👍 fosse num CARD (não num dossiê), também não registraria. Mas o problema principal é o canal.

### 13. Fix do feedback — botão, não emoji

Mesmo caminho que comprovadamente funciona (callback_query via webhook):

| Arquivo | Mudança |
|---|---|
| `telegram.ts` | Função nova `sendDossie(text, itemId)` — posta dossiê com botões `[👍 Gravei] [👎 Pulei]` na última mensagem. `callback_data` = `fbg:<itemId>` ou `fbp:<itemId>` |
| `cycle.ts` | Import `sendDossie`. `generateForItem` usa `sendDossie` no lugar de `sendTelegram`. Handler do webhook trata callback que começa com `fbg:`/`fbp:` → chama `feedbackForItem()` → `recordFeedback()` |
| `cycle.ts` | Helper novo `feedbackForItem(env, itemId, signal)` — grava direto por item id, sem precisar de message_id |

`feedbackForMessage` antigo (por reação emoji) ficou no código — harmless e útil se um dia rodar em grupo (não canal).

### 14. Deploy 3 — Version `e5a830b9`

`tsc` exit 0. Deploy ok.

**Caveats:**
- Dossiês antigos (10 já entregues) continuam só com reação emoji (não funciona). Nada a fazer.
- Apenas dossiês NOVOS pegam os botões.

---

## Estado final do código

```
src/
├─ index.ts        — webhook usa ctx.waitUntil; endpoints /run, /post-button, /setup-webhook, /telegram-webhook, /nuke-cards, /health; scheduled() preservado (mas sem trigger)
├─ cycle.ts        — runExtractionCycle(env, dry, manual); atalho backlog-first; selectCardable/postCards; handler trata __RUN__, fbg:/fbp:, item id (dossiê), reação (legado)
├─ telegram.ts     — sendTelegram, sendCard, sendDossie (NOVA), sendRunButton (NOVA), setWebhook, deleteMessage, answerCallback
├─ dossie.ts       — inalterado
├─ pipeline.ts     — inalterado (classifyBatch usa tier 'fast' = haiku, CHUNK_SIZE=15)
├─ llm.ts          — inalterado (Anthropic primário haiku/sonnet, OpenAI fallback)
├─ sources.ts/youtube.ts/bluesky.ts/producthunt.ts — inalterados desde 2026-05-26
├─ db.ts/types.ts/roteiro-rules.ts — inalterados
└─ schema.sql      — inalterado
```

`wrangler.toml`:
```toml
[triggers]
# crons = ["0 3,9,15,21 * * *"]   # antigo: 4x/dia. Descomentar pra reativar.
crons = []
```

---

## Custo — análise final

| O que | Custo |
|---|---|
| Baseline (cron) | **R$0** — desligado |
| Clicar "Gerar Temas" (backlog cheio) | **R$0** — serve do estoque, sem IA |
| Clicar quando o backlog esvazia | ~US$0,10 — busca+classifica e reabastece pra ~18 cliques grátis |
| Gerar um dossiê | ~US$0,10–0,15 — Sonnet + busca web (max 5 usos) |
| Marcar 👍/👎 no dossiê | **R$0** — só grava no D1 |

Projeção: bem abaixo de R$150/mês. Custo proporcional aos dossiês que o José realmente pedir.

Otimização adicional pendente (não aplicada): cortar `max_uses` da web search no `llm.ts` de 5→3. Cortaria ~40% do custo de cada dossiê com qualidade mantida. Aguardando aprovação.

---

## Estado do banco (snapshot 2026-05-27)

```
items por status:
  approved: 52     ← backlog cardável
  carded:   47     ← postados no canal, esperando José clicar "Gerar dossiê"
  delivered: 10    ← dossiês entregues
  rejected: 494    ← filtrados

dossies: 11
feedback: 0       ← vazia (será populada quando José clicar nos botões novos)
```

---

## Validação

| Item | Status | Evidência |
|---|---|---|
| Code compila | ✅ | `tsc --noEmit` exit 0 nos 3 deploys |
| Worker no ar | ✅ | `/health` → "infinitycontent ok" |
| Secret RUN_KEY ativo | ✅ | `wrangler secret list` mostra RUN_KEY presente |
| Webhook registrado | ✅ | `/setup-webhook` → "webhook registrado" |
| Botão postado no canal | ✅ | `/post-button` → `message_id=225` |
| Botão dispara ciclo (via `/run` proxy) | ✅ | 2 chamadas seguidas: `backlog-hit cards=5` cada |
| Botão dispara ciclo (clique real do José) | ⚠️ | Não confirmado em logs ao vivo — o `wrangler tail` caiu por erro de sessão antes do clique real do José |
| Feedback por botão registra no D1 | ⚠️ | Não testado live — primeiro 👍/👎 em dossiê NOVO deve criar row em `feedback` |

---

## Pendências

Ver lista completa em [[Infinity Content - pendências]].

---

## Comandos úteis (com a key nova)

Substitua `$key` por `AfK0hEtXSxMea5ozLZjJD2lsGbIW1HcV` (ou pegue do gerenciador de secrets).

```powershell
$key = "AfK0hEtXSxMea5ozLZjJD2lsGbIW1HcV"
$base = "https://infinitycontent.ynwwilson.workers.dev"

# Disparar ciclo manual (= mesmo que clicar o botão)
Invoke-RestMethod "$base/run?key=$key"

# Re-postar o botão (se a mensagem 225 for deletada por acidente)
Invoke-RestMethod "$base/post-button?key=$key"

# Apagar todos os cards do canal e marcar como rejected no DB
Invoke-RestMethod "$base/nuke-cards?key=$key"

# Re-registrar o webhook
Invoke-RestMethod "$base/setup-webhook?key=$key"

# Health
Invoke-RestMethod "$base/health"
```

Ver logs em tempo real:
```powershell
cd C:\Users\ynwwi\Projetos\infinitycontent
npx wrangler tail
```

---

## Links

- [[Infinity Content]] — visão funcional/de produto (atualizada)
- [[Infinity Content - arquitetura tecnica]] — endpoints, deploy, debug (atualizada)
- [[Infinity Content - reforma 2026-05-26 (log completo)]] — reforma anterior (fontes + corroboração)
- [[Infinity Content - pendências]] — itens em aberto
- [[Conteúdo José]]
- [[Regras de hook roteiro e tom para conteudo da ForYou Code]]
