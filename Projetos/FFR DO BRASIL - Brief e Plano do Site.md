# FFR DO BRASIL — Brief + Plano do Site

> Lead pago R$19,90 · 2026-06-20 · Site institucional · Objetivo: vender mais
> Entregável: brief interpretado + plano de seções pronto pra construir (Lovable / Next).

---

## 1. Dados do cliente

| Campo | Valor |
|---|---|
| Responsável | Flavio Rodrigues |
| Empresa | FFR DO BRASIL |
| WhatsApp | (45) 98811-4290 → `5545988114290` |
| E-mail | templodaslendas@gmail.com |
| CPF | 079.668.839-73 |
| Tipo | Site institucional |
| Objetivo | Vender mais / fechar negócio |
| Estilo | Premium e elegante |
| Cores | Bandeira do Brasil em destaque |
| Funções | WhatsApp / contato |

**O que a FFR faz (texto do cliente):** desenvolve sites e apps, além de automações e sistemas completos.

---

## 2. O que o cliente realmente quer (leitura entre linhas)

O formulário diz "site institucional". O objetivo real é **fechar negócio**. O site não é portfólio bonito parado — é **ferramenta de venda**.

Jornada-alvo do visitante:
1. Bate o olho → "essa empresa é séria e profissional" (premium resolve isso).
2. Entende em 5s o que a FFR faz e qual problema resolve.
3. Confia (prova social, garantia, identidade nacional sólida).
4. Abre o WhatsApp e puxa conversa → FFR fecha no 1:1.

Por isso o site precisa de **um CTA dominante (WhatsApp) repetido**, copy orientada a benefício (não a tecnologia), e visual que transmita confiança.

**Tensão a resolver — "cores da bandeira em destaque" + "premium":**
Verde/amarelo/azul saturados juntos = cara de barato / cara de governo. Solução premium: **base escura, amarelo tom ouro como cor de ação, verde sóbrio profundo, azul fechado**. Bandeira entra como *sotaque de identidade nacional*, não como tinta jogada na tela.

---

## 3. Identidade visual

**Paleta (premium-Brasil):**

| Uso | Cor | Hex |
|---|---|---|
| Fundo base | Grafite quase-preto | `#0B0E11` |
| Fundo seção alt | Verde-petróleo escuro | `#0E1A14` |
| Ação / destaque (CTA) | Amarelo-ouro | `#F2C200` |
| Sucesso / acento | Verde bandeira sóbrio | `#1B8A4B` |
| Detalhe / link | Azul nacional fechado | `#1B3A6B` |
| Texto principal | Branco gelo | `#F5F6F5` |
| Texto secundário | Cinza claro | `#A9B0AD` |

Regra de ouro: **amarelo só no que é pra clicar**. Verde e azul como acentos finos (bordas, ícones, números). Fundo escuro domina → sensação premium.

**Tipografia:** título display moderna e encorpada (ex.: *Sora*, *Space Grotesk* ou *Clash Display*); corpo neutro legível (*Inter*). Pesos altos no hero, espaçamento generoso.

**Linguagem visual:** muito respiro (whitespace), gradientes sutis verde→preto, micro-detalhes dourados, sombras suaves, cantos arredondados médios. Nada de glassmorphism exagerado nem stock genérico.

---

## 4. Estrutura da página (one-page, alta conversão)

Ordem das seções e função de cada uma:

### 4.1 Header (fixo)
- Logo FFR (esq.) · menu curto (Serviços · Como funciona · Contato) · **botão WhatsApp** (dir., amarelo).
- Sticky, encolhe no scroll.

### 4.2 Hero
- **Headline (benefício, não tecnologia):**
  *"Sites, apps e sistemas que fazem seu negócio vender mais."*
- **Sub:** *"A FFR do Brasil desenvolve sites, aplicativos, automações e sistemas completos sob medida. Tecnologia de verdade, feita pra dar resultado."*
- 2 botões: **[Falar no WhatsApp]** (primário, ouro) · [Ver o que fazemos] (secundário, scroll).
- Acento visual: faixa/gradiente discreto verde-amarelo-azul ou bandeira estilizada minimalista ao fundo.
- Selo de confiança curto: "Empresas atendidas em todo o Brasil" / anos de experiência (preencher real).

### 4.3 Prova de valor rápida (faixa)
3–4 números ou selos: projetos entregues · clientes · suporte · tecnologias. (Preencher com dados reais — ver §7.)

### 4.4 Serviços (núcleo)
Grid de 4 cards, ícone + título + 1 linha de benefício:
1. **Sites** — institucional, landing, e-commerce que converte.
2. **Aplicativos** — apps iOS/Android sob medida.
3. **Automações** — processos no automático, menos trabalho manual.
4. **Sistemas completos** — plataformas e ERPs feitos pro seu negócio.
Cada card pode ter mini-CTA "Quero esse" → WhatsApp com mensagem pré-preenchida do serviço.

### 4.5 Como funciona (3 passos)
Reduz fricção / objeção: **1. Você fala o que precisa → 2. A gente planeja e orça → 3. Entregamos e damos suporte.** CTA ao final.

### 4.6 Diferenciais / Por que a FFR
4–6 bullets de confiança: tecnologia atual, entrega no prazo, suporte direto, empresa brasileira, atendimento humano no WhatsApp. (Substituir por reais.)

### 4.7 Prova social
Depoimentos (2–3) e/ou logos de clientes e/ou prints de projetos. **Placeholder se ainda não houver — ver §7.**

### 4.8 CTA final (faixa forte)
Fundo amarelo ou verde profundo, headline direta: *"Bora tirar seu projeto do papel?"* + botão WhatsApp grande.

### 4.9 Footer
Logo · contato (WhatsApp, e-mail) · CNPJ/razão se houver · redes · © FFR do Brasil.

---

## 5. Conversão (detalhe do WhatsApp)

Todo botão WhatsApp usa link `wa.me` com mensagem pré-preenchida (cai direto na conversa, FFR já sabe a origem):

```
https://wa.me/5545988114290?text=Ol%C3%A1%2C%20vim%20pelo%20site%20da%20FFR%20do%20Brasil%20e%20quero%20um%20or%C3%A7amento.
```

Texto decodificado: *"Olá, vim pelo site da FFR do Brasil e quero um orçamento."*

- Variar o `text=` por serviço nos cards (ex.: "...quero um site", "...quero um app").
- Botão flutuante WhatsApp no canto inf. dir. em todas as seções (mobile especialmente).
- E-mail como contato secundário no footer.

---

## 6. Notas de build

- **Stack sugerida:** Next.js + Tailwind (ou Lovable, que era o destino). One-page, mobile-first.
- **Performance:** imagens otimizadas/WebP, fontes via `next/font` ou preload, lazy-load nas seções abaixo da dobra. Meta: LCP < 2,5s.
- **SEO básico:** `<title>` = "FFR do Brasil — Sites, Apps, Automações e Sistemas"; meta description com benefício; Open Graph (imagem + título) pro link bonito no WhatsApp/Insta; favicon; `lang="pt-BR"`.
- **Responsivo:** prioridade mobile — a maioria dos leads abre no celular.
- **Analytics:** pixel/GA opcional + evento de clique no botão WhatsApp (medir conversão).
- **Domínio:** definir (ffrdobrasil.com.br?) — checar disponibilidade.

---

## 7. Assets que faltam (pedir pro Flavio antes do build final)

- [ ] Logo da FFR (vetor/PNG fundo transparente).
- [ ] Números reais (anos no mercado, qtd. projetos/clientes).
- [ ] Portfólio real: 3–6 projetos com print + nome + link.
- [ ] Depoimentos de clientes (nome + foto/empresa).
- [ ] Razão social / CNPJ pro footer (se quiser passar mais credibilidade).
- [ ] Redes sociais (Instagram?).
- [ ] Domínio desejado.

Enquanto não vierem: usar placeholders premium e copy genérica-mas-forte; trocar depois.

---

## 8. Próximo passo

Confirmar com o Flavio os assets do §7 → construir a partir desta estrutura → deploy → mandar link pra ele aprovar e já começar a captar pelo WhatsApp.
