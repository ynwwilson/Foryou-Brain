# 12 — Immersive Interactions Catalog

> Voltar ao [[AG Estofados — Índice]]
>
> Catálogo de **18 interações imersivas** organizadas em 3 tiers. Cada uma com tech, descrição, quando ativar e risco de virar "AI slop".

## Tier 1 — Cinematografia base (lançamento obrigatório)

Sem isso, o site não atinge o nível combinado. Custo: tempo de implementação. Risco: zero.

| # | Interação | Tech | Descrição |
|---|---|---|---|
| 1 | **Hero com vídeo Veo 3 + áudio nativo** | Veo 3 + Cloudflare Stream | Vídeo loop 8s, áudio máquina de costura mixado. Lazy poster. |
| 2 | **SplitText char-by-char + mask reveal** | GSAP SplitText (gratuito desde 3.13) | Tipografia se constrói letra a letra, com overflow hidden |
| 3 | **Lenis smooth scroll** | Lenis 1.3 | Scroll com física, sem jank. Melhora INP automaticamente |
| 4 | **ScrollTrigger pin de seção crítica** | GSAP ScrollTrigger | "Como funciona o sob medida" trava na tela enquanto cena roda |
| 5 | **Custom cursor que reage** | CSS + JS leve | Cursor vira lupa em detalhe, vira flecha em CTAs |
| 6 | **Magnetic buttons** | GSAP + mouse pos | CTAs puxam o cursor quando aproxima (raio 60px, força 0.3) |
| 7 | **Image reveal com clip-path** | GSAP + clip-path | Fotos entram cortadas, abrem como cortina ao scroll |

## Tier 2 — 3D real (diferencial brutal)

Diferencial que concorrente local não tem. Mais esforço, mais retorno.

| # | Interação | Tech | Descrição |
|---|---|---|---|
| 8 | **Peça AG real em 3D rotacionável** | Polycam → Blender → Spline → @splinetool/react-spline | O sofá REAL da AG gira no scroll. Fotogrametria do produto físico |
| 9 | **Configurador de tecido em tempo real** | Cloudflare Worker + Nano Banana edit | Slider de tecido → peça atualiza em ~3s via API |
| 10 | **Tour 360° da loja** | Polycam scan + Three.js | "Andar" pela loja antes de visitar. Cliente decide ir até lá |
| 11 | **AR Preview (mobile)** | WebXR + USDZ (iOS) / GLB (Android) | Apontar câmera → peça aparece em escala 1:1 |

## Tier 3 — Awwwards-tier (Fase 2 ou iteração)

Cinematografia top — mas precisa de tempo e contenção.

| # | Interação | Tech | Descrição |
|---|---|---|---|
| 12 | **Scrubbing de vídeo Veo 3 pelo scroll** | GSAP ScrollTrigger + `video.currentTime` | Scroll controla o tempo do vídeo. Apple-style storytelling |
| 13 | **Texto variable axis animado** | Fonte variable + GSAP | Peso/largura/slant respira conforme scroll. Tipo "respira" |
| 14 | **Particle system (fios e poeira)** | Three.js + curl noise | Fios sutis flutuando no ar do hero. Imperceptível mas premium |
| 15 | **Transição entre páginas com WebGL** | Barba.js + GSAP | Site não recarrega — transiciona como SPA com curtain |
| 16 | **Sticky scrolly-telling** | ScrollTrigger pin + scrub | Cada peça do catálogo tem mini-história scrubada |
| 17 | **Voz narrando o site** | ElevenLabs (voz clonada do dono AG, autorização) | Toggle "Ouvir a história" — narração contextual por seção |
| 18 | **Modo "Bastidor"** | CSS variables + GSAP | Toggle muda paleta inteira pra "atelier" (marrom-couro, fonte muda, vídeo de oficina) |

## Tabela de decisão por tier

| Tier | Quando ativar | Custo de tempo | Impacto visual |
|---|---|---|---|
| **T1** | Lançamento (obrigatório) | 2–3 dias | ⭐⭐⭐⭐ |
| **T2** | Lançamento se conseguir | 3–5 dias por feature | ⭐⭐⭐⭐⭐ |
| **T3** | Fase 2 ou iteração específica | 1–2 dias por feature | ⭐⭐⭐ (cada uma) |

## Anti-padrões — o que NÃO fazer (mata o premium)

| Anti-padrão | Por quê não |
|---|---|
| Particle system em **toda** seção | Vira poluição visual, mata performance |
| Cursor com glitter/trail pronunciado | Datado, cansa em 30s |
| Parallax exagerado em tudo | Marca "feito pelo template" |
| Confetti em qualquer interação | Não combina com ofício/estofaria |
| Glow neon | Marca de "AI slop" — Impeccable banneia |
| Bounce easing forte | Padrão premium é power3/expo, não bounce |
| Tilt 3D em cada card | Vira site de eletrônico Shopify |
| Som ambiente no autoplay | Mata 30% dos usuários no 1º segundo |
| Texto piscando, blink, flash | Acessibilidade quebrada + visual ruim |
| Mais de 3 ocorrências de dourado por tela | Brega — disciplina é o que separa premium de kitsch |

## Regra de ouro

> **Imersão é contenção.**
> 5 momentos perfeitos > 50 efeitos espalhados.

## Recomendação pro lançamento da AG

```
Lançamento dia 1:
├── T1 completo (#1, #2, #3, #4, #5, #6, #7)  ← obrigatório
├── T2 #8 (3D real da peça hero)              ← se conseguir
├── T3 #12 (scrub vídeo do Ato II)            ← bate forte
└── T3 #16 (sticky scrolly-telling)           ← bate forte

Fase 2 (30-60 dias depois):
├── T2 #9 (configurador tecido tempo real)
├── T2 #10 (tour 360 da loja)
├── T2 #11 (AR Preview)
└── T3 #17 (voz narrativa) — se AG autorizar

Skip (não recomendo no contexto AG):
└── T3 #14 particles (overkill)
```

## Dependências de implementação

```
#8 (3D real) bloqueado por:
   - Polycam scan das peças → Polycam (Mestre faz com iPhone)
   - Blender pra limpar mesh → Mestre instala
   - Spline conta → free tier basta

#9 (configurador tecido) bloqueado por:
   - Cloudflare Workers ativo → ✅ token funciona
   - Nano Banana via API → ⚠️ falta GEMINI_API_KEY

#11 (AR Preview) bloqueado por:
   - Modelo 3D em USDZ + GLB → depende #8

#17 (voz narrativa) bloqueado por:
   - Autorização escrita da AG
   - ElevenLabs API key → ⚠️ falta
   - Voz clonada (3min de áudio do dono) → coleta no ensaio

Resto do T1 + T3 #12, #16:
   - Não bloqueado por nada externo
   - Implemento via MCP Claude Code direto no projeto Lovable
```
