---
tipo: knowledge
tags:
  - foryoucode
  - cases
  - vendas
  - prova-social
  - proposta
atualizado: '2026-05-21'
---

# Cases ForYou Code (consolidado para vendas)

> **Formato proposta-ready.** Os 3 cases lado a lado, com tudo que vendedor/proposta/site precisa em um só lugar. Substitui ter que abrir 4 notas diferentes pra montar pitch.

> **Fonte canônica:** detalhes técnicos completos em `knowledge/Catalogo de entregas ForYou Code.md`. Esta nota foca em **comunicação comercial** dos cases.
>
> **Posicionamento:** ver [[Posicionamento ForYou Code]]. Os cases devem provar que a ForYouCode não faz apenas app, CRM ou automação. Ela transforma operações reais em sistemas proprietários sob medida.

---

## Como apresentar os cases

Não apresentar como lista de funcionalidades.

Apresentar como transformação operacional:

- **Dayane:** escola com operação pedagógica inteira transformada em plataforma multi-perfil.
- **Concretize:** atendimento e venda pelo WhatsApp transformados em inteligência comercial com painel e takeover humano.
- **Smartcell:** venda online de eletrônicos transformada em e-commerce proprietário com pagamento, IA, admin e financeiro.
- **ForYou Leads:** prospecção ativa transformada em máquina com scraping, IA, DM, vídeo, pipeline, métricas e alertas.
- **Imerso:** visita imobiliária transformada em tour 3D navegável no celular.
- **Infinity Content:** pesquisa de novidades e criação de conteúdo transformadas em máquina de dossiês com web search e fontes reais.

Frase guia:

> A ForYouCode não entrega telas. Entrega sistemas que assumem partes reais da operação.

---

## Resumo de uma linha

| # | Cliente | O que é | Modelo | Status |
|---|---|---|---|---|
| 1 | **Concretize / Rodrigo** | IA de atendimento WhatsApp + painel + CRM | R$2.500 único + R$1.500/mês marketing | Em produção |
| 2 | **Rainha da Aprovação / Dayane** | Plataforma educacional multi-perfil | R$27.000 fechado | Entregue 20/03/2026, manutenção ativa |
| 3 | **Smartcell / Fellipe** | E-commerce premium com PIX automático e IA | 20% participação nos lucros | Entregue 25/04/2026, em produção |

---

## Case 1 — Concretize / Rodrigo

### One-liner
*"Construímos uma IA de atendimento que não é bot — é painel completo onde o dono vê cada lead, as objeções mapeadas e o raciocínio da IA antes de cada resposta."*

### Cliente
Rodrigo — Concretize Pré Moldados (fábrica de pré-moldados, construção civil B2B).

### Problema resolvido
Vendedor demorava pra responder e perdia venda. Marketing ficava cego — sem dados das conversas, não dava pra otimizar campanha. Os dois problemas em um só ciclo.

### O que entregamos
- IA respondendo leads 24h com contexto da Concretize
- Painel branded com funil visual de leads
- Objeções mapeadas automaticamente
- Histórico completo na tela ao assumir conversa
- Botão de pausar IA + assumir com humano
- Dados de conversa integrados ao marketing
- Capacidades técnicas: visão (analisa fotos), voz (transcreve áudio), mirroring de estilo, fatiamento em balões

### Stack
Vercel (webhook resiliente) + MegaAPI (WhatsApp) + Chatwoot self-hosted (atendimento) + Supabase + Upstash Redis (dedup, fila, lock por telefone) + Anthropic Claude (texto + visão) + OpenAI Whisper (áudio).

### Status
Em produção. Webhook publicado, dashboard ao vivo, instância MegaAPI conectada e validada. Manutenção ativa.

### Valor
R$2.500 (preço promocional — valor correto seria R$12-18k). Não divulgar valor.

### Asset visual para venda
Painel mostrando: lead chegando ao vivo → funil visual → objeção mapeada → contexto do lead → botão de pausar/assumir com histórico.

### Pitch pronto
> "A gente pegou um cliente que tinha 40, 50 mensagens por dia no WhatsApp e não conseguia responder tudo a tempo. Ele perdia venda por demora. A gente construiu uma IA que responde, qualifica e manda pro funil certo — mas o diferencial real não é a IA em si. É o painel: o dono abre e vê cada lead pelo nome, as objeções que a pessoa levantou, o que a IA respondeu e o raciocínio por trás. Se quiser entrar na conversa, clica e assume com o histórico completo na tela. E no final do mês, todos os dados de atendimento alimentam o marketing — sabe quais objeções aparecem mais, qual perfil fecha mais, qual horário converte melhor. Não é bot. É inteligência de vendas."

### ICP para clonar este case
Negócio com 30+ conversas/mês no WhatsApp, ticket médio R$500+, fatura R$50k+/mês, perde venda por demora, quer controle além de automação. Nicho amplo.

---

## Case 2 — Rainha da Aprovação / Dayane

### One-liner
*"Entregamos uma plataforma educacional completa para uma escola com 200+ alunos — app do aluno, painel do professor, dashboard executivo do diretor, tudo num só sistema com a marca deles."*

### Cliente
Dayane Alemar — Salinha / Rainha da Aprovação (escola física com 200+ alunos, foco em vestibular/ENEM).

### Problema resolvido
Escola dependia de várias ferramentas genéricas (sistema de questões de um lugar, comunicação de outro, gestão de turma de outro), nenhuma com a marca, todas mensalidade. Diretora não tinha visão real do desempenho de cada aluno.

### O que entregamos
**Plataforma multi-perfil com 4 áreas distintas:**

**Aluno:** dashboard, banco de questões, simulados, caderno de erros automático, flashcards, planner, redação, ranking, retry list.

**Professor:** correção de redação, gestão de turma, banco de questões, análise individual de aluno, materiais.

**Diretor:** dashboard executivo, **X-Ray do aluno** (evolução + erros + heatmap), análise de retenção, contratos, assinaturas, broadcast, Hall of Fame.

**Admin:** importação em massa de questões, gestão de e-mails.

### Stack
Lovable + Supabase + Vercel + Cloudflare + Autentique. Construído solo via vibe coding pelo José.

### Status
**Entregue em 20 de março de 2026.** Em produção em https://metodorainhadaaprovacao.vercel.app (migração futura pra `metodorainhadaaprovacao.com.br`). Manutenção ativa — correções e aprimoramentos contínuos até hoje. Dayane não paga mensalidade — só infraestrutura.

### Valor
R$27.000 (valor correto seria R$50k+). **Não divulgar valor**.

### Autorização
**Liberado como case público** — nome, marca e plataforma. Restrição: não mencionar valor cobrado.

### Asset visual para venda
Demo de 3 minutos: fluxo do aluno (simulado → caderno de erros → flashcard) → painel do professor (análise individual) → dashboard do diretor (X-Ray + retenção + contratos). Plataforma ao vivo em https://metodorainhadaaprovacao.vercel.app.

### Pitch pronto
> "A gente acabou de entregar uma plataforma completa pra uma escola com 200 alunos. O aluno entra e tem banco de questões, simulados, caderno de erros, flashcard, planner. O professor tem painel de turmas, correção de redação, análise individual. A diretora tem dashboard executivo, retenção, contratos, e o X-Ray de cada aluno. Tudo numa plataforma só com a marca deles. Isso é o que a gente faz."

### ROI defensável
Escola com 200 alunos × R$800/mês = R$160k/mês. Churn 10%/ano = 20 alunos perdidos = R$192k em risco. Plataforma reduz 30% do churn = R$57.600 preservado/ano. Investimento R$30k → break-even em 6 meses.

### ICP para clonar este case
Escolas, cursinhos, preparatórios, idiomas, escolas técnicas com 150+ alunos recorrentes, faturamento R$100k+/mês, base recorrente, dono decide.

---

## Case 3 — Smartcell Premium Store / Fellipe

### One-liner
*"Construímos um e-commerce premium completo com PIX automático, IA gerando descrição e imagem de produto e painel admin de 13 módulos — em modelo de participação nos lucros, sem cliente pagar projeto."*

### Cliente
Fellipe — Smartcell Premium Store (e-commerce de eletrônicos premium em Patos-MG: iPhone novos/seminovos, Mac, iPad, Watch, AirPods, Xiaomi, acessórios).

### Problema resolvido
Cliente queria loja online própria com a marca dele, mas sem capital pra fechar projeto pré-pago. ForYou Code aceitou modelo de participação porque o nicho tem volume e margem.

### O que entregamos
**Loja pública (26+ rotas):**
- Hero com vídeo background + parallax
- Catálogo dinâmico com filtros, comparador, lightbox, busca global
- Schema dedicado para seminovos (bateria %, IMEI, checklist 30 itens)
- Compartilhamento de imagem por modelo+cor entre condições
- Carrinho persistente em localStorage
- Frete por região MG (Patos R$9 / Triângulo R$40 / grátis >R$1.000)
- Checkout em 4 etapas com ViaCEP
- **PIX automático** (Mercado Pago + polling 5s + webhook)
- **PIX/Boleto Asaas**
- Finalização via WhatsApp `wa.me`
- Cupons + welcome popup + urgency triggers + recuperação de carrinho
- Reviews, comparador, favoritos, notify-me
- PWA com service worker

**Painel admin (13 módulos):**
Dashboard, Produtos, **Seminovos** (com IMEI/bateria/checklist), Pedidos com WhatsApp templates, CRM, **Financeiro com split de sócios** (José/Marco/Eduardo soma 100%), Categorias, Banners, Galeria, Avaliações, Usuários, Notificações, Jobs IA.

**IA & Automações (8 edge functions):**
Geração de descrição de produto, geração de imagem por cor (Gemini Image), fila de jobs IA, fallback Gemini ↔ GPT.

### Stack
Lovable + Lovable Cloud (Supabase) + Lovable AI Gateway (Gemini 2.5 + GPT-5) + Mercado Pago + Asaas + ViaCEP + WhatsApp `wa.me` + PWA. **Não tem MegaAPI** (checkout via wa.me direto).

### Status
**Entregue 25/04/2026.** Em produção em https://smartcellsite.com.br. Faturamento ainda em construção (loja recém-finalizada).

### Modelo
**20% participação nos lucros, sem fee de projeto.** Manutenção e evolução incluídas no acordo — "fazemos o que for preciso, sem mais nada a ser pago ou contratado".

### Asset visual para venda
Demo de 3 min: hero com vídeo → navegação na loja → fluxo PIX automático no checkout → painel admin completo → IA gerando descrição e imagem de produto.

### Autorização
Fellipe autorizou nome, marca e número (553438212212) como case público. Liberado para 4º asset gravado de venda.

### Pitch pronto
> "A gente construiu uma loja completa de eletrônicos premium em modelo de participação. Sem fee de projeto. PIX automático no site, IA gerando descrição e imagem de produto, schema dedicado pra seminovos com IMEI e checklist de 30 itens, painel admin com split de sócios. Tudo no domínio dele, com a marca dele. A gente entrega o ecossistema, ele toca a operação. Quando ele vende, a gente ganha. Quando ele cresce, a gente cresce junto."

### ICP para clonar este case
Varejo / e-commerce premium com volume regional, ticket médio R$1.000+, dono que quer marca própria, ou cliente sem capital de projeto fechado mas com volume e margem (modelo de participação).

### Atenção contratual (modelo de participação)
Modelo arriscado se cliente não tem volume real. Para próximos clientes do nicho, **preferir projeto fechado R$20-35k + manutenção** e participação só como complemento. Smartcell foi exceção com fundamento estratégico (validação de nicho + caso de sucesso pra portfólio).

---

## Comparação rápida (matriz)

| Dimensão | Concretize | Rainha da Aprovação | Smartcell |
|---|---|---|---|
| Nicho | Construção B2B | Educação | E-commerce varejo |
| Produto principal | IA atendimento | Plataforma multi-perfil | Loja completa |
| Stack diferencial | MegaAPI + Chatwoot + Redis | Multi-login + X-Ray | PIX automático + IA imagem |
| Tempo de entrega | ~3 semanas | ~10 semanas (estimativa) | ~12+ semanas |
| Modelo comercial | Único + recorrente | Único | Participação % |
| Status | Em produção | Entregue + manutenção | Entregue + manutenção incluída |
| ROI principal | Receita recuperada (lead que ia escapar) | Retenção de aluno | Volume de venda online |
| Asset visual | Painel de takeover | Dashboard da diretora | Loja + admin com IA |
| Tipo de demo | Live de chegada de lead | Tour por perfil | Compra completa com PIX |

---

## Como usar nesta nota

### Em call de venda
1. Identifique o nicho do prospect
2. Pegue o case mais próximo (Concretize = B2B/serviço, Rainha = recorrente, Smartcell = varejo)
3. Use o **One-liner** + **Pitch pronto** literalmente
4. Mostre o **Asset visual** correspondente
5. Quando entrar preço, use o **ROI defensável** ou **fórmula** do plano comercial

### Em proposta escrita
- Anexar a seção "O que entregamos" do case mais próximo + comparação rápida
- Adaptar o pitch pro nicho do prospect

### Em anúncio / criativo
- One-liner vira hook
- Asset visual vira o B-roll
- Pitch pronto vira VSL

### Em site
- Página de cases (ou página por nicho) puxa direto desta nota
- Headline + asset visual + pitch + ROI

---

## Status de gravação dos assets (Plano Comercial 2026 — Asset 1 a 4)

| Asset | Status | Pendência |
|---|---|---|
| 1 — Painel do Concretize/Rodrigo | A gravar | Agendar dia |
| 2 — App da Rainha/Dayane | A gravar | Marcar dia (autorização já dada). Plataforma em metodorainhadaaprovacao.vercel.app |
| 3 — App próprio ForYou Code | A gravar | Definir o que mostrar |
| 4 — Smartcell Premium Store | A gravar | Marcar dia com Fellipe (autorização já dada) |

**Regra do Plano Comercial:** gravar os 4 em 1 dia. Edição básica — autenticidade vende mais que produção.

---

## Links

- [[Catalogo de entregas ForYou Code|Catálogo completo de entregas]]
- [[Plano Comercial ForYou Code 2026|Plano Comercial 2026]]
- [[ICP da ForYou Code|ICP]]
- [[Processo de vendas da ForYou Code|Processo de vendas]]
- [[Projetos/Smartcell|Smartcell — projeto detalhado]]
- [[Projetos/Rainha da Aprovacao|Rainha da Aprovação — projeto detalhado]]
- [[knowledge/Licoes tecnicas e-commerce Smartcell|Lições técnicas Smartcell]]
- [[knowledge/Guia de Clonagem IA de Atendimento|Manual de clonagem IA — Concretize]]
- [[atlas/Mapa de clientes|Mapa de clientes]]
