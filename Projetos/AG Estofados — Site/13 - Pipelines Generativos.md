# 13 — Pipelines Generativos

> Voltar ao [[AG Estofados — Índice]]
>
> 15 pipelines automatizados que **rodam em sequência**, encadeando ferramentas via MCP/API. Cada pipeline tem fluxo, custo, status de decisão e quando ativar.

## P0 — Lançamento (impacto imediato)

### #1 Foto Insta → foto premium 4K
```
Foto baixa qualidade do Instagram
  → image-enhancer (skill) ou Topaz Photo AI → upscale 4x
  → Magnific AI → refina detalhe e textura
  → Nano Banana → relighting cinematográfico + ambiente novo
  → AVIF/WebP via cwebp/avifenc
  → Cloudflare R2 storage
  → site
```
**Impacto:** dispensa ensaio fotográfico no lançamento.
**Custo:** R$ 0 (skill image-enhancer) + uso de Magnific/Nano Banana via API.
**Status:** ✅ aprovado — depende de `GEMINI_API_KEY` + Magnific opcional.

### #2 Vídeo cinematográfico sem câmera (B-roll)
```
Nano Banana / Midjourney → 5 keyframes da peça em ambiente premium
  → Runway Gen-4 OU Luma Dream Machine Ray 2 OU Veo 3 → interpola movimento
  → Topaz Video AI → upscale 4K + frame interpolation
  → ffmpeg → codec H.265 / WebM
  → Cloudflare Stream → HLS adaptativo
  → hero do site
```
**Impacto:** B-roll de cinema sem filmar.
**Custo:** ~R$ 80-150 (créditos Runway, se necessário) — Veo 3 incluso no Gemini.
**Status:** ✅ aprovado — depende de `GEMINI_API_KEY` (Veo 3) ou `OPENAI_API_KEY` (Sora).

### #3 Peça real → modelo 3D rotacionável
```
AG ou Mestre faz 30 fotos da peça em volta (360°) com iPhone
  → Polycam app → fotogrametria → mesh GLB
  → Blender → limpa malha, aplica texturas, ilumina
  → Spline → exporta cena React
  → @splinetool/react-spline → embed na home (lazy-load)
```
**Impacto:** o sofá REAL da AG girando no site. **Diferencial regional total.**
**Custo:** R$ 0 (Polycam free) ou $8/mês Pro.
**Status:** ✅ aprovado — depende de Polycam instalado + sessão de scan na loja.

### #4 Mockup do ensaio fotográfico ANTES de filmar
```
Lista dos 60 shots planejados em [[07 - Plano de Produção Fotográfica]]
  → Nano Banana → gera cada shot como mockup
  → PDF "storyboard" via Markdown + pandoc
  → fotógrafo recebe antes do dia do ensaio
```
**Impacto:** zero retrabalho no ensaio. Fotógrafo entrega exatamente o esperado.
**Custo:** R$ 0 (Nano Banana via skill).
**Status:** ✅ aprovado.

### #5 Variações de tecido por IA
```
Foto da peça base
  → Nano Banana edit → mesmo sofá em 8 tecidos (linho cru, suede grafite, veludo bordô, couro caramelo, etc.)
  → 1 peça vira 8 variações visuais
  → Supabase storage por variação
  → catálogo na página de produto
```
**Impacto:** catálogo parece 5x maior. Cliente já vê "como ficaria".
**Custo:** R$ 0 (Nano Banana).
**Status:** ✅ aprovado.

## P1 — Showroom virtual (Fase 2, pós-lançamento)

### #6 Tour 360° da loja física
```
Mestre passa 5 min na loja com Polycam → scan completo
  → exporta cena navegável
  → embed no site /sobre via iframe ou Three.js
```
**Impacto:** cliente "anda" pela loja antes de visitar. Aumenta conversão de visita.
**Custo:** R$ 0 (Polycam free).

### #7 Editor de tecido em tempo real
```
Slider de cor/tecido na página do produto
  → fetch → Cloudflare Worker → Nano Banana edit (~3s)
  → cliente vê o sofá DELE no tecido DELE
  → cache no R2 por hash
  → botão "Quero esse, conversar no WhatsApp" com print incluso
```
**Impacto:** ninguém na região tem isso. Vira motivo de viralizar.
**Custo:** ~R$ 50-100/mês de Nano Banana sob demanda (depende de volume).

### #8 Showroom virtual no ambiente do cliente
```
Cliente faz upload de foto da sala dele
  → Cloudflare Worker → Nano Banana edit → coloca sofá X naquela sala
  → resultado renderizado em ~5s
  → cliente baixa imagem + manda no WhatsApp como prova
```
**Impacto:** orçamento já vem com visualização. Reduz desistência.
**Custo:** ~R$ 50-100/mês.

## P2 — Operação contínua (Fase 3, pós-estabilização)

### #9 Site atualiza sozinho do Instagram
```
Cron Cloudflare Workers (1x ao dia)
  → Instagram Graph API → pega posts novos da AG
  → Nano Banana → classifica e enquadra (case, peça nova, depoimento)
  → Neon staging table
  → notifica Mestre via WhatsApp/email
  → Mestre aprova via dashboard simples
  → publica no site
```
**Impacto:** AG posta no Insta, site cresce sozinho.
**Custo:** R$ 0 (Workers free tier + Nano Banana esporádico).

### #10 Blog SEO contínuo
```
Cron mensal
  → Exa + Firecrawl → pesquisa temas SEO local ("como escolher tecido", "quanto dura estofado sob medida")
  → Claude API (Anthropic) → redijo no tom da AG
  → Nano Banana → ilustra
  → Neon draft
  → AG/Mestre aprova
  → publica
```
**Impacto:** Google ranqueia AG pra dezenas de buscas long-tail em 6 meses.
**Custo:** ~R$ 30-50/mês de API calls (Claude + Nano).

### #11 Atendimento IA com avatar + voz
```
HeyGen / D-ID → avatar do dono da AG (com autorização escrita)
  → ElevenLabs → voz clonada (com autorização)
  → RAG sobre catálogo + FAQ no Pinecone/Qdrant
  → botão "Conversar com a AG" no site
  → conversa por voz, escala pra humano via WhatsApp
```
**Impacto:** atendimento 24/7 que parece humano. Diferencial brutal.
**Custo:** ~R$ 150-300/mês (HeyGen + ElevenLabs).

### #12 Memória de visitante (personalização sem login)
```
Cookieless via fingerprint leve (Cloudflare KV)
  → próxima visita: hero personalizado com peças do tipo que ele viu
  → CTA personalizada
```
**Impacto:** sutil mas premium. Cliente que voltou já vê "o caminho dele".
**Custo:** R$ 0 (Cloudflare KV free).

## P3 — Qualidade (sempre on)

### #13 Observabilidade unificada
```
Sentry MCP → erros em produção
  + PostHog → session replay + feature flags + A/B
  + Cloudflare Web Analytics → Core Web Vitals
  → dashboard único
```
**Status:** ✅ aprovado — ativar no lançamento.
**Custo:** R$ 0 (todos free tier).

### #14 A/B test de copy automatizado
```
PostHog feature flag
  → variant A: "SOB MEDIDA. PARA QUEM NÃO ACEITA GENÉRICO."
  → variant B: "Estofados sob medida em Patos de Minas"
  → 30 dias → variant vencedora vira default
  → Claude API analisa qualitativa
```
**Impacto:** otimização rolando sozinha.
**Custo:** R$ 0 (PostHog free).

### #15 Figma → Lovable sync via MCP (futuro)
**Impacto:** baixo no contexto AG.
**Status:** ❌ skip por enquanto.

## Tabela de decisão consolidada (decisões batidas em 2026-05-21)

| Pipeline | Decisão | Quando |
|---|---|---|
| #1 Foto Insta → 4K | ✅ Sim | Lançamento |
| #2 Vídeo cinematográfico | ✅ Sim | Lançamento |
| #3 Peça real em 3D | ✅ Sim | Lançamento |
| #4 Mockup ensaio | ✅ Sim | Antes do ensaio |
| #5 Variações de tecido | ✅ Sim | Lançamento |
| #6 Tour 360 da loja | 🟡 Fase 2 | 30-60 dias depois |
| #7 Editor tecido tempo real | 🟡 Fase 2 | 30-60 dias depois |
| #8 Showroom virtual | 🟡 Fase 2 | 30-60 dias depois |
| #9 Site auto-Instagram | 🟢 Fase 3 | Após estabilizar |
| #10 Blog SEO | 🟢 Fase 3 | Após estabilizar |
| #11 Avatar IA voz | 🟢 Fase 3 + autorização AG | Após estabilizar |
| #12 Memória visitante | 🟢 Fase 3 | Após estabilizar |
| #13 Observabilidade | ✅ Sim | Lançamento |
| #14 A/B copy | 🟡 Fase 2 | Quando tiver tráfego |
| #15 Figma sync | ❌ Skip | Não no contexto AG |

## Bloqueios e dependências

```
P0 (#1, #2, #3, #4, #5) depende de:
   - GEMINI_API_KEY (Veo 3, Imagen, Nano Banana via código)  ⚠️ pendente
   - Polycam app no iPhone do Mestre                           ⚠️ instalar
   - Cloudflare R2 bucket ag-estofados-media                   ✅ posso criar

P1 (#7, #8) depende de:
   - GEMINI_API_KEY                                            ⚠️ pendente
   - Cloudflare Workers + R2                                   ✅
   - Volume de tráfego pra justificar custo                    🔮 medir

P2 (#9, #10, #11) depende de:
   - Acesso Instagram Graph API (via Meta Business)            ⚠️ pendente
   - ElevenLabs API key (#11)                                  ⚠️ pendente
   - Autorização escrita AG (voz + imagem para #11)            ⚠️ pendente
   - 30 dias de site estável                                   🔮 esperar

P3 (#13, #14) depende de:
   - Sentry + PostHog accounts                                 ⚠️ criar
   - Tráfego real (#14)                                        🔮 esperar
```
