---
title: "Smartcell — Plano de crescimento"
type: plano
created: 2026-05-27
projeto: Smartcell
tags: [smartcell, crescimento, trafego-pago, vip, instagram, foryoucode]
status: em-execucao
---

# Smartcell — Plano de crescimento

> **Tese-mãe:** site nacional > loja física no médio prazo. Ver [[Projetos/Smartcell - Tese estrategica|Tese estratégica]] como documento que governa este plano.
>
> Objetivo deste plano: transformar audiência existente (28k IG + 1k VIP) em pedidos **nacionais** no smartcellsite.com.br, e usar R$ 2k/mês de tráfego pago pra escalar o que já funciona.

## Diagnóstico do momento

| Camada | Estado | Gargalo |
|---|---|---|
| Audiência IG | 28k seguidores, stories diários, reels semanais | Tráfego pro site não é medido |
| Grupo VIP | 1.000 pessoas, há muito tempo ativo | Sem rotina de oferta exclusiva — gente parada |
| Site | smartcellsite.com.br em produção, PIX automático | Sem Analytics, sem Pixel — qualquer ads paga é cego |
| Tráfego pago | R$ 2.000/mês disponível | Falta Pixel + catálogo no Meta = dinheiro queimado |
| Conteúdo | Posta rotina, conta consolidada | Vídeos não levam à compra (falta CTA-site nos stories e bio) |

**Tradução:** o problema não é gerar audiência. É **fechar o ciclo "viu → entrou → comprou"**.

---

## PRIORIDADE 0 — Tecnologia que precisa ativar AGORA (essa semana)

Sem isso, todo o resto roda no escuro.

### 0.1. Google Analytics 4 no site
- Criar propriedade GA4 pra smartcellsite.com.br
- Instalar tag global no head do site (Eduardo/Lovable)
- Configurar eventos: `view_item`, `add_to_cart`, `begin_checkout`, `purchase`, `pix_gerado`
- Dashboard básico: tráfego por canal, taxa de conversão, top produtos
- **Tempo:** 1 dia útil

### 0.2. Meta Pixel + Conversions API (CAPI)
- Criar Pixel no Meta Business da Smartcell
- Instalar no site (head global + eventos)
- Configurar CAPI (Conversions API) via Supabase edge function — backup do navegador, essencial pós-iOS 14
- Eventos: `PageView`, `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase`
- **Tempo:** 2 dias úteis (CAPI é o trabalho)

### 0.3. Catálogo Meta Business sincronizado
- Criar Catálogo no Meta Business
- Feed de produtos via XML/CSV do Supabase (edge function que exporta)
- Sincronização automática diária
- Habilitar Instagram Shopping + tags em posts e stories
- **Tempo:** 2-3 dias úteis

### 0.4. WhatsApp Business com catálogo
- Cadastrar produtos top 30 no catálogo do WhatsApp Business
- Mensagem de boas-vindas automática com link do site
- Etiquetas: "Lead VIP", "Comprou", "Visitou site", "Abandonou carrinho"
- **Tempo:** 1 dia útil

### 0.5. UTM em toda comunicação
Padrão fixo pra rastrear origem:
- `smartcellsite.com.br/?utm_source=instagram&utm_medium=stories&utm_campaign=iphone15-set26`
- Link bio: `?utm_source=instagram&utm_medium=bio`
- Grupo VIP: `?utm_source=whatsapp&utm_medium=grupo-vip`
- Ads: `?utm_source=meta&utm_medium=ads&utm_campaign=<id>`
- Marketplace cupom físico: `?utm_source=marketplace&utm_medium=cupom-fisico&utm_campaign=ml-pos-venda`

### 0.6. Integração Melhor Envio (frete nacional)
- Conta na Melhor Envio + API key
- Edge function `calcular-frete-nacional` integrada no checkout
- Regra: **frete grátis acima de R$ 1.000** (decisão Mestre 27/05)
- Abaixo de R$ 1.000: cálculo automático Correios PAC / Sedex via Melhor Envio
- **Tempo:** 3-5 dias úteis

### 0.7. Material físico do canal marketplace
- Cartão Smartcell + cupom R$ 50 OFF (válido só no site) + mini-manual de boas-vindas
- Design + impressão de 1.000 unidades
- **Custo:** ~R$ 800
- **Tempo:** 5-7 dias úteis (design + gráfica)

**Quem implementa P0:** Mestre via Lovable/Claude Code (vocês são os builders) — ou terceirizar com dev externo se a fila do Mestre estiver cheia.
**Prazo total P0:** 7 dias corridos.
**Sem P0 pronto, não acende ads.**

---

## PRIORIDADE 1 — Grupo VIP como motor de venda (semana 2)

1.000 pessoas dentro de um grupo de loja de celular **deveria gerar pedido toda semana**. Hoje provavelmente gera abaixo do potencial. Plano:

### 1.1. Reformatar o grupo
- Definir nome e descrição claros (ex: "Smartcell VIP — ofertas antes de todo mundo")
- Regra fixa: **só admin posta**. Membro responde no privado da loja.
- Pinned message com: link do site + WhatsApp + horário de atendimento + como funciona a oferta VIP

### 1.2. Rotina de postagem no VIP (a partir da semana 2)

| Dia | Horário | Conteúdo |
|---|---|---|
| Segunda | 10h | "Chegou na loja" — 3-5 produtos novos da semana com preço VIP |
| Terça | 19h | Curiosidade técnica de 1 produto + link site |
| Quarta | 11h | Depoimento real de cliente (print/áudio) |
| Quinta | 20h | **Oferta relâmpago VIP** — 1 produto, preço só hoje, válido só pelo site com cupom **VIP15** |
| Sexta | 15h | "Sextou" — 3 ofertas do final de semana exclusivas VIP |
| Sábado | 11h | Bastidor da loja (movimento, novidade chegando) |
| Domingo | 19h | Recap da semana + 1 produto destaque pra começar a semana |

### 1.3. Cupom exclusivo VIP
- Cupom **VIP15** = 15% off em produtos selecionados, exclusivo do grupo
- Cadastrar no admin do site, válido só dentro de horários definidos
- Tracking: pedidos com cupom VIP15 medem o ROI do grupo

### 1.4. Programa de indicação dentro do VIP
- "Convide um amigo pro VIP, ele compra com VIP15, você ganha R$ 50 de crédito"
- Rastreável via campo "indicado por" no checkout
- Cresce o grupo organicamente sem gastar ads

### 1.5. Lançamento sempre no VIP primeiro
- Produto novo: divulgar no VIP **3-6 horas antes** do Instagram público
- Cria sensação real de exclusividade
- Aumenta retenção do grupo

---

## PRIORIDADE 2 — Tráfego pago R$ 2.000/mês (semana 3 em diante)

R$ 2k/mês = R$ 66/dia. É dinheiro de verdade, dá pra estrutura completa **se** P0 estiver pronto.

### 2.1. Estrutura — primeiros 30 dias 100% Meta (decisão Mestre 27/05)

R$ 2.000/mês integralmente no Meta. Avaliar no dia 30 e decidir split com Google.

| Campanha | % | Valor/mês | Objetivo |
|---|---|---|---|
| **Catálogo dinâmico (DPA)** | 50% | R$ 1.000 | Mostra o produto certo pra quem visitou ou similar — máximo ROI |
| **Retargeting** | 25% | R$ 500 | Quem visitou site últimos 30 dias / engajou stories / mensagem WhatsApp |
| **Topo orgânico impulsionado** | 25% | R$ 500 | Impulsiona reels que já performaram bem organicamente |

### 2.1.b — Avaliação no dia 30 (decide próxima fase)

Critério de decisão pra liberar diversificação pra Google Ads:

| ROAS Meta após 30 dias | Decisão |
|---|---|
| **> 3x** | Meta tá rendendo. Liberar R$ 600-800 pra Google Ads, manter R$ 1.200 no Meta |
| **2x a 3x** | Ajustar criativo/público no Meta antes de diversificar. Mais 30 dias só Meta. |
| **< 2x** | Algo está errado — não diversifica. Investigar (criativo, oferta, página, frete, preço) |

Critérios adicionais a observar no dia 30:
- CAC abaixo de R$ 80 ✓
- Pixel com 50+ eventos de Compra (Lookalike fica preciso) ✓
- 30%+ dos pedidos vindos de fora de MG (tese nacional validando) ✓
- Taxa de conversão site acima de 1,5% ✓

Se 3 dos 4 critérios bateram + ROAS acima de 3x = libera Google Ads.

### 2.2. Públicos prioritários (NACIONAL — atualizado 27/05)
1. **Visitantes do site 30 dias** (retargeting)
2. **Lookalike 1% dos compradores** (precisa de Pixel acumulando 50+ compras pra calibrar — leva ~30 dias)
3. **Lookalike 1% do grupo VIP** (importar lista de telefones do VIP no Meta Business)
4. **Interesse:** "Apple", "iPhone", "tecnologia", "seminovos" + **Brasil inteiro** + idade 22-45 + renda média-alta
5. **Cidades-foco no início:** capitais e regiões metropolitanas (SP, RJ, BH, BSB, POA, CWB, REC, SSA, FOR) — onde ticket médio é mais alto
6. ~~Patos + Triângulo + raio 80km~~ — descontinuado, foco agora é nacional

### 2.3. Criativos
- **Não fazer criativo do zero pra ads.** Pega os reels orgânicos com melhor desempenho e impulsiona como ad.
- Adicionar legenda "swipe up" / "compra no link" + UTM
- Trocar criativo a cada 7-10 dias pra evitar fadiga

### 2.4. Métricas a vigiar (semanal)
- **CAC (custo por aquisição)** = orçamento ÷ pedidos do mês — meta inicial R$ 50-80
- **ROAS** (retorno sobre investimento) = receita ÷ gasto — meta inicial 4x (R$ 4 pra cada R$ 1)
- **CPM e CTR** dos criativos — quem caiu, trocar
- **Taxa de conversão do site** (visita → pedido) — meta inicial 1,5-2%

---

## CONTEÚDO — calendário semanal (a partir de semana 2)

### Instagram público (28k)

| Dia | Stories (4-6/dia) | Reels |
|---|---|---|
| Segunda | Movimentação da loja + produto novo + sticker link site | — |
| Terça | Bastidor checklist seminovo + enquete | **Reels 1** (TOPO — humor/skit) |
| Quarta | Cliente recebendo na loja + depoimento texto | — |
| Quinta | Comparativo rápido 2 produtos + link site | **Reels 2** (MEIO — venda descontraída) |
| Sexta | Sextou — ofertas do fim de semana com cupom geral | — |
| Sábado | Bastidor + produto chegando + carrossel | **Reels 3** (BASTIDOR/RELATO) |
| Domingo | Recap da semana + agradecimento + CTA site | — |

### Stories — regra de ouro
- **Todo dia tem que ter 1 story com sticker link pro site.** Sem exceção.
- Mix recomendado por dia (4-6 stories):
  - 1 produto novo / oferta
  - 1 bastidor / humano
  - 1 prova social (cliente, mensagem real, recebendo)
  - 1 CTA site (sticker link explícito)
  - 1 enquete/caixinha (engajamento)
  - 1 livre (variar)

### Reels — regra de ouro
- 3 reels/semana > 1 reel/semana. Volume bate qualidade no algoritmo.
- 60% topo (humor/skit/situação) · 30% meio (produto contextualizado) · 10% fundo (oferta)
- Não vender no reels. CTA fica na legenda + bio.

---

## CRONOGRAMA — 30 dias

### Semana 1 (27/05 a 02/06)
- [ ] Mestre: GA4 instalado no site (via Lovable/Claude Code)
- [ ] Mestre: Meta Pixel + CAPI instalados
- [ ] Mestre: Catálogo Meta criado e sincronizado
- [ ] Fellipe: WhatsApp Business com catálogo
- [ ] Fellipe: revisar grupo VIP (pinned, regras, descrição)
- [ ] Equipe Smartcell: rotina IG mantida como já está

### Semana 2 (03/06 a 09/06)
- [ ] Validar P0 funcionando (eventos chegando no Pixel/GA)
- [ ] Lançar rotina nova do VIP (calendário 1.2)
- [ ] Criar cupom VIP15 no admin do site
- [ ] Criar 5 reels novos seguindo proporção 60/30/10 (referência: aguardando vídeos do Mestre)
- [ ] Stories: começar regra "1 sticker link por dia"

### Semana 3 (10/06 a 16/06)
- [ ] Estruturar Meta Ads: 3 campanhas com R$ 2.000/mês
- [ ] Subir primeiros criativos (reels orgânicos que performaram)
- [ ] Importar lista de telefones do VIP no Meta Business pra Lookalike
- [ ] Primeira leitura de métricas GA + Pixel (7 dias de dado)

### Semana 4 (17/06 a 23/06)
- [ ] Otimizar campanhas: pausar criativo ruim, escalar o que rendeu
- [ ] Primeira oferta relâmpago grande no VIP (semana de teste)
- [ ] Revisar plano: o que funcionou, o que cortar, o que dobrar

---

## INDICADORES SEMANAIS

Toda segunda revisar:

| Métrica | Onde ver | Meta inicial |
|---|---|---|
| Pedidos no site (semana) | Admin Smartcell | Crescimento semanal |
| Pedidos via cupom VIP15 | Admin Smartcell | 30%+ do total |
| Tráfego site por canal | GA4 | IG > Direto > Ads |
| Taxa de conversão site | GA4 | 1,5-2% |
| ROAS Meta Ads | Meta Business | 4x+ |
| Crescimento VIP (membros) | WhatsApp | +5%/mês |
| Crescimento IG (seguidores) | Instagram | +3%/mês |

---

## O QUE PRECISA DECISÃO DO MESTRE (antes de executar)

1. **Quem vai ser o gestor de tráfego pago da Smartcell?** Marco? Você? Contratar freelancer? O Meta Ads precisa de cuidado semanal — não dá pra rodar sozinho.
2. **Cupom VIP15 — Fellipe topa 15% off?** Confirma margem.
3. **Reels: tem alguém pra editar dentro do prazo** (3 por semana)? Ou precisa terceirizar?
4. **Tem alguém pra cuidar do grupo VIP diariamente** (postar no horário, responder admin)?

---

## Relacionado
- [[Projetos/Smartcell|Projeto Smartcell — escopo completo]]
- [[Projetos/Smartcell - 5 Roteiros venda site|Roteiros de venda (em revisão)]]
- [[knowledge/Licoes tecnicas e-commerce Smartcell|Lições técnicas]]
- [[knowledge/Catalogo de entregas ForYou Code|Catálogo de entregas]]
