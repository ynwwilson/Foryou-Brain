---
tipo: projeto
tags: [foryoucode, conteudo, jose, infinity-content, automacao]
atualizado: 2026-05-27
---

# Infinity Content — máquina de dossiês de conteúdo

> Máquina **sob demanda** que vigia ~25 fontes de novidades de IA, filtra o que vale virar Reels, e entrega **dossiês prontos pra gravar** no Telegram de José. Ele toca um botão → recebe 5 cards → escolhe quais quer → recebe dossiês completos. Construída em 2026-05-20/21. Refatorações: 2026-05-23 (polling → webhook), 2026-05-26 (fontes + corroboração), **2026-05-27 (cron desligado, botão sob demanda, feedback por botão, controle de custo)**.

## O que é

A Infinity Content alimenta o **pilar de news/skill/tutorial** do canal do José (@ynwwilson) de forma automática. Os pilares de humor, case e bastidor continuam vindo do sistema manual em [[Conteúdo José]] — a máquina não substitui aquilo, complementa.

## Onde roda

| Item | Detalhe |
|---|---|
| Hospedagem | Cloudflare Worker + D1 (banco). **Cron desligado em 2026-05-27** — geração 100% sob demanda. |
| Código | `C:\Users\ynwwi\Projetos\infinitycontent` |
| Repositório | github.com/ynwwilson/infinitycontent (privado) |
| Worker URL | https://infinitycontent.ynwwilson.workers.dev |
| Entrega | Canal Telegram "Infinity Content" · bot `@infinitycontent_bot` |
| Cérebro (LLM) | Anthropic (primário) · OpenAI (fallback) |
| Endpoints | ver [[Infinity Content - arquitetura tecnica]] |

## Como funciona — o fluxo (versão 2026-05-27)

1. **Disparo manual:** José toca no botão fixo **"🔄 Gerar Temas Agora"** (mensagem fixada no canal, `id 225`).
2. **Cards:** 5 cards aparecem no canal, cada um com botão **📝 Gerar dossiê**. Quase sempre vêm do backlog (em ~1s, sem chamar IA — atalho de custo). Se o backlog esvaziar, busca conteúdo novo (~1 min, chama IA).
3. **Escolha:** José lê os 5 cards e toca em "Gerar dossiê" nos que quer gravar.
4. **Dossiê** (webhook em tempo real): o clique gera o dossiê (Sonnet + busca web) e posta no canal em **~30s**.
5. **Feedback:** cada dossiê novo vem com `[👍 Gravei] [👎 Pulei]` — José marca, o sistema aprende com o tempo.

**Sem cron, sem teto.** Toda vez que clica, 5 temas. Pode clicar 1x por dia ou 10x. Só paga quando gera dossiê de verdade.

> Cards e backlog atuais: 47 cards na fila esperando, 52 itens aprovados de reserva. Estoque alto — primeiros cliques saem instantâneos sem chamar IA nenhuma.

## Limites de produção (versão 2026-05-27)

**Clique manual:** sempre **5 cards por clique**, sem teto. José controla a frequência.

**Cron (desligado, mas se reativado):** tetos antigos seguem definidos no código:
- Lançamentos/notícias (`perecivel` + `rumor`): 10/dia rolling 24h
- Skills/plugins/métodos/prompts (`estavel`): 1/ciclo

Esses tetos **só valem se o cron for reativado**. Em clique manual, são ignorados — você sempre recebe 5 (ou menos, se o estoque de tema novo de IA estiver vazio mesmo).

## Fontes (~25, reformadas em 2026-05-26)

- **Blogs oficiais (RSS)**: OpenAI, Anthropic, claude.com, Google AI, Google DeepMind, Microsoft AI, Hugging Face, GitHub, Vercel, Cursor, Lovable, Replit, Together AI
- **Jornalismo de IA (RSS)**: **The Decoder, TechCrunch AI, VentureBeat AI** — cobrem lançamento de qualquer empresa (Mistral, xAI, Perplexity, Runway…) com data e resumo. Resolve "lançamento não aparecia".
- **YouTube (RSS gratuito por canal)**: Anthropic, OpenAI, Mistral, Perplexity, xAI, ElevenLabs, Runway, Stability, Lovable, Cursor, Replit, DeepMind + criadores (Matt Wolfe, Matthew Berman, AI Explained). Demo de lançamento sai aqui antes do blog.
- **Bluesky (API pública)**: Simon Willison, Ethan Mollick, swyx, Matt Wolfe, ElevenLabs, Karpathy — sinal antecipado dos criadores que migraram do Twitter.
- **Product Hunt**: ferramentas novas com votos reais (tração = gente usando).
- **GitHub**: releases (Claude Code, Codex, Cline) + skills/MCPs **com tração** (stars altos + ativos — não mais "criado essa semana").
- **Hacker News**: notícias de IA + Show HN
- **Hugging Face**: modelos novos com tração
- **Busca web**: livre, na hora de escrever cada dossiê (resolve o corte de conhecimento do modelo)
- **Scrape best-effort**: Mistral, ElevenLabs (sem RSS oficial)
- **Twitter/X**: Fase 2 (precisa conta + RSSHub auto-hospedado)

## Filtro e regras

- **Barra de Reels**: descarta release de manutenção, bugfix, plumbing, incremento vazio, notícia corporativa operacional e coisa nichada demais. Conteúdo técnico-acessível passa.
- **Frescor**: novidade/lançamento/atualização só passa com data comprovada nas **últimas 48h**; sem data confiável = cortado. Skill, plugin, método e prompt não têm limite de idade.
- **Sem repetir assunto**: dedup por tópico (janela rolling 14 dias) — nunca 2 dossiês da mesma novidade.
- **Corroboração / "o que todo mundo fala"**: conta quantas fontes distintas falam do mesmo assunto. 3+ fontes = HOT, ganha destaque "🔥 ALTA REPERCUSSÃO" e sobe na fila. Assunto de fonte única e obscura afunda. É o que faz lançamento grande emergir e skill que ninguém usa sumir.
- **Roteiro**: gerado no padrão de [[Regras de hook roteiro e tom para conteudo da ForYou Code]] — 6 etapas, hook no segundo 1-2, linguagem simples, tela rachada, vídeo oficial pra tela de cima.
- **Loop de aprendizado**: cada dossiê novo sai com botões `[👍 Gravei] [👎 Pulei]` (desde 2026-05-27). Clique no botão grava no DB e ajusta o gosto da máquina com o tempo. **Por que botão e não emoji:** reação emoji em canal é anônima/agregada — o Telegram não entrega a reação per-usuário ao bot. O botão usa callback_query (mesmo caminho do "Gerar dossiê"), que funciona perfeito.

## Status e custo

- Mensagem diária de status no canal: desativada com o cron (era postada no ciclo das 00h BRT). Pode ser reativada se quiser.
- **Custo (revisado 2026-05-27):**
  - Baseline: **R$0** (sem cron rodando sozinho)
  - Por clique: **R$0** quando serve do backlog (a maioria dos casos)
  - Por refetch (quando backlog esvazia): ~US$0,10, reabastece pra ~18 cliques grátis
  - Por dossiê: ~US$0,10–0,15 (Sonnet + busca web)
  - Total esperado: muito abaixo de R$150/mês, proporcional aos dossiês que José realmente pedir.

## Fora do escopo atual (Fase 2)

- **Twitter/X em tempo real** — daria timing de primeira-mão em lançamentos; depende de API paga.
- **Instagram** — monitorar perfis exigiria navegador automatizado.
- **Entrega do lead magnet** ("comenta X") — José resolve manualmente no ManyChat (mensagem + link).
- **Regras de roteiro ao vivo** — bloqueado: o doc de regras precisa estar sincronizado no GitHub do vault; hoje as regras estão embarcadas no código.

## Links

- [[Infinity Content - arquitetura tecnica]] — endpoints, deploy, como debugar
- [[Infinity Content - reforma 2026-05-27 (botão sob demanda + custo + feedback)]] — última reforma, log completo
- [[Infinity Content - pendências]] — itens em aberto
- [[Infinity Content - reforma 2026-05-26 (log completo)]] — reforma anterior (fontes + corroboração)
- [[Conteúdo José]]
- [[Regras de hook roteiro e tom para conteudo da ForYou Code]]
- [[Mapa do sistema de conteudo]]
- [[Cada socio da ForYou Code tem persona e estrutura de roteiro propria e intransferivel]]
