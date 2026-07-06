---
projeto: Hub Imobiliário Patos de Minas
status: planejamento / pré-validação
data: 2026-06-29
socios: Wilson (Mestre, builder técnico), Marco, Eduardo (vendas/relacionamento)
cidade: Patos de Minas — MG (~150k hab)
tags: [foryoucode, imobiliario, saas, hub, patos-de-minas]
---

# Hub Imobiliário Patos de Minas — Conselho e Plano

> Nome do projeto provisório. Origem: conversa de planejamento (Perplexity) +
> conselho de 6 especialistas convocado em 2026-06-29.

## A visão (corrigida pelo Mestre)

Um **hub de imóveis da cidade inteira**, no objetivo igual ao **DF Imóveis** de
Brasília (mas não idêntico na execução).

- **A porta principal é o HUB / busca.** Cliente final entra, **filtra**
  (metragem, quartos, bairro, preço, tipo...) e aparecem os imóveis **mais
  próximos do que ele pediu** — misturados, de corretores e imobiliárias
  variados, **independente de quem é o dono**. O filtro manda, não a marca nem
  o tamanho do anunciante.
- Clica no imóvel → fala direto com o dono.
- **Em paralelo**, cada corretor / imobiliária / construtora tem **perfil
  próprio tipo Instagram**, com todos os imóveis dele juntos. O cliente pode
  entrar no perfil e ver só daquele profissional.

Igual ao DF Imóveis no **objetivo** (juntar todo mundo da região num site
buscável; cada profissional tem conta/painel; selo de confiança; parceria entre
corretores). Diferente na execução — adaptado a Patos.

## Veredito do conselho (presidente, palavra final)

**Vale a pena — mas NÃO como o plano original (marketplace aberto que nasce
querendo competir de frente com o imobpatos).** O hub é o **destino certo**; o
conselho só resolveu o "como encher sem morrer no cold-start":

- O hub **não pode nascer vazio** brigando com o imobpatos (que já agrega ~25
  imobiliárias, +4 mil imóveis E o tráfego/SEO local de "imóveis Patos de Minas").
- Forma de encher: **assina corretor/imobiliária → o estoque dele entra no hub
  E ele ganha o perfil.** O hub cresce por **adesão legítima**, nunca por pegar
  imóvel de quem não topou (isso queima confiança e em cidade pequena é fatal —
  corretor liga pro CRECI, não assina).
- **Mesma visão do Mestre; o conselho só resolveu o motor de preenchimento.**

### Regra-mãe inegociável
> Só aparece no hub imóvel de **quem assinou e autorizou**. Zero scraping de
> estoque alheio.

## O que vamos construir (MVP)

Núcleo enxuto (~6–8 semanas):

1. **Hub de busca da cidade** — filtro por metragem, quartos, bairro, preço,
   tipo, status. Ordem por **aderência ao filtro** (melhor-match primeiro),
   independente do anunciante. Imóveis só dos pagantes/autorizados.
2. **Página de imóvel** com captura de **lead nominal** (nome + telefone + de
   qual imóvel veio).
3. **Perfil tipo Instagram** por corretor/imobiliária (todos os imóveis dele +
   contadores vendidos/alugados) — cliente acessa direto.
4. **Painel do anunciante** — seus imóveis, leads recebidos, marcar
   vendido/alugado, acompanhar.
5. **Onboarding por importação de feed** — sobe o estoque do anunciante de uma
   vez (sem cadastro manual um a um), só o estoque dele.

### Fora do MVP (fase 2+)
WhatsApp automático em massa · IA de atendimento · sistema de pagamento dentro
da plataforma · relatórios complexos · módulo construtora · destaque pago.

## Por tipo de cliente

- **Corretor:** perfil Instagram próprio + imóveis no hub + lead nominal (sabe
  de qual imóvel veio) + quadro de acompanhamento + contadores.
- **Imobiliária:** perfil institucional + vários corretores na mesma conta +
  vê todos os leads + estoque/status. Sem planilha/caderno.
- **Construtora (fase 2):** página de lançamento + capta interessado por
  empreendimento.
- **Cliente final:** busca a cidade inteira, filtra exatamente o que quer,
  melhor-match primeiro, fala direto com o dono. Sem caçar em 10 sites.

## Dinheiro

- Começa **de graça** pra entrar e provar que chega contato.
- Quando provar valor: **mensalidade fixa baixa** (founding R$199–249/mês,
  travado 12 meses, **sem setup fee**).
- Destaque pago / performance: só **fase 2**, depois de tráfego provado.
- **Estudar modelos free** (pedido do Mestre): freemium / trial / free + cobra
  no resultado. (pendente)

### Projeção (planejar pelo piso)
| Fase | Contas | MRR |
|------|--------|-----|
| Mês 0–3 | 5 founding × R$199 | ~R$1.000 |
| Mês 4–6 | 12–15 × ~R$220 | ~R$2,6–3,3k |
| Mês 7–12 | 25–30 × ~R$230 | ~R$5,7–6,9k → break-even |

Enterprise R$2,5k/mês = fantasia no ano 1. Esquecer.

## 5 maiores riscos + mitigação

1. **Atribuição lead→venda (fecham offline)** → lead nominal por imóvel +
   wa.me/UTM + "marcar vendido" + lembrete mensal. Dia 1.
2. **Vazamento de captação (corretor acha que alimenta o rival)** → selo
   "captado por", flag de exclusividade, lead vai sempre pro dono. Só estoque
   de quem assinou.
3. **Cold-start vs imobpatos** → encher por adesão; SEO local por bairro sobre
   o estoque dos pagantes.
4. **Mercado pequeno (teto MRR ~R$9–25k)** → sócios = time, burn ~zero,
   tech simples, escopo cortado.
5. **Não fechar os 5 founding** → o gate de pré-venda É a mitigação.

## Gate de morte (decisão do presidente)

> **Não fechou 5 anunciantes pagantes (PIX/compromisso na mão) em 90 dias =
> encerra.** Critério por escrito. É hobby caro, não negócio.

## Plano 90 dias

- **Dias 1–30:** Marco + Eduardo levantam 15–20 alvos via relacionamento e
  vendem no olho (vitrine + lead nominal + selo). **Meta dura: 5 PIX.** Wilson
  faz protótipo de 1 tela pra demo.
- **Dias 31–60:** Wilson constrói o MVP + importação de feed só dos founding.
  Atribuição instrumentada com lead real.
- **Dias 61–90:** liga o hub público + SEO por bairro dos founding. Relatório
  de lead na mão de cada cliente. Fechar contas 6–10.

## Time

- **Wilson (Mestre):** único builder técnico (Marco e Eduardo não codam).
- **Marco + Eduardo:** vendas e relacionamento local — exatamente o trabalho
  mais duro dos 90 dias (fechar os founding).
- Mais um técnico só se quiser **acelerar** o build; não é pré-requisito.

## Decisões ainda pendentes (Mestre)

1. Flag do hub público nasce ON ou OFF por padrão? (recomendação: ON pros
   founding, com saída fácil)
2. Exclusividade = trava dura (imóvel só de 1 corretor) ou só selo "captado por"?
3. Quem são os 3–5 âncoras nominais e qual sócio fecha cada um.
4. ARPU founding: R$199 ou R$249? Travar e não mexer 12 meses.
5. Construtora + IA: confirmar fase 2.
6. Qual dos modelos free adotar (estudar).

---

## Anexos / contexto
- Conversa original de planejamento: `Downloads/Precisamos fazer um estudo de
  mercado relacionado.md` (export Perplexity).
- Concorrente incumbente: **imobpatos.com.br** (agregador, ~25 imobiliárias,
  +4 mil imóveis).
- Inspiração de objetivo: **DF Imóveis** (dfimoveis.com.br) — hub do DF.
- Conselho de 6 especialistas (estratégia, produto, financeiro, growth,
  mercado local, cético) + presidente — convocado 2026-06-29.
