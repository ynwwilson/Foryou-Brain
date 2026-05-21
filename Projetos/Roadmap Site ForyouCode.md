---
title: Roadmap Site ForYou Code — v1
type: roadmap
created: 2026-05-04T00:00:00.000Z
tags:
  - projeto
  - site
  - foryoucode
  - roadmap
status: ativo
target: v1
domain: foryoucodee.com.br
atualizado: '2026-05-21'
---

# Roadmap Site ForYou Code — v1

> Documento mestre. Fonte única da verdade pra construção do site institucional da ForYou Code.
> Cada fase tem **prompt pronto pra colar** na ferramenta certa.
> **Escopo desta nota: até v1 live em foryoucodee.com.br.** Pós v1: pausar, avaliar com sócios, decidir v2 em conversa nova.

---

## 0. Resumo executivo

| Item | Valor |
|---|---|
| Objetivo v1 | Site institucional alto impacto + form gerando escopo via IA + deploy em foryoucodee.com.br |
| Estimativa | 13–17 dias de trabalho |
| Total de prompts | 19 (numerados sequenciais) |
| Stack base | TanStack Start (Vite + React 19 + SSR) + TS + Tailwind + shadcn + Framer Motion + Lenis + R3F + Supabase + Claude API |
| Deploy | Cloudflare Workers Builds + Cloudflare DNS (mesma conta) |
| Repo | `foryou-code-digital-ecosystems` (privado, criado via Lovable→GitHub) |

---

## 0.1 ESTADO ATUAL — onde paramos (2026-05-05, fim de tarde)

> **Continuação por outra conta Claude.** Ler esta seção primeiro.

### ✅ Concluído

| Fase | Status | Detalhes |
|---|---|---|
| **Phase 0.1** Lovable scaffolding | ✅ | Prompt 1 colado no Lovable. Shell pronta: header fixo + relógio ao vivo "GMT-3 · Patos de Minas, MG", hero 2 linhas display ("Não fazemos site." / "Entregamos o sistema do seu negócio."), dual CTA (roxo + ghost), footer 3 colunas, cursor custom, Lenis scroll. Botão header diz "Falar com a gente" (corrigido do "Falar com agente"). |
| **Phase 0.2** Lovable → GitHub | ✅ | Repo: `ynwwilson/foryou-code-digital-ecosystems` (privado, sync bidirecional com Lovable). |
| **Phase 0.3** Cloudflare Worker | ✅ | Project: `foryoucodee` no Cloudflare Workers Builds. Build verde (1309 KiB / 268 KiB gzip / startup 22ms). URL: `https://update-worker-name-to-foryoucodee-foryoucodee.ynwwilson.workers.dev`. Cada push em `main` dispara novo deploy. |
| **Phase 0.5** Supabase | ✅ | Project criado em South America (São Paulo). 3 tabelas (`leads`, `briefings`, `escopos`) + RLS + policies + indices rodaram com sucesso. URL: `https://ontmdqdtzlxrjkvbhumv.supabase.co`. |
| **Env vars no Worker** | ✅ | `VITE_SUPABASE_URL` e `VITE_SUPABASE_ANON_KEY` adicionadas em Settings → Variables and Secrets (Plaintext). |
| **Env vars locais** | ✅ | `.env.local` criado em `C:\Users\ynwwi\foryou-code-digital-ecosystems\.env.local` (não vai pro git). |

### 🔒 Bloqueado

| Fase | Motivo |
|---|---|
| **Phase 0.4** Custom Domain `foryoucodee.com.br` | Domínio ainda não foi comprado no registro.br. Próximo dia útil. Quando estiver na Cloudflare, é 1 clique em Workers → foryoucodee → Settings → Domains & Routes → Add Custom domain. |

### ✅ Phase 2 FECHADA + Mobile fix (Lovable, 2026-05-05 noite)

Prompts 1, 3, 4, 5, 6, 7 + mobile-fix + 3 ajustes finos entregues no Lovable:
- **P1** Shell (header relógio, hero, footer, cursor custom, Lenis) ✅
- **P3** Seção "Dor" (7 ícones dispersos, pulso, linhas SVG falhando) ✅ — aguarda upgrade D1 no P9
- **P4** Seção "Como funciona" (3 cards limpos numerados) ✅ — aguarda upgrade D2 no P10 (cards empilhados WorkOS-style)
- **P5** Seção "Quem constrói" (3 sócios) ✅ — aguarda fotos reais (D3)
- **P6** Seção "Cases" (bento grid 4 cards) ✅ — aguarda vídeos no P17 (D4) + decisão sobre Totus (não está em produção)
- **P7** CTA final + footer separator ✅
- **Mobile-fix v1** (todas as seções < 768px alinhadas com referências Mobbin + Sites that Move + WorkOS AuthKit) ✅
- **Mobile-fix v2** (header pílula sem vazar + respiro pra faixa relógio + cases padronizados) ✅ confirmado por Mestre

**DNA visual travado** (registrado em `Site ForYouCode — Dívida visual (pendente Antigravity).md`):
- Header/relógio = Sites that Move
- Hero/glow = WorkOS AuthKit
- Linhas pontilhadas + corner markers = WorkOS Radix
- CTAs pílula + espaçamento = Mobbin
- Tags badge cases = Sites that Move

### ⏳ Próxima ação imediata (próxima sessão)

**Phase 3 — Prompt 8 no Antigravity** (Hero refinado + R3F leve placeholder).

Antes do P8: varredura visual no Lovable + ajustes finos de copy/padding (Lovable vira só dashboard depois).

Migrar pro Antigravity:
1. `rtk git pull` na pasta local `C:\Users\ynwwi\foryou-code-digital-ecosystems`
2. Antigravity → Open folder → essa pasta
3. Colar P8 no Composer

**Phase 2 anterior — Prompts 3 a 7 no Lovable (seções estáticas).**

Filosofia confirmada com Mestre:
- **Lovable** → Prompts 3, 4, 5, 6, 7 (seções estáticas: dor, como funciona simples, quem constrói, cases bento estático, CTA final). Preview ao vivo + sync GitHub automático.
- **Antigravity** (motor principal segundo CLAUDE.md global) → Prompts 8, 9, 10, 11, 12, 15, 16, 17 (motion complexa, scroll triggers, R3F, parallax, form, customizer, vídeos).
- **Claude Code** → Prompts 13, 14, 18, 19 (Supabase migrations CLI, Edge Function gerar-escopo, SEO/meta, Lighthouse audit).
- **Cursor** → backup. Só se Antigravity travar.

**Regra de ouro:** 1 ferramenta por arquivo por turno. Antes de cada turno em Antigravity/Claude Code/Cursor → `rtk git pull` (Lovable empurra primeiro).

### 📋 Credenciais salvas (não recriar)

- **Supabase URL:** `https://ontmdqdtzlxrjkvbhumv.supabase.co`
- **Supabase anon key:** já configurada no Worker e em `.env.local`. Buscar em Supabase Dashboard → Settings → API se precisar de novo.
- **GitHub repo:** `ynwwilson/foryou-code-digital-ecosystems`
- **Cloudflare Worker name:** `foryoucodee`
- **Pasta local clonada:** `C:\Users\ynwwi\foryou-code-digital-ecosystems`

### ⚠️ Pendências técnicas conhecidas

- `ANTHROPIC_API_KEY` ainda **NÃO foi configurada**. Vai entrar no Supabase Edge Function (Phase 5, Prompt 14) via `supabase secrets set ANTHROPIC_API_KEY=<chave>`. **NUNCA** colocar no Worker nem em variável `VITE_*`.
- Notificação pro Marco quando lead chegar (Telegram vs WhatsApp vs email) — decisão pendente. Default sugerido: começar só com email, evoluir depois.

### 📌 Dívida visual (pendente Antigravity)

> Toda vez que o Lovable não consegue um efeito desejado, registrar em [[Site ForYouCode — Dívida visual (pendente Antigravity)]].
>
> Quando chegar nas Fases 3-4 (Prompts 8-12), abrir esse arquivo e implementar tudo. **Não esquecer.**

---

## 1. Visão e resultado v1

**Promessa central do site** (1 frase):
> "Transformamos a operação real da sua empresa em sistema próprio."

**Posicionamento canônico:** [[Posicionamento ForYou Code]].

O site não deve vender "app, CRM e automação" como lista de módulos. Deve vender capacidade de construção: se é legal, tecnicamente possível e melhora venda, controle, entrega, cobrança, atendimento, experiência ou decisão, a ForYouCode consegue desenhar, construir ou integrar.

**ICP** (lead que o site qualifica):
- Dono/CEO de empresa brasileira
- Faturamento R$80k–R$100k+/mês ou mais
- Operação real rodando com clientes, leads, cobrança, entrega ou equipe
- Sofrendo com WhatsApp, planilha, ferramenta pronta, dado espalhado ou processo manual
- Quer transformar a operação em sistema próprio, não só comprar uma tela bonita

**KPIs do site** (mensuráveis pós-launch):
- Leads/semana via form de escopo
- Taxa form completo → reunião agendada
- Tempo médio em página
- Lighthouse 95+ em todas as métricas

**Resultado final esperado v1:**
1. Site dark premium em `foryoucodee.com.br` com 9 seções
2. Form de 8 perguntas que gera briefing + escopo + faixa de investimento via Claude
3. Lead salvo automaticamente no Supabase
4. Notificação Telegram/WhatsApp pro Marco a cada lead
5. Hero 3D leve (orbe fragmentada) + 1 momento "uau" (explosão de ícones)
6. Mobile responsivo perfeito

---

## 2. DNA visual (moodboard travado)

| Ref | Sacada que entra |
|-----|------------------|
| **AuthKit** | Cards de UI real flutuando · customização ao vivo · dual CTA · dark dev-feel |
| **Mobbin** | Explosão de ícones + idle floating + counters scroll-triggered + bento grid |
| **Dylan Brouwer** | Hero 2 linhas editorial · time display ao vivo · device mockups layered · accordion services · cursor lerp |
| **Linear** | Headlines 1 frase · ritmo "3 batidas" · whitespace generoso · contenção |
| **Igloo (cirúrgico)** | Apenas: scroll = câmera 3D no hero. Cena leve. |

**Filosofia:**
- Linear é a alma (contenção + tipografia)
- AuthKit é a estrutura (produto exposto)
- Mobbin é o momento "uau" (explosão de ícones)
- Dylan é o detalhe humano (relógio, cursor, micro-motion)

**Regras invioláveis:**
- Máximo **2 momentos "uau"** no site inteiro
- **1 ideia por viewport**
- Headline = 1 frase. Sub = 1 frase.
- Roxo aparece como **glow e accent**, nunca como bloco grande de cor
- Zero ilustração genérica de IA, zero stock photo

---

## 3. Identidade visual exata

### 3.1 Paleta (CSS variables)

```css
:root {
  /* Backgrounds */
  --bg-primary: #0A0A0B;          /* preto absoluto, fundo principal */
  --bg-elevated: #131316;         /* cards, modals, header */
  --bg-secondary: #1C1C1F;        /* hover de cards */

  /* Texto */
  --text-primary: #FAFAFA;        /* texto principal */
  --text-secondary: #A1A1AA;      /* texto suporte */
  --text-tertiary: #52525B;       /* labels, captions */

  /* Roxo */
  --purple-primary: #7C3AED;      /* CTA, accent */
  --purple-deep: #3B0764;         /* glow profundo */
  --purple-hover: #8B5CF6;        /* hover de roxo */
  --purple-glow: rgba(124, 58, 237, 0.4);  /* box-shadow glow */

  /* Bordas */
  --hairline: #27272A;            /* divisores finos */
  --hairline-purple: rgba(124, 58, 237, 0.2);  /* divisor accent */
}
```

### 3.2 Tipografia

| Uso | Fonte | Pesos | Tamanho desktop |
|---|---|---|---|
| Display (hero, h1) | **Reckless Neue** (Fontshare) ou fallback **Fraunces** (Google) | 400 | 96px |
| Heading h2 | Reckless Neue | 400 | 64px |
| Heading h3 | Reckless Neue | 400 | 40px |
| Body | **Geist Sans** | 400, 500 | 16px |
| Body large | Geist Sans | 400 | 18px |
| Mono (números, código, micro) | **Geist Mono** | 400 | 13px |

**Mobile:** display reduz pra 48–56px. Body permanece 16px.

### 3.3 Motion tokens

```typescript
export const motion = {
  duration: {
    fast: 0.2,
    base: 0.4,
    slow: 0.8,
    epic: 1.4,  // só pra reveals de hero
  },
  easing: {
    smooth: [0.22, 1, 0.36, 1],     // ease-out premium
    snap: [0.6, 0, 0.4, 1],         // snap rápido
    bounce: [0.34, 1.56, 0.64, 1],  // bounce sutil
  },
  stagger: {
    base: 0.08,
    slow: 0.12,
    fast: 0.04,
  },
};
```

### 3.4 Espaçamento (escala 4px)

- Section padding vertical: 120px desktop / 64px mobile
- Container max-width: 1280px
- Gutter: 24px desktop / 16px mobile

---

## 4. Stack técnica

| Camada | Tecnologia | Função |
|---|---|---|
| Meta-framework | TanStack Start | SSR + roteamento file-based (template oficial Lovable) |
| Build tool | Vite | Bundler |
| Framework | React 19 + TypeScript | UI |
| Styling | Tailwind + shadcn/ui | Sistema de design |
| Motion | Framer Motion | Animações |
| Scroll | Lenis | Scroll suave global (client-only — wrap em ClientOnly) |
| 3D | React Three Fiber + Drei | Hero scene (client-only — wrap em ClientOnly) |
| Backend | Supabase | DB + Auth + Edge Functions |
| IA | Claude Sonnet 4.6 | Geração de briefing/escopo |
| Deploy | Cloudflare Workers Builds | Hosting + CI/CD (build automático via GitHub, `wrangler deploy`) |
| DNS | Cloudflare | foryoucodee.com.br (mesma conta) |
| Repo | GitHub privado | Source control |

### 4.1 Onde construir cada parte

| Fase | Ferramenta | Por quê |
|---|---|---|
| Scaffolding + shell + seções estáticas | **Lovable** | Preview ao vivo, GitHub sync, prompts visuais |
| Motion complexo + scroll triggers | **Antigravity** | Composer multi-arquivo, motor principal segundo CLAUDE.md global |
| Hero 3D R3F | **Antigravity** | Iteração rápida com shaders/scroll |
| Supabase migrations + Edge Function | **Claude Code** | Terminal puro, RTK, gh CLI |
| Polimento visual + microajustes | **Lovable** | Preview instantâneo, atalho pra trocar copy/cor/padding |
| Deploy + DNS | **Cloudflare Workers Builds + Cloudflare DNS** painéis | Manual, 1 vez. Tudo dentro da Cloudflare — sem Vercel. |

> **Regra de ouro do fluxo:** Lovable = janela de preview que também atende ajuste rápido. Antigravity = motor principal de construção. Claude Code = infraestrutura e operações. **1 ferramenta por arquivo por turno** — não editar simultaneamente.

---

## 5. Arquitetura de dados (Supabase)

### 5.1 Tabelas

```sql
-- Tabela: leads
CREATE TABLE leads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  nome TEXT NOT NULL,
  email TEXT NOT NULL,
  whatsapp TEXT NOT NULL,
  empresa TEXT,
  cargo TEXT,
  status TEXT DEFAULT 'novo' CHECK (status IN ('novo', 'contato', 'reuniao', 'proposta', 'fechado', 'perdido')),
  origem TEXT DEFAULT 'site',
  utm_source TEXT,
  utm_medium TEXT,
  utm_campaign TEXT
);

-- Tabela: briefings (respostas do form)
CREATE TABLE briefings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id UUID REFERENCES leads(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  negocio_descricao TEXT NOT NULL,
  tamanho_time TEXT NOT NULL,
  faturamento_faixa TEXT NOT NULL,
  ferramentas_atuais TEXT[] DEFAULT '{}',
  dores_principais TEXT[] DEFAULT '{}',
  sonho_funcionando TEXT NOT NULL,
  prazo_desejado TEXT NOT NULL,
  investimento_disponivel TEXT NOT NULL
);

-- Tabela: escopos (gerado pela IA)
CREATE TABLE escopos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  briefing_id UUID REFERENCES briefings(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  briefing_estruturado TEXT NOT NULL,
  escopo_macro TEXT NOT NULL,
  prazo_estimado TEXT NOT NULL,
  faixa_investimento TEXT NOT NULL,
  preview_visual TEXT,
  pdf_url TEXT,
  modelo_usado TEXT DEFAULT 'claude-sonnet-4-6'
);

-- Indices
CREATE INDEX idx_leads_email ON leads(email);
CREATE INDEX idx_leads_created ON leads(created_at DESC);
CREATE INDEX idx_briefings_lead ON briefings(lead_id);
CREATE INDEX idx_escopos_briefing ON escopos(briefing_id);
```

### 5.2 RLS Policies

```sql
-- RLS ativo em todas
ALTER TABLE leads ENABLE ROW LEVEL SECURITY;
ALTER TABLE briefings ENABLE ROW LEVEL SECURITY;
ALTER TABLE escopos ENABLE ROW LEVEL SECURITY;

-- Inserção pública (qualquer pessoa pode preencher form)
CREATE POLICY "Anyone can insert leads" ON leads FOR INSERT WITH CHECK (true);
CREATE POLICY "Anyone can insert briefings" ON briefings FOR INSERT WITH CHECK (true);
CREATE POLICY "Anyone can insert escopos" ON escopos FOR INSERT WITH CHECK (true);

-- Leitura: apenas service_role (admin)
CREATE POLICY "Service role can read leads" ON leads FOR SELECT USING (auth.role() = 'service_role');
CREATE POLICY "Service role can read briefings" ON briefings FOR SELECT USING (auth.role() = 'service_role');
CREATE POLICY "Service role can read escopos" ON escopos FOR SELECT USING (auth.role() = 'service_role');
```

---

## 6. Wireframe das 9 seções (com copy)

### Seção 1 — Hero
**Função:** ancorar promessa + capturar atenção
**Copy:**
- H1 linha 1: `Não vendemos app.`
- H1 linha 2: `Construímos o sistema da sua operação.`
- Sub: `A gente transforma WhatsApp, planilha, ferramenta solta e processo manual em tecnologia própria: app, painel, IA, automações, integrações e dados do jeito que sua empresa funciona.`
- CTA primário: `Gerar escopo grátis →`
- CTA secundário: `Ver cases`
**Motion:** clip-path reveal stagger entre as 2 linhas. Sub fade-in 200ms depois. Cena 3D R3F leve no fundo.

### Seção 2 — A dor
**Função:** espelho indireto (técnica do Marco)
**Copy:**
- H2: `Você está rodando seu negócio em 7 ferramentas que não conversam.`
- Sub: `Planilha pra estoque. WhatsApp pra atendimento. Excel pra financeiro. Caderno pra escala. Cabeça pra lembrar do resto.`
**Motion:** 7 ícones de ferramentas dispersas pulsando levemente, com linhas pontilhadas tentando conectá-los e falhando.

### Seção 3 — O que entregamos (sacada Mobbin)
**Função:** mostrar amplitude de capacidade, sem parecer cardápio básico
**Copy:**
- H2: `Se dá pra transformar em operação, dá pra transformar em sistema.`
- Sub: `App, painel, IA, cobrança, busca, tour 3D, CRM, automação, integração, área do cliente ou produto inteiro — a forma depende do que melhora o negócio.`
**Motion:**
- Estado inicial: 12 ícones agrupados no centro formando logo-cluster ForYou
- Scroll trigger: explosão para fora, easing smooth, stagger random 0–400ms
- Idle: cada ícone flutuando suavemente
- Counter scroll-triggered no centro: `+R$ 2,4M processados · 4 cases em produção · 3 sócios. 1 stack. 0 dependência.`

### Seção 4 — Cases reais (bento grid)
**Função:** prova
**Copy:**
- H2: `Sistemas em produção, gerando resultado.`
**Cards (4):**
1. **Operacional ForYou** — App de gestão operacional. Lovable + Supabase. operacionalforyou.com.br
2. **SmartCell** — Plataforma proprietária estilo Shopify. Catálogo, vendas, financeiro em painel único.
3. **Salinha** — Sistema da escola da Dayane Alemar. Gestão de alunos, turmas, fluxos pedagógicos.
4. **Concretize Pré-Moldados** — IA de atendimento dedicada. Painel visual, controle absoluto.
**Motion:** bento grid alturas variadas, vídeo loop em cada card (8s), parallax sutil 0.85x ao rolar, hover lift + glow roxo.

### Seção 5 — Customização ao vivo (sacada AuthKit)
**Função:** materializar o "white-label"
**Copy:**
- H2: `Sua marca. Seu domínio. Seu sistema.`
- Sub: `Não é template. É o seu negócio digitalizado.`
**Componente interativo:**
- Mockup de app à direita
- Painel à esquerda com: cor primária (color picker), logo upload, nome empresa (input), border radius (slider)
- Mudanças refletem **em tempo real** no mockup

### Seção 6 — Como funciona (accordion 3 etapas, pin scroll)
**Função:** desmistificar processo
**Copy:**
- H2: `3 etapas. Sem gambiarra. Sem dependência.`

**Etapa 1 — Mapeamos**
> Briefing IA + reunião. Saímos sabendo o seu negócio melhor que você.

**Etapa 2 — Construímos**
> Transformamos a operação em sistema próprio. Pode virar app, painel, IA, cobrança, busca, automação, integração, tour 3D ou produto digital inteiro — depende do que resolve o negócio.

**Etapa 3 — Sustentamos**
> Manutenção mensal. Seu sistema evolui com o seu negócio. Sem dependência de agência terceira.

**Motion:** seção pinned. Scroll progride pelos 3 cards revelando um a um.

### Seção 7 — Formulário escopo grátis (a isca)
**Função:** capturar lead high-intent
**Copy:**
- H2: `Gere o escopo do seu sistema em 3 minutos.`
- Sub: `8 perguntas. IA gera briefing + faixa de investimento + prazo. Sem custo. Sem compromisso.`

**Form: 8 perguntas** (detalhe completo na Seção 7 deste documento)

**Após envio:**
- Loading screen com mensagem "Nossa IA está montando seu escopo… (isso leva ~30 segundos)"
- Tela de resultado mostrando escopo gerado + opção "Baixar PDF" + "Marcar reunião"

### Seção 8 — Quem constrói
**Função:** humanizar
**Copy:**
- H2: `Três sócios. Uma stack. Direto.`

**Cards:**
1. **Mestre** — orquestração técnica. Foto. Frase: `Constrói o motor. Cuida do que faz o sistema rodar.`
2. **Marco** — vendas + relacionamento. @yngomesmarco. Foto. Frase: `Tradução entre o que o cliente quer e o que a gente entrega.`
3. **Eduardo** — estratégia + conteúdo. Foto. Frase: `Pega o problema do mercado e devolve em produto.`

### Seção 9 — CTA final + footer
**Copy:**
- H2: `Pronto pra ver como seria o seu?`
- Dual CTA: `Gerar escopo grátis` (roxo cheio) / `Falar com a gente agora` (WhatsApp direto)

**Footer 3 colunas:**
- Marca + endereço Patos de Minas
- Links rápidos
- Redes (WhatsApp, Instagram dos sócios)

---

## 7. Schema do formulário (8 perguntas)

```typescript
const formQuestions = [
  {
    id: 'negocio_descricao',
    type: 'textarea',
    label: 'Qual o seu negócio em 1 frase?',
    helper: 'Sem enrolação. Tipo "loja de celular em Patos de Minas".',
    required: true,
    minLength: 10,
  },
  {
    id: 'tamanho_time',
    type: 'select',
    label: 'Quantas pessoas no time hoje?',
    options: ['Só eu', '2-5', '6-15', '16-50', '50+'],
    required: true,
  },
  {
    id: 'faturamento_faixa',
    type: 'select',
    label: 'Faturamento mensal aproximado?',
    helper: 'Pra calibrar o escopo. Não vamos compartilhar.',
    options: [
      'Menos de R$ 30k/mês',
      'R$ 30k–80k/mês',
      'R$ 80k–200k/mês',
      'R$ 200k–500k/mês',
      'R$ 500k+/mês',
    ],
    required: true,
  },
  {
    id: 'ferramentas_atuais',
    type: 'multiselect',
    label: 'Quais ferramentas você usa hoje?',
    options: [
      'Excel/Planilha',
      'WhatsApp',
      'CRM (qual?)',
      'ERP (qual?)',
      'Sistema próprio',
      'Caderno/papel',
      'Nada estruturado',
    ],
    required: true,
  },
  {
    id: 'dores_principais',
    type: 'multiselect',
    label: 'Onde mais dói hoje?',
    helper: 'Pode marcar mais de uma.',
    options: [
      'Atendimento lento ou perdido',
      'Controle financeiro bagunçado',
      'Vendas vazando por falta de follow-up',
      'Dado espalhado em mil lugares',
      'Time sem visibilidade',
      'Estoque sem controle',
      'Não consigo escalar sem virar gargalo',
    ],
    required: true,
    minSelected: 1,
  },
  {
    id: 'sonho_funcionando',
    type: 'textarea',
    label: 'O que você sonha ter funcionando?',
    helper: 'Solta. Sem filtro. É a parte que importa.',
    required: true,
    minLength: 30,
  },
  {
    id: 'prazo_desejado',
    type: 'select',
    label: 'Em quanto tempo você quer isso rodando?',
    options: ['Ontem (urgente)', '1-3 meses', '3-6 meses', '6-12 meses', 'Sem pressa'],
    required: true,
  },
  {
    id: 'investimento_disponivel',
    type: 'select',
    label: 'Investimento disponível pra esse projeto?',
    helper: 'Faixas. Pra calibrarmos a proposta certa.',
    options: [
      'Até R$ 10k',
      'R$ 10k–30k',
      'R$ 30k–60k',
      'R$ 60k–120k',
      'R$ 120k+',
    ],
    required: true,
  },
];

// Após o form: 3 campos de contato
const contactFields = [
  { id: 'nome', label: 'Seu nome', type: 'text', required: true },
  { id: 'email', label: 'E-mail', type: 'email', required: true },
  { id: 'whatsapp', label: 'WhatsApp (com DDD)', type: 'tel', required: true },
];
```

**Lógica condicional:**
- Se `faturamento_faixa === 'Menos de R$ 30k/mês'` E `investimento_disponivel === 'Até R$ 10k'` → mostrar mensagem suave: "Talvez ainda não seja o momento de um ecossistema completo. Mas vamos te mandar um conteúdo gratuito que pode ajudar." (não bloqueia, captura como lead frio)

---

## 8. Edge Function `gerar-escopo` (spec completa)

### 8.1 Endpoint
- URL: `https://<projeto>.supabase.co/functions/v1/gerar-escopo`
- Método: POST
- Body: `{ briefing_id: UUID }`
- Response: `{ escopo_id: UUID, escopo_macro: string, prazo: string, faixa: string, ... }`

### 8.2 System prompt do Claude (Sonnet 4.6)

```
Você é um consultor sênior da ForYou Code, empresa brasileira de ecossistemas digitais 
white-label B2B high-ticket sediada em Patos de Minas/MG.

A ForYou Code entrega:
- CRM customizado com a marca do cliente
- App branded (iOS/Android) com identidade do cliente
- IA de atendimento dedicada (já entregue pra Concretize Pré-Moldados)
- Painel operacional sob medida (case: Operacional ForYou, Salinha)
- Plataforma proprietária estilo Shopify (case: SmartCell)
- Automações WhatsApp API
- Pagamentos integrados
- Integração com sistemas existentes

Faixas de preço da casa:
- IA de Atendimento + Painel: R$ 3.000–5.000 + manutenção mensal
- Ecossistema Completo: R$ 30.000–60.000 + manutenção mensal
- Projetos maiores customizados: a partir de R$ 60.000

Sua tarefa: receber o briefing de um lead que preencheu o formulário do site e devolver 
um JSON estruturado com:
1. Briefing reorganizado e claro (problema central, objetivo, contexto)
2. Escopo macro do que a ForYou Code entregaria (módulos, integrações)
3. Prazo estimado realista (em meses)
4. Faixa de investimento (em R$)
5. Prévia visual sugerida (3-5 telas-chave que o sistema teria)

Tom: direto, brasileiro, sem corporativês. Sem "ótima pergunta", sem enrolação. 
Sem prometer o que não dá pra entregar. Se o lead não tem perfil pra high-ticket 
(faturamento baixo + investimento baixo), seja honesto e sugira começar mais simples.

Output OBRIGATORIAMENTE em JSON válido com este schema:

{
  "briefing_estruturado": "string (3-5 parágrafos)",
  "escopo_macro": "string (lista de módulos com bullet points)",
  "prazo_estimado": "string (ex: '4-6 meses')",
  "faixa_investimento": "string (ex: 'R$ 35.000-55.000')",
  "preview_visual": "string (descrição de 3-5 telas)",
  "ajuste_recomendado": "string ou null (caso o perfil não bata, sugestão honesta)"
}

NÃO retorne markdown. NÃO inclua texto fora do JSON. APENAS o JSON puro.
```

### 8.3 Lógica de execução

```typescript
// Pseudocódigo da edge function

import { createClient } from '@supabase/supabase-js';
import Anthropic from '@anthropic-ai/sdk';

export default async (req: Request) => {
  const { briefing_id } = await req.json();
  
  const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY);
  const anthropic = new Anthropic({ apiKey: CLAUDE_API_KEY });

  // 1. Buscar briefing
  const { data: briefing } = await supabase
    .from('briefings')
    .select('*, leads(*)')
    .eq('id', briefing_id)
    .single();
  
  // 2. Montar user message
  const userMessage = `
Briefing do lead:
- Negócio: ${briefing.negocio_descricao}
- Tamanho time: ${briefing.tamanho_time}
- Faturamento: ${briefing.faturamento_faixa}
- Ferramentas atuais: ${briefing.ferramentas_atuais.join(', ')}
- Dores: ${briefing.dores_principais.join(', ')}
- Sonho: ${briefing.sonho_funcionando}
- Prazo: ${briefing.prazo_desejado}
- Investimento: ${briefing.investimento_disponivel}

Gere o escopo conforme instruções.
`;

  // 3. Chamar Claude
  const response = await anthropic.messages.create({
    model: 'claude-sonnet-4-6',
    max_tokens: 4096,
    system: SYSTEM_PROMPT,
    messages: [{ role: 'user', content: userMessage }],
  });

  // 4. Parse JSON
  const escopoData = JSON.parse(response.content[0].text);

  // 5. Salvar no Supabase
  const { data: escopo } = await supabase
    .from('escopos')
    .insert({
      briefing_id,
      ...escopoData,
    })
    .select()
    .single();

  // 6. Notificar Marco via Composio (Telegram/WhatsApp)
  await fetch(COMPOSIO_WEBHOOK, {
    method: 'POST',
    body: JSON.stringify({
      lead: briefing.leads,
      escopo: escopoData,
    }),
  });

  return Response.json(escopo);
};
```

---

## 9. ROADMAP COM PROMPTS (19 prompts em ordem)

### FASE 0 — Setup (1 dia, manual)

#### Passo 0.1 — Criar projeto no Lovable

1. Abrir https://lovable.dev
2. Clicar em "New Project"
3. Colar o **Prompt 1** (abaixo)
4. Aguardar Lovable construir a shell

#### 🟣 PROMPT 1 — Lovable: Shell inicial

```
Criar site institucional de alto impacto pra ForYou Code — empresa 
brasileira de ecossistemas digitais white-label B2B high-ticket sediada 
em Patos de Minas/MG.

STACK: Vite + React + TypeScript + Tailwind + shadcn/ui. 
Instalar também: framer-motion, lenis, lucide-react.
(React Three Fiber a gente adiciona em prompt futuro pra fase 3D.)

PALETA — definir como CSS variables no index.css:
- bg-primary: #0A0A0B
- bg-elevated: #131316
- text-primary: #FAFAFA
- text-secondary: #A1A1AA
- purple-primary: #7C3AED
- purple-deep: #3B0764
- purple-glow: rgba(124, 58, 237, 0.4)
- hairline: #27272A

TIPOGRAFIA — importar do Google Fonts:
- Display headlines: "Fraunces" (variable, peso 400)
- Corpo: "Geist" (Google Fonts) — pesos 400 e 500
- Mono: "Geist Mono"

Configurar tudo no Tailwind como font-display, font-sans, font-mono.

CRIAR APENAS A SHELL — não construir cases, form, accordion, ou animações 3D ainda:

1. LAYOUT global dark fullscreen (bg-primary). Lenis configurado pra 
   scroll suave em toda a página (importar e iniciar no main.tsx).

2. HEADER fixo no topo, com backdrop-blur e fundo semi-transparente:
   - Esquerda: "ForYou Code ✦" em font-display, branco
   - Centro: nav com 4 links — "Sobre", "Cases", "Como funciona", "Escopo grátis"
   - Direita: botão "Falar com a gente" em roxo (#7C3AED) com box-shadow 
     glow no hover usando purple-glow
   - Barra inferior do header: relógio AO VIVO formatado 
     "23:15 GMT-3 · Patos de Minas, MG" em Geist Mono cinza pequeno 
     (atualiza a cada segundo via setInterval com new Date())

3. HERO placeholder, alinhado à esquerda com padding-top 160px e 
   padding-x do container max-w-1280:
   - Linha 1 display gigante (96px desktop, 48px mobile, leading-tight): 
     "Não fazemos site."
   - Linha 2 display gigante: "Entregamos o sistema do seu negócio."
   - Cada linha entra com clip-path reveal de baixo pra cima usando 
     Framer Motion, stagger de 120ms entre elas, easing 
     [0.22, 1, 0.36, 1], duration 0.8s.
   - Sub abaixo (24px, text-secondary): "Ecossistemas digitais 
     white-label pra donos de empresa que querem operação de verdade — 
     não planilha no Excel."
   - Dois CTAs lado a lado: 
     * Primário "Gerar escopo grátis →" (bg-purple-primary, 
       text-white, rounded-xl, padding generoso)
     * Secundário "Ver cases" (ghost, border hairline, hover muda border 
       pra purple-primary)

4. FOOTER minimal com 3 colunas em grid:
   - Coluna 1: marca "ForYou Code ✦" + endereço 
     "Rua Artur Magalhães, 1350 B3 301 · Patos de Minas, MG · 38703-572"
   - Coluna 2: Links rápidos (Sobre, Cases, Como funciona, Escopo grátis, 
     Privacidade)
   - Coluna 3: "Falar agora" com WhatsApp (link wa.me) e Instagram 
     (@foryoucode placeholder)
   - Hairline roxa fina (#3B0764, opacity 30%) separando footer do 
     conteúdo de cima.

5. CURSOR CUSTOM: ponto roxo 8px (purple-primary) seguindo o mouse 
   com lerp 0.15 (smooth lag). Em hover de link/botão, expande pra 
   círculo 32px com mix-blend-mode: difference. Esconder em mobile 
   (matchMedia max-width 768px).

6. RESPONSIVO: mobile-first. Em mobile:
   - Headlines reduzem pra 48px
   - Nav vira hamburger menu (sheet shadcn)
   - Cursor custom desativado
   - Padding do hero reduz proporcional

PERSONALIDADE — siga essas regras:
- Dark premium, contido, dev-feel
- Whitespace generoso (estilo Linear)
- Zero ilustração genérica de IA, zero stock photo
- Roxo aparece como GLOW e ACCENT, nunca como bloco grande de cor
- Bordas arredondadas consistentes (rounded-xl ou rounded-2xl)

Após criar tudo isso, conectar ao GitHub criando um repo novo chamado 
"foryoucodee-site" privado.
```

#### Passo 0.2 — Conectar Lovable → GitHub
1. No Lovable, clicar em "GitHub" (ícone canto superior direito)
2. Autorizar Lovable na sua conta GitHub
3. Selecionar "Create new repository" → nome `foryoucodee-site` → privado
4. Confirmar. Repo nasce com sync bidirecional automático.

#### Passo 0.3 — Conectar Cloudflare Workers Builds ao repo
> **Decisão (2026-05-05):**
> 1. Tirar Vercel do stack deste site por problemas na integração Vercel↔GitHub.
> 2. **Worker, não Pages.** Lovable scaffolda template oficial **TanStack Start** com SSR — exige Worker pra rodar. Pages só serve site estático puro. Workers Builds é o destino certo e fica na mesma conta da Cloudflare.

1. https://dash.cloudflare.com → menu lateral **Workers & Pages** → **Create application** → **Continue with GitHub** (NÃO clicar em "Looking to deploy Pages? Get started")
2. Selecionar o repo `foryou-code-digital-ecosystems`
3. Configurar:
   - Project name: `foryou-code-site` (vira `<nome>.workers.dev`)
   - Build command: `npm run build`
   - Deploy command: `npx wrangler deploy`
   - Production branch: `main`
   - Builds for non-production branches: ✓ (pra ter preview deploys)
4. **Deploy**. Cloudflare faz o primeiro build (1-3 min)
5. Cada push no `main` dispara novo deploy. Cada PR ganha preview deploy automático.

> **Atenção ao `wrangler.jsonc`:** o Lovable já cria esse arquivo no repo. Se o build falhar com `ParseError: PropertyNameExpected`, é trailing comma na última propriedade — pedir ao Lovable: "Remover a vírgula final no `wrangler.jsonc` antes do `}`". Se falhar com `lockfile is frozen` em `bun install`, pedir: "Regenerar `bun.lockb` rodando `bun install`".

#### Passo 0.4 — Apontar foryoucodee.com.br pro Worker
> Como o domínio já está na Cloudflare, isso vira 1 clique — sem mexer em CNAME manual.

1. Workers & Pages → `foryou-code-site` → **Settings** → **Domains & Routes**
2. **Add → Custom domain** → digitar `foryoucodee.com.br` → confirmar
3. Cloudflare cria automaticamente os registros DNS necessários e provisiona SSL
4. Repetir pro `www.foryoucodee.com.br` se quiser (recomendado: redirect www → apex via Page Rule ou Bulk Redirect)
5. Aguardar SSL ativo (geralmente <5 min, pode chegar a 30 min na primeira vez)
6. Verificar: `dig foryoucodee.com.br` deve resolver pro Worker, e abrir no navegador deve servir HTTPS sem warning

#### Passo 0.5 — Criar projeto Supabase + tabelas

1. https://supabase.com/dashboard → "New project"
2. Nome: `foryoucodee-site`
3. Senha forte. Região: South America (São Paulo).
4. Aguardar provisionar.
5. Aba "SQL Editor" → colar o **SQL da Seção 5** deste documento → Run.
6. Aba "Settings → API": copiar `Project URL` e `anon key`.

#### 🟣 PROMPT 2 — Claude Code: Setup local + env vars

> Cole no terminal Claude Code rodando do vault:

```
Configurar projeto local pra desenvolvimento:

1. Clonar o repo: gh repo clone foryoucodee-site && cd foryoucodee-site
2. Criar arquivo .env.local na raiz com:
   VITE_SUPABASE_URL=<colar URL do Supabase>
   VITE_SUPABASE_ANON_KEY=<colar anon key>
3. Adicionar .env.local ao .gitignore se não estiver
4. Configurar variáveis no Cloudflare Worker (dashboard):
   Workers & Pages → foryou-code-site → Settings → Variables and Secrets
   - VITE_SUPABASE_URL = <URL do Supabase>     (Type: Plaintext)
   - VITE_SUPABASE_ANON_KEY = <anon key>        (Type: Plaintext)
   (NÃO adicionar ANTHROPIC_API_KEY aqui — chave secreta nunca sobe pro Worker.
   Ela vive APENAS como secret na Supabase Edge Function — passo 5.)
5. No Supabase, criar secret pra Edge Function:
   supabase secrets set ANTHROPIC_API_KEY=<chave>
6. Verificar: rtk git status e rtk git pull
```

---

### FASE 1 — Shell pronta (já feito no Prompt 1) ✅

Confirmar que tá funcionando:
- [ ] Header fixo com relógio ao vivo
- [ ] Hero com 2 headlines em clip-path reveal
- [ ] Footer 3 colunas
- [ ] Cursor custom funcionando
- [ ] Lenis scroll suave
- [ ] Repo GitHub conectado
- [ ] Cloudflare Worker deployando (`foryou-code-site.workers.dev` ou similar)
- [ ] foryoucodee.com.br apontando via Custom domain do Worker

---

### FASE 2 — Seções estáticas (2-3 dias, Lovable)

> Colar cada prompt **separadamente** no Lovable. Espera ele terminar antes do próximo.

#### 🟣 PROMPT 3 — Lovable: Seção "A dor"

```
Adicionar nova seção logo abaixo do hero, com id="dor":

Padding vertical: 120px desktop / 64px mobile.
Container max-w-1280, alinhamento centralizado.

CONTEÚDO:
- H2 (font-display, 64px desktop, 36px mobile): 
  "Você está rodando seu negócio em 7 ferramentas que não conversam."
- Sub (text-secondary, 20px, max-w 720px, centralizado): 
  "Planilha pra estoque. WhatsApp pra atendimento. Excel pra financeiro. 
  Caderno pra escala. Cabeça pra lembrar do resto."

VISUAL:
Abaixo do texto, um grid 4x2 com 7 ícones em cards quadrados 
(bg-elevated, border hairline, rounded-xl, 80x80px):
1. Excel/planilha
2. WhatsApp
3. Caderno
4. Calculadora
5. Email
6. Post-it
7. Calendário
+ 1 card vazio com "?" indicando "o que mais?"

Cada card tem:
- Ícone central (lucide-react)
- Pulse animation sutil em loop (scale 1 → 1.02 → 1, 3s, infinite)
- Hover: glow roxo sutil

Entre os cards, linhas pontilhadas tracejadas finas (border-dashed, 
hairline) tentando conectar uns aos outros, mas em ângulos quebrados — 
sugerindo "desconexão". Renderizar via SVG absoluto sobre o grid.

Quando a seção entra na viewport (whileInView do Framer Motion), 
cards aparecem com stagger de 80ms cada, fade + translateY 20px.
```

#### 🟣 PROMPT 4 — Lovable: Seção "Como funciona" (3 etapas)

```
Adicionar seção com id="como-funciona" abaixo da seção dor.

Padding vertical: 120px / 64px mobile.

CONTEÚDO:
- H2 (font-display, 64px): "3 etapas. Sem gambiarra. Sem dependência."
- Sub (text-secondary, 20px): "Do briefing ao sistema rodando, sempre 
  com você no controle."

GRID DE 3 CARDS (3 colunas desktop, 1 coluna mobile, gap 24px):

CARD 1 — "Mapeamos"
- Número grande "01" em font-mono purple-primary, 32px
- H3 (font-display, 32px): "Mapeamos"
- Texto (text-secondary, 16px): "Briefing IA + reunião. Saímos sabendo 
  o seu negócio melhor que você."
- Ícone lucide "Search" no canto inferior direito do card

CARD 2 — "Construímos"
- Número "02"
- H3: "Construímos"
- Texto: "Sistema sob medida com a sua marca. CRM, app, automação, IA 
  — o que você precisar, no seu domínio."
- Ícone lucide "Code"

CARD 3 — "Sustentamos"
- Número "03"
- H3: "Sustentamos"
- Texto: "Manutenção mensal. Seu sistema evolui com o seu negócio. 
  Sem dependência de agência terceira."
- Ícone lucide "Infinity"

ESTILO DOS CARDS:
- bg-elevated, border hairline, rounded-2xl, padding 32px
- Altura igual entre os 3 (h-full)
- Hover: lift -4px translateY, border-color muda pra purple-primary 
  (transition 0.4s smooth easing)
- Hover: ícone do canto fica purple-primary

ANIMAÇÃO de entrada: cards aparecem com stagger 120ms, fade + 
translateY 30px quando entram na viewport.

(IMPORTANTE: nesta fase ainda NÃO implementar pin scroll. 
Deixar simples. Pin scroll vem em prompt futuro.)
```

#### 🟣 PROMPT 5 — Lovable: Seção "Quem constrói"

```
Adicionar seção id="quem-constroi" antes do footer.

Padding vertical: 120px / 64px mobile.

CONTEÚDO:
- H2 (font-display, 64px): "Três sócios. Uma stack. Direto."
- Sub (text-secondary, 20px): "Quem responde a sua mensagem é quem 
  constrói o seu sistema."

GRID DE 3 CARDS verticais (3 cols desktop, 1 col mobile, gap 24px):

CARD 1 — Mestre
- Foto circular placeholder 120x120 (use emoji 🧠 por enquanto, 
  trocar depois)
- Nome: "Mestre" (font-display, 24px)
- Role: "Orquestração técnica" (font-mono, 13px, text-tertiary)
- Frase: "Constrói o motor. Cuida do que faz o sistema rodar."

CARD 2 — Marco
- Foto circular placeholder (emoji 🎯)
- Nome: "Marco"
- Role: "Vendas + relacionamento"
- Handle: "@yngomesmarco" (text-tertiary, font-mono)
- Frase: "Tradução entre o que o cliente quer e o que a gente entrega."

CARD 3 — Eduardo
- Foto circular placeholder (emoji 🚀)
- Nome: "Eduardo"
- Role: "Estratégia + conteúdo"
- Frase: "Pega o problema do mercado e devolve em produto."

ESTILO:
- Cards bg-elevated, border hairline, rounded-2xl, padding 32px, 
  text-center
- Foto com border-2 purple-primary em hover
- Hover: lift -4px

ENTRADA: stagger 100ms cada card.
```

#### 🟣 PROMPT 6 — Lovable: Seção "Cases reais" (bento grid estático)

```
Adicionar seção id="cases" entre "Como funciona" e "Quem constrói".

Padding vertical: 120px / 64px mobile.

CONTEÚDO:
- H2 (font-display, 64px): "Sistemas em produção, gerando resultado."
- Sub (text-secondary, 20px): "Cada um construído sob medida. Cada 
  um com a marca do dono."

BENTO GRID — 4 cards com alturas e larguras variadas:

Layout (12 colunas desktop, stack vertical mobile):
- Card 1: col-span-7, row-span-2 (grande, esquerda topo)
- Card 2: col-span-5, row-span-1 (médio, direita topo)
- Card 3: col-span-5, row-span-1 (médio, direita meio)
- Card 4: col-span-12, row-span-1 (largo, embaixo)

CARDS (todos bg-elevated, border hairline, rounded-2xl, padding 32px, 
overflow hidden):

CARD 1 — Operacional ForYou (grande)
- Tag superior: "App interno" (font-mono, 12px, text-tertiary)
- Title: "Operacional ForYou" (font-display, 32px)
- Descrição: "App de gestão operacional. Plano do dia, escalas, fluxos 
  do time em painel único."
- Stack visível: badges "Lovable" "Supabase"
- Link discreto: "operacionalforyou.com.br ↗"
- Placeholder de imagem grande no fundo (gradient placeholder 
  bg-gradient-to-br from-purple-deep to-bg-primary com texto 
  "📱 Screenshot" no centro — trocar por screenshot real depois)

CARD 2 — SmartCell
- Tag: "Plataforma proprietária"
- Title: "SmartCell"
- Descrição: "Plataforma estilo Shopify do dono. Catálogo, vendas, 
  estoque, financeiro, clientes — painel único."

CARD 3 — Salinha
- Tag: "Sistema sob medida"
- Title: "Salinha"
- Descrição: "Sistema da escola da Dayane Alemar. Gestão de alunos, 
  turmas e fluxos pedagógicos."

CARD 4 — Concretize
- Tag: "IA de Atendimento"
- Title: "Concretize Pré-Moldados"
- Descrição: "IA dedicada com painel visual. Controle absoluto sobre 
  comportamento. Em produção desde maio/2026."

ESTILO de cada card:
- Hover: lift -6px, border purple-primary, glow purple-primary 
  (box-shadow 0 0 60px purple-glow)
- Tag superior em letras maiúsculas, tracking-wider
- Transição smooth easing 0.4s

ENTRADA: stagger 80ms quando entra na viewport.

(IMPORTANTE: vídeos em loop entram em prompt futuro. Por enquanto, 
placeholders de imagem.)
```

#### 🟣 PROMPT 7 — Lovable: CTA final + ajuste do footer

```
Adicionar seção id="cta-final" entre "Quem constrói" e o footer.

Padding vertical: 160px / 80px mobile.

CONTEÚDO centrado:
- H2 (font-display, 96px desktop, 56px mobile, max-w-960, 
  alinhamento centralizado): 
  "Pronto pra ver como seria o seu?"
- Sub (text-secondary, 20px, max-w-640): 
  "8 perguntas. 3 minutos. IA gera o briefing + faixa de investimento. 
  Sem custo, sem compromisso."

DOIS CTAS lado a lado (gap 16px, centralizados):
- Primário (grande, h-14, padding-x 32px): 
  "Gerar escopo grátis →" 
  bg-purple-primary, hover purple-hover, glow purple-glow no hover
- Secundário (grande, h-14, ghost): 
  "Falar agora no WhatsApp" 
  border-2 hairline, hover border purple-primary
  Ícone lucide "MessageCircle" antes do texto
  Link: wa.me/55<numero> (placeholder)

BACKGROUND da seção: glow radial sutil com purple-deep no centro 
(radial-gradient(circle at center, rgba(59, 7, 100, 0.15), transparent 60%))

ENTRADA: H2 com clip-path reveal stagger linha por linha, sub fade-in 
200ms depois, CTAs aparecem com stagger 100ms.

AJUSTAR FOOTER existente: garantir que vem logo abaixo desta seção, 
sem padding top extra.
```

---

### FASE 3 — Motion + scroll triggers (2-3 dias, Antigravity)

> Migrar pra **Antigravity** agora — motor principal de construção segundo CLAUDE.md global. Abrir o repo `foryou-code-digital-ecosystems` clonado local. Os prompts a seguir são pro Composer do Antigravity.
>
> **⚠️ Regra TanStack Start (SSR):** componentes que usam `window`, `document`, animações Framer Motion ricas, Lenis, Three.js, ou cursor custom — **obrigatoriamente** envoltos em `<ClientOnly>` (use o `ClientOnly` do `@tanstack/react-start` ou crie um wrapper que só renderiza filhos quando `useState(false)` vira true via `useEffect`). Senão = hidratação mismatch.

#### 🟣 PROMPT 8 — Antigravity: Hero refinado + cena R3F leve placeholder

```
Refinar o componente Hero (src/components/Hero.tsx) com as seguintes 
melhorias:

1. ADICIONAR SHOWREEL placeholder no canto direito do hero:
   - Container 480x320 desktop (oculto em mobile <768px)
   - Por enquanto, placeholder bg-gradient com texto "▶ Showreel" 
     no centro (substituiremos por <video> real depois)
   - Borda rounded-2xl, border hairline, leve rotação rotate-y(-8deg) 
     pra dar perspectiva
   - Sombra: drop-shadow purple-glow sutil

2. INSTALAR React Three Fiber + Drei:
   npm install three @react-three/fiber @react-three/drei

3. CRIAR componente HeroCanvas em src/components/HeroCanvas.tsx:
   - <Canvas> R3F absolute positioned, z-index -1, atrás do hero
   - Cena leve: 1 esfera com material distorcido (MeshDistortMaterial 
     da @react-three/drei), cor #7C3AED, opacity 0.3
   - Câmera fixa, esfera rotaciona lento no useFrame
   - Performance: limit pixel ratio a 1.5, frameloop="demand" não 
     (queremos contínuo aqui, mas com perf otimizada)
   - Wrap em <Suspense> com fallback null
   - Detectar prefers-reduced-motion: se true, render estático sem 
     rotação

4. AJUSTAR LAYOUT do Hero:
   - Grid 12 cols desktop: texto col-span-7, showreel col-span-5
   - Mobile: stack vertical, showreel oculto
   - Padding-top 160px desktop, 96px mobile

5. MELHORAR clip-path reveal das duas linhas H1:
   - Estado inicial: clipPath "inset(0 0 100% 0)"
   - Estado final: clipPath "inset(0 0 0% 0)"
   - Transition: easing [0.22, 1, 0.36, 1], duration 0.9s
   - Stagger: linha 2 começa 150ms depois da linha 1
   - Trigger: ao montar (useEffect), não whileInView (é hero)

6. SUB e CTAs entram com fade + translateY 16px, stagger após 
   as linhas H1 terminarem (delay total ~1.2s da montagem).

Manter classes Tailwind consistentes com o resto do projeto.
```

#### 🟣 PROMPT 9 — Antigravity: Sacada Mobbin — explosão de ícones + counters

```
Criar nova seção entre "Cases" e "Quem constrói" chamada 
"O ecossistema" — id="ecossistema".

Componente: src/components/Ecosystem.tsx

CONCEITO:
- 12 ícones de módulos da ForYou Code começam agrupados no centro 
  formando um cluster denso.
- Conforme o usuário rola, os ícones explodem pra fora em posições 
  espalhadas pela viewport, com easing smooth e stagger random.
- Idle: cada ícone flutua suavemente em loop infinito (translateY 
  random ±8px).
- No centro da seção, conforme entra na viewport, counters de 
  números reais aparecem com rolling digits (animação de número 
  de 0 → valor final).

ÍCONES (12 módulos lucide-react):
1. Users (CRM)
2. MessageSquare (WhatsApp API)
3. CreditCard (Pagamentos)
4. Smartphone (App branded)
5. Bot (IA Atendimento)
6. LayoutDashboard (Painel operacional)
7. Workflow (Automação)
8. Package (Estoque)
9. DollarSign (Financeiro)
10. Calendar (Escala)
11. BarChart3 (BI)
12. Lock (Auth)

ESTRUTURA:
- Section h-screen sticky, position relative
- Centro: container com texto + counters
- Ícones: position absolute, distribuídos pelos 4 cantos da 
  viewport quando "explodidos"

POSIÇÕES FINAIS dos 12 ícones (em % da viewport, distribuídas pra 
parecer orgânico, não simétrico):
const positions = [
  { top: '12%', left: '10%' },
  { top: '8%', right: '15%' },
  { top: '20%', right: '8%' },
  { top: '38%', left: '6%' },
  { bottom: '18%', left: '14%' },
  { bottom: '8%', right: '20%' },
  { top: '60%', right: '4%' },
  { bottom: '32%', right: '10%' },
  { top: '15%', left: '38%' },  // próximo ao centro mas off
  { bottom: '24%', left: '40%' },
  { top: '45%', left: '12%' },
  { bottom: '6%', left: '6%' },
];

LÓGICA DE SCROLL com Framer Motion useScroll/useTransform:
- useScroll pegando offset relativo à seção
- Transformar scrollYProgress (0 → 1) em motion values:
  - Quando 0: ícones no centro empilhados (top: 50%, left: 50%, 
    transform translate -50% -50%)
  - Quando 0.4: ícones já espalhados pelas posições finais
  - Quando >0.4: ícones permanecem nas posições finais com idle 
    floating

IDLE FLOATING (após explosão):
- Cada ícone em <motion.div> com animate={{ y: [-8, 8, -8] }} e 
  duration random entre 3-5s, infinite, ease "easeInOut"
- Quebrar sincronia: cada ícone tem delay random 0-2s

GLOW nos ícones:
- Cada ícone em card 56x56, bg-elevated, border hairline, rounded-xl
- Hover: border purple-primary + box-shadow purple-glow
- Sempre: opacity 0.85, hover opacity 1

CONTEÚDO CENTRAL (texto + counters):
- H2 (font-display, 64px): "Um sistema. Sua marca. Tudo conversando."
- Sub: "CRM, app, automação, IA — escolhe o que precisa, a gente entrega."
- 3 counters em grid 3 cols (ou 1 col mobile):
  - "+R$ 2,4M" / "Processados pelos sistemas"
  - "4 cases" / "Em produção"
  - "3 sócios" / "1 stack. 0 dependência."

COUNTERS animados:
- useEffect quando seção entra na viewport (useInView do Framer Motion)
- Animar número de 0 até valor final em 1.6s, easing easeOut
- Para "+R$ 2,4M": animar de 0 a 2400000 e formatar com Intl.NumberFormat

PERFORMANCE:
- Disable em mobile <768px: substituir por grid estático 4x3 dos ícones 
  + counters sem animação. Mobile não precisa do uau, precisa de leveza.
- Verificar prefers-reduced-motion: se true, mostrar estado final sem 
  transição.

Salvar componente e importar em src/App.tsx ou src/pages/Index.tsx 
no lugar correto.
```

#### 🟣 PROMPT 10 — Antigravity: Pin scroll na seção "Como funciona"

```
Refatorar a seção "Como funciona" (src/components/HowItWorks.tsx) pra 
ter pin scroll com reveal sequencial das 3 etapas.

COMPORTAMENTO DESEJADO:
- Quando o usuário rola até a seção, ela "prende" no viewport (sticky)
- Conforme continua rolando, os 3 cards (Mapeamos, Construímos, 
  Sustentamos) aparecem um a um, sequencialmente
- Após o terceiro card aparecer completamente, a seção "solta" e o 
  scroll continua normal

IMPLEMENTAÇÃO:
- Section com height ~300vh (3x viewport — pra ter scroll suficiente 
  pra pinar 3 estados)
- Inner div com position: sticky, top: 0, height: 100vh
- useScroll de Framer Motion com offset ["start start", "end end"] na 
  section
- 3 cards com motion values:
  - Card 1: visível de 0 → 0.33 do scroll
  - Card 2: aparece em 0.33 → 0.66
  - Card 3: aparece em 0.66 → 1
- Animação de entrada por card: opacity 0 → 1 + translateY 40px → 0

VISUAL:
- Manter os 3 cards do PROMPT 4 (Mapeamos, Construímos, Sustentamos)
- Layout: 3 cols desktop, 1 col mobile, gap 32px
- Em mobile: NÃO pinar. Cards aparecem normal com whileInView 
  (perf primeiro).

INDICADOR de progresso (opcional, sutil):
- Barra fina no topo da viewport (durante o pin) mostrando 
  scrollYProgress visualmente
- 1px altura, bg purple-primary, scaleX baseado no progress

Verificar que o pin funciona suave com Lenis (Lenis + sticky pode 
exigir ajuste — testar e iterar).
```

#### 🟣 PROMPT 11 — Antigravity: Parallax sutil + hovers refinados nos cases

```
Refinar a seção Cases (src/components/Cases.tsx) com:

1. PARALLAX sutil em cada card:
   - useScroll com offset ["start end", "end start"] em cada card
   - useTransform: y de [-40, 40] baseado em scrollYProgress
   - Apenas em desktop (matchMedia min-width 768px)

2. HOVER 3D nos cards:
   - onMouseMove no card: capturar posição do cursor
   - Aplicar transform: rotateX e rotateY baseado na posição relativa 
     (max ±4deg)
   - onMouseLeave: voltar a 0deg
   - Transition smooth 0.4s

3. GLOW dinâmico no hover:
   - radial-gradient seguindo o cursor com cor purple-glow
   - Implementar com pseudo-elemento ::before usando custom properties 
     CSS (--mouse-x, --mouse-y) atualizadas via JS

4. TAG superior dos cards: animar com underline reveal no hover do card 
   (não da tag em si).

Se algo ficar pesado em performance, simplificar — prioridade é 
60fps em scroll.
```

---

### FASE 4 — 3D Hero (2 dias, Antigravity)

> **⚠️ R3F + TanStack Start:** envolver `HeroCanvas` em `<ClientOnly>`. Importar via `lazy(() => import('./HeroCanvas'))` ou usar guard `typeof window !== 'undefined'`. Three.js NÃO roda no server.

#### 🟣 PROMPT 12 — Antigravity: Cena R3F definitiva do hero (orbe fragmentada)

```
Substituir o HeroCanvas placeholder por uma cena R3F mais elaborada 
mas otimizada.

CONCEITO:
- Uma esfera roxa fragmentada flutuando no fundo do hero
- Composta por ~80 pequenos cubos/módulos posicionados em coordenadas 
  esféricas
- Esfera gira lentamente
- Conforme o usuário rola (scroll progress 0 → 0.6), a esfera começa 
  a se desmontar — os fragmentos se afastam radialmente do centro
- Após scroll progress > 0.6, fragmentos param e flutuam em idle

IMPLEMENTAÇÃO:
- Usar <Instances> do drei pra performance (geometria compartilhada)
- Geometria: BoxGeometry 0.15 (pequeno, parece "pixel 3D")
- Material: MeshStandardMaterial com:
  - color: #7C3AED
  - emissive: #3B0764
  - emissiveIntensity: 0.4
  - roughness: 0.3
  - metalness: 0.6

POSIÇÕES dos cubos (em coordenadas esféricas convertidas pra 
cartesianas, raio 1.5):
- 80 pontos distribuídos uniformemente na superfície de uma esfera 
  usando Fibonacci sphere algorithm
- Cada cubo armazena sua posição "home" (na esfera) e "exploded" 
  (raio 3-4)

LÓGICA DE SCROLL:
- useScroll da drei (com Canvas dentro de ScrollControls) OU 
  useScroll do Framer com sync via context
- scrollProgress (0 → 1) controla interpolação entre "home" e 
  "exploded" position por cubo:
  - lerp(homePos, explodedPos, easeInOutCubic(progress))

ROTAÇÃO da esfera:
- useFrame: group.rotation.y += 0.002 (lento, contínuo)

LIGHTING:
- ambientLight intensity 0.3
- directionalLight position [5, 5, 5] intensity 1
- pointLight position [0, 0, 2] color #7C3AED intensity 2 (key light 
  roxa)

CÂMERA:
- PerspectiveCamera position [0, 0, 5], fov 50

PERFORMANCE:
- dpr={[1, 1.5]} limita pixel ratio
- Suspense com fallback null
- frameloop="always" mas otimizado
- Em mobile (matchMedia <768px): renderizar apenas 30 cubos em vez 
  de 80, ou desativar Canvas e mostrar imagem PNG estática
- prefers-reduced-motion: estado final estático sem rotação nem 
  scroll-driven

Salvar como src/components/HeroCanvas.tsx (substituindo o placeholder).

Wrappar em <Canvas style={{ position: 'absolute', inset: 0, 
zIndex: -1, pointerEvents: 'none' }}>.

TESTAR fps no DevTools Performance tab. Alvo: 60fps.
```

---

### FASE 5 — Form + IA (2 dias, Claude Code)

> Migrar pro Claude Code. Comandos no terminal, dentro do diretório `foryoucodee-site`.

#### 🟣 PROMPT 13 — Claude Code: Schemas Supabase + RLS

```
Criar migrations Supabase pra esse projeto.

1. Inicializar Supabase localmente se ainda não estiver:
   supabase init
   supabase link --project-ref <PROJECT_REF>

2. Criar migration:
   supabase migration new initial_schema

3. No arquivo gerado em supabase/migrations/, colar o SQL completo da 
   Seção 5.1 e 5.2 deste roadmap (3 tabelas + RLS policies + indices).

4. Aplicar:
   supabase db push

5. Verificar via dashboard que as 3 tabelas (leads, briefings, escopos) 
   foram criadas com RLS ativo.

6. Commitar: rtk git add . && rtk git commit -m "feat: schema inicial 
   leads, briefings, escopos com RLS"
```

#### 🟣 PROMPT 14 — Claude Code: Edge Function `gerar-escopo`

```
Criar edge function que recebe briefing_id e gera escopo via Claude API.

1. Criar:
   supabase functions new gerar-escopo

2. Em supabase/functions/gerar-escopo/index.ts, implementar conforme 
   spec da Seção 8 deste roadmap:
   - Buscar briefing do Supabase
   - Montar mensagem pro Claude
   - Chamar Claude Sonnet 4.6 com system prompt especificado
   - Parsear JSON do response
   - Salvar em escopos
   - (Opcional v1.1) Notificar Marco via Composio webhook
   - Retornar escopo gerado

3. Configurar secrets:
   supabase secrets set ANTHROPIC_API_KEY=<chave>

4. Deploy:
   supabase functions deploy gerar-escopo

5. Testar com curl:
   curl -i --location --request POST \
     'https://<PROJECT_REF>.supabase.co/functions/v1/gerar-escopo' \
     --header 'Authorization: Bearer <ANON_KEY>' \
     --header 'Content-Type: application/json' \
     --data '{"briefing_id":"<UUID_DE_TESTE>"}'

6. Commitar: rtk git add . && rtk git commit -m "feat: edge function 
   gerar-escopo via Claude Sonnet 4.6"

OBSERVAÇÕES:
- System prompt EXATO está na Seção 8.2 deste roadmap. Não modificar.
- Response do Claude deve ser JSON estrito. Se vier markdown, parsear 
  com regex pra extrair o JSON. Se falhar, retornar erro 500 pro 
  frontend.
- Adicionar timeout de 60s na chamada Claude.
- Adicionar try/catch robusto.
```

#### 🟣 PROMPT 15 — Antigravity: Componente de formulário (8 perguntas)

```
Criar src/components/EscopoForm.tsx com formulário de 8 perguntas + 
3 campos de contato.

USAR SCHEMA da Seção 7 deste roadmap (formQuestions + contactFields).

ESTRUTURA:
- Multi-step: dividir em 4 telas
  - Tela 1: Perguntas 1-2 (negócio + tamanho time)
  - Tela 2: Perguntas 3-5 (faturamento + ferramentas + dores)
  - Tela 3: Perguntas 6-8 (sonho + prazo + investimento)
  - Tela 4: Contato (nome, email, whatsapp)
- Indicador de progresso no topo (4 dots, atual em purple-primary, 
  futuros em hairline)
- Botões "Voltar" / "Continuar" (último é "Gerar escopo →")

UI:
- Container max-w 640
- Cada tela em motion.div com slide horizontal entre telas (presence 
  + key)
- Inputs grandes (h-14, text-lg), bg-elevated, border hairline, 
  focus-within border purple-primary
- Multi-select: chips clicáveis (toggleáveis) em vez de checkboxes
- Textarea: h-32, resize-none

VALIDAÇÃO:
- React Hook Form + Zod
- Zod schema baseado no formQuestions (required, minLength, etc)
- Erros embaixo de cada campo em vermelho discreto

LÓGICA CONDICIONAL:
- Se faturamento_faixa === 'Menos de R$ 30k/mês' E 
  investimento_disponivel === 'Até R$ 10k':
  Mostrar mensagem em card amarelo discreto antes do botão final: 
  "Talvez ainda não seja o momento de um ecossistema completo. Mas 
  vamos te mandar um conteúdo gratuito que pode ajudar."
  Não bloqueia o envio. Captura como lead frio.

SUBMIT:
1. Inserir em supabase.from('leads') os 3 campos de contato → pegar 
   lead_id
2. Inserir em supabase.from('briefings') as 8 respostas com lead_id → 
   pegar briefing_id
3. Chamar edge function gerar-escopo com briefing_id
4. Mostrar tela de loading "Nossa IA está montando seu escopo… 
   (isso leva ~30 segundos)" com spinner roxo + frase rotando 
   ("Analisando seu negócio…", "Calibrando faixa de investimento…", 
   "Estruturando o escopo…")
5. Quando edge function retorna, mostrar tela de resultado com:
   - Briefing estruturado
   - Escopo macro (bullet points)
   - Prazo estimado
   - Faixa de investimento
   - Botão "Falar com a gente no WhatsApp" (link wa.me com mensagem 
     pré-preenchida: "Oi, acabei de gerar meu escopo no site (ID: 
     <escopo_id>). Quero conversar.")

INTEGRAÇÃO no site:
- Trocar o CTA "Gerar escopo grátis →" do hero e do CTA final pra 
  abrir um <Sheet> shadcn (slide lateral) com o EscopoForm dentro
- Em mobile, Sheet vira fullscreen
```

---

### FASE 6 — Customização ao vivo + vídeos cases (2 dias, Antigravity)

#### 🟣 PROMPT 16 — Antigravity: Seção "Customização ao vivo"

```
Criar nova seção id="customizacao" entre "Cases" e "Como funciona".

Componente: src/components/LiveCustomizer.tsx

CONCEITO:
- Mockup de app à direita
- Painel de controle à esquerda com inputs que mudam o mockup em 
  tempo real

PAINEL ESQUERDO (col-span-5 desktop):
- H2 (font-display, 48px): "Sua marca. Seu domínio. Seu sistema."
- Sub: "Não é template. É o seu negócio digitalizado."
- 4 controles:
  1. Cor primária — color picker (input type="color", grande)
  2. Logo upload — input file (mostrar preview circular ao subir, 
     fallback letra inicial do nome)
  3. Nome da empresa — input text (default "Sua Empresa")
  4. Border radius — slider 0-32px (default 12)

MOCKUP DIREITO (col-span-7 desktop):
- Container 360x720 (proporção mobile), bg-elevated, border hairline, 
  rounded baseado no border-radius do controle
- Conteúdo simulando app:
  - Header com logo (uploaded ou letra) + nome empresa
  - Bottom tab bar com 4 ícones (Home, Pedidos, Clientes, Mais)
  - Card central com "Vendas hoje: R$ X.XXX" + gráfico SVG simples
  - Botão flutuante FAB com cor primária

TODOS OS ELEMENTOS DO MOCKUP usam state values dos inputs. Mudança 
em tempo real (controlled inputs + state).

ANIMAÇÃO:
- Quando o usuário muda cor ou logo: transition 0.3s smooth
- Mockup entra com fade + scale 0.95 → 1 quando seção aparece

MOBILE:
- Stack vertical: painel em cima, mockup embaixo (centered, scale 0.9)

ESTILO:
- Inputs do painel em bg-bg-primary, border hairline
- Slider customizado em roxo (Tailwind accent-purple-500)
```

#### 🟣 PROMPT 17 — Antigravity: Vídeos loop nos cards de cases

```
Adicionar vídeos em loop nos 4 cards de cases (src/components/Cases.tsx).

PRÉ-REQUISITO: gravar/exportar 4 vídeos de 8s cada em formato webm + 
mp4, salvar em public/videos/:
- /videos/operacional-foryou.webm (+ .mp4)
- /videos/smartcell.webm (+ .mp4)
- /videos/salinha.webm (+ .mp4)
- /videos/concretize.webm (+ .mp4)

Resolução: 1280x800. Bitrate baixo (otimizado pra web). Duração 8s. 
Loop perfeito (frame inicial = frame final).

Se ainda não temos os vídeos: usar placeholders com vídeo 
"genéricos" do Pexels/Coverr ou screenshots animados em CSS.

IMPLEMENTAÇÃO:
- Em cada card, substituir o placeholder de imagem por:
  <video autoPlay muted loop playsInline>
    <source src="/videos/<nome>.webm" type="video/webm" />
    <source src="/videos/<nome>.mp4" type="video/mp4" />
  </video>
- preload="metadata"
- Wrap em container com overflow-hidden e rounded-2xl
- Aplicar overlay gradient sobre o vídeo: 
  bg-gradient-to-t from-bg-primary/80 to-transparent (legibilidade do 
  texto)

PERFORMANCE:
- Em mobile, NÃO autoplay vídeos (usar poster image em vez disso)
- Usar Intersection Observer pra pausar vídeos fora da viewport
- Lazy load: começar a baixar só quando estiver a 200px da viewport

Adicionar logging discreto no console pra ver fps/perf.
```

---

### FASE 7 — Polimento + Launch (1-2 dias)

#### 🟣 PROMPT 18 — Antigravity: SEO + OG image + meta tags

```
Adicionar SEO completo ao site.

1. Em index.html, atualizar <head>:
   - <title>ForYou Code — Sistemas proprietários sob medida</title>
   - <meta name="description" content="Transformamos a operação real da sua empresa em sistema próprio: app, painel, IA, automações, integrações e dados sob medida. Patos de Minas/MG.">
   - <meta name="keywords" content="ecossistema digital, white label, 
     CRM customizado, app branded, IA atendimento, ForYou Code">
   - <link rel="canonical" href="https://foryoucodee.com.br">
   - Favicon (criar /public/favicon.ico + /public/icon.png 512x512 com 
     "FYC ✦" em roxo sobre preto)

2. Open Graph tags:
   - <meta property="og:type" content="website">
   - <meta property="og:url" content="https://foryoucodee.com.br">
   - <meta property="og:title" content="ForYou Code — Sistemas proprietários sob medida">
   - <meta property="og:description" content="Transformamos operação real em tecnologia própria.">
   - <meta property="og:image" content="https://foryoucodee.com.br/og.png">

3. Twitter Card:
   - <meta name="twitter:card" content="summary_large_image">
   - <meta name="twitter:title" content="...">
   - <meta name="twitter:description" content="...">
   - <meta name="twitter:image" content="https://foryoucodee.com.br/og.png">

4. CRIAR OG image (1200x630) em /public/og.png:
   - bg #0A0A0B
   - "ForYou Code ✦" no canto superior em Fraunces
   - H1 grande centralizado: "Não fazemos site. / Entregamos o sistema 
     do seu negócio."
   - Glow roxo radial atrás do texto
   - "foryoucodee.com.br" no rodapé em Geist Mono cinza
   (Pode gerar via Figma, Photopea, ou comando IA. Salvar como PNG 
   otimizado.)

5. CRIAR /public/sitemap.xml e /public/robots.txt:
   robots.txt: 
     User-agent: *
     Allow: /
     Sitemap: https://foryoucodee.com.br/sitemap.xml
   
   sitemap.xml: incluir apenas a homepage.

6. Adicionar JSON-LD structured data (Organization schema) no <head>:
   {
     "@context": "https://schema.org",
     "@type": "Organization",
     "name": "ForYou Code",
     "url": "https://foryoucodee.com.br",
     "logo": "https://foryoucodee.com.br/icon.png",
     "address": {
       "@type": "PostalAddress",
       "streetAddress": "Rua Artur Magalhães, 1350 B3 301",
       "addressLocality": "Patos de Minas",
       "addressRegion": "MG",
       "postalCode": "38703-572",
       "addressCountry": "BR"
     }
   }

Commit: rtk git commit -m "feat: SEO completo + OG image + structured 
data"
```

#### 🟣 PROMPT 19 — Antigravity: Lighthouse audit + correções

```
Rodar Lighthouse audit e corrigir tudo que não tiver 95+.

1. Build production: npm run build && npm run preview
2. Abrir Chrome DevTools → Lighthouse → run em Performance, 
   Accessibility, Best Practices, SEO (mode: Mobile, throttling 
   Slow 4G)

ALVOS:
- Performance: 95+
- Accessibility: 100
- Best Practices: 100
- SEO: 100

CORREÇÕES PROVÁVEIS:
- Imagens sem alt → adicionar
- Imagens sem width/height → adicionar
- Imagens não otimizadas → converter pra WebP/AVIF, lazy loading
- Fontes bloqueando render → usar font-display: swap
- LCP alto → otimizar hero (lazy load 3D, preload critical fonts)
- Cumulative Layout Shift → reservar espaço pra imagens/vídeos
- Contraste de cor insuficiente → ajustar text-secondary/tertiary
- Botões sem aria-label → adicionar
- Faltando lang no <html> → <html lang="pt-BR">
- Faltando viewport meta tag

Após cada round de correções, rodar Lighthouse de novo até bater os 
alvos.

Commit: rtk git commit -m "perf: lighthouse 95+ em todas as métricas"
```

---

## 10. Checklist pré-launch v1

Antes de divulgar o site, verificar TUDO:

### Funcionalidade
- [ ] Form de 8 perguntas funciona ponta a ponta
- [ ] Edge function gerar-escopo retorna em <60s
- [ ] Lead salvo em Supabase
- [ ] Escopo salvo em Supabase
- [ ] PDF gerado e enviado por email (se implementado)
- [ ] Notificação chega pro Marco (se Composio integrado)
- [ ] CTAs do hero e final abrem o sheet do form
- [ ] Botão WhatsApp funciona com mensagem pré-preenchida
- [ ] Links do footer funcionam

### Visual
- [ ] Hero com 2 linhas em clip-path reveal funciona
- [ ] Cena R3F roda 60fps
- [ ] Explosão de ícones funciona com scroll
- [ ] Counters animados aparecem
- [ ] Pin scroll do "Como funciona" é suave
- [ ] Bento de cases tem parallax
- [ ] Customizador ao vivo responde em tempo real
- [ ] Cursor custom funciona em desktop

### Mobile
- [ ] Hamburger menu abre/fecha
- [ ] Headlines reduzem proporcional
- [ ] Cursor custom desativado
- [ ] Hero R3F desativado/leve
- [ ] Form funciona perfeito
- [ ] Touch targets ≥ 44px
- [ ] Vídeos não autoplay (poster em vez)

### Performance
- [ ] Lighthouse Performance 95+
- [ ] Lighthouse Accessibility 100
- [ ] Lighthouse Best Practices 100
- [ ] Lighthouse SEO 100
- [ ] LCP < 2.5s
- [ ] CLS < 0.1
- [ ] FID < 100ms

### SEO
- [ ] Title + description + OG configurados
- [ ] OG image 1200x630 criado
- [ ] Favicon
- [ ] sitemap.xml + robots.txt
- [ ] JSON-LD Organization
- [ ] lang="pt-BR" no html

### Acessibilidade
- [ ] Todos os botões com aria-label ou texto
- [ ] Contraste mínimo WCAG AA
- [ ] Navegável por teclado
- [ ] prefers-reduced-motion respeitado
- [ ] Form labels associadas

### Deploy
- [ ] foryoucodee.com.br aponta certo
- [ ] SSL ativo
- [ ] Cloudflare Worker build sem erros
- [ ] Env vars configuradas em prod
- [ ] Supabase RLS ativo
- [ ] Edge function deployada

---

## 11. Riscos + mitigação

| Risco | Probabilidade | Mitigação |
|---|---|---|
| Lovable engasga em prompt grande e gera bug | Alta | Prompts pequenos por seção. Se quebrar, reverter via GitHub e refazer. |
| R3F pesa em mobile | Alta | Detectar mobile e renderizar imagem PNG estática em vez de Canvas. |
| Edge function Claude > 60s | Média | Streaming + skeleton + mensagem "estamos perto…". Fallback: salvar briefing e gerar escopo offline + email. |
| Lead spam no form | Média | Rate limit no Supabase (RPC com check de IP), honeypot field invisível, reCAPTCHA invisível v3. |
| Fonte Fraunces/Reckless não disponível | Baixa | Fallback CSS pra serif system. Self-host se persistir. |
| Cloudflare Worker SSL não emite | Baixa | Esperar 30 min. Verificar com `dig foryoucodee.com.br`. Conferir Custom domain ativo no painel do Worker. Em último caso, remover e re-adicionar o domain. |
| Hidratação mismatch (HTML server difere do client) | Média | Coisas dinâmicas (relógio do header, IDs random) precisam wrap em `<ClientOnly>` ou guarda `typeof window !== 'undefined'`. R3F + Lenis + cursor custom obrigatórios em `<ClientOnly>`. |
| Build falha por wrangler.jsonc malformado ou bun.lockb antigo | Baixa | Pedir ao Lovable pra fixar. Não tentar editar manualmente esses arquivos. |
| Lovable + Antigravity + Claude Code desincronizam | Média | Sempre `rtk git pull` antes de editar. **1 ferramenta por arquivo por turno** (não editar simultaneamente). Commit atômico após cada prompt. |
| Vídeos dos cases pesam e estouram banda | Média | Comprimir agressivo com ffmpeg, lazy load, posters em mobile, host em CDN se necessário. |
| Claude API key vaza no frontend | Crítico | NUNCA expor em variável VITE_*. Usar SOMENTE em edge function (server-side). |

---

## 12. Pós-v1 (fora do escopo desta nota)

Após v1 live e validado por uns dias:
1. Analisar com sócios o que ajustar
2. Decidir v2 em conversa nova
3. Possíveis adições v2:
   - Página interna por case (/cases/operacional-foryou, etc)
   - Blog/changelog
   - Página "Sobre" expandida
   - Calculadora de ROI
   - Multi-idioma (en)
   - Painel admin pra gerenciar leads
   - Integração CRM próprio

**NÃO construir nada do v2 antes de v1 estar live e rodando.**

---

## 13. Contatos e referências do projeto

- Domínio: foryoucodee.com.br
- Repo: github.com/<owner>/foryoucodee-site (privado)
- Lovable project: [link após criar]
- Cloudflare Worker project: `foryou-code-site` (URL temporária: `foryou-code-site.<subdomain>.workers.dev`)
- Supabase project: [link após criar]
- Cloudflare zone: foryoucodee.com.br

---

**Última atualização:** 2026-05-05 (fim de tarde — Phase 0.1, 0.2, 0.3, 0.5 concluídas; env vars configuradas; site rodando em `foryoucodee.workers.dev`. Phase 0.4 bloqueada até registro.br. Próxima ação: Prompts 3-7 no Lovable. Continuação por outra conta Claude.)
**Próxima revisão:** após v1 live
