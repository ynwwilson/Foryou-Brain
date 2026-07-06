---
tipo: projeto
tags: [foryoucode, conteudo, leticia, bot, automacao, planejamento]
criado: 2026-05-27
atualizado: 2026-05-27
status: planejamento
---

# Leticia Content — projeto (bot)

> Bot autônomo no padrão [[Infinity Content]] do José, **adaptado para o perfil institucional ForYou Code executado por [[Leticia]]**.
> Mesmo esqueleto técnico, miolo (fontes, filtro, tom) trocado para falar com dono de negócio, não com builder.
> **Status: planejamento.** Decisão de seguir tomada em 2026-05-27.

## Por que existe
Leticia precisa entregar **6 vídeos/dia** no perfil ForYou Code ([[Conteúdo ForYou Code (Leticia)]]). Sem máquina, ela queima horas/dia caçando notícia e adaptando para linguagem de empresário. Com o bot, ela abre o Telegram, escolhe os cards do dia, clica → recebe dossiê pronto pra gravar.

É a mesma promessa do Infinity Content do José, com mundo de fontes e filtro diferente.

## Decisão arquitetural (tomada 2026-05-27)
Replica **exatamente** a arquitetura do [[Infinity Content]] funcionando hoje:

- Cloudflare Worker + D1 + Cron Triggers
- 2 ciclos:
  - **Extração** (cron 4x/dia, igual ao Infinity): coleta, filtra, posta **cards** no Telegram com botão "📝 Gerar dossiê"
  - **Cliques** (webhook em tempo real ou cron 5min): clique → gera dossiê → posta no canal
- Mesmo merge de tópicos, frescor 48h, dry mode, status diário, loop de aprendizado por 👍/👎
- LLM: Anthropic (haiku=classifica, sonnet=dossiê), OpenAI fallback

**Decisão do user (literal):** *"clique gera dossies, apenas. assim como está o meu infinity content"*

## O que MUDA em relação ao Infinity do José

### 1. Fontes (`src/sources.ts`)
**Tirar:** GitHub releases técnicos, repos de skill/MCP, Hacker News, Show HN, blogs ultra-técnicos (simonwillison.net puro).
**Manter:** Blogs oficiais grandes (OpenAI, Anthropic, Google, Microsoft) — porque viram notícia traduzida pra empresário também.
**Adicionar (a definir pelo José):**
- Jornalismo de IA em PT-BR (Olhar Digital, Tecmundo seção IA, Canaltech IA, Brasil Jornal IA, MIT Tech Review Brasil, Exame IA, Forbes Brasil tech, NeoFeed tech)
- Casos empresariais (McKinsey AI, BCG GenAI, HBR, Bain insights — relatórios)
- Dados de mercado / adoção (Statista IA, Gartner, Stanford AI Index)
- Vertical do ICP da ForYou (saúde/estética/educação/varejo — onde IA já tá entrando)
- TikTok/Instagram trending de negócios com IA (Fase 2 — depende de scrape)

**Lista exata ainda PENDENTE** — José disse: *"vou buscar pra voce tudo que quero pra ela, referencias, etc"*

### 2. Filtro / classificação (`src/pipeline.ts` → `CLASSIFY_SYSTEM`)
Reescrito do zero. Pergunta-filtro nova:

> *"Isso renderia um Reels que um dono de clínica/escola/distribuidora ia entender em 15s e pensar 'isso afeta MEU negócio'?"*

**Aprova:**
- IA mudando setor concreto (saúde, educação, varejo, jurídico)
- Caso real de empresa cortando custo / aumentando venda com IA
- Dado de mercado que vira munição de venda
- Alerta de risco (SaaS subindo preço, ferramenta desaparecendo, dependência perigosa)
- Tendência grande, mas explicada em termos de negócio

**Descarta:**
- Skill/plugin/método/prompt técnico (isso é do José)
- Release de SDK, mudança de API, feature interna
- "Modelo novo no Hugging Face" sem aplicação concreta
- Qualquer coisa que precise saber código pra entender

### 3. Categorias (esquema do D1)
**Substituir:** `lancamento | skill | plugin | metodo | prompt`
**Por (proposta a confirmar):** `noticia-ia | case-empresa | dado-mercado | alerta-saas | tendencia | aplicacao-vertical`

### 4. Regras de roteiro (`src/roteiro-rules.ts`)
**Não usar** o documento de regras de hook do José (esse é monolito/intransferível por design).
**Usar** um documento próprio do perfil ForYou Code — **a criar**:
- Hook traduzindo termo técnico para impacto de negócio
- Sem ALL CAPS técnico, sem jargão de builder
- Verbos que dono de empresa entende: "economiza", "perde", "fatura", "concorrente"
- Encerramento: deixar ele desconfortável o suficiente pra pensar "preciso conversar com alguém disso" → BOF do funil ([[Plano Comercial ForYou Code 2026]] §9)

### 5. Volume e cadência
**Infinity (José):** ~10 cards/ciclo × 4 ciclos = teto 40/dia, mas só ~10 viram dossiê/dia.
**Leticia:** alvo de **6 vídeos/dia entregues**. Cadência sugerida:
- Opção A: 2 cards × 3 ciclos = 6 cards/dia (1:1 com vídeo postado)
- Opção B: 6 cards/ciclo × 4 ciclos = 24 cards/dia (Leticia escolhe os 6 melhores)
- **Recomendado:** B — dar margem de escolha, não obrigar a gravar todo card.

### 6. Telegram
- **Bot novo** (BotFather): nome a definir (`@foryoucode_content_bot`?)
- **Canal novo** dedicado pra ela (não usar o da Infinity Content do José)
- Bot precisa ser admin do canal pra entregar callback_query
- Webhook próprio (`/telegram-webhook` na URL do Worker novo)

### 7. Repo + Worker
- Repo novo: `ynwwilson/leticia-content` (ou nome que José preferir)
- Worker novo: `leticia-content.ynwwilson.workers.dev`
- D1 novo: `leticia-content` (banco separado — não compartilhar com infinity, dedup/topic ficariam confusos)
- Secrets: ANTHROPIC_API_KEY (compartilhável), OPENAI_API_KEY (compartilhável), TELEGRAM_BOT_TOKEN (novo), TELEGRAM_CHANNEL_ID (novo), RUN_KEY (novo), GITHUB_PAT (opcional — só se manter fontes GH)

## O que vai ser COPIADO sem mudança
- Schema base (`schema.sql`)
- `cycle.ts` (lógica de orquestração, merge de tópicos, frescor 48h, status diário)
- `db.ts`, `llm.ts`, `telegram.ts`, `index.ts`
- `pipeline.ts` → estrutura igual; só `CLASSIFY_SYSTEM` e categorias mudam
- Motor de corroboração (3+ fontes = HOT) — funciona pra qualquer tipo de conteúdo
- Loop de aprendizado por 👍/👎
- Dry mode (`/run?key=...&dry=1`)
- Endpoints `/health`, `/run`, `/telegram-webhook`, `/setup-webhook`

## Estado / fase de execução
**Fase atual: planejamento.** Nada construído ainda. Bloqueadores listados em "Pendências".

Plano de fases após desbloqueio:
1. **Fontes**: implementar `sources.ts` com as fontes definidas
2. **Filtro**: escrever `CLASSIFY_SYSTEM` novo, testar com 50 itens reais em dry-run
3. **Roteiro**: escrever doc de regras do perfil ForYou Code e embarcar como `roteiro-rules.ts`
4. **Deploy**: criar Worker + D1 + bot + canal, rodar primeiro ciclo em dry
5. **Validação**: 3 dias rodando com Leticia gravando os cards e dando feedback
6. **Ajuste fino**: refinar prompts e fontes pelos primeiros resultados reais

## Pendências bloqueantes (pra desbloquear precisa do José)
1. **Lista de fontes** — José disse que vai mandar. Sem isso, `sources.ts` não fecha.
2. **Documento de regras de hook/roteiro do perfil ForYou Code** — não existe no vault hoje. Análogo de [[Regras de hook roteiro e tom para conteudo da ForYou Code]] (que é do José). Precisa ser escrito do zero, com tom institucional/empresário, OU José decide reaproveitar trechos.
3. **Nome do repo e do bot Telegram** — `leticia-content` é proposta minha; José decide.
4. **Canal Telegram dela** — criar canal novo ou usar existente? Quem mais entra? Só Leticia, ou José/Marco também?
5. **Categorias finais** — confirmar `noticia-ia | case-empresa | dado-mercado | alerta-saas | tendencia | aplicacao-vertical` ou ajustar.
6. **Cadência: A (2×3) ou B (6×4)?** — recomendei B.

## Pendências não-bloqueantes (decidir antes do deploy)
- ICP vertical do bot: foca no ICP atual ([[Pacote inicial ForYou MVP (sites R$1.500-2.000)]] = saúde/estética), ou cobre vertical amplo desde o início?
- Mensagem de status diário no canal: replicar o do Infinity ou ajustar layout?
- Limite de itens novos por ciclo (`MAX_NEW_PER_CYCLE` no Infinity = 45) — manter ou ajustar?

## Histórico da decisão
- **2026-05-27 15h26** — Sessão Claude Nova `f253da0a` (José). Mestre perguntou se eu conhecia o Infinity Content; depois pediu *"fizemos atualizações que mudaram algumas coisas, veja tudo"* — analisei o repo `ynwwilson/infinitycontent`, 9 commits (último em 21/05), li o código atual.
- **2026-05-27 15h31** — Mestre: *"Apenas precisamos fazer algo parecido para a leticia, um bot pra ela do mesmo jeito. mas claro, coisas diferentes"*.
- **2026-05-27** — Definido: replicar arquitetura, trocar fontes/filtro/roteiro/canal, manter cards + clique gera dossiê.
- **Próximo passo:** José manda fontes e referências.

## Relacionado
- [[Infinity Content]] — espelho técnico (José)
- [[Infinity Content - arquitetura tecnica]] — referência de implementação
- [[Conteúdo ForYou Code (Leticia)]] — operação maior em que esse bot encaixa
- [[Leticia]]
- [[Plano Comercial ForYou Code 2026]]
- [[Cada socio da ForYou Code tem persona e estrutura de roteiro propria e intransferivel]]
