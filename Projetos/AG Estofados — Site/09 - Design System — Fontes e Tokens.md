# 09 — Design System — Fontes e Tokens

> Voltar ao [[AG Estofados — Índice]]
>
> ⚠️ Atualizado após decisão de [[10 - Toolchain Premium e Workflow MCP]] — par tipográfico mudou de Cormorant para Migra/PP Editorial New para criar tensão tipográfica.

Decisão final de tipografia e fechamento dos tokens. Documento de referência para o projeto Lovable e para a injeção via MCP (Fase 4 — ver [[05 - Roadmap e Próximos Passos]]).

## 1. Decisão final de fontes

### Par escolhido

| Função | Fonte | Origem |
|---|---|---|
| **Display (hero, headlines grandes)** | **PP Editorial New** (alternativa: Migra) | Pangram Pangram (freemium uso comercial pequeno) |
| **Corpo / interface** | **Inter** | Google Fonts / Fontsource |
| **Quotes / depoimentos** | **Cormorant Garamond italic** | Google Fonts |

### Por que esse par

**PP Editorial New** é serif moderna desenhada para criar tensão tipográfica em caixa alta gigante — mesma família estética de sites como Nalu Faria, COCO HOME e estúdios premium contemporâneos. Pesos altos têm corte afiado; pesos baixos viram editorial elegante. Combina com "feito à mão desde 1997" sem virar "loja antiga".

**Inter** continua como body por ser UI-native, variable (1 arquivo, todos os pesos) e altamente legível em qualquer tamanho sobre fundo escuro.

**Cormorant Garamond italic** retorna como detalhe elegante em depoimentos e citações — onde calma é virtude.

### Pesos usados

- **PP Editorial New:** Ultralight (100), Light (300), Regular (400), Italic (400i). O contraste entre Ultralight gigante e Regular médio é o que cria a tensão característica.
- **Inter:** Regular (400), Medium (500), SemiBold (600), Bold (700).
- **Cormorant Garamond:** Italic (400i) apenas.

### Carregamento

- Self-host via **Fontsource** (Inter, Cormorant) + arquivos locais (PP Editorial New, baixados do Pangram Pangram).
- `font-display: swap`.
- Preload do Ultralight 100 do PP Editorial New + Inter 400 (pesos do hero).
- Subset latin-ext (cobre português).

## 2. Escala tipográfica

Sistema baseado em 16 px = 1 rem. Razão modular ~1.333 (escala forte para sustentar headlines gigantes).

| Token | Mobile | Desktop | Fonte | Peso | Uso |
|---|---|---|---|---|---|
| `--font-display` | 56 px / 3.5 rem | 144 px / 9 rem | PP Editorial | 100 (Ultralight) | Hero da Home (gigante, caixa alta) |
| `--font-display-sm` | 40 px / 2.5 rem | 96 px / 6 rem | PP Editorial | 100 | Heros internos |
| `--font-h1` | 36 px / 2.25 rem | 64 px / 4 rem | PP Editorial | 300 (Light) | Títulos de seção principais |
| `--font-h2` | 28 px / 1.75 rem | 44 px / 2.75 rem | PP Editorial | 300 | Títulos secundários |
| `--font-h3` | 22 px / 1.375 rem | 32 px / 2 rem | PP Editorial | 400 | Nomes de peça, subtítulos |
| `--font-h4` | 18 px / 1.125 rem | 20 px / 1.25 rem | Inter | 600 | Labels grandes / cards |
| `--font-body-lg` | 18 px / 1.125 rem | 18 px / 1.125 rem | Inter | 400 | Texto principal de Sobre, hero sub |
| `--font-body` | 16 px / 1 rem | 16 px / 1 rem | Inter | 400 | Corpo padrão |
| `--font-body-sm` | 14 px / 0.875 rem | 14 px / 0.875 rem | Inter | 400 | Microcopy, legendas |
| `--font-caption` | 11 px / 0.6875 rem | 12 px / 0.75 rem | Inter | 500 | Caps lock — faixa de credibilidade, badges |
| `--font-quote` | 20 px / 1.25 rem | 28 px / 1.75 rem | Cormorant Garamond | 400 italic | Depoimentos e citações |

**Line-height:**

- Display/H1: `0.95` (caixa alta gigante respira pouco — esse é o look)
- H2/H3: `1.1`
- H4: `1.3`
- Body: `1.6`
- Body-sm: `1.55`
- Quote: `1.4`

**Letter-spacing:**

- Display em caixa alta: `-0.02 em` (gigante levemente apertado = mais peso visual)
- H1/H2: `-0.015 em`
- Caption (caps): `+0.12 em` (caps espaçada vira sinalização)
- Body: `0`
- Quote italic: `+0.005 em`

**Transform:**

- Hero, faixa de credibilidade, CTAs entre colchetes: `text-transform: uppercase`.
- Todo o resto: case natural.

## 3. Tokens de cor

Mapeados a partir de [[03 - Identidade Visual e Tom de Voz#2. Paleta de cores]] com nomes semânticos.

```css
:root {
  /* superfícies */
  --color-bg:            #0A0A0A;  /* fundo principal — mais escuro que antes pra dramaticidade */
  --color-surface:       #141414;  /* cards, seções, modais */
  --color-surface-2:     #1E1E1E;  /* hover, faixa secundária */

  /* marca */
  --color-accent:        #C9A24B;  /* dourado champanhe — CTAs, links, ícones */
  --color-accent-hover:  #E0C079;  /* dourado claro — hover/focus */
  --color-accent-soft:   rgba(201, 162, 75, 0.12);

  /* texto */
  --color-text:          #F5F1E8;  /* off-white — texto principal */
  --color-text-muted:    #8C8C8C;  /* cinza — secundário, captions */
  --color-text-dim:      #5A5A5A;  /* cinza escuro — placeholders, microcopy */
  --color-text-on-accent:#0A0A0A;  /* texto sobre botão dourado */

  /* linhas */
  --color-border:        #2A2A2A;
  --color-border-strong: #4A4A4A;

  /* funcional */
  --color-success:       #4ADE80;
  --color-error:         #F87171;
  --color-overlay:       rgba(0, 0, 0, 0.7);  /* lightbox de galeria */
}
```

**Regras de uso (inalteradas):**

- Dourado é acento, cobertura máxima ~5% da tela.
- Texto principal sempre sobre `--color-bg` ou `--color-surface`. Nunca dourado em parágrafo longo.
- Botão primário = dourado de fundo + preto no texto. Secundário = transparente + borda dourada.

## 4. Espaçamentos

```css
--space-1:  0.25 rem;
--space-2:  0.5 rem;
--space-3:  0.75 rem;
--space-4:  1 rem;
--space-5:  1.5 rem;
--space-6:  2 rem;
--space-8:  3 rem;
--space-10: 4 rem;
--space-12: 6 rem;
--space-16: 8 rem;
--space-20: 10 rem;
--space-24: 12 rem;  /* respiro extra entre seções principais (estilo editorial) */
```

Espaço em branco mais agressivo que o padrão — esse é o look "menos é mais" dos sites premium 2026.

## 5. Raio, sombra e transição

```css
--radius-sm: 4 px;     /* inputs (visual mais editorial, menos arredondado) */
--radius:    10 px;
--radius-lg: 20 px;
--radius-pill: 9999 px;

--shadow-sm:  0 1 px 2 px rgba(0,0,0,0.4);
--shadow:     0 4 px 16 px rgba(0,0,0,0.5);
--shadow-lg:  0 16 px 40 px rgba(0,0,0,0.6);
--shadow-accent: 0 8 px 24 px rgba(201, 162, 75, 0.25);

--ease-out:    cubic-bezier(0.22, 1, 0.36, 1);    /* padrão GSAP expo.out */
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
--ease-power:  cubic-bezier(0.16, 1, 0.3, 1);     /* power3.out — entrada com peso */

--duration-fast: 180 ms;
--duration:      280 ms;
--duration-slow: 600 ms;
--duration-hero: 1100 ms;   /* hero text reveal */
```

## 6. Componentes

### 6.1 Botão primário (CTA dourado)

```
Estado normal:
  fundo:   var(--color-accent)
  texto:   var(--color-text-on-accent)
  fonte:   Inter 600, 13 px, letter-spacing 0.08em, UPPERCASE
  padding: 16 px 32 px
  radius:  var(--radius-sm)   ← menos arredondado para estética editorial
  formato visual: [ TEXTO ENTRE COLCHETES ] — colchetes são parte do texto

Hover:
  fundo:  var(--color-accent-hover)
  sombra: var(--shadow-accent)
  transform: translateY(-2 px)

Focus (teclado):
  outline: 2 px sólido var(--color-accent-hover)
  outline-offset: 4 px
```

### 6.2 Botão secundário

```
fundo:  transparente
borda:  1 px sólido var(--color-text)
texto:  var(--color-text), Inter 600, 13 px, UPPERCASE letter-spacing 0.08em
hover:  fundo var(--color-text), texto var(--color-bg)  (inversão dramática)
```

### 6.3 Card de produto

```
fundo:  var(--color-surface)
radius: var(--radius)
overflow: hidden
estrutura:
  - foto 4:5 (mais vertical, estilo editorial)
  - padding 24 px:
      - categoria (font-caption, color-text-muted, UPPERCASE)
      - nome (font-h3)
      - [Ver detalhes →] (link dourado discreto)

hover desktop:
  - foto sofre scale(1.04) com easing var(--ease-power), 600 ms
  - nome muda para var(--color-accent)
  - card sobe translateY(-4 px)
```

### 6.4 Input do formulário (estilo editorial)

```
fundo:  transparente
borda:  bottom 1 px sólido var(--color-border)  ← só borda inferior (estilo formulário editorial)
radius: 0
padding: 14 px 0
texto:  Inter 400, 16 px (evita zoom iOS)
label:  Inter 500, 12 px, UPPERCASE, letter-spacing 0.08em, color-text-muted

foco:
  borda inferior: 1 px sólido var(--color-accent)
  label muda para color-accent
```

### 6.5 Chip de filtro (catálogo)

```
fundo:  transparente
borda:  1 px var(--color-border)
texto:  var(--color-text-muted), Inter 500, 12 px, UPPERCASE letter-spacing 0.08em
padding: 10 px 18 px
radius: var(--radius-pill)

ativo:
  fundo:  var(--color-text)
  texto:  var(--color-bg)
  borda:  transparente
```

### 6.6 Badge / faixa de credibilidade

```
texto:  Inter 500, 11 px (mobile) / 12 px (desktop), UPPERCASE letter-spacing 0.12em
cor:    var(--color-text-muted)
ícone:  20 px Lottie em loop sutil (ou Lucide estático), contorno dourado
```

## 7. Botão de WhatsApp flutuante

```
posição: fixed, bottom 24 px, right 24 px (mobile 20/20)
tamanho: 56 px × 56 px
formato: circular (radius pill)
fundo:   #25D366 (verde oficial WhatsApp)
ícone:   WhatsApp branco, 28 px
sombra:  var(--shadow)

hover desktop:
  - scale(1.08), sombra mais forte
  - tooltip "Fale com a AG" à esquerda

animação de entrada:
  - aparece com fade + slide-up 280 ms após scroll passar do hero (ScrollTrigger)
  - pulse sutil 1× ao aparecer (não em loop — vira poluição)

acessibilidade:
  - aria-label="Falar com a AG no WhatsApp"
  - target="_blank" rel="noopener"
```

## 8. Iconografia

- **Biblioteca primária:** **Lucide** (linha 1.5 px) para ícones funcionais.
- **Lottie** para ícones da faixa de credibilidade (animados em loop sutil).
- **WhatsApp:** SVG oficial, não usar do Lucide (reconhecimento de marca).
- **Tamanho:** 18 px no corpo, 24 px em destaques, 28 px no flutuante.
- **Cor:** `currentColor` por padrão. CTAs e faixas forçam `var(--color-accent)`.

## 9. Imagens

| Uso | Proporção | Tamanho exportação |
|---|---|---|
| Hero da Home (vídeo + fallback poster) | 16:9 desktop / 9:16 mobile | 2400×1350 + 1080×1920 |
| Card de categoria | 3:4 | 800×1067 |
| Card de produto (catálogo) | 4:5 ← mais vertical | 1000×1250 |
| Foto principal do produto | 4:5 | 2000×2500 |
| Thumbnail de galeria | 1:1 | 400×400 |
| Ambiente / processo (Sobre) | 16:9 | 2000×1125 |
| Open Graph | 1.91:1 | 1200×630 |

Formato: **AVIF + WebP fallback + JPG fallback**. Lazy-load nativo exceto no hero.

## 10. Princípios visuais finais

- **Respiração agressiva.** Áreas vazias enormes (`--space-20`+ entre seções). Em dúvida: dobra o padding.
- **Tipografia gigante.** Display do hero ocupa quase a tela inteira. Pequeno não impressiona.
- **Foto > ornamento.** Nenhum elemento decorativo pode competir com a fotografia.
- **Dourado com economia.** Mais de 3 ocorrências na mesma tela = excesso.
- **Tensão é virtude.** Quebras assimétricas de linha no hero. Caixa alta. Colchetes nos CTAs. Linha vertical fina como scroll indicator.
- **Animação contida e sincronizada.** GSAP + Lenis trabalhando juntos. Toda transição usa o easing de [[10 - Toolchain Premium e Workflow MCP#3.1]].
- **Performance é design.** Lighthouse 90+ inegociável. Spline lazy. Imagens AVIF. Fontes self-hosted.
