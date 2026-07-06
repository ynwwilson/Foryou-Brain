# Modelo Financeiro, Monetização e ROI — deep dive

> Doc dedicado. Vinculado a `Plataforma Imobiliária Patos de Minas.md` (seção 11).
> Aprofunda a seção 8 (Investimento) e 9 (Free) com unit economics, LTV/CAC, breakeven duplo, modelo mês a mês, sensibilidade e motor de crescimento.
> Escrito 2026-07-01.

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
- R$199/mês = **R$2.388/ano**. **Um único negócio a mais no ano paga a assinatura ~7,5×.**
- Pitch que se escreve sozinho: *"Custa menos que 2% de uma comissão. Se te der 1 lead que fecha no ano, se pagou 7 vezes."*

O imobpatos dá **visibilidade** (anúncio parado). Nós damos **o lead com nome + uma secretária que trabalha por ele**. Visibilidade é commodity; lead atribuído + tempo não é. Por isso **não subprecificar** — preço baixo sinaliza valor baixo e mata o runway.

---

## 2. Estrutura de preço (tiers)

| Plano | Preço | Pra quem | O que destrava |
|---|---|---|---|
| **Free** (isca) | R$0 | todo corretor/imob | perfil + imóveis ilimitados no hub + **vê a contagem** de leads ("3 pessoas chamaram") + 1-2 leads revelados/mês (degustação) |
| **Pro** | **R$199/mês** | corretor autônomo | leads ilimitados (nome+tel+qual imóvel) + secretária IA + CRM/status + destaque |
| **Imobiliária** | **R$449-599/mês** | imob com equipe | tudo do Pro + múltiplos usuários + mais estoque + painel de equipe |
| **Founding** | **R$149/mês travado 12m** | primeiros ~20 | = Pro, preço de fundador (prova social + puxa caixa cedo) |

**Regras de preço:**
- **Anual à vista = 2 meses grátis** (10× o mês por 12 meses). Puxa caixa pra frente (runway) + derruba churn.
- **Sem setup fee** no lançamento (mata adesão). Onboarding pago só pra imobiliária grande, fase 2.
- Founding é **time-boxed** (só a 1ª leva). Não descontar pra sempre — treina o mercado a não pagar.
- ARPU-alvo (fase founding) ~**R$180 blended**; sobe pra ~R$200+ conforme full-price substitui founding e imobiliárias entram.

---

## 3. Estilo de cobrança (mecânica de pagamento)

- **Gateway: Asaas.** Melhor pro Brasil interior — **PIX recorrente + boleto + cartão + régua de cobrança (dunning) automática**, taxa baixa (~1% PIX / ~R$0,49-1,99 boleto). Stripe é pior aqui (cultura de PIX/boleto; Asaas já cobra e recobra sozinho).
- **Recorrência** no cartão/PIX. Oferecer **anual à vista** (desconto) pra quem topar → caixa adiantado + anti-churn.
- **Primeiros 5 founding**: pode ser **PIX manual** pra validar antes de fiar o gateway (economiza build) — MAS migrar pro Asaas cedo, porque cobrança manual gera **churn silencioso** (esqueceu de pagar = sumiu).
- Contato do lead **passa pela plataforma** (form / wa.me mascarado / chat) — senão o corretor põe telefone na foto e fura o paywall.

---

## 4. Modelo Free — "converter muito sem perder dinheiro"

O pulo do gato: **o Free custa ~R$0 pra nós** (anúncio = linha no banco + storage). Então:
- **Generoso na visibilidade** (que não custa): perfil + imóveis ilimitados no hub. Quanto mais cheio o hub → mais comprador → mais lead → melhor SEO. O Free **é o que enche a vitrine**.
- **Mesquinho no lead** (que é o valor): mostra a **contagem** ("alguém quer seu imóvel"), esconde o contato. 1-2 revelações/mês de degustação.

**Gatilho de conversão = FOMO de lead real.** *"Alguém quer teu imóvel — assina pra falar com ele."* Converte quente porque **o dinheiro do próprio corretor está do outro lado do paywall.**

Risco: corretor furar o paywall (telefone na foto). Mitigação: contato roteado pela plataforma + no Free o contato direto fica oculto. Não é à prova de bala no dia 1, mas secretária IA + CRM seguram ele dentro.

---

## 5. Unit economics (os números que decidem vida/morte)

| Métrica | Valor | Nota |
|---|---|---|
| ARPU blended (founding) | ~R$180 | sobe com full-price + imobiliária |
| Margem bruta | **~88-90%** | SaaS; custo variável = gateway ~4% + tokens IA R$5-15/conta + infra ~R$0 |
| Lucro bruto / conta Pro | **~R$160-170/mês** | contribuição por cliente |
| Churn mensal (early) | ~6% | founding 12m trava o churn da 1ª leva |
| **LTV** | **~R$2.750-3.300** | lucro bruto ÷ churn (6% → 2.750; 5% → 3.300) |
| **CAC cash** | **~R$300-500** | mídia é demand-gen compartilhada; corretor fecha no relacionamento (Marco/Eduardo ≈ R$0 cash) |
| **LTV/CAC** | **~5,5-9×** | saudável (bar do mercado = 3×) |
| **Payback** | **~3 meses** | CAC ÷ lucro bruto |

**Insight de CAC (importante):** a mídia (R$3k/mês) compra **demanda do comprador**, reutilizável em todos os corretores — **não é custo por corretor**. Corretor é fechado no olho por Marco/Eduardo (CAC cash ≈ 0, só tempo). Mesmo jogando toda a mídia como se fosse aquisição de corretor (6/mês → R$500), o LTV/CAC continua ótimo. Real é melhor.

---

## 6. Os DOIS breakevens (onde quase todo mundo se engana)

Separar é vital — são números diferentes:

1. **Breakeven de sobrevivência** (cobre só o inescapável: infra+ferramentas ~R$250 + gateway + IA):
   → **~3 corretores pagantes.** Trivial. Com os 5 founding do gate, **as luzes já ficam acesas.**

2. **Breakeven de crescimento** (cobre o burn TOTAL, **incluindo R$3k de mídia**):
   → **~16 pagantes @ R$199** · **~20 @ R$149 founding.** É o número que importa pra "crescer se pagando".

**Mídia é um DIAL, não custo fixo.** Caixa apertado → corta mídia pra ~R$0 → sobrevivência em ~3 corretores, cresce mais devagar no orgânico. **Essa opcionalidade é a rede de segurança** — nunca cavar o buraco mais fundo se o MRR travar.

---

## 7. Modelo mês a mês (rampa conservadora, alinhada à meta de breakeven 3-5 meses)

**Premissas:** one-time M0 R$3.500 (pacote lançamento) · fixo R$250/mês · mídia R$3.000/mês (ligada) · IA R$10×contas · gateway 4%×MRR · net-novo **6 pagantes/mês** · ARPU sobe R$170→R$195.

| Mês | Pagantes | ARPU | MRR | Custo total | Resultado | Caixa acumulado |
|---|---|---|---|---|---|---|
| M0 | — | — | — | 3.500 | −3.500 | **−3.500** |
| M1 | 6 | 170 | 1.020 | 3.351 | −2.331 | −5.831 |
| M2 | 12 | 175 | 2.100 | 3.454 | −1.354 | −7.185 |
| M3 | 18 | 180 | 3.240 | 3.560 | −320 | **−7.505** ← fundo do poço |
| M4 | 24 | 185 | 4.440 | 3.668 | +772 | −6.733 |
| M5 | 31 | 190 | 5.890 | 3.796 | +2.094 | −4.639 |
| M6 | 38 | 195 | 7.410 | 3.926 | +3.484 | −1.155 |
| M7 | ~45 | 197 | ~8.900 | ~4.050 | +~4.850 | **+~3.700 ✅** |

**Leitura:** breakeven mensal ~**M3-M4** · caixa acumulado positivo (recupera todo o investimento) ~**M7** · **buraco máximo ~R$7.500.**

### Sensibilidade (a parte honesta)
| Cenário | Net-novo/mês | Breakeven mensal | Buraco máx | Capital necessário |
|---|---|---|---|---|
| Pessimista | 4 | ~M5-6 | ~R$11-12k | **R$15-18k** |
| Base | 6 | ~M3-4 | ~R$7,5k | R$12-15k |
| Otimista | 8 | ~M3 | ~R$6k | R$10-12k |
| **Lean (mídia OFF)** | orgânico | sobrevive em ~3 pagantes | ~R$3-4k | **R$6-8k** |

**Capital recomendado: R$15-18k** (aguenta o pessimista + churn maior). Anual à vista encolhe o buraco (puxa caixa). Lean é o plano B se o aporte apertar.

---

## 8. Fontes de receita — ranqueadas por fase

- **P0 (MVP/lançamento):** assinatura **Pro** (corretor), freemium lead-unlock. **É o dinheiro.**
- **P1 (pós-PMF):** tier **Imobiliária** (multi-seat, expande ARPU) · **anual** · **destaque/boost** ⚠️ *ver alerta abaixo*.
- **P2 (escala):** **pay-per-lead** avulso (corretor esporádico) · **página de lançamento** pra construtora (incorporadora paga caro por campanha de lançamento) · **relatório de mercado** premium pro profissional · **indicação** de financiamento/seguro (parcerias).
- **EVITAR sempre:** comissão sobre a venda (jurídico/CRECI, corretor recusa) · cobrar do comprador.

### ⚠️ Alerta do "boost" (protege a galinha dos ovos de ouro)
A promessa **"o filtro manda"** é a confiança do comprador. Se boost pago distorce o resultado da busca, o comprador percebe e vai embora → morre tudo. Então monetizar posição **só de formas que não mentem pro comprador**: selo "destaque", desempate entre matches iguais, promoção no nível de perfil, carrossel "patrocinado" **claramente rotulado** — **nunca reordenar o resultado honesto do filtro.**

---

## 9. Como NÃO perder dinheiro (disciplina)

- **Não gastar mídia antes de:** (1) hub no ar, (2) hub semeado com founding, (3) captura de lead funcionando. Mídia em hub vazio = queima sem conversão.
- **Gate de morte:** 5 pagantes (PIX na mão) em 90 dias, ou encerra. Kill test inegociável.
- **Mídia atrelada ao breakeven:** MRR travou 2 meses → corta mídia, não cava o buraco.
- **Founding só na 1ª leva**, time-boxed. Não vira desconto eterno.
- **Anual à vista** pra puxar caixa = runway de graça.
- **Infra lean:** free tier Vercel/Supabase → pago só quando a métrica forçar.
- **Zero salário/pró-labore** antes do breakeven de crescimento. Sócios comem equity/futuro, não caixa agora.
- **North-star = pagantes** (não signups, não tráfego). Secundário: **NRR** (net revenue retention) + **leads entregues/corretor** (a prova de valor).

---

## 10. Como CRESCER (não só sobreviver)

**Flywheel local:** mídia → compradores → leads → corretor vê lead → corretor paga → corretor traz o estoque dele → hub mais rico → ranqueia orgânico/SEO → mais comprador → (gira). Mídia paga é o **primer**; **SEO local + boca a boca** é o motor que **compõe**. Em cidade de 150k, boca a boca de corretor é **brutal** nos dois sentidos — acerta os 10 primeiros e eles vendem por você; queima um e espalha.

**Land-and-expand:** corretor individual → imobiliária inteira (o tier Imobiliária é o expansor de ARPU). Secretária IA + CRM = stickiness → upsell (destaque, mais estoque, assentos) → **NRR >100%** mesmo com algum churn de logo.

### O prêmio grande: clone regional
- **Teto honesto de Patos:** ~150-300 corretores ativos + ~25 imobiliárias. Pegando 30-40% pagantes → **60-120 contas** → MRR **R$12-24k** → ~R$150-290k/ano, margem ~85%. Negócio saudável pra 3 sócios — **não unicórnio**, mas máquina real.
- **Como estourar o teto:** replicar o playbook **cidade a cidade** — Uberlândia, Uberaba, Araxá, Patrocínio (Alto Paranaíba/Triângulo). Ganhar **Patos como template**, depois clonar.
- Por isso **secretária IA + SEO programático importam**: deixam cada nova cidade **barata de lançar**. Reframe o ROI: de "um site de cidade pequena" pra **"motor de hub local franqueável"** — aí o ROI fica grande de verdade.

---

## 11. Prazos / marcos financeiros

| Quando | Marco |
|---|---|
| Jul/2026 (agora) | fechar modelo, buildar MVP (2-3 sem), fiar Asaas, semear founding |
| M1 (~Ago, lança) | 5-6 founding pagantes → sobrevivência OK, **gate passado** |
| M3-4 | **breakeven de crescimento** (~16-20 pagantes) |
| M7 | **caixa acumulado positivo** (investimento recuperado) |
| M12 | ~50-70 pagantes se a rampa segurar → MRR ~R$10-13k → **primeiro pró-labore/lucro distribuível** |

---

## 12. Decisões financeiras pendentes (Mestre)

1. **Preço final:** Pro R$199 (recomendado) · founding R$149 travado 12m — confirma?
2. **Tier Imobiliária** entra já no lançamento ou fase 2? (recomendo: já, mesmo que 1-2 imobs).
3. **Gateway:** Asaas (recomendado) — confirma? PIX manual só nos 5 primeiros?
4. **Anual à vista com 2 meses grátis** — liga desde o dia 1? (recomendo sim, puxa caixa).
5. **Capital aportado:** confirmar R$15-18k (ou rodar Lean R$6-8k com mídia OFF).
6. **Boost pago:** só selo/desempate/rotulado (nunca reordenar o filtro) — de acordo?

---

## 13. ⏳ PROPOSTA — Reprecificação (pendente, decidir 2026-07-02)

> Mestre levantou (2026-07-01): *"pra tudo que oferecemos, não tá barato demais?"* — instinto certo. O pacote cheio (com secretária IA) está **subprecificado no valor**. Proposta abaixo NÃO está travada; discutir amanhã antes de aplicar.

**Âncora de mercado (concorrência cobra só por anúncio+lead, sem IA):** ZAP/VivaReal ~R$200-700/mês · OLX ~R$100-300 · CRM imob (Jetimob/Tecimob/Kenlo/Vista) ~R$100-500. Nós temos + **secretária IA por voz com poder total** (ninguém tem). Corretor fecha ~R$18k/comissão → não pisca pra R$400/mês.

**Novo esquema proposto (ancora alto, entra barato, tiera a IA):**

| Plano | Preço-lista | Contém |
|---|---|---|
| Free | R$0 | isca |
| **Essencial** | **R$197** | hub + lead nominal + CRM + perfil + destaque (bate imobpatos, entra fácil) |
| **Premium (com Secretária IA)** | **R$397** | tudo + secretária IA poder total + proativa + relatório falado ← tier do dinheiro |
| **Imobiliária** | **R$697-997** | multi-corretor + painel de equipe |
| **Founding** (primeiros ~15) | **R$247** travado 12m | = Premium, preço de fundador |

**Lógica:**
- Âncora alta (R$397) faz o valor parecer alto + captura corretor top.
- Essencial R$197 = entrada sem atrito, bate o imobpatos grátis.
- **Secretária IA vira o upsell** (land no Essencial → expand no Premium); NRR >100%. IA cara em token → cobrar mais protege margem.
- Founding R$247 = desconto **explícito** ("preço de fundador, congela 12m") → adesão rápida + lealdade, sem baratear a marca.

**Impacto no modelo (melhora tudo):**
- ARPU blended sobe ~R$185 → **~R$280-320**.
- Breakeven de crescimento cai **~17 → ~12 contas**.
- Menos contas pra se pagar = menos capital em risco, breakeven mais cedo.
- Risco novo: *"pagam R$397?"* → resolver com founding + **descoberta de teto** na 1ª leva.

**Regra de ouro do preço:** praça nova com incumbente grátis = não se sabe o teto. **Ancora a lista alta, entra founding barato, descobre WTP com a 1ª leva.** Subir depois é fácil (grandfather nos founders); baratear depois é sinal de fraqueza (quase irreversível). **Errar pra cima na âncora.**

**Decisão pendente:** aplicar este esquema (Essencial R$197 / Premium-IA R$397 / Founding R$247) e refazer breakeven/ARPU? — decidir 2026-07-02.
