---
tipo: prd
tags: [foryoucode, conteudo, infinity-content, painel, dashboard]
atualizado: 2026-06-09
status: EM ESTUDO (não iniciado — Mestre quer estudar e conversar mais antes de construir)
---

# Infinity Content — Painel / Centro de Comando (PRD vivo)

> Documento de estudo. Mestre quer **tudo** (4 pilares) e decidir plataforma depois.
> NÃO construir até ordem explícita. Refinar conversando.

## Visão

Centro de comando de conteúdo: tudo que Mestre faz pelo Telegram + métricas reais de
Instagram + inteligência de "o que performa" + automação + organização. Fecha o ciclo:
**tema → roteiro → gravou → postou → views reais → o sistema aprende o que rende.**

Paridade total com o Telegram (toda ação também no painel) + camada de dados/métricas/
automação que o Telegram não dá.

## Os 4 pilares (todos prioridade — Mestre marcou os 4)

### 1. Métricas Instagram profundas
- **Conta:** seguidores (total, curva, ganhou/perdeu/dia, velocidade), alcance, impressões, visitas ao perfil, cliques, % alcance de não-seguidores, contas engajadas, taxa de engajamento (tendência).
- **Por Reel:** views/plays, likes, comentários, shares, **saves**, alcance, **retenção** (curva), tempo médio, replays, **seguidores ganhos pelo Reel**, visitas ao perfil vindas dele.
- **Cortes:** ranking melhores/piores; por categoria (lançamento×tutorial×humor), tom, fonte do tema, horário, hashtag; comparação vs média / vs 30d.

### 2. "O que performa pra mim" (killer feature)
- Cruza views reais × atributo do tema (categoria, tom, estilo de hook, fonte, horário).
- Saída: "lançamento rende 2,3× a média · tutorial 0,7× · hook por número performa menos que hook pela jogada · melhor horário 19h".
- Vira **predição**: cada tema novo chega com **score de performance prevista** do histórico real. Substitui o palpite por dado.
- Conecta com a afinidade que já existe (gravei/pulei) — agora ponderada por performance real, não só por gravou.

### 3. Automação & controle
- Agendar Reel (fila com legenda pronta → post via Meta API OU lembrete + 1 clique).
- Pull automático das métricas IG (cron diário).
- Regras ("lançamento oficial + 3 fontes → gera dossiê sozinho").
- Ações em lote (gerar dossiê / descartar vários).
- Brief da manhã (top 3 temas + performance do Reel de ontem).

### 4. Organização / pipeline
- **Kanban de produção:** ideia → roteiro → gravado → editando → postado (arrasta).
- **Calendário:** gravado / agendado / postado.
- Abas/subabas, busca, filtros, views salvas, tags.
- Subabas pedidas por Mestre: **Gravados / Não gravados** (com motivo do pulei).

## Estrutura de navegação (abas → subabas)
- **Dashboard** — KPIs macro (backlog, gravados/semana, taxa, melhor Reel, alcance, custo).
- **Conteúdo** — Temas (backlog) · Roteiros · Gravados · Não gravados · Postados.
- **Métricas** — Instagram · Conteúdo (funil, fonte, aproveitamento) · Aprendizado (afinidade, motivos, padrões).
- **Ações** — gerar temas · dossiê · buscar · link · print→roteiro · gravei/pulei · padrão.
- **Fontes** — 12 fontes, on/off, add handle/blog/sub.
- **Config** — cron, regras de roteiro, keys.

## Arquitetura (rascunho)
| Camada | O quê |
|--------|-------|
| Cérebro/API | Worker + D1 atual vira a API REST (já tem temas/dossiês/feedback/exemplos) |
| Novos dados | `reels` (dossiê↔post IG↔métricas), `metricas_snapshot` (diário por reel + conta), `agenda` (posts agendados), `pipeline` (estado kanban) |
| Instagram | Meta Graph API — insights (ler) + content publishing (postar) |
| Cara | SPA glassmorphism dark (plataforma A DECIDIR — Lovable / Next-Vercel / Worker) |
| Coleta IG | cron diário puxa métricas de cada Reel + conta |
| Auth | login simples (Mestre é o único usuário) |

## Fases sugeridas
- **Fase A — Controle + métricas de conteúdo** (zero dependência externa): painel lê/controla o que já existe (temas, dossiês, gravados/não, ações, fontes, funil, aproveitamento). Sai rápido.
- **Fase B — Instagram** (depende de setup Meta): pull de métricas por Reel + conta, linkar Reel↔dossiê, cortes por atributo.
- **Fase C — Inteligência**: "o que performa pra mim" + score de predição.
- **Fase D — Automação de post**: agendar + publicar via Meta API.

## ⚠️ O QUE PRECISA SER ESTUDADO (dependências / decisões)

1. **Acesso à Meta Graph API (CRÍTICO — gating de tudo do IG):**
   - Conta IG **Business ou Creator** ligada a uma **Página do Facebook**.
   - **App no Meta for Developers** + permissões: `instagram_basic`, `instagram_manage_insights` (métricas), `instagram_content_publish` (postar).
   - **App Review da Meta** pra liberar permissões além do modo dev — tem fricção/prazo.
   - Estudar: qual conta IG do José, já é Business/Creator?, tem Página ligada?, criar o app.
2. **Linkar Reel ↔ dossiê:** manual (casar na hora de postar) vs automático (puxar mídias recentes do IG e casar por legenda/horário). Definir.
3. **Postar automático vs lembrete:** content publishing API tem specs de vídeo + rate limit. Decidir se vale o automático ou começar com lembrete+1clique.
4. **Onde os dados moram:** D1 (atual, é o cérebro) vs Supabase (fluxo Lovable). Se Lovable, reconciliar — provável: D1 continua cérebro, painel bate na API do Worker.
5. **Plataforma da cara:** Lovable (rápido/bonito) × Next-Vercel (robusto) × Worker (1 deploy). Mestre vai decidir depois.
6. **Multi-plataforma futura:** TikTok / YouTube Shorts têm APIs próprias — fase posterior.

---

# Banco de ideias — ideação multi-lente (2026-06-09)

> Workflow de 6 especialistas (automação, analytics, formato, roteiro, crescimento, operação) → 87 ideias → sintetizadas. Ideias NOVAS além do PRD acima. Material de estudo.

## 🔁 1. Reaproveitamento & Multi-formato
- **Estúdio Multi-formato (1 tema → N)** — botão no dossiê transpõe o ângulo em carrossel, thread X, Stories, outline de vídeo longo, cada um no tom lofi. *(médio)*
- **Gerador de Carrossel lofi** — carrossel estruturado (hook+corpo+CTA) com preview; formato mais "salvável" do IG. *(médio)*
- **Banco de Ângulos Descartados** — o refugo que a regra de ouro corta vira backlog taggeado por pilar. *(baixo)*
- **Planejador de Cortes (longo↔curtos)** — case/live denso → 2-3 cortes independentes. *(médio)*
- **Reciclador de órfão/evergreen** — dossiê não-gravado em 10-14d é reescrito perecível→evergreen; evergreen antigo volta remixado. *(médio)*
- **Resumo semanal → peça publicável** — "a semana da IA em 60s" / carrossel "5 novidades". *(baixo)*

## 🤖 2. Automação de publicação & engajamento (Meta API)
- **First-comment automático + fixar** — planta o comentário do autor (link/contexto fora da legenda) no segundo 0. *(médio)*
- **DM por palavra-chave / lead magnet** — "comenta CODE" → DM automática + lead no D1. Mecânica do ManyChat nativa → captação ForYou Code. *(médio)*
- **Inbox de comentários com resposta no tom José** — LLM redige resposta lofi; auto-envia as seguras, manda as delicadas pro Telegram. *(médio)*
- **Alerta de 1ª hora fria** — velocidade abaixo da média nos 60min → "tá esfriando, responde agora" + iscas. *(médio)*
- **Sprint de lançamento autônomo** — drop grande → pacote de 3 peças (reação/tutorial/hot-take) em 48h. *(médio)*
- **Freio de mão "não postei hoje"** — passou do horário → promove melhor roteiro + oferece agendar. *(baixo)*
- **Cross-posting adaptado** — Shorts/TikTok/Bluesky por plataforma. *(alto — APIs externas)*

## 📊 3. Analytics anti-hype (métrica que vira decisão)
- **Funil de produção real** — coleta→aprovado→gravado→postou→bateu; mostra onde os temas morrem. *(baixo)*
- **Save-rate como métrica-norte** — rankeia por saves+shares/mil views, não views. *(baixo)*
- **Cohort de fonte → performance** — qual fonte gera Reel que performa, pra realocar peso da coleta. *(médio)*
- **Radar dos 7 pilares (mix × performance)**. *(médio)*
- **Detector de outlier + post-mortem** — Reel >2σ é flagado e o LLM explica o porquê → vira regra. *(médio)*
- **Benchmark z-score contra si mesmo** (mediana móvel 30d). *(baixo)*
- **Atribuição de seguidores por Reel** — o que RECRUTA vs o que só entretém. *(médio)*
- **Custo por Reel postado** · **Heatmap do firehose** (picos de coleta → gravar em lote). *(médio/baixo, sem Meta)*

## 🎣 4. Loop de roteiro/hook que aprende sozinho
- **Hook Arena + Hook DNA** — marca o hook gravado; 48-72h depois puxa watch-time, calcula win-rate por alavanca, injeta vencedores no prompt. *(médio)*
- **Editor com diff que vira exemplo-de-ouro** — toda edição salva o diff e promove a few-shot, sem depender do reply "padrão". *(médio)*
- **Linter lofi do roteiro** — sublinha clichê de IA/lacração/jargão em tempo real + score. *(baixo)*
- **Botões de tom (dials)** — regenera SÓ um eixo (+lofi, +cybersec, mais curto, mais polêmico). *(baixo)*
- **Ouvir antes de gravar (TTS)** · **Cronômetro de fala 50-60s**. *(baixo)*
- **Retenção → roteiro pelo print (vision)** — sobe o gráfico de retenção, a IA acha o segundo da queda → frase a reescrever. *(médio)*
- **Mesmo tema, 7 pilares** lado a lado. *(baixo)*

## 🎛️ 5. Operação & controle
- **Sync bidirecional Telegram ↔ painel** — uma fonte de verdade. *(baixo)* — pré-requisito de adoção.
- **Versionamento de roteiro com diff** ("volta pra essa"). *(médio)*
- **Busca universal FTS5** (nativo D1) · **Smart views (filtros salvos)**. *(médio/baixo)*
- **Modo foco de gravação** — teleprompter mobile + gravei/refazer/próximo. *(médio)*
- **Cofre de assets + b-roll (R2)** · **Undo + lixeira** · **Timeline/auditoria** · **Painel de saúde operacional**. *(vários)*

## 📅 6. Cadência, mix & crescimento
- **Balanceador dos 7 pilares** — campo `pilar` + alerta de desvio ("70% trends, 0% humor"). *(médio, sem Meta)*
- **Lote noturno de roteiros prontos por pilar** — acorda com 3-4 roteiros prontos pra câmera. *(médio)*
- **Calendário pilar-dia** · **Streak/metas sóbrias** · **Nudge de perecível esfriando** · **Melhor horário aprendido do histórico**. *(vários)*
- **Audiência como fonte de pauta** (clusteriza comentários → cards) · **Séries/franquias** · **Efemérides de IA** · **Espião de pares/colab**. *(vários)*

## 🏆 TOP 5 KILLER
1. **Estúdio Multi-formato (1 tema → N)** — ataca o gargalo nº1 (produção). 1 pesquisa vira a semana toda.
2. **Loop de hook/voz auto-aprendiz** — calibra as ROTEIRO_RULES pelo desempenho real; ativo que mais valoriza com o tempo.
3. **Balanceador dos 7 pilares** — protege o posicionamento multifacetado (a regra de ouro vira métrica). Barato.
4. **DM lead-magnet + first-comment** — único elo direto conteúdo→negócio ForYou Code.
5. **Lote noturno de roteiros prontos** — entrega pronto pra câmera, não lista. Mata o atrito que mata a máquina.

## ⚡ QUICK WINS
Linter lofi · Banco de ângulos descartados · Smart views · Botões de tom · Funil de produção. (+Sync Telegram↔painel)

## 🕳️ ÂNGULOS QUE FALTAVAM (os mais frescos)
1. **Atribuição de negócio** — CRM-lite no D1: qual Reel → DM → conversa → cliente fechado. Vale mais que views.
2. **Fala-solta → roteiro (voice-input)** — José manda áudio, IA transcreve+estrutura no tom dele. Matéria-prima mais autêntica, mata o "soa decorado".
3. **Guard-rails da automação (AppSec aplicado a si)** — rate-limit, kill-switch, sandbox de aprovação, detector de shadowban. Automação que posta/comenta/DM sozinha pode derrubar a conta. Especialidade dele, risco silencioso.
4. **Preview do grid 3×3** — ver os próximos 9 posts montados antes de agendar (coerência estética lofi).
5. **Content runway + ativo owned** — medidor "X dias de conteúdo na pista" (anti-burnout) + captura de email (não depender 100% do algoritmo).

## Links
- [[Infinity Content]]
- [[Infinity Content - plano de execução]]
- [[Infinity Content - pendências]]
