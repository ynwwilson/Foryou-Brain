# Plataforma Imobiliária Patos — CTS & COGS (pré-lançamento) — v2 FUNDO

> Worksheet vivo. CTS Unitário = COGS por assinatura. Reescrito 2026-07-02 mais fundo.
> **Correção-chave:** o custo NÃO é por-lead — é por **interação com o agente de IA**. O agente é a interface diária do corretor (controla painel, conversa, responde, entrega relatório, recebe áudio). O corretor gera a maior parte do consumo, não os leads.
> Valores = estimativa (USD~R$5,5). A IA precisa ser MEDIDA (§11).

---

## 1. Inventário COMPLETO de custos (tudo que desembolsamos)

| Categoria | Fornecedor | Tipo | ~R$/mês |
|---|---|---|---|
| Hosting front/app | Cloudflare Pages (ou Vercel) | fixo | R$0 (Pages) · R$110 (Vercel) |
| Banco/Auth/Realtime | Supabase Pro | fixo | R$140 |
| Storage de imagem | Cloudflare R2 | variável | ~R$0,08/GB (sem egress!) |
| Entrega de imagem | Cloudflare Images/CDN | variável | ~R$5/100k imagens |
| Workers/edge | Cloudflare Workers | fixo | R$30 |
| Mapa do hub | Mapbox/Google (ou Leaflet grátis) | variável | R$0-100 (tráfego) |
| **LLM (o agente)** | Anthropic Haiku/Sonnet | **variável** | **domina — ver §4-6** |
| STT (voz→texto) | Whisper/Deepgram | variável | R$0,03/min |
| Vision (agente LÊ imagem/doc que o corretor manda) | Anthropic (tokens) | variável | ~1,6k tokens/imagem |
| Geração de IMAGEM (agente cria) | fal/Flux/nano-banana | variável | ~R$0,06-0,22/imagem |
| Geração de DOCUMENTO (PDF/relatório) | LLM tokens + render | variável | tokens + ~R$0 render |
| Gateway | Asaas | variável | R$2 (PIX) · R$10 (cartão) |
| Email/notificação | Resend | variável | R$0,005/email |
| Domínio + monitoring | — | fixo | R$50 |

---

## 2. Preços unitários LLM (a linha que domina)

| Modelo | Input | Output | Input CACHEADO (leitura) |
|---|---|---|---|
| Haiku-class (rotina) | ~R$5/M | ~R$25/M | **~R$0,50/M (10%)** |
| Sonnet-class (pesado) | ~R$18/M | ~R$90/M | ~R$1,80/M |

> **Prompt caching é a alavanca #1.** O agente manda o MESMO prefixo grande toda call (system prompt + definição de ferramentas + estado da conta). Cacheando esse prefixo, a leitura cai pra ~10%. Sem caching, o custo 2-3×.

---

## 3. Perfil de uso do AGENTE (a premissa a validar)

O corretor conversa com o agente o dia todo. Cada interação = ~2 calls LLM (ida + volta com ferramenta), contexto ~7k tokens (6k estático/cacheável + 1k dinâmico), saída ~400.

| Uso | Interações/dia | Calls/mês | Áudios (STT) |
|---|---|---|---|
| **Leve** | ~5 | ~300 | ~5 min/dia |
| **Médio** | ~15 | ~900 | ~10 min/dia |
| **Pesado** | ~40 | ~2.400 | ~15 min/dia |

---

## 4. Custo LLM+STT por Pro — COM vs SEM caching

| Cenário | LLM sem cache | **LLM com cache** | STT | **IA total (cache)** |
|---|---|---|---|---|
| Leve | R$18 | **R$7** | R$2 | **~R$9** |
| Médio | R$40 | **R$16** | R$5 | **~R$21** |
| Pesado | R$108 | **R$43** | R$13 | **~R$56** |

> Sem caching, o pesado bate **~R$120/mês** só de IA. Com caching, **~R$56**. Essa escolha de engenharia decide a margem.

---

## 5. Custo variável TOTAL por Pro (caching ligado, resposta em texto)

| Item | Leve | Médio | Pesado |
|---|---|---|---|
| IA (LLM+STT) | R$9 | R$21 | R$56 |
| Gateway | R$3 | R$3 | R$3 |
| Storage/entrega img (R2) | R$2 | R$3 | R$4 |
| Notificação | R$1 | R$1 | R$1 |
| **Variável Pro** | **~R$15** | **~R$28** | **~R$64** |

**IA responde em texto, imagem e documento (NÃO em voz)** → sem custo de TTS. Modais extras já inclusos no variável: geração de imagem (~R$1-3/mês), geração de doc (~R$0,5), e vision pra ler imagem/doc do corretor (~R$1-2). Input de áudio (STT) continua.

---

## 6. Custo FIXO escalonado — 2 opções de stack

| Item | Stack Cloudflare | Stack Vercel |
|---|---|---|
| Hosting | R$0 (Pages) | R$110 (Vercel Pro) |
| Supabase Pro | R$140 | R$140 |
| Cloudflare Workers/R2/Images | R$40 | R$40 |
| Mapa (cedo, free tier) | R$0-50 | R$0-50 |
| Domínio/monitoring/email | R$50 | R$50 |
| **Fixo base** | **~R$250** | **~R$390** |

> Recomendo **stack Cloudflare** (Pages grátis + R2 sem egress) → fixo ~R$100 menor. Combina com o histórico do Mestre (foryoucodee já é Cloudflare Pages).

---

## 7. CTS Unitário Pro = variável + (fixo ÷ contas) — stack Cloudflare (fixo R$250)

**Cenário Médio (variável R$28):**
| Contas pagas | Fixo/conta | CTS Pro | Lucro (R$279) | Margem |
|---|---|---|---|---|
| 10 | R$25 | **R$53** | R$226 | 81% |
| 25 | R$10 | **R$38** | R$241 | 86% |
| 50 | R$5 | **R$33** | R$246 | 88% |
| 100 | R$2,5 | **R$30,5** | R$248 | 89% |

**Cenário Pesado (variável R$64):**
| Contas | CTS Pro | Lucro | Margem |
|---|---|---|---|
| 10 | **R$89** | R$190 | 68% |
| 50 | **R$69** | R$210 | 75% |
| 100 | **R$67** | R$212 | 76% |

> Corretor pesado + base pequena = margem ~68%. Ainda lucra, mas é o pior caso realista. Fair-use protege a cauda além disso.

---

## 8. Free e Imobiliária
- **Free:** sem gateway, IA só no trial 7d. Fora do trial ~R$1-2/mês (notif+storage). O burn do free = **fixo diluído + custo dos trials de IA** (~R$7-15 por free que testa o agente). É custo de aquisição.
- **Imobiliária (R$199/assento):** cada corretor da equipe usa o agente → variável ~igual ao Pro por assento (R$28 médio). Lucro ~R$171/assento (86%) médio; ~R$135 (68%) se todos pesados.

---

## 9. Alavancas OBRIGATÓRIAS pra segurar a margem (não são opcionais)
1. **Prompt caching** — cacheia system prompt + ferramentas + estado da conta. Corta o input ~90%. **Sem isso o pesado inviabiliza (~R$120 IA).**
2. **Roteamento de modelo** — Haiku na rotina (marcar vendido, responder, atualizar); Sonnet só em tarefa pesada (relatório, campanha). 
3. **Trimming de contexto** — não mandar histórico inteiro toda call; resumir + recuperar só o relevante.
4. **Batch API** pra relatório/resumo assíncrono = 50% off.
5. **Imagens no R2** (não egress do Supabase) — R2 não cobra saída.
6. **Fair-use** — pacote generoso de ações de IA/mês; cauda (whale 40+/dia) limitada/avisada.
7. **Geração de imagem com teto** — imagem é o modal de output mais caro; incluir N/mês, excedente limitado/avisado.

---

## 10. Número de planejamento (usar até medir)

| | Começo (poucas contas) | Escala madura |
|---|---|---|
| **CTS Pro médio** | ~R$53 | ~R$30 |
| **CTS Pro pesado** | ~R$89 | ~R$67 |
| **Margem médio** | ~81% | ~89% |
| **Margem pesado** | ~68% | ~76% |

**Planejamento conservador: CTS ~R$60/Pro no começo → ~R$35 maduro.** Margem ~78% começo → ~88% escala. (com caching + Cloudflare + Haiku)

---

## 11. Como CRAVAR o número real (calibração pré-lançamento)
1. **Instrumentar por conta desde o dia 1:** tokens LLM (in/out/cached), minutos STT, chars TTS, GB storage. Sem isso é chute eterno.
2. **Piloto 2-4 semanas** com 3-5 founding usando o agente de verdade → ler consumo real de IA/usuário (é o número que decide tudo) + faturas Supabase/Cloudflare/Anthropic.
3. **Medir a distribuição:** quantos % são leves vs pesados. O ARPU-custo depende do mix.
4. Substituir estas estimativas pelos números medidos.

---

## 12. Custo POR LEAD — todos os serviços, carregado

IA responde em **texto, imagem e documento** (sem voz). Referência: **50 contas Pro · corretor médio = 40 leads/mês + 15 interações/dia com o agente** → 2.000 leads/mês na plataforma.

### Dois números (ambos verdadeiros)
- **Custo DIRETO por lead** (só o que UM lead dispara: notificação + auto-resposta do agente + entrega da foto ao comprador): **~R$0,05-0,15.**
- **Custo CARREGADO por lead** (TUDO do mês ÷ leads — inclui o uso do agente que o corretor faz o dia todo): **~R$1,00.**

> A diferença = o agente/infra que o corretor consome INDEPENDENTE de lead. "Por lead" é ruído — o motor de custo é o **uso do agente** (dirigido pelo corretor), não o lead.

### Todo serviço → R$/mês (1 corretor médio) → R$/lead (÷40)

| Serviço / API | R$/mês | R$/lead | Dispara por |
|---|---|---|---|
| LLM texto (agente, c/ cache) | R$16 | R$0,400 | agente |
| STT (áudio que o corretor manda) | R$5 | R$0,125 | agente |
| Vision (lê imagem/doc do corretor) | R$2 | R$0,050 | agente |
| Geração de imagem (agente cria) | R$2 | R$0,050 | agente |
| Geração de documento (PDF/relatório) | R$0,5 | R$0,013 | agente |
| Gateway Asaas | R$3 | R$0,075 | conta |
| Storage R2 (fotos dos imóveis) | R$2 | R$0,050 | conta |
| Entrega de imagem CDN (ao comprador) | R$1 | R$0,025 | lead |
| Notificação (email/push do lead) | R$0,4 | R$0,010 | lead |
| Mapa do hub (comprador busca) | R$0,5 | R$0,013 | lead |
| Fixo rateado (Supabase+Cloudflare ÷50) | R$5 | R$0,125 | fixo |
| **TOTAL** | **~R$39** | **~R$1,00/lead** | |

### Faixa por perfil (por-lead é noisy porque o agente é dirigido pelo corretor)
| Perfil | R$/mês | Leads/mês | **R$/lead carregado** |
|---|---|---|---|
| Leve | ~R$21 | 20 | ~R$1,10 |
| Médio | ~R$39 | 40 | ~R$1,00 |
| Pesado | ~R$80 | 100 | ~R$0,80 |

> Pesado rateia por mais leads → por-lead MENOR, absoluto maior. Faixa **~R$0,80-1,10 → chama de ~R$1/lead carregado.**

### O que isso decide
- **Free (5 leads/mês, sem agente pós-trial):** custo direto ~R$0,25-0,75/mês total. Praticamente grátis → confirma dar os 5.
- **Pro:** o lead custa **centavos** direto; o que pesa é o **agente**. Controlar consumo do agente (caching + fair-use + geração de imagem com teto) importa 10× mais que controlar leads.
