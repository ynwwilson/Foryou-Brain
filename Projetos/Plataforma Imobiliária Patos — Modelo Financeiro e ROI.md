# Modelo Financeiro, Monetização e ROI — deep dive

> Doc dedicado. Vinculado a `Plataforma Imobiliária Patos de Minas.md` (seção 11).
> Escrito 2026-07-01. **REVISADO 2026-07-07 (v2):** preço Pro R$279, founding cortado, escada Free/Pro/Imobiliária, CTS v2 (driver = uso do agente IA, doc `— CTS & COGS (pré-lançamento).md`), modo bootstrap (~R$2k, sem raise). Supersede todos os números com R$199/R$149.

---

## 0. A verdade central (de onde tudo deriva)

**Isso é um SaaS B2B vestido de marketplace.**
- Quem **paga** = corretor / imobiliária (lado da oferta).
- Comprador **nunca paga** — cobrar comprador mata o tráfego.
- O comprador é o **motor de demanda**: é o que faz o corretor querer pagar.
- Logo: **dinheiro de verdade = MRR recorrente de corretor.** Comprador = grátis pra sempre = nosso estoque de atenção, que vendemos ao corretor na forma de **lead com nome**.

Consequência prática: **o paywall trava o LEAD, não o anúncio.** Anúncio é commodity (OLX/ZAP/Insta já dão grátis) e pra nós custa ~R$0 (uma linha no Postgres). O escasso é o **contato qualificado + o tempo economizado** (secretária IA). É isso que se cobra.

---

## 1. Por que o corretor paga (tendo imobpatos grátis)

Resposta estrutural, não torcida — ancorada na economia dele:

- Corretor em Patos fecha comissão ~**6% de um imóvel ~R$300k = ~R$18.000** por venda.
- Pro R$279/mês = **R$3.348/ano**. **Um único negócio a mais no ano paga a assinatura ~5,4×.**
- Pitch que se escreve sozinho: *"Custa menos de 20% de UMA comissão no ano inteiro. Se te der 1 lead que fecha, se pagou 5 vezes."*

O imobpatos dá **visibilidade** (anúncio parado). Nós damos **o lead com nome + uma secretária IA que trabalha por ele**. Visibilidade é commodity; lead atribuído + tempo não é. R$279 é coerente com o valor: âncora de mercado ZAP/VivaReal R$200-700 e CRM imob R$100-500 — **todos SEM IA**.

---

## 2. Estrutura de preço (DECIDIDA 2026-07-02)

| Plano | Preço | Pra quem | O que destrava |
|---|---|---|---|
| **Free** (isca) | R$0 | todo corretor/imob | perfil + 3 imóveis (5 p/ imob) + 5 fotos + **5 leads/mês com botão WhatsApp** + lead 6+ borrado/travado (gancho) + trial IA no 1º uso (depois bloqueia 100%) |
| **Pro** | **R$279/mês** ou **R$2.790/ano** (2 meses off) | corretor autônomo | leads ilimitados na hora + secretária IA completa + CRM + atribuição + tempo real + imóveis/fotos ilimitados |
| **Imobiliária** (Fase 2) | **R$199/corretor/mês** | imob com equipe | tudo do Pro por assento + distribuição de leads + painel de equipe (mais barato/cabeça, soma mais no total) |

**Regras de preço:**
- **SEM founding** (cortado 2026-07-02). No lugar: **anual à vista = 2 meses grátis** — puxa caixa, derruba churn, é o "desconto" oficial.
- **Sem setup fee** (mata adesão).
- Comprador 100% grátis sempre · ranking nunca pago · boost (Fase 2) = slot rotulado, nunca reordena o filtro.
- Descoberta de teto na 1ª leva: R$279 é hipótese com boa âncora — **kill-test de preço** (§9) valida. Subir/segurar é fácil; baratear é irreversível.
- ARPU-alvo: ~R$279 puro no lançamento (só Pro); blended ~R$250-260 quando Imobiliária entrar (assentos a R$199 puxam pra baixo mas somam mais receita total).

---

## 3. Estilo de cobrança (mecânica de pagamento)

- **Gateway: Asaas** (confirmado). PIX recorrente + boleto + cartão + régua de cobrança (dunning) automática, taxa ~1% PIX.
- **Primeiros ~5 pagantes: PIX manual** (valida antes de fiar gateway) → migrar pro Asaas cedo (cobrança manual = churn silencioso).
- **Anual à vista** ofertado desde o dia 1 (R$2.790) → caixa adiantado + anti-churn.
- Contato do lead **passa pela plataforma** (botão WhatsApp mediado, número cru escondido) + **OCR anti-contato** na foto/texto do free — sem isso o paywall é teatro.

---

## 4. Modelo Free — "converter muito sem perder dinheiro"

- Free custa ~centavos pra nós (5 leads/mês = ~R$0,05-0,15 diretos cada; anúncio = linha no banco). **Generoso em ser-visto, mesquinho na grana.**
- Cota: 3 imóveis (corretor) / 5 (imob) + 5 fotos. Aparece e ranqueia por match igual todo mundo.
- **A gota:** 5 leads/mês com botão. Lead 6+ = **borrado/visível-mas-travado** — corretor sabe que existe, não vê nem age. FOMO de dinheiro real.
- **Trial da IA:** dispara no 1º uso → 7 dias completos → bloqueia 100% → só Pro.
- Reseta mensal. Free = folder profissional excelente, não ferramenta de negócio.

---

## 5. Unit economics (v2 — R$279 + CTS real)

Base CTS: doc `— CTS & COGS (pré-lançamento).md` — CTS Pro ~R$60/conta no começo (base pequena rateia fixo) → ~R$35 maduro; variável pura leve R$15 / médio R$28 / pesado R$64 (driver = interação com agente IA, não lead).

| Métrica | Valor | Nota |
|---|---|---|
| ARPU (lançamento) | **R$279** | só Pro no ar |
| Contribuição/conta (variável médio + gateway) | **~R$248/mês** | 279 − 28 (CTS var) − 3 (gateway ~1%) |
| Contribuição pior caso (corretor pesado) | ~R$212/mês | 279 − 64 − 3 |
| Margem bruta | **~78% começo → ~88% maduro** | CTS R$60→R$35 com escala |
| Churn mensal (early) | ~6% | anual à vista trava parte da base |
| **LTV** | **~R$3,6-5,0k** | contribuição ÷ churn (248/0,06 ≈ 4,1k; pesado/6% ≈ 3,5k; médio/5% ≈ 5,0k) |
| **CAC cash (bootstrap)** | **~R$0-250** | fechamento no relacionamento (Marco/Eduardo) ≈ R$0; atribuindo os R$2k de influencer à 1ª leva de ~8-10 ≈ R$200-250 |
| **LTV/CAC** | **>15× bootstrap · ~8× com mídia ligada** | mídia futura R$3k/6 net-novos → CAC ~R$500 → ainda 7-10× |
| **Payback** | **~1 mês bootstrap · ~2 meses com mídia** | CAC ÷ contribuição |

**Salto vs modelo antigo (R$199/149):** contribuição sobe ~R$165→~R$248 (+50%), LTV ~R$3,3k→~R$4-5k, e o breakeven cai pela metade (§6). O R$279 paga o custo da IA com folga e ainda melhora tudo.

---

## 6. Os DOIS breakevens (v2)

1. **Breakeven de sobrevivência** (fixo Cloudflare+Supabase ~R$250/mês + variáveis já cobertos pela contribuição):
   → **2 contas Pro.** O gate de 5 pagantes = MRR R$1.395 e **~R$1.000/mês de lucro operacional** — as luzes ficam acesas com folga.

2. **Breakeven de crescimento** (se/quando ligar mídia R$3k/mês):
   → (250 + 3.000) ÷ 248 ≈ **~14 contas Pro** (era ~17-20 no modelo antigo).

**Mídia é DIAL, não custo fixo — e no bootstrap começa OFF.** Regra de ligar (proposta): só quando MRR ≥ ~R$3,5k (≥13 contas) E churn da 1ª renovação OK — aí a mídia se paga do próprio MRR, sem cavar buraco.

---

## 7. Modelo mês a mês (v2 — bootstrap, mídia OFF)

**Premissas:** aporte único M0 **R$2.000** (4 vídeos influencer, tudo incluso) · fixo R$250/mês · CTS variável R$28×contas · gateway ~1%×MRR · **net-novo 4 pagantes/mês** (relacionamento + influencer) · ARPU R$279 · churn embutido na rampa.

| Mês | Pagantes | MRR | Custo total | Resultado | Caixa acumulado |
|---|---|---|---|---|---|
| M0 | — | — | 2.250 | −2.250 | **−2.250** ← fundo do poço |
| M1 | 4 | 1.116 | 373 | +743 | −1.507 |
| M2 | 8 | 2.232 | 496 | +1.736 | **+229 ✅** |
| M3 | 12 | 3.348 | 619 | +2.729 | +2.958 |
| M4 | 16 | 4.464 | 742 | +3.722 | +6.680 |
| M5 | 20 | 5.580 | 865 | +4.715 | +11.395 |
| M6 | 24 | 6.696 | 988 | +5.708 | **+17.103** |

**Leitura:** breakeven mensal **M1** · caixa acumulado positivo (investimento recuperado) **M2** · buraco máximo = **o próprio aporte de R$2.250**. O modelo bootstrap quase não tem downside financeiro — o risco é 100% de adesão (o gate), não de caixa.

### Sensibilidade (a parte honesta)
| Cenário | Net-novo/mês | Breakeven mensal | Caixa acum. positivo | Capital necessário |
|---|---|---|---|---|
| Pessimista | 2 | M1 (ainda positivo) | ~M4 | **R$2,5-3k** |
| Base | 4 | M1 | M2 | R$2-2,5k |
| Otimista | 6 | M1 | M2 | R$2k |
| Gate falha | <5 em 90d | — | — | encerra, perda ≈ R$2,5k |

Com contribuição de R$248/conta, **qualquer cenário com ≥1 conta já cobre o fixo**. A variável que mata não é custo — é **não fechar corretor**. Por isso o gate de morte continua inegociável.

---

## 8. Fontes de receita — ranqueadas por fase

- **P0 (MVP/lançamento):** assinatura **Pro R$279** + anual R$2.790. **É o dinheiro.**
- **P1 (pós-PMF):** tier **Imobiliária** (R$199/assento, multi-seat expande receita total) · **boost/destaque rotulado** ⚠️ *nunca reordena o filtro*.
- **P2 (escala):** pay-per-lead avulso · página de lançamento pra construtora · relatório de mercado premium · indicação de financiamento/seguro (parcerias).
- **EVITAR sempre:** comissão sobre a venda (CRECI/jurídico, corretor recusa) · cobrar do comprador · desconto permanente (treina o mercado a não pagar).

### ⚠️ Alerta do "boost" (protege a galinha dos ovos de ouro)
A promessa **"o filtro manda"** é a confiança do comprador. Boost pago que distorce resultado da busca → comprador percebe → morre tudo. Monetizar posição só de formas que não mentem: selo "destaque", desempate entre matches iguais, carrossel "patrocinado" **claramente rotulado**. **Nunca reordenar o resultado honesto do filtro.**

---

## 9. Como NÃO perder dinheiro (disciplina)

- **Gate de morte:** 5 pagantes (PIX na mão) em 90 dias, ou encerra. Kill test inegociável.
- **Kill-tests adicionais:** churn na 2ª renovação <10% · **teto de preço**: se a 1ª leva travar em R$279, testar R$249→R$199 ANTES de concluir que não há mercado (baratear controlado ≠ pânico).
- **Mídia OFF até:** hub no ar + semeado + captura de lead OK + MRR ≥ ~R$3,5k. Influencer (R$2k) é o único gasto de marketing do lançamento.
- **Instrumentar tokens/usuário desde o dia 1** + piloto 2-4 semanas com os 3-5 primeiros → crava CTS real (IA é o maior desconhecido). Alavancas obrigatórias: prompt caching, roteamento Haiku/Sonnet, trimming, fair-use.
- **Infra lean:** Cloudflare (~R$250 tudo) — não Vercel (~R$390).
- **Zero pró-labore** antes de MRR sustentado. Sócios comem equity/futuro.
- **North-star = pagantes** (não signups, não tráfego). Secundário: NRR + leads entregues/corretor (a prova de valor).

---

## 10. Como CRESCER (não só sobreviver)

**Flywheel local:** influencer/orgânico → compradores → leads → corretor vê lead borrado → paga → traz estoque → hub mais rico → SEO local → mais comprador → (gira). Em cidade de 150k, boca a boca de corretor é **brutal** nos dois sentidos — acerta os 10 primeiros e eles vendem por você.

**Land-and-expand:** corretor individual → imobiliária inteira (tier por assento). Secretária IA + CRM = stickiness → NRR >100%.

### O prêmio grande: clone regional
- **Teto honesto de Patos:** ~150-300 corretores ativos + ~25 imobiliárias. 30-40% pagantes → **60-120 contas** → com blended ~R$250-260 → **MRR R$15-31k → ~R$190-375k/ano**, margem ~85%+.
- **Estourar o teto:** replicar cidade a cidade — Uberlândia, Uberaba, Araxá, Patrocínio. Patos = template; secretária IA + SEO programático deixam cada cidade nova **barata de lançar**. Reframe: não é "site de cidade pequena", é **motor de hub local franqueável**.

---

## 11. Prazos / marcos financeiros (v2)

| Quando | Marco |
|---|---|
| Jul/2026 (agora) | cravar nome/domínio, buildar MVP (2-3 sem), gravar 4 vídeos influencer |
| M1 (~Ago, lança) | 5+ pagantes → **gate passado**, MRR ~R$1,4k, lucro op. ~R$1k/mês |
| M2-3 | **caixa acumulado positivo** (aporte de R$2k recuperado) |
| M4-6 | 16-24 contas → MRR R$4,5-6,7k → decidir ligar mídia (dial) |
| M12 | 40-60 contas → MRR R$11-17k → **primeiro pró-labore/lucro distribuível** |

---

## 12. Decisões financeiras — status

**Fechadas (2026-07-02):**
1. ✅ Preço: **Pro R$279/mês · R$2.790/ano** (2 meses off) · Imobiliária R$199/assento (Fase 2).
2. ✅ **Founding cortado** — anual é o desconto oficial.
3. ✅ Gateway: **Asaas**; PIX manual só nos ~5 primeiros.
4. ✅ Capital: **bootstrap ~R$2k** (4 vídeos), sem raise de R$15-18k.
5. ✅ Boost: Fase 2, sempre rotulado, nunca reordena filtro.
6. ✅ Imobiliária: Fase 2 (não entra no lançamento).

**Abertas:**
1. ⏳ Nome/domínio (Imora favorito; `imora.com.br` ocupado até 02/2027 — opções livres: `imora.imb.br`, `imoraimoveis.com.br`, `useimora.com.br`, `imorapatos.com.br`).
2. ⏳ Critério formal pra ligar mídia (proposta §6: MRR ≥ R$3,5k + churn 1ª renovação OK).
3. ⏳ Agenda dos 4 vídeos de influencer (amarrar com data de lançamento).

---

## 13. ✅ RESOLVIDO — Reprecificação (histórico)

A proposta Essencial R$197 / Premium-IA R$397 / Founding R$247 (levantada 2026-07-01) **morreu em 2026-07-02**. Decisão final do Mestre: escada simples **Free / Pro R$279 / Imobiliária por assento**, sem founding, IA dentro do Pro (não tierada). Racional preservado que continua valendo: âncora de mercado alta (ZAP R$200-700 sem IA), errar preço pra cima, descoberta de WTP na 1ª leva. Números deste doc já refletem a decisão.
