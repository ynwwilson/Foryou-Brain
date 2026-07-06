# 10 — Toolchain Premium e Workflow MCP

> Voltar ao [[AG Estofados — Índice]]

> Este documento **sobrescreve** partes específicas de [[04 - Especificação Técnica]] (stack), [[03 - Identidade Visual e Tom de Voz]] (tipografia/tom) e [[09 - Design System — Fontes e Tokens]] (par tipográfico). Quando houver conflito, vale o que está aqui.

## 1. Decisão final de stack

**Lovable em TanStack Start + (Supabase ou Neon) + Vercel + Cloudflare DNS.**

Lovable não gera Next.js nativo. O que ele gera hoje é **TanStack Start (Vite + React + SSR + file-based routing)**, que entrega na prática o mesmo que Next App Router pra esse projeto — SSR funcional, SEO indexável, OG dinâmico.

| Camada | Tecnologia | Papel |
|---|---|---|
| Frontend + SSR | **Lovable (TanStack Start + React + Tailwind + shadcn/ui)** | Layout, rotas, componentes, integração Supabase |
| Animação | **GSAP 3.13+ + Lenis 1.3+ + @gsap/react** | Hero reveal, scroll, parallax, ScrollTrigger |
| 3D | **Spline + @splinetool/react-spline** | 1 cena hero rotacionável (lazy-load) |
| Micro-interação | **Framer Motion + Lottie** | Hovers, ícones animados |
| Backend | **Supabase ou Neon** | Catálogo, leads, depoimentos (CMS leve) — Postgres nos dois; ver §6 |
| Deploy | **Vercel** | SSR, preview por branch, OG dinâmico |
| DNS / CDN | **Cloudflare** | DNS de `agestofados.com.br` |
| E-mail | **Resend** | Notificação de leads do formulário |
| Vídeo | **Cloudflare Stream** | Hospedagem de B-roll (HLS adaptativo) |
| Analytics | **Vercel Analytics + Cloudflare Web Analytics** | Sem cookies, sem banner |

**O que muda em relação ao [[04 - Especificação Técnica]]:** Astro sai. Cloudflare Pages sai. Entram Lovable + TanStack Start + Vercel.

## 2. Divisão de trabalho — Lovable vs Claude Code

Lovable trava nos últimos 30% (animação fina, refs React, cleanup GSAP, timelines encadeadas). Solução: dividir.

| LOVABLE faz (via prompt visual) | CLAUDE CODE via MCP faz (cirurgia) |
|---|---|
| Estrutura de rotas | Hero GSAP SplitText + mask reveal |
| Layout base de cada página | Lenis smooth scroll + integração ScrollTrigger |
| Componentes shadcn (botões, cards, inputs, dialog) | ScrollTrigger orquestrado (pin, parallax, reveals) |
| Integração com Supabase (catálogo, leads) | Embed Spline 3D com lazy-load |
| Form de orçamento (validação básica) | Lottie/Framer Motion em microinterações |
| Header/Footer responsivos | Refino fino de tokens (spacing, easing, durations) |
| Textos e SEO (meta, OG) | Performance — Lighthouse, INP, LCP |
| Deploy Vercel | QA visual via Playwright + dev-browser |
| Mobile-first responsivo | Cross-browser quirks |

Regra: **se gera bug loop no Lovable, sai do Lovable e resolve via MCP no Claude Code.**

## 3. Stack de animação detalhada

### 3.1 Bibliotecas e versões

```json
{
  "gsap": "^3.13.0",
  "@gsap/react": "^2.1.2",
  "lenis": "^1.3.0",
  "@splinetool/react-spline": "^4.0.0",
  "framer-motion": "^11.5.0",
  "lottie-react": "^2.4.0"
}
```

GSAP 3.13 liberou **SplitText, MotionPathPlugin, Physics2DPlugin, MorphSVG, DrawSVG** gratuitos pra todo mundo. Era o que travava esse tipo de site antes.

### 3.2 Setup base (Lenis + GSAP + ScrollTrigger sincronizados)

```ts
// src/app/providers/scroll-provider.tsx
"use client";
import Lenis from "lenis";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useEffect } from "react";

gsap.registerPlugin(ScrollTrigger);

export function ScrollProvider({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
    });

    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((time) => lenis.raf(time * 1000));
    gsap.ticker.lagSmoothing(0);

    return () => { lenis.destroy(); };
  }, []);

  return <>{children}</>;
}
```

### 3.3 Hero reveal — referência do que vamos construir

```ts
// src/components/hero.tsx
"use client";
import { gsap } from "gsap";
import { SplitText } from "gsap/SplitText";
import { useGSAP } from "@gsap/react";
import { useRef } from "react";

gsap.registerPlugin(SplitText, useGSAP);

export function Hero() {
  const ref = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    const split = new SplitText(".hero-title", { type: "chars,lines", mask: "lines" });
    const tl = gsap.timeline({ delay: 0.2 });

    tl.from(split.chars, {
      yPercent: 110, opacity: 0,
      stagger: 0.025, duration: 1.1, ease: "expo.out"
    })
    .from(".hero-sub", { opacity: 0, y: 20, duration: 0.8 }, "-=0.6")
    .from(".hero-cta", { opacity: 0, y: 20, duration: 0.6, stagger: 0.1 }, "-=0.4")
    .from(".scroll-indicator", { opacity: 0, duration: 0.5 }, "-=0.2");

    gsap.to(".scroll-indicator", {
      opacity: 0,
      scrollTrigger: { trigger: "body", start: "top top", end: "+=200", scrub: true }
    });

    return () => split.revert();
  }, { scope: ref });

  return (
    <section ref={ref} className="relative h-screen w-full overflow-hidden bg-bg">
      <video className="absolute inset-0 h-full w-full object-cover opacity-50"
             autoPlay muted loop playsInline poster="/hero-poster.jpg">
        <source src="/hero-loop.webm" type="video/webm" />
      </video>

      <div className="relative z-10 flex h-full flex-col justify-center px-8">
        <h1 className="hero-title font-display text-display leading-none">
          SOB<br/>MEDIDA.<br/>PARA QUEM<br/>NÃO ACEITA<br/>GENÉRICO.
        </h1>
        <p className="hero-sub mt-8 max-w-md text-body-lg text-text-muted">
          Estofados feitos à mão em Patos de Minas, desde 1997.
        </p>
        <div className="hero-cta mt-10 flex gap-4">
          <button className="btn-primary">[ Pedir orçamento ]</button>
          <button className="btn-secondary">Ver catálogo →</button>
        </div>
      </div>

      <div className="scroll-indicator absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2">
        <span className="text-caption text-text-muted">DESLIZE</span>
        <div className="h-12 w-px bg-accent animate-pulse" />
      </div>
    </section>
  );
}
```

### 3.4 Padrões de ScrollTrigger no resto do site

- **Reveals por seção:** texto e cards entram com `y: 60, opacity: 0` ao 80% da viewport.
- **Pin + parallax** na seção "Como funciona o sob medida" (4 passos).
- **Galeria do produto:** scroll horizontal em desktop.
- **Faixa de credibilidade:** stagger de ícones com mask reveal.

## 4. Tipografia e tom — revisão

### 4.1 Par tipográfico final (substitui §3 do [[03 - Identidade Visual e Tom de Voz]] e §1–2 do [[09 - Design System — Fontes e Tokens]])

| Função | Fonte | Origem | Por quê |
|---|---|---|---|
| **Display (hero, headlines)** | **PP Editorial New** ou **Migra** | Pangram Pangram (freemium) | Serif moderna com tensão — combina ofício + premium |
| **Body / interface** | **Inter** | Google Fonts / Fontsource | UI legível, peso variable, performance |
| **Quotes / italics de destaque** | **Cormorant Garamond italic** | Google Fonts | Volta como acento elegante em depoimentos |

**Cormorant Garamond sai do display.** Era elegante mas calma — não cria a tensão tipográfica do nível Nalu/COCO. Migra/PP Editorial New entregam tensão sem perder o ar "desde 1997".

### 4.2 Tom de voz revisado

Substituir o "premium acolhedor" por **"afiado, manifesto, ofício"**. Frases curtas, caixa alta nas headlines, colchetes nos CTAs, copy que escolhe lado.

**Mantra:** "Estofar é ofício. Não é prateleira."

**Headlines revisadas (versões afiadas — escolher uma por seção):**

| Seção | Versão suave (descartar) | Versão afiada (usar) |
|---|---|---|
| Hero | Estofados feitos à mão, sob medida... | **SOB MEDIDA. PARA QUEM NÃO ACEITA GENÉRICO.** |
| Faixa credibilidade | Desde 1997 · Feito à mão · Sob medida | **Há 27 anos contra o estofado de fábrica.** |
| Categorias | Para cada ambiente, uma peça pensada | **Cada peça é única. Como deve ser.** |
| Como funciona | Do primeiro café à entrega na sua sala | **Conversa, projeto, ofício, entrega. Sem atalhos.** |
| Sobre | Mais de duas décadas estofando à mão | **Desde 1997 transformando ambiente em manifesto.** |
| CTA final | Vamos criar a sua peça? | **Sua casa não merece um móvel de prateleira.** |

CTAs sempre entre colchetes: `[ Pedir orçamento ]` · `[ Ver catálogo ]` · `[ Falar agora ]`.

Versões longas e parágrafos seguem o [[06 - Conteúdo e Copy]] — ajustar tom posteriormente caso o cliente queira algo intermediário.

## 5. Geração de assets

### 5.1 Imagens (Nano Banana + outros)

**Skill `nano-banana` já instalada.** Casos de uso:

- **Ambientação aspiracional** (hero, blocos de seção): "sala estar premium fundo escuro, luz lateral dourada, sofá modular minimalista em destaque, atmosfera cinematográfica, sem texto, ratio 16:9".
- **Variações de tecido** por peça (close de textura).
- **Backgrounds atmosféricos** pra seções (textura mármore preto sutil, fios de tecido, agulhas).

**Regra inviolável:** a peça em si nunca é gerada. Fotos generativas só pra ambiente/textura/fundo. Se gerar a peça, vira fake.

Fallback se nano-banana falhar em fotorrealismo: **GPT-Image-1** (ChatGPT) ou **Midjourney v7**.

### 5.2 Vídeo (B-roll cinematográfico)

- **Runway Gen-4** ou **Google Veo 3** (você tem acesso?).
- 4 a 6 clips de 5–10s cada:
  - Mãos costurando capitonê (close)
  - Tesoura cortando tecido (zoom lento)
  - Panorâmica de rolos de tecido empilhados
  - Pé de sofá sendo lixado/envernizado
  - Sala vazia → cortina abrindo → sofá iluminado (transição)
  - Detalhe de costura aparente (macro)
- Sem som. WebM ou MP4 H.265.
- Hospedar via Cloudflare Stream (HLS adaptativo, lazy autoplay).

**Plano:** B-roll IA pro lançamento → trocar pelo vídeo real filmado junto do ensaio fotográfico (Fase 2 do roadmap).

### 5.3 3D (Spline)

- **1 cena 3D na home:** sofá hero rotacionável com scroll horizontal (mouse drag).
- Cena montada em [Spline](https://spline.design), exportada como componente React.
- Lazy-load via `next/dynamic` ou `React.lazy` — não trava o LCP.
- Tamanho-alvo: ≤ 800kb por cena.

### 5.4 Lottie / ícones animados

- Faixa de credibilidade: 5 ícones em Lottie (entrada com stagger).
- Loader entre rotas: animação curta com monograma AG.
- Origem: [LottieFiles](https://lottiefiles.com) (filtrar pelo estilo "line, gold").

## 6. Banco como CMS leve — Supabase ou Neon

> **Os dois servem — é Postgres nos dois casos** e o schema abaixo roda igual. A diferença está no **modelo de segurança** e no painel. A escolha (e o conflito do banco compartilhado da ForYou Leads) está em [[17 - Status do Projeto (Live)#Conflito do banco Neon]].
>
> - **Supabase** — traz RLS nativo, painel de tabelas pronto, Storage e Edge Functions no mesmo lugar. Bom se a AG for editar direto pelo painel.
> - **Neon** — Postgres serverless puro. **Sem RLS nativo**: a segurança fica na **camada de API** (função serverless na Vercel valida cada acesso). É a opção quando se quer isolar do banco compartilhado.

Schema mínimo (idêntico nos dois):

```sql
-- peças do catálogo
create table products (
  id            uuid primary key default gen_random_uuid(),
  slug          text unique not null,
  name          text not null,
  category      text not null, -- sofas | sofas-automatizados | poltronas | cabeceiras | banquetas-pufs
  description   text,
  featured      boolean default false,
  images        jsonb,         -- [{ url, alt, ratio }]
  customization jsonb,         -- ["medidas", "tecidos", "cor", ...]
  related_slugs text[],
  created_at    timestamptz default now()
);

-- leads do formulário
create table leads (
  id              uuid primary key default gen_random_uuid(),
  name            text not null,
  whatsapp        text not null,
  city            text not null,
  product_type    text,
  message         text,
  reference_slug  text,
  source          text,           -- "form" | "whatsapp-button"
  created_at      timestamptz default now()
);

-- depoimentos
create table testimonials (
  id          uuid primary key default gen_random_uuid(),
  author      text not null,
  city        text,
  body        text not null,
  approved    boolean default false,
  created_at  timestamptz default now()
);
```

**Segurança — depende do banco escolhido:**

- **No Supabase:** RLS ativado em todas as tabelas. `products` e `testimonials` (com `approved = true`) são leitura pública; `leads` aceita insert público e leitura só pra ForYou. A chave anônima vai no frontend; a Service Role só no Claude Code, nunca no bundle do cliente.
- **No Neon:** não existe RLS. O frontend **nunca** fala direto com o banco — todo acesso passa por **função serverless na Vercel**, que aplica as regras (lê `products`/`testimonials` aprovados, grava `leads`, leitura de `leads` só autenticada). A `DATABASE_URL` fica só no servidor, jamais no código que vai pro navegador.

**Painel / CMS:**

- **Supabase:** o painel de tabelas nativo já serve de CMS — a AG aprende em ~15 min.
- **Neon:** usar o SQL Editor do console ou um painel simples — esforço equivalente.

**Notificação de lead novo via Resend:** Edge Function (Supabase) ou a própria função serverless da Vercel (Neon).

## 7. Setup dos MCPs

Você roda 1 vez. Eu te passo o passo a passo de cada um abaixo.

### 7.1 Lovable MCP

1. Abrir Claude Code → Settings → **Connectors** (ou MCP servers).
2. **Add custom connector**.
3. Nome: `Lovable` · URL: `https://mcp.lovable.dev`.
4. Salvar → OAuth no navegador → autorizar.
5. Confirmar: as ferramentas Lovable aparecem no menu de tools.

⚠️ **Segurança:** o token Lovable dá acesso a **todos** os projetos da sua conta. Não compartilhe.

### 7.2 Banco — Supabase MCP **ou** Neon MCP

> Conectar **um** dos dois, conforme a escolha de §6 / [[17 - Status do Projeto (Live)]]. Preferência atual: **Neon** (projeto novo `ag-estofados`, isolado do banco da ForYou Leads).
>
> **Neon:** criar projeto em [console.neon.tech](https://console.neon.tech) → New Project → `ag-estofados` → região `AWS São Paulo` → pegar a `DATABASE_URL`. MCP oficial: Neon Tools / `mcp.neon.tech`.

**Supabase (alternativa):**

1. Criar projeto Supabase: [supabase.com/dashboard](https://supabase.com/dashboard) → New Project → nome `ag-estofados` → senha forte → região `South America (São Paulo)`.
2. Pegar o **Project URL** e a **Service Role Key** em Settings → API.
3. Em Claude Code → Settings → Connectors → Add custom → instalar `mcp-server-supabase` (ou use o oficial em `https://supabase.com/docs/guides/getting-started/mcp`).
4. Configurar com a Service Role Key.

⚠️ Service Role Key bypassa RLS — só usar em ambiente local (Claude Code). Nunca embarcar no frontend.

### 7.3 Vercel MCP

1. Criar conta Vercel: [vercel.com](https://vercel.com) → conectar com GitHub.
2. Em Vercel → Settings → Tokens → criar token com escopo `Full Access`.
3. Em Claude Code → adicionar MCP `https://mcp.vercel.com` ou o pacote oficial `@vercel/mcp`.
4. Autenticar com o token.

### 7.4 GitHub (provavelmente já tem via Composio)

Verificar no menu de tools. Se não tiver, instalar [github.com/github/github-mcp-server](https://github.com/github/github-mcp-server).

### 7.5 Context7 (já tem)

Confirmar acesso. Vamos usar pra puxar docs sempre atualizadas de GSAP, Lenis, Spline, TanStack Start, shadcn/ui.

## 8. Workflow operacional

```
DIA 1
─────
[Mestre] assina Lovable Pro · cria Vercel · cria Supabase (1h)
[Mestre] conecta os 3 MCPs em mim seguindo §7 (15 min)
[Claude] roda schema Supabase via Supabase MCP
[Claude] inicia projeto Lovable via Lovable MCP com prompt sistema completo
         (briefing 01-09 + tom afiado + decisões batidas)

DIA 2-3
───────
[Lovable] gera estrutura base (rotas, layout, header, footer, shadcn)
[Mestre] revisa no preview, manda prompts visuais
[Claude] paralelamente: instala gsap/lenis/spline no projeto via PR Vercel
[Claude] implementa Hero GSAP (§3.3)
[Claude] implementa Lenis + ScrollProvider (§3.2)

DIA 4-5
───────
[Claude] cena Spline da home (1 sofá hero)
[Claude] ScrollTrigger nas seções
[Claude] microinterações Framer Motion
[Mestre] aprova/ajusta visualmente

DIA 6-7
───────
[Claude] gera assets generativos com nano-banana (10-15 imagens)
[Claude] B-roll com Runway/Veo (4-6 clips)
[Claude] upscale fotos do Instagram com image-enhancer (plano B)
[Mestre] sobe vídeos no Cloudflare Stream

DIA 8-10
────────
[Mestre] cobra inputs da AG (WhatsApp, peças, depoimentos)
[Claude] popula Supabase com peças reais
[Claude] QA via Playwright + dev-browser
[Claude] Lighthouse 90+

DIA 11+
───────
[Mestre + Claude] aprovação visual final
Deploy produção. Domínio agestofados.com.br no DNS Cloudflare apontando pra Vercel.

PÓS-LANÇAMENTO
──────────────
Trocar B-roll IA por vídeo real após ensaio fotográfico.
Trocar fotos Insta upscale por fotos do ensaio.
```

## 9. Custo realista

| Item | Custo |
|---|---|
| Lovable Pro (você já tem) | ✅ — |
| Vercel Hobby | R$ 0/mês |
| Supabase Free | R$ 0/mês |
| Cloudflare DNS | R$ 0/mês |
| Cloudflare Stream (vídeo) | ~R$ 25/mês (opcional — pode hospedar no Vercel mesmo) |
| Resend Free | R$ 0/mês (até 3k emails) |
| Runway / Veo (só durante construção) | ~R$ 80–150/mês (desliga depois) |
| Domínio `agestofados.com.br` | ~R$ 40/ano |
| Fontes (Migra / PP Editorial New) | R$ 0 — freemium para uso comercial pequeno |
| Spline (free tier) | R$ 0/mês |

**Total recorrente pós-lançamento:** ~R$ 0/mês fora o Lovable que você já paga.

## 10. Riscos e mitigações específicos desta toolchain

| Risco | Mitigação |
|---|---|
| Lovable trava em animação complexa | **Não tentar GSAP no Lovable.** Tudo de animação vem via MCP no Claude Code. |
| Spline 3D pesa o LCP | Lazy-load via `next/dynamic` + `loading` placeholder estático. Carrega só após scroll inicial. |
| Vídeo IA fica "fake" demais | Curar bem. Se for ruim, ir só com imagem + animação tipográfica. Movimento não é obrigatório. |
| Custo de Runway/Veo explode | Definir budget de R$ 200 só pra geração inicial. Depois corta. |
| Lovable regenera arquivo e quebra animação | Após Claude Code mexer em arquivo, **proibir Lovable de editá-lo via prompt.** Definir convenção `// LOCKED — edit via Claude Code`. |
| Migração futura pra Next.js (se precisar) | TanStack Start → Next via [NextLovable](https://nextlovable.com) ou DIY. Tratado em Fase 7. |

---

## Próximo passo imediato

Conferir [[AG Estofados — Índice#Próximo passo]] — a partir daqui, ação é **conectar os MCPs (§7) e disparar o projeto Lovable**.
