---
tipo: log
tags: [foryoucode, conteudo, infinity-content, reforma, cloudflare, telegram, twitter, reddit, jina, sources]
data_inicio: 2026-05-28
data_fim: 2026-05-28
status: implementado
deploys: [efc93efe, 7d69ab7f, fd7efc82, 55299b83, 06509499, a35bd1a1, 24fe1f51]
---

# Infinity Content — reforma 2026-05-28 (Twitter + Reddit + Jina + Google News)

> Sessão que transformou a cobertura de fontes do Infinity Content. Mestre detectou gap: "Claude lançou Opus 4.8, Lovable lançou Subagents, Higgsfield lançou — nada apareceu". Diagnóstico: atalho backlog-first nunca chamava IA enquanto tinha estoque, e fontes principais (Anthropic, Lovable, Manus, Higgsfield) não tinham RSS oficial. Resultado: **+8 fontes novas**, **+92 cards no backlog**, **Twitter sem custo**, Claude Opus 4.8 + Lovable Subagents capturados.

---

## Resumo executivo

**Problema:** José gerou 3x desde 27/05, sempre serviu do backlog (atalho de custo nunca refetchava). Lançamentos importantes não apareceram. Plus blogs modernos (Anthropic, Lovable, Higgsfield, Manus) não têm RSS.

**Solução em 4 frentes:**

1. **Atalho exige item <24h** — backlog estagnado força refetch automático
2. **+12 queries Google News** — cobertura de qualquer empresa via jornalismo
3. **Classificador fixado** — "lançamento de feature" agora vira `perecivel` mesmo quando categoria é `skill`
4. **3 fontes novas**:
   - **Twitter sem custo** via `syndication.twitter.com` (mesmo endpoint do widget oficial)
   - **Reddit JSON** público, 10 subs de IA
   - **Jina AI Reader** (`r.jina.ai`) para blogs sem RSS (Anthropic, claude.com, Lovable, Higgsfield, Manus, OpenAI Codex devs)
   - **3 newsletters** RSS: Smol.ai AINews, Latent Space, Import AI

**Antes:** ~25 fontes, lançamentos importantes escapavam.
**Depois:** ~60 fontes, 333 candidates/refetch (vs 244 antes), 92 cards no backlog.

---

## Linha do tempo da sessão

### 1. Diagnóstico inicial — "gerei 3x e nenhuma vez veio"

Mestre mandou screenshot do anúncio "Lovable Now with subagents" (27/05) e listou: "Highsfield+Claude pra criativo nada apareceu".

Query no DB confirmou: **último item coletado em 27/05 03:00 UTC**. José clicou 3x desde então — sempre `backlog-hit`, nunca refetch. Atalho de custo (reforma 2026-05-27) era a causa.

### 2. Fix de frescor backlog — `efc93efe`

`cycle.ts:123` — atalho só dispara se `selectCardable` retorna ≥target itens **E pelo menos 1 tem `created_at` <24h**.

```ts
const FRESH_MS = 24 * 3600 * 1000;
const hasFresh = ready.some((b) => Date.parse(b.created_at) > Date.now() - FRESH_MS);
if (ready.length >= target && hasFresh) { /* atalho */ }
```

Backlog estagnado (todos itens >24h) → atalho não dispara → refetch automático.

### 3. Mapeamento de opções de coleta (deep research)

Mestre pediu "ultrathink — vá mais fundo, existem muitas opções no mercado". Mapeei:

| Categoria | Opções pesquisadas |
|---|---|
| Search/Scrape APIs | Firecrawl ($19/mês), Tavily, Exa, **Jina AI Reader (grátis)**, Linkup, Brave Search API, Serper, SerpAPI, Perplexity, You.com, Diffbot |
| Twitter sem auth $ | Apify ($0,30/1k), socialdata.tools ($0,20/1k), **syndication.twitter.com (grátis)**, Nitter, RSSHub, rettiwt-api |
| Comunidades | **Reddit JSON (grátis)**, Lobsters RSS, HN search |
| Newsletter | Smol.ai AINews, Ben's Bites, The Batch, Latent Space, Import AI |
| Papers | arXiv RSS, HF Papers daily |
| Change-tracking | distill.io, visualping.io, Firecrawl /changeTracking |
| Twitter alts | Bluesky firehose, Mastodon RSS por usuário |

Mestre escolheu: "preciso de Twitter sem custo".

### 4. Twitter via syndication endpoint — `a35bd1a1`

Descoberta: `https://syndication.twitter.com/srv/timeline-profile/screen-name/{handle}?dnt=true` retorna HTML Next.js com `<script id="__NEXT_DATA__">JSON</script>` contendo até 20 tweets do user. **Sem auth, sem rate limit visível.** É o que o widget oficial usa.

`src/twitter.ts`:
- 16 handles: AnthropicAI, claudeai, Lovable, GoogleAIStudio, GeminiApp, xai, grok, ManusAI_HQ, higgsfield_ai, OpenAI, OpenAIDevs, Codex_Changelog, RoundtableSpace, kloss_xyz, mattworkman, EHuanglu
- Filtros: retweets cortados (`RT @`), replies cortados (`in_reply_to_status_id`), idade >7d cortada
- Max 5 tweets/handle, source = `twitter`
- Risk: Twitter pode mudar endpoint a qualquer momento

Primeiro refetch trouxe **"Subagents now in Lovable" score 89** e **"Claude Opus 4.8" via outros canais**.

### 5. Reddit JSON — `24fe1f51`

`https://www.reddit.com/r/{sub}/new.json?limit=15` sem auth.

`src/reddit.ts`:
- 10 subs: LocalLLaMA, ClaudeAI, singularity, StableDiffusion, OpenAI, MachineLearning, vibecoding, PromptEngineering, AIToolkit, ChatGPTCoding
- Filtros: stickies/NSFW cortados, score mínimo 5 upvotes
- Max 5/sub, source = `reddit`

Primeiro refetch: **26 items, 12 aprovados** — dominou top scores ("Mythos Opus 5 soon", "100M images dataset", "LiquidAI LFM2.5", "Reachy Mini local", "InvokeAI 6.13").

### 6. Jina AI Reader pra blogs sem RSS — `24fe1f51`

`r.jina.ai/{URL}` devolve markdown limpo. Free, sem auth.

`src/blogScrape.ts`:
- 6 blogs: anthropic.com/news, claude.com/blog, lovable.dev/blog, higgsfield.ai/blog, manus.im/blog, developers.openai.com/blog/topic/codex
- Estratégia: fetch markdown do índice, regex pra extrair `[título](url)` que apontam pra `/blog/SLUG`, top 5 por blog
- `publishedAt` = now - posição*1h (heurística — blogs renderizam chrono DESC; posição no índice indica recência)
- Source = `blog`

### 7. Google News expansão — deploys `06509499`, `55299b83`

12 queries agrupadas em `sources.ts` RSS_FEEDS:

| Feed name | Cobertura |
|---|---|
| gnews-anthropic | Anthropic, Claude AI, claude.com |
| gnews-builders | Lovable.dev, Lovable AI, Bolt.new, v0.dev, Vercel v0 |
| gnews-video-gen | Higgsfield, Pika, Luma AI, Runway, Krea, Hedra |
| gnews-avatar | HeyGen, Synthesia, Captions AI |
| gnews-audio | Suno, Udio, ElevenLabs |
| gnews-xai | xAI, Grok |
| gnews-manus | Manus AI, Manus.im |
| gnews-perplexity | Perplexity AI |
| gnews-llm-alt | DeepSeek, Qwen, Mistral |
| gnews-coding-agents | Cursor, Windsurf, Cline, Codeium, Codex |
| gnews-google-ai | Gemini, Google AI Studio, DeepMind |
| gnews-genspark-notion | Genspark, Notion AI |

Requer UA browser (`Mozilla/5.0 ... Chrome/120 ...`) — UA genérico recusa.

### 8. Newsletters — `24fe1f51`

3 feeds adicionados em RSS_FEEDS:

```ts
{ name: 'smol-ainews', url: 'https://buttondown.com/ainews/rss', digest: true },
{ name: 'latent-space', url: 'https://www.latent.space/feed', digest: false },
{ name: 'import-ai', url: 'https://importai.substack.com/feed', digest: false },
```

Ben's Bites (`bensbites.beehiiv.com/feed`) e The Batch sem RSS válido — não adicionados.

### 9. Classificador fix — `7d69ab7f`

`pipeline.ts` `CLASSIFY_SYSTEM`:

**Antes:**
> tag: perecivel (lancamento/noticia grande) | estavel (skill/plugin/metodo/prompt)

**Depois (regra-chave adicionada):**
> Se a notícia É QUE a ferramenta GANHOU algo novo ("now with X", "introducing Y", "anuncia Z", "launches A") → **perecivel**, MESMO QUE category seja skill/plugin/método. O eixo TEMPORAL decide, não o TIPO.

Resolve o caso "Subagents in Lovable" que estava sendo marcado `estavel` por causa da categoria.

### 10. Janela perecível 48h → 7d — `55299b83`

`cycle.ts` `tooOld()`: trocado `48 * 3600000` por `7 * 24 * 3600000`. Razão: Google News tem latência — Anthropic news de 3-5 dias atrás chegava e era cortada por idade. Dedup por tópico (14d) continua impedindo repetir o mesmo lançamento.

### 11. Endpoint `/run?force=1` — `fd7efc82`

`runExtractionCycle(env, dry, manual, forceRefetch=false)` — quarto param. Quando `forceRefetch=true` bypassa atalho backlog-first mesmo com hasFresh=true. Útil pra validar fontes novas ou puxar lançamento sob suspeita.

`index.ts:/run` lê `?force=1` da querystring.

### 12. Logs de feed falhando — `06509499`

`fetchOneFeed` em `sources.ts`: agora logga `feed-bad-status {name} {status}` e `feed-empty-parse {name} len={n}` em vez de catch silencioso. Diagnóstico via `wrangler tail`.

---

## Estado final

**Fontes ativas (~60 endpoints):**

| Categoria | Fontes |
|---|---|
| Blogs RSS oficiais | tldr-ai, simonwillison, openai, google-ai, google-deepmind, huggingface, github-ai, vercel, microsoft-ai, replit, together-ai, cursor |
| Jornalismo RSS | the-decoder, techcrunch-ai, venturebeat-ai |
| Google News (12 queries) | anthropic, builders, video-gen, avatar, audio, xai, manus, perplexity, llm-alt, coding-agents, google-ai, genspark-notion |
| Newsletters | smol-ainews, latent-space, import-ai |
| YouTube | anthropic, openai, mistral, runway, stability, lovable, aiexplained, matthewberman |
| Bluesky | simonwillison, emollick, swyx, mattwolfe, elevenlabs, karpathy |
| **Twitter (NOVO)** | 16 handles via syndication endpoint |
| **Reddit (NOVO)** | 10 subs JSON |
| **Jina Blogs (NOVO)** | anthropic.com/news, claude.com/blog, lovable.dev/blog, higgsfield.ai/blog, manus.im/blog, developers.openai.com/blog/topic/codex |
| GitHub | releases + skills/MCPs com tração |
| Outras | Hacker News, Product Hunt, Hugging Face, scrape Mistral/ElevenLabs |

**Coletados por refetch:** 244 → **333** (+37%)
**Cards no backlog:** 47 → **92** (+96%)
**Cobertura:** Anthropic Opus 4.8 ✅, Lovable Subagents ✅, Grok Build ✅, Higgsfield Adobe ✅, Krea 2 ✅, Mistral chips ✅, OpenAI Codex Thursday ✅

---

## Comandos úteis

```powershell
$key = "AfK0hEtXSxMea5ozLZjJD2lsGbIW1HcV"
$base = "https://infinitycontent.ynwwilson.workers.dev"

# Refetch normal (atalho dispara se backlog tem item <24h)
Invoke-RestMethod "$base/run?key=$key"

# Force refetch (bypassa atalho — coleta real das fontes)
Invoke-RestMethod "$base/run?key=$key&force=1"

# Force dry (testa filtro sem postar cards)
Invoke-RestMethod "$base/run?key=$key&force=1&dry=1"

# Health
Invoke-RestMethod "$base/health"
```

---

## Pegadinhas novas

- **Twitter syndication HTML, não JSON** — extrair via `<script id="__NEXT_DATA__">JSON</script>` regex.
- **Reddit precisa User-Agent identificável** — vazio ou padrão Cloudflare = 403/429.
- **Google News exige UA browser real** — `infinitycontent/1.0` retorna 0 items.
- **Cloudflare Workers podem cachear outbound fetches** — 1ª chamada Google News retorna 60 items, 2ª chamada 0. Não é rate limit, é cache de CF.
- **Jina Reader retorna `text/plain` markdown** — não XML/JSON. Parse via regex de markdown link.
- **`publishedAt` heurístico em Jina blogs** — `now - position*1h`. Funciona porque blogs renderizam chrono DESC.

---

## Pendência única

Ver [[Infinity Content - pendências]] — validar feedback button. 92 cards no backlog (~80 pós-deploy `e5a830b9` que servem pro teste).

---

## Links

- [[Infinity Content]] — visão funcional (atualizada)
- [[Infinity Content - arquitetura tecnica]] — endpoints, deploy, debug
- [[Infinity Content - reforma 2026-05-27 (botão sob demanda + custo + feedback)]] — reforma anterior
- [[Infinity Content - pendências]] — itens em aberto
- [[Conteúdo José]]
