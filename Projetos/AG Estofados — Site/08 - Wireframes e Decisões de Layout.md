# 08 — Wireframes e Decisões de Layout

> Voltar ao [[AG Estofados — Índice]]

Wireframes em ASCII (referência rápida) + decisões de comportamento. Servem de base para o mockup de alta fidelidade no Antigravity (Fase 3 — ver [[05 - Roadmap e Próximos Passos]]).

## 1. Sistema de grid

| Breakpoint | Largura | Colunas | Gutter | Container max |
|---|---|---|---|---|
| Mobile | < 768 px | 4 | 16 px | 100% (com padding 20 px) |
| Tablet | 768 – 1023 px | 8 | 20 px | 720 px |
| Desktop | 1024 – 1439 px | 12 | 24 px | 1200 px |
| Wide | ≥ 1440 px | 12 | 24 px | 1320 px |

**Princípio:** mobile-first. A maior parte do tráfego vem do link da bio do Instagram.

## 2. Header (todas as páginas)

```
┌──────────────────────────────────────────────────────────────────┐
│ [AG logo dourado]    Início  Catálogo  Sobre  Projetos  Contato  │
│                                                  [🟢 WhatsApp]    │
└──────────────────────────────────────────────────────────────────┘
```

**Decisões:**

- **Sticky** (gruda no topo no scroll), com leve transparência sobre hero e fundo sólido fora dele.
- Altura: 72 px desktop, 56 px mobile.
- Mobile: logo à esquerda + ícone hamburger à direita. Menu vira drawer lateral.
- Botão WhatsApp visível **no header** (desktop) **e flutuante** (mobile + desktop ao scrollar).

## 3. Home

```
┌──────────────────────────────────────────────────────────────────┐
│  HEADER                                                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   HERO — foto ambientada full-bleed (90vh desktop / 80vh mobile) │
│   ┌────────────────────────────────────┐                         │
│   │  Estofados feitos à mão, sob medida│                         │
│   │  para o seu jeito de viver.        │                         │
│   │                                    │                         │
│   │  Em Patos de Minas desde 1997.     │                         │
│   │                                    │                         │
│   │  [Solicitar orçamento] [Catálogo]  │                         │
│   └────────────────────────────────────┘                         │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│  FAIXA DE CREDIBILIDADE — 5 ícones em linha dourada              │
│   [⏳ Desde 1997]  [✋ À mão]  [📐 Sob medida]  [🎨 3D]  [🚚 Região] │
├──────────────────────────────────────────────────────────────────┤
│  CATEGORIAS — grade de 5 cards com foto                          │
│   ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐         │
│   │ Sofás  │ │ Autom. │ │Poltrona│ │Cabeceira│ │Banqueta│        │
│   └────────┘ └────────┘ └────────┘ └────────┘ └────────┘         │
├──────────────────────────────────────────────────────────────────┤
│  PEÇAS EM DESTAQUE — carrossel horizontal (3 cards visíveis)     │
│   ┌──────────┐ ┌──────────┐ ┌──────────┐                         │
│   │ [foto]   │ │ [foto]   │ │ [foto]   │     →                   │
│   │ Nome     │ │ Nome     │ │ Nome     │                         │
│   │ Categoria│ │ Categoria│ │ Categoria│                         │
│   │ [Orçar]  │ │ [Orçar]  │ │ [Orçar]  │                         │
│   └──────────┘ └──────────┘ └──────────┘                         │
├──────────────────────────────────────────────────────────────────┤
│  COMO FUNCIONA — 4 passos numerados em linha                     │
│   01           02           03           04                      │
│   Conversa  → Projeto 3D → Produção  → Entrega                   │
├──────────────────────────────────────────────────────────────────┤
│  BLOCO SOBRE — split 50/50                                       │
│   ┌─────────────────┐ ┌─────────────────┐                        │
│   │ Mais de duas    │ │  [foto da loja] │                        │
│   │ décadas...      │ │                 │                        │
│   │ [Nossa história]│ │                 │                        │
│   └─────────────────┘ └─────────────────┘                        │
├──────────────────────────────────────────────────────────────────┤
│  PROJETOS 3D — galeria de 6 thumbnails + [Ver tudo]              │
├──────────────────────────────────────────────────────────────────┤
│  DEPOIMENTOS — carrossel de 3–5                                  │
│   ┌──────────────────────────────────────┐                       │
│   │ "Texto do depoimento..."             │                       │
│   │ — Nome, Cidade                       │                       │
│   └──────────────────────────────────────┘                       │
├──────────────────────────────────────────────────────────────────┤
│  CTA FINAL — faixa full-bleed escura com foto sutil de fundo     │
│   Vamos criar a sua peça?                                        │
│   [Chamar no WhatsApp]  [Solicitar orçamento]                    │
├──────────────────────────────────────────────────────────────────┤
│  FOOTER — 4 colunas: marca, navegação, contato, redes            │
└──────────────────────────────────────────────────────────────────┘

  [Botão WhatsApp flutuante — canto inferior direito, todas as páginas]
```

**Prioridade visual:** hero > categorias > peças em destaque > sobre/credibilidade > depoimentos > CTA.

## 4. Catálogo (`/catalogo`)

```
┌──────────────────────────────────────────────────────────────────┐
│  HEADER                                                          │
├──────────────────────────────────────────────────────────────────┤
│  Catálogo                                                        │
│  Algumas peças que já fizemos. Tudo é produzido sob medida.      │
├──────────────────────────────────────────────────────────────────┤
│  FILTROS (chips horizontais — sticky no scroll)                  │
│  [ Tudo ] [ Sofás ] [ Automatizados ] [ Poltronas ] [ Cabec. ]   │
├──────────────────────────────────────────────────────────────────┤
│  GRADE DE CARDS — 3 colunas desktop, 2 tablet, 1 mobile          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                          │
│  │ [foto]   │ │ [foto]   │ │ [foto]   │                          │
│  │ Nome     │ │ Nome     │ │ Nome     │                          │
│  │ Categoria│ │ Categoria│ │ Categoria│                          │
│  │ [Ver]    │ │ [Ver]    │ │ [Ver]    │                          │
│  └──────────┘ └──────────┘ └──────────┘                          │
│  (repete até esgotar)                                            │
├──────────────────────────────────────────────────────────────────┤
│  FAIXA CTA — "Não achou o ideal? A gente desenha pra você."      │
│  [Solicitar orçamento personalizado]                             │
├──────────────────────────────────────────────────────────────────┤
│  FOOTER                                                          │
└──────────────────────────────────────────────────────────────────┘
```

**Decisões:**

- Filtros como **chips** (não dropdown) — visual mais limpo, mais convidativo ao toque mobile.
- Sem paginação (catálogo é enxuto, 8–15 peças cabem em uma tela rolável).
- Card hover desktop: leve scale + dourado discreto no nome.

## 5. Página de Produto (`/produto/[slug]`)

```
┌──────────────────────────────────────────────────────────────────┐
│  HEADER                                                          │
├──────────────────────────────────────────────────────────────────┤
│  Catálogo > Sofás > Nome da peça     (breadcrumb)                │
├──────────────────────────────────────────────────────────────────┤
│  SPLIT 60/40 (desktop) — empilha no mobile                       │
│  ┌───────────────────────────┐ ┌──────────────────────┐          │
│  │                           │ │  Nome da peça        │          │
│  │     [FOTO PRINCIPAL]      │ │  Sofás · Sob medida  │          │
│  │                           │ │                      │          │
│  │  [thumb] [thumb] [thumb]  │ │  3 parágrafos de     │          │
│  │  [thumb] [thumb]          │ │  descrição.          │          │
│  │                           │ │                      │          │
│  │                           │ │  Você pode escolher: │          │
│  │                           │ │  • Medidas           │          │
│  │                           │ │  • Tecido            │          │
│  │                           │ │  • Cor               │          │
│  │                           │ │  • Densidade         │          │
│  │                           │ │  • Pé                │          │
│  │                           │ │  • Acabamentos       │          │
│  │                           │ │                      │          │
│  │                           │ │  ┌────────────────┐  │          │
│  │                           │ │  │ Solicitar      │  │          │
│  │                           │ │  │ orçamento      │  │          │
│  │                           │ │  └────────────────┘  │          │
│  └───────────────────────────┘ └──────────────────────┘          │
├──────────────────────────────────────────────────────────────────┤
│  FAIXA DE CONFIANÇA — "Feito à mão · Sob medida · Desde 1997"    │
├──────────────────────────────────────────────────────────────────┤
│  PEÇAS RELACIONADAS — 3 cards da mesma categoria                 │
├──────────────────────────────────────────────────────────────────┤
│  CTA FINAL                                                       │
├──────────────────────────────────────────────────────────────────┤
│  FOOTER                                                          │
└──────────────────────────────────────────────────────────────────┘
```

**Decisões:**

- **Galeria sticky** no desktop: a coluna esquerda fica fixa enquanto rola o conteúdo da direita.
- Thumbnails clicam para trocar a foto principal — lightbox em fullscreen ao clicar de novo.
- Botão de orçamento **sticky no mobile** (fica visível durante a rolagem).
- Sem preço, sem "quantidade", sem "adicionar ao carrinho" — proibido qualquer elemento de e-commerce.

## 6. Sobre / Nossa História

```
┌──────────────────────────────────────────────────────────────────┐
│  HEADER                                                          │
├──────────────────────────────────────────────────────────────────┤
│  HERO — foto da fachada/interior da loja (60vh)                  │
│   Estofar é o que a gente faz há mais de 25 anos.                │
├──────────────────────────────────────────────────────────────────┤
│  TEXTO PRINCIPAL — coluna única centralizada (max 720 px)        │
│  3–4 parágrafos da história.                                     │
├──────────────────────────────────────────────────────────────────┤
│  3 COLUNAS DE VALORES                                            │
│   ┌────────┐ ┌────────┐ ┌────────┐                               │
│   │À mão   │ │Sob med.│ │Exigente│                               │
│   └────────┘ └────────┘ └────────┘                               │
├──────────────────────────────────────────────────────────────────┤
│  GALERIA DE PROCESSO — 4–6 fotos: mãos, tecidos, ferramentas     │
├──────────────────────────────────────────────────────────────────┤
│  EQUIPE — foto do grupo (full-bleed) + parágrafo                 │
├──────────────────────────────────────────────────────────────────┤
│  CTA FINAL                                                       │
└──────────────────────────────────────────────────────────────────┘
```

## 7. Projetos 3D / Portfólio

```
┌──────────────────────────────────────────────────────────────────┐
│  HEADER                                                          │
├──────────────────────────────────────────────────────────────────┤
│  HERO simples — título + 1 frase                                 │
│   Projetos 3D — você vê antes da gente produzir.                 │
├──────────────────────────────────────────────────────────────────┤
│  GALERIA — grade de 2–3 colunas com pares render × foto real     │
│  ┌─────────────┐ ┌─────────────┐                                 │
│  │ Render 3D   │ │ Peça real   │  (par sincronizado)             │
│  └─────────────┘ └─────────────┘                                 │
├──────────────────────────────────────────────────────────────────┤
│  CTA — "Quer ver o seu ambiente em 3D? A gente faz junto."       │
└──────────────────────────────────────────────────────────────────┘
```

## 8. Contato

```
┌──────────────────────────────────────────────────────────────────┐
│  HEADER                                                          │
├──────────────────────────────────────────────────────────────────┤
│  SPLIT 50/50 (empilha no mobile)                                 │
│  ┌─────────────────┐ ┌─────────────────┐                         │
│  │ Vamos conversar │ │   [MAPA]        │                         │
│  │                 │ │                 │                         │
│  │ Loja:           │ │                 │                         │
│  │ Rua Silva...    │ │                 │                         │
│  │                 │ │                 │                         │
│  │ Horário: ...    │ │                 │                         │
│  │ [WhatsApp]      │ │                 │                         │
│  │ Instagram: @ag..│ │                 │                         │
│  └─────────────────┘ └─────────────────┘                         │
├──────────────────────────────────────────────────────────────────┤
│  FOOTER                                                          │
└──────────────────────────────────────────────────────────────────┘
```

## 9. Orçamento

```
┌──────────────────────────────────────────────────────────────────┐
│  HEADER                                                          │
├──────────────────────────────────────────────────────────────────┤
│  FORMULÁRIO — coluna única centralizada (max 600 px)             │
│   Solicitar orçamento                                            │
│   Conta pra gente o que você está pensando.                      │
│                                                                  │
│   [ Nome completo ]                                              │
│   [ WhatsApp ]                                                   │
│   [ Cidade ]                                                     │
│   [ Tipo de peça ▼ ]                                             │
│   [ Conta pra gente o que você imagina (textarea) ]              │
│   [ Modelo de referência (preenchido se vem de produto) ]        │
│                                                                  │
│   [ Enviar orçamento ]                                           │
│                                                                  │
│   Ou fale direto: [WhatsApp]                                     │
├──────────────────────────────────────────────────────────────────┤
│  FOOTER                                                          │
└──────────────────────────────────────────────────────────────────┘
```

## 10. Footer (todas as páginas)

```
┌──────────────────────────────────────────────────────────────────┐
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐             │
│  │ [Logo]   │ │ Navegação│ │ Contato  │ │ Siga     │             │
│  │ Tagline  │ │ • Início │ │ Rua...   │ │ [Insta]  │             │
│  │          │ │ • Catál. │ │ WhatsApp │ │ [WApp]   │             │
│  │          │ │ • Sobre  │ │ Horário  │ │          │             │
│  │          │ │ • Projet.│ │          │ │          │             │
│  │          │ │ • Contato│ │          │ │          │             │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘             │
│  ───────────────────────────────────────────────────────────     │
│  © AG Estofados, desde 1997 · Patos de Minas/MG                  │
│  Site por ForYou Code                                            │
└──────────────────────────────────────────────────────────────────┘
```

## 11. Comportamentos transversais

- **Botão WhatsApp flutuante** — canto inferior direito, todas as páginas, 56 px circular, fundo verde WhatsApp, ícone branco. Aparece sempre que se rola além do hero.
- **Animações** — fade-in suave em entradas de seção (Intersection Observer, sem libs pesadas). Hover discreto nos cards. Sem parallax exagerado, sem efeitos que comprometam Lighthouse.
- **Scroll** — suave no clique de âncoras. Sticky header com leve sombra ao deixar o topo.
- **Loading** — imagens com lazy-load nativo + placeholder de cor dominante. Nada de spinners genéricos.
- **Estados vazios** — não aplicáveis nesta fase (sem busca, sem listas dinâmicas).
- **404** — página simples com ilustração mínima + "Voltar ao início" + sugestão de catálogo.

## 12. Breakpoints e regras de adaptação

| Componente | Mobile | Desktop |
|---|---|---|
| Menu | Drawer lateral via hamburger | Linha horizontal no header |
| Hero | Vertical 80vh, foto ocupa fundo | Vertical 90vh, foto ocupa fundo |
| Categorias | Carrossel horizontal (swipe) | Grade de 5 colunas |
| Peças em destaque | Carrossel 1.2 cards visíveis | Carrossel 3 cards visíveis |
| Como funciona | 4 passos empilhados | 4 passos lado a lado com seta |
| Produto | 1 coluna (galeria sobre conteúdo) | Split 60/40 com galeria sticky |
| Footer | Acordeão por seção (opcional) | 4 colunas |
| Botão WhatsApp | Flutuante 56 px | Flutuante 56 px + visível no header |
