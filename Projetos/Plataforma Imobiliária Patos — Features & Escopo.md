# Plataforma Imobiliária Patos — Features & Escopo

> Doc de escopo. Vinculado a `Plataforma Imobiliária Patos de Minas.md` (negócio) e `Plataforma Imobiliária Patos — Modelo Financeiro e ROI.md` (números).
> Fechado 2026-07-02. Cada feature tem: **Quem** (comprador/corretor), **Plano** (Free/Pro/Imob/sistema), **Fase** (MVP / Fast-follow / Fase 2).

---

## Decisões travadas nesta rodada

1. **Cobrança = assinatura mensal.** Descartado: cobrança por uso (bill shock + fere flywheel), taxa sobre venda (CRECI/jurídico, não rastreável).
2. **Secretária IA no free = trial de 7 dias completo → bloqueia 100% → só Pro.** (escolha do Mestre — opção A). Dispara no 1º lead real (ver Pendências).
3. **Free = folder profissional excelente, NÃO ferramenta de negócio.** Generoso em ser-visto + provar; muro na grana (lead, IA, ferramenta).
4. **Contato mediado (confirmado 2026-07-02):** comprador preenche **nome+telefone** → aí aparece o botão **"Mandar mensagem (WhatsApp)"**. Free libera os **primeiros 5 leads/mês** com botão; do 6º em diante o botão só aparece se o corretor for **Pro** (senão o comprador só preenche o form e o lead fica travado pro corretor). **OCR anti-contato** apaga número escrito na foto/texto — é o que torna o limite de 5 exigível (senão o corretor burla e o comprador liga direto, e nada passa por nós). Do **6º lead+ no free**, o lead fica **borrado/travado**: o corretor sabe que existe (contador) mas **não vê o contato nem consegue agir** → gancho "3 clientes esperando, vire Pro". Cota de 5 **reseta por mês**.

---

## Regras que NÃO são escolha (travas de arquitetura)

- **Lado comprador = 100% grátis pra sempre.** Comprador é o motor de demanda, nunca paga.
- **Ranking/posição no filtro nunca é pago** (pay-to-win mata confiança do comprador = morte).
- **Cadastrar imóvel tem cota free (não zero)** — capar em 0 esvazia o hub.
- **Boost/destaque = slot rotulado, nunca reordena o filtro orgânico.**
- **Ser achado nunca é pago.**

---

## Plano FREE (corretor) — o que entra

| Feature | Detalhe |
|---|---|
| Perfil completo + vitrine | tipo Instagram, bio/foto/região |
| Cadastrar imóveis | **3** (corretor) / **5** (imobiliária, trial) |
| Fotos por imóvel | **5** |
| Aparecer no hub + ranquear por match | flywheel, nunca cobra |
| Página SEO de cada imóvel | traz tráfego orgânico pro corretor |
| Contador de interesse | "5 pessoas quiseram falar" — prova tráfego antes de pagar |
| Contato do comprador (lead) | **5 leads/mês com botão de WhatsApp**, depois só Pro |
| Notificação de lead | atrasada (Pro = tempo real) |
| Selo verificado (CRECI) | confiança ajuda o hub |
| Views por imóvel | gostinho de analytics |
| **Secretária IA** | **trial 7 dias (dispara no 1º uso) → depois bloqueia 100%** |

## Plano PRO (corretor) — a grana

Lead nominal **ilimitado + contato na hora** · **Secretária IA completa** · atribuição (de qual imóvel veio) · CRM/pipeline cheio · notificação tempo real · imóveis **ilimitado** · fotos ilimitado + vídeo/tour · destaque/boost · analytics avançado.

## Plano IMOBILIÁRIA (Fase 2)

Tudo do Pro + multi-corretor, distribuição de leads, papéis (admin/corretor), performance por corretor, white-label leve.

---

## Catálogo completo (~75 features)

Legenda Fase: **M** = MVP v1 · **FF** = Fast-follow (logo após MVP) · **2** = Fase 2

### A. Hub / Busca — comprador (grátis)
| # | Feature | Fase |
|---|---|---|
| A1 | Filtro (tipo, venda/aluguel, bairro, preço, m², quartos, banho, vaga) | M |
| A2 | Ordenação por match (nunca por quem paga) | M |
| A3 | Página individual do imóvel, indexável (SEO) | M |
| A4 | Galeria de fotos | M |
| A5 | Vídeo / tour 360 / 3D | 2 |
| A6 | Botão "Tenho interesse" → captura lead (mediado) | M |
| A7 | Busca por mapa / bairro | M |
| A8 | Favoritar imóvel | 2 |
| A9 | Salvar busca + alerta de novo imóvel | 2 |
| A10 | Comparar imóveis | 2 |
| A11 | Compartilhar imóvel | M |
| A12 | Inteligência de mercado: preço/m² por bairro | 2 |

### B. Perfil corretor/imobiliária
| # | Feature | Quem/Plano | Fase |
|---|---|---|---|
| B1 | Perfil público (bio, foto, região, contato mediado) | Free | M |
| B2 | Vitrine/feed dos imóveis | Free | M |
| B3 | Selo verificado (CRECI) | Free | M |
| B4 | Link único / vanity URL | Pro | 2 |
| B5 | Stats públicos (nº imóveis, tempo resposta) | Free | 2 |
| B6 | Seguir corretor | Comprador | 2 |

### C. Gestão de imóveis — corretor
| # | Feature | Plano | Fase |
|---|---|---|---|
| C1 | Cadastrar imóvel | Free 3/5 · Pro ilimitado | M |
| C2 | Editar / pausar / arquivar | Free | M |
| C3 | Marcar vendido/alugado (tira do hub) | Free | M |
| C4 | Fotos por imóvel | Free 5 · Pro ilimitado | M |
| C5 | Vídeo / tour | Pro | 2 |
| C6 | Destaque/boost (slot rotulado) | Pro | FF/2 |
| C7 | Importação em massa (imob) | Pro | 2 |
| C8 | Sync com portais (ZAP/VivaReal/OLX) | Pro | 2 |

### D. Leads / conversão — corretor (o coração)
| # | Feature | Plano | Fase |
|---|---|---|---|
| D1 | Captura de lead nominal (nome+tel+imóvel) | Free 5/mês · Pro ilimitado | M |
| D2 | Contato mediado (form→botão WhatsApp; número escondido) | mecânica base | M |
| D3 | Cota de lead c/ botão WhatsApp | Free 5/mês · Pro ilimitado | M |
| D4 | Notificação de lead | Free atrasada · Pro tempo real | M |
| D5 | Atribuição (de qual imóvel veio) | Pro | M |
| D6 | Contador público de interesse | Free | M |
| D7 | Reembolso/disputa de lead falso | Pro | 2 |
| D8 | Histórico de leads | Free simples · Pro full | M |

### E. CRM / funil — corretor (Pro)
| # | Feature | Fase |
|---|---|---|
| E1 | Pipeline (novo→contato→visita→proposta→fechado) | M |
| E2 | Notas por lead | M |
| E3 | Follow-up / lembrete | 2 |
| E4 | Tags | 2 |
| E5 | Exportar | 2 |

### F. Secretária IA — corretor (**trial 7d completo → bloqueia 100% → Pro**)
| # | Feature | Fase |
|---|---|---|
| F1 | Comando por voz/áudio + texto | FF |
| F2 | Poder total na conta (marcar vendido, atualizar, cadastrar por voz) | FF |
| F3 | Rascunho/resposta automática de lead | FF |
| F4 | Follow-up automático | 2 |
| F5 | Qualificação de lead | 2 |
| F6 | Gerar descrição de anúncio | FF |
| F7 | Gerar post/campanha social | 2 |
| F8 | Relatório falado ("como foi minha semana") | 2 |
| F9 | Agendar visita | 2 |
| F10 | Secretária no WhatsApp | 2 |

### G. Imobiliária / equipe — Pro Imob (Fase 2)
| # | Feature | Fase |
|---|---|---|
| G1 | Múltiplos corretores numa conta | 2 |
| G2 | Distribuição de leads pra equipe | 2 |
| G3 | Papéis/permissões (admin/corretor) | 2 |
| G4 | Performance por corretor | 2 |
| G5 | White-label leve | 2 |

### H. Analytics — corretor
| # | Feature | Plano | Fase |
|---|---|---|---|
| H1 | Views por imóvel | Free | M |
| H2 | Origem do tráfego | Pro | 2 |
| H3 | Conversão view→lead | Pro | M |
| H4 | Posição do imóvel no filtro | Pro | 2 |
| H5 | Comparativo com média do mercado | Pro | 2 |

### I. Conta / pagamento — corretor
| # | Feature | Fase |
|---|---|---|
| I1 | Cadastro/login corretor (valida CRECI) | M |
| I2 | Assinatura mensal + upgrade/downgrade | M |
| I3 | Cobrança Asaas (PIX recorrente/boleto/cartão) | M |
| I4 | Nota fiscal | 2 |
| I5 | Plano anual à vista (2 meses off) | M |

### J. Confiança / moderação — sistema
| # | Feature | Fase |
|---|---|---|
| J1 | Moderação de anúncio (anti-spam) | M |
| J2 | **OCR anti-contato na foto/texto (free)** — pilar | M |
| J3 | Denunciar imóvel (comprador) | 2 |

### K. Fase 2 — monetização extra
| # | Feature |
|---|---|
| K1 | Referral: financiamento/seguro/avaliação/mudança (comissão) |
| K2 | Anúncio de construtora/lançamento (ticket alto) |
| K3 | Portal de construtora |
| K4 | API pública |
| K5 | App mobile nativo |

---

## Escopo do MVP v1 (só o osso que prova pagamento)

Hub (A1,A2,A3,A4,A6,A7,A11) · Perfil (B1,B2,B3) · Imóveis (C1,C2,C3,C4) · Leads (D1-D6,D8) · CRM lite (E1,E2) · Conta (I1,I2,I3,I5) · Moderação (J1,**J2**).

**Fast-follow (banco pronto dia 1):** Secretária IA lite (F1,F2,F3,F6) — liga o trial de 7 dias e vira a âncora do Pro.

> No lançamento v1 a IA ainda não existe → paywall inicial = o **lead** (lead ilimitado + tempo real + atribuição = valor do Pro). Quando a IA sobe (fast-follow), o trial de 7 dias entra e vira o gancho principal do Pro.

**Fora (Fase 2):** vídeo/tour, salvar busca, comparar, inteligência de mercado, multi-seat/imob, analytics avançado, referral, construtora, app, WhatsApp IA, follow-up auto.

**Nunca buildar:** enterprise, cobrança por uso, taxa sobre venda.

---

## Decisões 2026-07-02 (Mestre)
- **Estrutura = 3 tiers (escada): Free → Pro (corretor R$279) → Imobiliária (equipe, R$199/corretor, Fase 2).** O "Max" = o plano de imobiliária.
- **Preço Pro = R$279/mês.** Planos **mensal + anual** (anual com desconto — rec 2 meses off = R$2.790/ano). **Sem founding** (Mestre cortou).
- **Secretária IA:** trial 7 dias, dispara **no 1º uso da IA** (não no cadastro) → depois bloqueia 100% → Pro.
- **Contato/lead:** free = **5 leads/mês (reseta) com botão de WhatsApp**, depois só Pro. Contato mediado (form→botão) + OCR anti-contato confirmados. Leads 6+ ficam **borrados/visíveis-mas-travados** (corretor sabe que existe, não vê nem age).
- **Início bootstrap:** aporte mínimo (~R$2k = 4 vídeos de influencer). Mídia só depois de tração. Descarta o raise de R$15-18k.
- Cota free travada: **3 imóveis (corretor) / 5 (imob)** + **5 fotos**.
- Boost (C6) = **Fase 2**.
- Nome = **Imora** (codinome; decide depois).

## Resolvido 2026-07-02
A1 → 3 tiers (Free/Pro/Max) · B1 → trial dispara no 1º uso da IA · B4 → free 5 leads com botão WhatsApp, depois Pro · B6 → resolvido pelo B4 (contato mediado via form + OCR) · cota 5 leads **reseta por mês** · leads 6+ no free = **borrados/visíveis-mas-travados** (sabe que existe, não vê nem age → gancho de conversão).

## Planos definidos (provisório 2026-07-02 — "deixa assim, com tempo mudamos")

**3 tiers, escada: Free → Pro (corretor) → Imobiliária (equipe).** Toggle mensal/anual (anual = 2 meses off).

### FREE — R$0 · corretor começando
Perfil pro + vitrine · até **3 imóveis** (5 fotos) · aparece no hub + Google (SEO) · **5 leads/mês** com botão WhatsApp · contador de interesse · **7 dias de Secretária IA** (dispara no 1º uso) · views por imóvel.
**Trava:** 6º lead+ borrado/bloqueado (vê que tem cliente, não consegue falar).

### PRO — R$279/mês · ou R$2.790/ano (2 off) · corretor solo ⭐
Tudo do Free + **leads ilimitados com contato na hora** · **Secretária IA completa** (voz/responde/cadastra) · imóveis+fotos ilimitados · vídeo/tour · atribuição · CRM completo · notificação tempo real · analytics.

### IMOBILIÁRIA — R$199/corretor/mês · anual 2 off · equipe · **Fase 2**
Tudo do Pro por corretor + vários corretores/1 conta · distribuição de lead · painel+ranking de equipe · papéis (admin/corretor) · 1 fatura · estoque compartilhado.
Por assento = mais barato/cabeça que Pro solo, mas soma mais no total; a **camada de equipe** é o que impede canibalizar (senão compram N Pro avulsos).

*(cards visuais + racional de preço no histórico da sessão)*
