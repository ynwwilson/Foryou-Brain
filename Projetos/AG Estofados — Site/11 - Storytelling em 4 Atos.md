# 11 — Storytelling em 4 Atos

> Voltar ao [[AG Estofados — Índice]]
>
> O site é tratado como **filme**, não como página. Scroll é tempo cinematográfico. Cada seção é uma cena. Tem começo, meio e fim.

## Arquitetura narrativa

```
ATO I — CONFLITO         (0–100vh)
ATO II — REVELAÇÃO       (100vh – 300vh)
ATO III — A PEÇA EXISTE  (300vh – 500vh)
ATO IV — CONVITE         (500vh – fim)
```

Ritmo: cada ato tem **1 beat visual forte + 1 frase de manifesto + 1 ação opcional pro visitor**. Sem isso vira "site bonito" — vira site cinematográfico só com isso.

## Ato I — Conflito (Hero)

**Mensagem:** *"Sua casa não merece um móvel de prateleira."*

**Visual:**
- Vídeo Veo 3 fundo: corte rápido entre **fábrica industrial fria** (luz fluorescente, esteira, móveis idênticos) → **ateliê silencioso** (luz lateral quente, mãos costurando, peça única). Loop seamless 8s.
- Áudio nativo: máquina de costura sutil ao fundo (volume 5%, toggle no header).

**Tipografia em tensão (PP Editorial New 100, ~144px desktop):**

```
SOB
MEDIDA.
PARA QUEM
NÃO ACEITA
GENÉRICO.
```

**Animação:**
- SplitText char-by-char com mask reveal, stagger 25ms, easing expo.out, duração 1.1s.
- Subtítulo Inter 18px entra fade+y 0.8s depois.
- CTAs `[ Pedir orçamento ]` e `[ Ver catálogo ]` aparecem 0.6s depois.

**Ação opcional:**
- Scroll indicator centralizado embaixo: linha vertical animada + caption "DESLIZE". Some no primeiro scroll (`opacity: 1 - progress`).

## Ato II — Revelação do ofício (100vh–300vh)

**Mensagem:** *"Estofar é ofício. Não é prateleira."*

**Visual:**
- ScrollTrigger pin + scrub: a câmera "anda" pelo ateliê AG. Vídeo Veo 3 longo (~30s) com scrub controlado pelo scroll.
- Cada beat do vídeo revela um elemento + uma palavra surgindo:

```
beat 1 → palavra "AGULHA"      → mão segurando agulha
beat 2 → palavra "TECIDO"      → close de linho/suede
beat 3 → palavra "PROJETO 3D"  → render aparecendo
beat 4 → palavra "ENTREGA"     → peça na sala do cliente
```

**Tipografia das palavras:** PP Editorial 300, ~96px, entra com mask reveal letter, sai com clip-path.

**Animação:**
- GSAP ScrollTrigger `pin: true, scrub: 0.5, start: "top top", end: "+=2000"`.
- Cada beat tem `progress` próprio (`0–0.25`, `0.25–0.5`, etc.).
- Som ambiente continua. Volume sobe sutilmente nos beats.

## Ato III — A peça existe (300vh–500vh)

**Mensagem:** *"Cada peça é única. Como deve ser."*

**Visual:**
- Galeria assimétrica das 8–15 peças. Sem grid uniforme — **layout editorial**.
- Cada peça aparece com mini-narrativa em 1 frase (puxada do Supabase/Neon).
- **Peça hero:** modelo 3D real (fotogrametria Polycam) gira no scroll.

**Layout assimétrico (referência editorial):**

```
┌──────────────────────────┬───────────────┐
│                          │  poltrona     │
│   sofá toscana grande    │  pequena      │
│                          │               │
├──────────────┬───────────┴───────────────┤
│              │                           │
│ cabeceira    │   sofá automatizado       │
│              │                           │
└──────────────┴───────────────────────────┘
```

Cada peça com hover scale + nome em dourado + frase italic Cormorant.

**Animação:**
- Entrada com clip-path reveal (cortina abrindo).
- 3D Spline com `onScroll → rotateY` controlado.
- Cursor vira **lupa** quando passa em detalhe de costura (close).

## Ato IV — Convite (500vh+)

**Mensagem:** *"Sua casa entra nesse mapa?"*

**Visual:**
- Mapa interativo de Patos de Minas com pins das peças entregues. Cada pin abre tooltip com foto + ano + bairro (sem dado pessoal).
- Depoimentos em tipografia editorial: **Cormorant Garamond italic 28px**, sobre fundo `--color-surface`, com aspas tipográficas grandes.
- Bloco final cinematográfico: vídeo Sora 2 curto (3–5s) de ambiente convidativo + voz ElevenLabs opcional ("toggle ouvir") + CTA.

**Tipografia:**
- *"Sua casa não merece um móvel de prateleira."* — última frase do site, em display 96px.

**Animação:**
- Mapa: pins entram com stagger, pulse sutil.
- Depoimentos: carrossel horizontal com scrub.
- CTA final: magnetic button (puxa cursor).

## Regras de ritmo

| Regra | Por quê |
|---|---|
| 1 mensagem por ato | Mais que isso = ruído. Cada ato carrega 1 frase. |
| Máx 4 atos | Site não é livro. Mais atos = perda de fim. |
| Transições suaves entre atos | Sem corte abrupto — use Lenis + ScrollTrigger sincronizados |
| Som ambiente sempre toggle off por padrão | Autoplay com som mata 30% no 1º segundo |
| Tipografia gigante = peso da mensagem | Display 9rem+ no desktop. Se medo, não é cinema. |
| Espaço em preto enorme entre atos | `--space-24` ou mais. Respiração é virtude. |

## Como cada Ato vira código

| Ato | Componente React | Conteúdo do Supabase/Neon | Asset gerado por |
|---|---|---|---|
| I | `<HeroAct1 />` | hardcoded copy | Veo 3 (vídeo hero) |
| II | `<AtelierAct2 />` (pin + scrub) | hardcoded steps | Veo 3 (vídeo longo) |
| III | `<ProductsAct3 />` (asymmetric grid) | `products` table | Polycam + Nano Banana ambientação |
| IV | `<InviteAct4 />` (mapa + depoimentos) | `testimonials` table + `delivery_pins` | Sora 2 (clip curto) + ElevenLabs (voz opcional) |

## Decisões batidas

| Decisão | Data | Origem |
|---|---|---|
| Site tratado como filme em 4 atos | 2026-05-21 | Sessão com Mestre |
| Copy afiado tom Nalu adaptado pro ofício | 2026-05-21 | [[10 - Toolchain Premium e Workflow MCP#4.2]] |
| Som ambiente toggle off por padrão | 2026-05-21 | Regra antislop |
| Tipografia gigante (display 144px desktop) | 2026-05-21 | [[09 - Design System — Fontes e Tokens]] |

## Pendências

- [ ] Confirmar dados pra mapa de Patos (peças entregues por bairro) — pedir pra AG
- [ ] Definir se voz narrativa entra no lançamento (ElevenLabs) ou só Fase 2
- [ ] Definir quantas peças entram no Ato III (8 mínimo, 15 máximo)
- [ ] Storyboard cada beat do Ato II antes de gerar vídeo Veo 3
