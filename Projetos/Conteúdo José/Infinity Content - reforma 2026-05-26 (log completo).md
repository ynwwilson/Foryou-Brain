---
tipo: log
tags: [foryoucode, conteudo, jose, infinity-content, reforma, log-sessao, cloudflare, telegram]
atualizado: 2026-05-26
data_sessao: 2026-05-26
---

# Infinity Content — reforma 2026-05-26 (log completo da sessão)

> Registro passo a passo da reforma de fontes + motor de corroboração + descoberta do bloqueio de crédito. Tudo que foi diagnosticado, decidido, construído, deployado e validado nesta sessão. Docs vivos: [[Infinity Content]] (funcional) e [[Infinity Content - arquitetura tecnica]] (técnica).

> [!summary] TL;DR
> A Infinity Content estava entregando conteúdo ruim (skill que ninguém usa, lançamentos não apareciam). O diagnóstico achou **dois problemas**: (1) fontes e critérios errados; (2) **Anthropic e OpenAI sem crédito** — a classificação estava em fallback "aprova tudo como estável", então nada era filtrado de verdade. Foram reformadas as fontes (jornalismo de IA, YouTube, Bluesky, Product Hunt), reescrita a descoberta de skills (tração real, não "criado essa semana"), e construído um **motor de corroboração** (3+ fontes = HOT). Após o José recarregar a Anthropic, o sistema passou a classificar de verdade (aprovava 39/90 em vez de 90/90) e postou cards com lançamentos reais. Por fim, o **score foi exposto no card** pra calibrar com dado real ao longo do tempo.

---

## 1. O problema (relato do José)

- "Conteúdos péssimos, não é o que eu quero."
- Vinha muita skill/MCP que ninguém usa, ninguém comenta; e as boas (que aparecem no Instagram) não vinham.
- Novidades/lançamentos das empresas (Lovable, Claude, ChatGPT, Cursor, etc.) não apareciam ou apareciam mal.
- Critério de skill desejado: alto número de estrelas; mesmo com poucas estrelas, tem que ser muito útil/revolucionário, gente usando.
- Quer cobrir o mercado de IA amplo: se lançou IA grande nova, opensource, atualização que muda algo de empresa — tem que falar.
- Referência: criadores gringos no Instagram sempre pegam primeiro; José quer descobrir de onde eles tiram a informação pra gravar antes.

## 2. Diagnóstico

### Causa raiz de fontes
- O sistema buscava skills no GitHub por `created:>14d` (repos criados na semana) → pescava lixo sem tração.
- Faltavam as fontes onde a notícia NASCE: Twitter/X (onde empresas anunciam primeiro), YouTube oficial (demos de lançamento), jornalismo especializado, sinal social.
- A maioria das IAs **não tem RSS** (Mistral, xAI, ElevenLabs, Runway, Perplexity, Pika).

### Causa raiz de inteligência
- O sistema avaliava cada notícia **isolada** — sem noção de "quantas fontes falam disso". A correção é um **motor de corroboração**: o mesmo assunto em 3+ fontes = HOT (sobe); fonte única obscura afunda.

### Causa raiz real (descoberta no deploy)
- **Anthropic e OpenAI sem crédito.** Com os dois LLMs falhando, `classifyChunk` caía no `fallbackClass()` que retorna `approve`/`estavel`. Sintoma: `aprovados=90/90` e 1 card só. Isso provavelmente já acontecia ANTES das mudanças → metade do "conteúdo péssimo" vinha daí.

## 3. Estrutura desenhada — 4 camadas de sinal

| Camada | Fontes |
|---|---|
| Oficial | blogs RSS + scrape + **YouTube RSS** |
| Social | **Twitter (Fase 2)** + **Bluesky** + Product Hunt (Reddit foi descartado pelo José) |
| Jornalismo | **The Decoder + VentureBeat AI + TechCrunch AI** |
| Builder | awesome-lists + GitHub (stars altos) |

Tudo passa pelo **motor de corroboração** antes de virar card.

## 4. Decisões tomadas (com motivo)

| Decisão | Escolha | Motivo |
|---|---|---|
| Infra | **Workers Paid ($5/mês)** | Plano free limita a 50 subrequests/execução; com muitas fontes estoura. Paid sobe pra 1000. |
| Twitter | **Fase 2** | Peça frágil: rotas de Twitter do RSSHub hoje exigem `auth_token` de conta logada + hospedagem. Bluesky+jornalismo+YouTube já dão ~80%. |
| Deploy | **Claude faz com `CLOUDFLARE_API_TOKEN`** | José passou o token (já estava no `.env`); confirma ações externas antes. |
| Reddit | **Descartado** | José não quis. Sinal social fica com Bluesky + Product Hunt + HN. |
| Filtragem extra | **Não cortar agora; expor score** | José: "problema não é quantidade, é que às vezes vem algo que não quero." Em vez de filtrar no escuro (risco de matar o bom), mostra o score no card e calibra por padrão real depois. |

## 5. Fontes e perfis monitorados (referência)

### Twitter/X (Fase 2 — quando montar conta + RSSHub)
- **Empresas:** @AnthropicAI, @OpenAI, @lovable_dev, @cursor_ai, @MistralAI, @perplexity_ai, @xai, @elevenlabs, @runwayml, @HuggingFace, @GoogleDeepMind, @github, @StabilityAI, @replit, @pika_labs
- **CEOs/fundadores:** @darioamodei, @sama, @antonosika, @mntruell, @arthurmensch, @AravSrinivas, @c_valenzuelab, @demi_guo_, @amasad, @elonmusk, @ClementDelangue, @demishassabis
- **Sinal antecipado:** @karpathy, @jackclarkSF, @_philschmid, @emollick, @swyx, @_akhaliq
- **Criadores:** @mreflow (Matt Wolfe), @rowancheung, @mckaywrigley, @matthewberman, @AIExplainedYT

### Bluesky (ATIVO — verificados via API)
`simonwillison.net` · `emollick.bsky.social` · `swyx.io` · `mattwolfe.bsky.social` · `elevenlabs.io` · `karpathy.bsky.social`
(descartados por 0 posts: mckaywrigley, rowancheung, anthropic.com)

### YouTube (ATIVO — channelIDs)
- Confirmados: Perplexity `UCYqxnCFtaC4-iC_bwt2bRLg` · ElevenLabs `UC-ew9TfeD887qUSiWWAAj1w` · Cursor `UCpV_X0VrL8-jg3t6wYGS-1g` · Replit `UCgoJjdR6-7AMu9fDitb6nVw` · DeepMind `UCP7jMXSY2xbc3KCAE0MHQ-A` · Matt Wolfe `UCawZsQWqfGSbCI5yjkdVkTA`
- Resolvidos por @handle (cacheados no `state`): anthropic-ai, OpenAI, MistralAIOfficial, runwayml, StabilityAI, lovable, aiexplained-official, MatthewBermanAI

### RSS de jornalismo (ATIVO — testados)
- The Decoder `https://the-decoder.com/feed/` ✅
- TechCrunch AI `https://techcrunch.com/category/artificial-intelligence/feed/` ✅
- VentureBeat AI `https://venturebeat.com/category/ai/feed/`

### Sem RSS (403/404 — cobertos por jornalismo/YouTube/Bluesky)
Mistral, xAI (403), Perplexity (403), ElevenLabs (404), Runway (404), Pika, Lovable (404). Scrape best-effort: Mistral, ElevenLabs.

## 6. O que foi construído (cada arquivo)

Diretório: `C:\Users\ynwwi\Projetos\infinitycontent\src`

| Arquivo | Mudança |
|---|---|
| `schema.sql` | + coluna `corroboration INTEGER DEFAULT 1`, + `card_message_id`, + índice `idx_items_topic` |
| `types.ts` | + `PRODUCTHUNT_TOKEN` no Env; + `corroboration` no Item |
| `youtube.ts` (**novo**) | RSS por canal; resolve `@handle→channelId` e cacheia no `state`; vídeos dos últimos 7d, 3/canal |
| `producthunt.ts` (**novo**) | GraphQL top do dia, filtra por tópico AI + votos ≥ 80 (tração real) |
| `bluesky.ts` (**novo**) | API pública `getAuthorFeed`; posts com link externo ou ≥25 likes, últimos 3d |
| `sources.ts` | + feeds de jornalismo; SCRAPE_BLOGS + Mistral/ElevenLabs; **`githubSkills` reescrito** (stars altos, sem `created:>14d`); plugou youtube/producthunt/bluesky no `gatherCandidates` |
| `pipeline.ts` | + `looksLikeJunk` (pré-filtro heurístico, conservador); classificador tunado p/ penalizar obscuro sem tração |
| `cycle.ts` | **motor de corroboração** + boost de score; pré-filtro aplicado; `MAX_NEW_PER_CYCLE` 45→90; **score visível no card** |
| `db.ts` | `insertItem` inclui corroboration; `recentTopicSources` (corroboração entre ciclos); `usedTopics` com janela rolling 14d |

### Motor de corroboração (o conserto-chave)
- Conta fontes distintas por tópico = lote atual + DB recente (`recentTopicSources`, 3 dias).
- **3+ fontes = HOT** → boost de score (`+8` por fonte, teto 4) + etiqueta `🔥 ALTA REPERCUSSÃO — N fontes` no card.
- Single-source obscuro fica com corroboração 1 → afunda.
- É o que faz "o que todo mundo fala" subir e "skill que ninguém usa" sumir. No começo frio fica tudo em 1; o HOT emerge ao longo dos dias.

## 7. Deploy — passo a passo

> [!warning] Pré-requisitos que só o José fez
> - Product Hunt: criou app, gerou Developer Token (Redirect URI = URL do worker, não usada).
> - Cloudflare: ativou **Workers Paid ($5/mês)**.
> - Token Cloudflare verificado: ativo, com escopo Workers + D1.

1. **Migração D1** (não-destrutiva): `ALTER TABLE items ADD COLUMN corroboration INTEGER DEFAULT 1` → success.
2. **Secrets**: `PRODUCTHUNT_TOKEN` + nova `RUN_KEY` (write-only, rotacionada).
3. **Deploy**: `wrangler deploy` → OK (Version ID novo).
4. **Webhook**: re-registrado via `/setup-webhook` (a URL do webhook embute a RUN_KEY; rotacionar a key exige re-registrar).
5. **Validação**: `/run?dry=1` (não posta).

> [!bug] Pegadinha #1 — secret com `\n`/BOM
> `wrangler secret put` via **pipe** do PowerShell injeta um `\n`/BOM no fim do secret → 401 (RUN_KEY não batia). **Solução:** setar via redirecionamento de arquivo com bytes exatos:
> ```
> [IO.File]::WriteAllText("$env:TEMP\k.txt", $valor)   # sem newline
> cmd /c "wrangler.cmd secret put NOME < `"$env:TEMP\k.txt`""
> ```

> [!bug] Pegadinha #2 — LLM sem crédito = aprova tudo
> Primeiro dry-run real: `coletados=263 novos=90 aprovados=90 cards=1`. **Aprovar 90/90 = sinal de fallback** (classificação falhando). Teste direto das APIs:
> - Anthropic → *"Your credit balance is too low to access the Anthropic API."*
> - OpenAI → 429 (sem quota)
> Os dois sem crédito → `classifyChunk` cai no `fallbackClass()` (approve/estavel). **Não era bug de código — era billing.** José recarregou a Anthropic.

## 8. Validação (antes × depois do crédito)

| Métrica | Sem crédito | Com crédito |
|---|---|---|
| coletados | 263 | 263–264 |
| após-split | 263 | 273–274 (newsletters sendo quebradas ✅) |
| aprovados | **90/90** (fallback) | **39/90** → depois **16/90** (filtro real, rejeita ~57–80%) |
| cards | 1 (tudo estável) | 6 (dry) → **9 (real, postados)** |

Após recarga: re-setei `ANTHROPIC_API_KEY` com bytes exatos, limpei 101 itens-lixo do dry-run quebrado (`DELETE FROM items WHERE reason='classificacao automatica (fallback)'`), rodei dry-run real (39/90 aprovados) e depois `/run` real → **9 cards postados no canal** (message_ids confirmados no Telegram).

### Cards reais que saíram (qualidade nova)
- 🎬 ElevenLabs — Music v2 (YouTube oficial)
- 🎬 DeepMind — Gemini for Science (YouTube oficial)
- 🎬 Grok Build CLI lançado (xAI)
- 🎬 Pi Coding Agent
- 🔒 Microsoft Copilot Cowork exfiltra arquivos (pilar cybersec)
- ♻️ skills com tração: nexu-io/open-design, plumb-mcp, claude-code-mini

### O filtro rejeitando corretamente (amostra)
fotos de pelicano/leão-marinho (blog do Simon Willison) · awesome-claude-code ("lista curadora, não é novidade") · flow-next (baixa tração) · UMG+TikTok (corporativo) · ingressos TechCrunch Disrupt (marketing) · encíclica do Papa sobre IA.

### Dossiê
Geração ponta a ponta **confirmada funcionando** (card → clique → webhook → LLM com busca web → dossiê no canal). Latência ~30s+ (busca web) é o esperado.

## 9. Ajuste final — score visível + abordagem de calibração

- Decisão do José: **não é volume**, é que às vezes vem algo que ele não quer. Em vez de apertar o classificador no escuro (risco de matar lançamento bom), **expor o score no card** e calibrar por padrão real.
- Implementado: card agora mostra `📊 NN`. Exemplo:
  ```
  🎬 LANCAMENTO — elevenlabs (YouTube): Introducing Music v2
  🔥 perecivel · 📊 82 · 🕐 há 3h
  por quê: ...
  ```
- **Insight técnico pra quando for cortar:** os release de versão (`claude-code v2.1.149`) pontuaram 72, IGUAL ao Grok CLI/Pi Agent (que o José quis). Score sozinho não separa. O conserto certo (futuro) é o classificador **pontuar** lançamento alto (80+) e patch incremental baixo (50) — sem mexer no que ele rejeita (preserva recall) — aí uma régua de card corta o patch e a corroboração fura a régua. Só fazer quando o padrão ficar claro nos dados.

## 10. Pegadinhas conhecidas (memória operacional)

- **LLM sem crédito → classificação aprova tudo como estável.** Sintoma: `aprovados=N/N`, 1 card/ciclo. Billing, não bug.
- **`wrangler secret put` via pipe injeta `\n`/BOM** → 401/auth quebrada. Usar redirecionamento de arquivo com bytes exatos.
- **RUN_KEY write-only** — rotacionar exige re-rodar `/setup-webhook`.
- **Bot precisa ser admin do canal**; canais não entregam callback_query via getUpdates → webhook obrigatório.
- **Cards antigos** do sistema pré-mudança podem estar no canal (não foram limpos). `/nuke-cards` apaga TODOS os carded (não dá pra limpar só os antigos sem regra específica).

## 11. Estado atual

- ✅ Sistema no ar (Workers Paid), classificando de verdade, fontes ricas, filtro afiado.
- ✅ Dossiê funcionando ponta a ponta.
- ✅ Score visível nos cards (a partir do próximo cron).
- ✅ Docs e memória atualizados.
- 🔒 Volume e lógica de filtro **intactos** ("mantenha por enquanto").

## 12. Próximos passos / backlog

- [ ] **Observar os scores** nos cards; quando um padrão claro aparecer ("tipo X com score < N eu nunca quero"), cortar cirúrgico com dado real.
- [ ] **Twitter (Fase 2)**: conta descartável + `auth_token` + RSSHub auto-hospedado (Render free ou VPS) → plugar `twitter.ts` com fallback.
- [ ] Calibrar classificador pra pontuar lançamento > patch incremental (quando o padrão confirmar).
- [ ] (Ideia) Injeção manual via Telegram: responder com um link → gera dossiê na hora.
- [ ] (Ideia) Digest "Hot agora" + status diário com corroboração por fonte.
- [ ] (Opcional) Recarregar OpenAI pra reativar o fallback (hoje 429).

## 13. Referência operacional

```powershell
# pré: cd C:\Users\ynwwi\Projetos\infinitycontent ; $env:CLOUDFLARE_API_TOKEN=... ; $env:CLOUDFLARE_ACCOUNT_ID=64f87e0d24c915cc2dbd50376712a030
npx wrangler deploy                                   # deploy
npx wrangler tail                                     # logs ao vivo
npx wrangler d1 execute infinitycontent --remote --command "<sql>"
# endpoints (precisa ?key=RUN_KEY exceto /health):
#   /health  /run?dry=1  /run  /setup-webhook  /nuke-cards
```

> [!danger] Segredos NÃO vão neste doc
> O vault sincroniza pro GitHub da equipe. RUN_KEY, ANTHROPIC_API_KEY, PRODUCTHUNT_TOKEN, etc. **não são versionados aqui** — ficam nos secrets da Cloudflare / na conversa / gerenciador. A RUN_KEY foi rotacionada nesta sessão; valor está no histórico da conversa com o Claude.

## Links
- [[Infinity Content]] — visão funcional/de produto
- [[Infinity Content - arquitetura tecnica]] — endpoints, deploy, debug
- [[Regras de hook roteiro e tom para conteudo da ForYou Code]]
- [[Conteúdo José]]
