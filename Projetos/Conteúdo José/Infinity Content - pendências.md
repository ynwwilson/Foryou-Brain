---
tipo: pendencias
tags: [foryoucode, conteudo, infinity-content, pendencias]
atualizado: 2026-06-09
---

# Infinity Content — pendências

> **2026-06-09 — incidente "nada gerado" resolvido.** 3 causas empilhadas; ver seção abaixo. Cron 2x/dia reativado (só refetch). Backlog fresco com 39 itens novos. Pendência degradada: reddit 403 + jina 429.

## Incidente 2026-06-09 — clique não gerava nada (RESOLVIDO)

Três bugs empilhados, todos sintoma de **timeout do refetch no waitUntil de webhook**:

1. **Pool semáforo vazava** (`http.ts`) — `active`/`waiters` eram estado de módulo; isolate morto com fetches em voo deixava `active` travado → próximos cliques congelavam na fila. Fix: `resetPool()` no início do ciclo.
2. **Gate `hasFresh`** (`cycle.ts`) — atalho backlog-first exigia item criado <24h. Backlog tinha 4+ dias → todo clique falhava o gate → caía no refetch completo → estourava waitUntil (~30s) → CF cancelava antes de postar. Fix: removido o gate; **tem card no backlog → posta**.
3. **Refetch pesado no webhook** — `gather + classify(LLM) + assignTopics + datas` não cabe em ~30s. Fix: extraído `refillBacklog()`, movido pro **cron 2x/dia** (handler `scheduled` tem orçamento generoso).

**Nova RUN_KEY setada** (a antiga era write-only, sem recuperação). Webhook re-registrado, botão re-postado (`message_id=322`, **precisa fixar**).

### Arquitetura nova (pós-2026-06-09)
- **Clique "Gerar Temas"** → enfileira `{kind:'temas'}` → consumer roda `runTemasLive`: busca fontes OFICIAIS **ao vivo** (`gatherOfficial`: blogs Jina + scrape oficial + releases GitHub + Twitter oficial), classifica, insere, e posta 5 cards **oficiais primeiro** (resto preenche do backlog do cron). ~40s. Responde "chega em ~40s" na hora. Pedido Mestre: lançamento oficial é a 1ª camada de busca no clique.
- **Prioridade de seleção** (`selectCardable` + `isOfficialSource`): camada 1 = lançamento oficial (jina/scrape/release/twitter oficial), 2 = outras novidades (Google News/HN/Reddit/etc), 3 = estáveis.
- **Fila `dossie-queue`** = union `{kind:'dossie'|'temas'}`. Consumer ramifica.
- **Clique "Gerar dossiê"** → `enqueueDossie`: marca 'generating', responde na hora, joga na **fila `dossie-queue`**. O consumer (`queue()` em index.ts) gera o dossiê (~56s, Sonnet+web) fora de request. **NÃO roda no webhook** — lá o waitUntil ~30s matava na metade (item travava em 'generating', nada chegava). Causa do bug "gerar dossiê não chega nada".
- **Cron `0 0,12 * * *`** (21h/09h BRT) → `cronRefill()` → só reabastece o backlog, **não posta card**. Status diário no run das 12h UTC.
- **Endpoints debug (key-gated):** `/refill` (reabastece), `/gen-dossie?id=` (gera dossiê direto, retry manual), `/test-enqueue?id=` (enfileira, valida consumer), `/run?force=1` (refetch forçado).

### Blindagem (2026-06-09) — alertas no chat + fallbacks
`src/ops.ts` `notifyOps(env, type, msg, throttleMin)`: alerta no canal Telegram, throttled por tipo (`state` key `alert:*`). Best-effort, nunca lança. Pontos cobertos:
- **API caindo** (`llm.ts`): Anthropic com erro de crédito/cota/auth (400/401/403/429/billing) → avisa "recarregar" (2h throttle). Anthropic+OpenAI caindo → alerta forte (30min). É a detecção de "API acabando".
- **Dossiê falha** → avisa com tema + "card volta, re-clica"; item volta pra `carded` (retryável).
- **Temas**: busca ao vivo falha → serve do backlog + avisa (não derruba); 0 cards (backlog seco) → avisa.
- **Botão __RUN__**: fila indisponível → fallback serve backlog na hora + avisa.
- **Consumer da fila**: catch-all → alerta por tipo de job.
- `/test-alert?key=` valida o cano de alerta. Validado 2026-06-09.
- **Limitação:** "API acabando" detecta na 1ª FALHA (crédito zerou), não prevê saldo baixo antes — isso precisaria da Admin/billing API da Anthropic (admin key). Pendente se Mestre quiser aviso preventivo.

### Gotcha central de TODO o sistema
**Webhook waitUntil ≈ 30s. Trabalho pesado (refetch ~30-60s, dossiê ~56s) NÃO cabe lá** — CF mata na metade. Refetch → cron. Dossiê → queue. Ambos fora de request = orçamento generoso. Foi a raiz de 3 incidentes seguidos em 2026-06-09.

## Pendência crítica — validar feedback por botão

Botões `[👍 Gravei] [👎 Pulei]` implementados no deploy `e5a830b9` (2026-05-27), **ainda não testados ao vivo**. Tabela `feedback` segue vazia.

### Passo a passo (José, no Telegram)

1. Abrir canal Infinity Content → escolher qualquer card pós-2026-05-28 (~80 disponíveis, incluindo Claude Opus 4.8, Lovable Subagents, Grok Build, etc).
2. Tocar **"📝 Gerar dossiê"**.
3. Esperar ~30s o dossiê chegar.
4. **Tocar em 👍 Gravei OU 👎 Pulei** na última mensagem do dossiê.

### Verificação D1

```powershell
cd C:\Users\ynwwi\Projetos\infinitycontent
npx wrangler d1 execute infinitycontent --remote --command "SELECT * FROM feedback ORDER BY created_at DESC LIMIT 5"
```

Esperado: 1+ linha com `signal = 'gravei'` ou `'pulei'`.

### Se não aparecer

- `npx wrangler tail` enquanto clica
- Procurar callback `fbg:<id>` ou `fbp:<id>`
- Callback chega mas não grava → bug `feedbackForItem()`/`recordFeedback()` em `cycle.ts`
- Callback não chega → bug em `sendDossie` (`telegram.ts`) ou `allowed_updates`

---

## Averiguação completa 2026-06-09 — resultado

Rodei force-refetch com captura total de erros, medi cada fonte, li todo caminho silencioso.

**Resolvido na averiguação:**
- ✅ **Jina (6 blogs)** — `JINA_API_KEY` secret + header `Authorization: Bearer`. Era 0 (429), agora ~40-90 itens de blog/refill.
- ✅ **HuggingFace sempre-zero** — buscava `sort=createdAt` + filtro de tração → modelo novo sem like cortava os 50 → 0. Agora `sort=trendingScore` + recência <=30d. Validado: 30 itens.
- ✅ **Status diário órfão** — morreu quando cron passou a chamar `cronRefill`. Re-religado, 1x/dia às 12h UTC (09h BRT).
- ✅ **Texto "48h"** — razão de descarte agora diz "7 dias" (janela real).

**Pendência ativa — só reddit:**
- **Reddit (10 subs) → 403** — `www.reddit.com/*.json` bloqueia IP de datacenter da Cloudflare. **Rota via Jina TESTADA e FALHOU** (Jina renderiza o .json como prosa, descarta o JSON cru). Único fix = **OAuth reddit** (`oauth.reddit.com` + client_id/secret de um app reddit tipo "script"). Precisa de ação do Mestre: criar app em reddit.com/prefs/apps, passar credenciais. Não-fatal — 11 fontes cobrem. Quando tiver as creds: implementar client_credentials grant + trocar fetch pra `oauth.reddit.com/r/<sub>/new`.

**Edge case conhecido (baixo risco):** clique com backlog vazio → refetch dentro do webhook → pode dar timeout. Mitigado pelo cron que mantém backlog cheio.

## Conhecido e aceito

- ℹ️ **10 dossiês antigos sem botão** — pré-deploy `e5a830b9`. Sem fix retroativo.
- ℹ️ **Janela perecível 7d** (era 48h) — Google News tem latência.
- ℹ️ **Twitter syndication endpoint pode mudar a qualquer momento** — sem auth, oficial-ish. Quando quebrar, fallback Nitter ou Apify scraper.
- ℹ️ **`/run?force=1`** bypassa atalho backlog-first — útil pra validar fonte nova.
- ℹ️ **Validar feedback por botão** — botões `[👍 Gravei] [👎 Pulei]` (deploy `e5a830b9`); tabela `feedback` tem 3 linhas (2 gravado, 1 pulado) — funcionando, mas amostra mínima.

## Planejado — conversado 2026-06-09, NÃO implementado ainda

> **Plano de execução completo (9 features, 5 fases):** [[Infinity Content - plano de execução]].
> Mestre vai liberar quando quiser. NÃO mexer até ele mandar.

### Feature A — Busca sob demanda
- **O quê:** Mestre manda texto no canal → bot trata como pesquisa → busca web ao vivo (Sonnet + web search) sobre o termo → monta 1 card → posta com botão "Gerar dossiê" normal → segue o fluxo existente.
- **Gatilho:** provável `buscar <termo>` (palavra-chave, não qualquer mensagem — evita disparo à toa). A confirmar.
- **Quantos cards:** 1 card direto (menos ruído). A confirmar.
- **Custo:** ~US$0,10 por busca (1 Sonnet + web search), só quando ele pede.
- **Risco:** termo vago traz fraco; classificador filtra.
- **Valor:** tira a dependência do que as fontes acharam — viu algo no Twitter, manda o nome, vira card.

### Feature B — Resumo semanal
- **O quê:** domingo à noite (cron) o bot posta um fechamento da semana no canal.
- **Base de dados:** tabela `feedback` (sinal `gravado`/`pulado` dos botões 👍 Gravei / 👎 Pulei) + `items`/`dossies`. Os dados JÁ são coletados — depende de Mestre clicar Gravei/Pulei na semana.
- **Conteúdo:** temas que saíram, quantos ele gravou, temas que bombaram (corroboração 3+ fontes) que ele não tocou.
- **Acionável:** resumo vem com botões "Gerar dossiê" nos temas quentes perdidos — vira ferramenta, não só relatório.
- **Decisão PENDENTE:** foco principal do resumo — (a) o que perdeu, (b) ritmo/estatística, ou (c) temas mais fortes da semana. Mestre ainda não decidiu.
- **Conexão entre A e B:** o resumo aponta o que perdeu, a busca sob demanda resgata na hora.

### Feature C — Gerador de roteiro a partir de input do Mestre
- **O quê:** Mestre manda no canal um **print de um post** (imagem) ou uma **legenda/texto** colado → bot gera um roteiro/dossiê em cima daquilo. Não depende das fontes nem de busca — o INPUT é o conteúdo.
- **Dois tipos de entrada:**
  - **Imagem (print de post):** webhook recebe `message.photo` → `getFile` + download de `api.telegram.org/file/bot<token>/<path>` → manda a imagem pro Claude **vision** (block de imagem base64) → modelo lê o post/legenda da imagem → gera roteiro.
  - **Texto (legenda colada):** vai direto pro gerador, sem vision.
- **Saída:** mesmo formato do dossiê (aplica `ROTEIRO_RULES` + MODO LANÇAMENTO se for lançamento). Hook + roteiro + CTA etc.
- **Gatilho DECIDIDO (2026-06-09):** mensagem contém **"gerar roteiro"** + qualquer payload (link, texto, imagem, ou combinação). O bot pega o que veio junto como FONTE e gera roteiro sobre aquilo. Sem "gerar roteiro" = não dispara.
- **Tipos de payload:**
  - **Imagem (print):** `message.photo` + legenda "gerar roteiro" → vision lê o post → roteiro.
  - **Link:** texto "gerar roteiro <url>" → busca o conteúdo da URL (Jina/web) → roteiro.
  - **Texto puro:** "gerar roteiro <texto/legenda>" → roteiro direto.
  - **Combinação:** imagem + legenda com texto → usa os dois.
- **Stack:** Claude tem vision — factível no mesmo Worker. Custo: 1 chamada Sonnet (com imagem se for print, +web se for link).
- **Saída:** roteiro no formato do dossiê (`ROTEIRO_RULES` + MODO LANÇAMENTO se aplicável).
- **Valor:** Mestre vê QUALQUER post por aí (concorrente, referência, ideia) → manda "gerar roteiro" + o conteúdo → tem roteiro no estilo dele na hora. Gerador de roteiro UNIVERSAL, não só de novidades de IA.

### Feature D — Aprendizado por exemplo (PRIORIDADE Mestre — "muda o jogo")
- **O quê:** quando Mestre reescreve/corrige um roteiro e manda de volta, o sistema guarda a versão FINAL dele como "exemplo de ouro" e injeta no prompt do dossiê (few-shot). Cada roteiro futuro sai mais no estilo dele — composto, sem calibrar prompt na mão.
- **Mecanismo provável:** Mestre responde a um dossiê (reply no Telegram) com o roteiro corrigido → bot salva em tabela `exemplos` → as N melhores entram no `DOSSIE_INSTRUCTION` como exemplos. Gatilho a definir (reply? comando "esse é o padrão"?).
- **Por quê:** ataca a raiz da queixa "roteiro ruim/técnico" — em vez de a gente ajustar regra toda vez, o sistema aprende sozinho com as edições reais. Vimos Mestre reescrever Opus 4.8 e Fable 5; essas edições viram treino.

### Feature E — Legenda + hashtags + título junto do roteiro
- **O quê:** o dossiê passa a entregar também a **legenda do Reels, título e hashtags** prontos. Hoje para no roteiro; Mestre escreve a legenda na mão.
- **Esforço:** baixo (mais um bloco no `DOSSIE_INSTRUCTION`/saída). Ganho diário.

### Feature F — "Tela de cima" entregue pronta
- **O quê:** hoje o dossiê SUGERE o vídeo/página pra por acima da cabeça (formato tela rachada). Passar a ENTREGAR o link do vídeo oficial pronto (ou o clipe), achado via busca web — Mestre não caça a referência visual.
- **Esforço:** médio (já tem a busca; é garantir o link real e validá-lo).

### Feature G — Feedback "por quê" (sem fricção)
- **O quê:** ao Pulei (👎), oferecer toque opcional do motivo: técnico demais / já vi / fraco / não é minha praia. Ensina o filtro e a afinidade ~5× mais rápido.
- **Conexão:** acelera Feature B (resumo) e o aprendizado de afinidade existente.
- **Cuidado:** opcional, 1 toque — não pode virar fricção.

### Feature H — Detector de lançamento iminente
- **O quê:** teaser/rumor de algo grande vindo → aviso "fica de olho, isso vem aí". Deixa Mestre PRIMEIRO no tema, não correndo atrás.
- **Base:** tag `rumor` + sinais de teaser nas fontes oficiais. Empurra alerta no chat.

### Feature I — Card vende o ângulo (mudança no card, não adição)
- **O quê:** hoje o card mostra título + "por quê". Passar a trazer já **o gancho/hook do Reels** — Mestre bate o olho e sabe se rende, antes de gerar o dossiê.
- **Esforço:** baixo (o classificador já pode cuspir um hook curto junto).

### NÃO escolhido
- ~~Anti-saturação de tema (forçar variedade entre os 7 pilares)~~ — Mestre não marcou em 2026-06-09.

## Backlog Fase 2 / futuro

- [ ] **Chave Jina grátis** (`JINA_API_KEY`) — resolve 429 dos 6 blogs. Mais barato e rápido de fazer.
- [ ] **OAuth reddit** — resolve 403 dos 10 subs. Mais trabalhoso.
- [ ] **Firecrawl** ($19/mês) — `/search` premium + `/changeTracking`. Substitui Google News com qualidade superior.
- [ ] **Apify Twitter Scraper** (~$0,30/1k tweets) — fallback se syndication endpoint quebrar.
- [ ] **Sincronizar regras de roteiro** do vault pro código (`roteiro-rules.ts`).

---

## Links

- [[Infinity Content]]
- [[Infinity Content - arquitetura tecnica]]
- [[Infinity Content - reforma 2026-05-28 (Twitter + Reddit + Jina + Google News)]]
- [[Infinity Content - reforma 2026-05-27 (botão sob demanda + custo + feedback)]]
- [[Conteúdo José]]
