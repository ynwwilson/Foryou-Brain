# 04 — Especificação Técnica

> Voltar ao [[AG Estofados — Índice]]
>
> ⚠️ **Stack atualizada (2026-05-21).** A recomendação original deste doc (Astro + Cloudflare Pages + Antigravity) foi **substituída** pela toolchain de [[10 - Toolchain Premium e Workflow MCP]]. As seções abaixo já refletem a decisão final. Quando houver conflito, vale o doc 10.

## 1. Natureza do site

Site de **conteúdo** (institucional + catálogo), sem app, sem login, sem checkout. Características que definem a stack:

- Páginas em sua maioria estáticas, com catálogo gerado a partir de dados.
- SEO local é prioridade — renderização estática/SSR é obrigatória.
- Performance e custo baixo de hospedagem.
- Pouca interatividade: menu, carrossel, formulário, botão de WhatsApp.

## 2. Stack do projeto

**Lovable (TanStack Start) + Vercel + Cloudflare DNS.** Detalhamento completo em [[10 - Toolchain Premium e Workflow MCP#1. Decisão final de stack]].

- **Lovable em TanStack Start** (Vite + React + SSR + file-based routing) — gera a base do site: rotas, layout, componentes shadcn/ui, integração com o banco. SSR funcional, SEO indexável, OG dinâmico.
- **Vercel** — hospedagem e deploy: SSR, preview por branch, OG dinâmico, deploy automático no push.
- **Cloudflare** — apenas **DNS** de `agestofados.com.br` (o site é servido pela Vercel, não por Cloudflare Pages).
- **Animação fina** (GSAP, Lenis, Spline) entra via Claude Code/MCP, não pelo Lovable — ver [[10 - Toolchain Premium e Workflow MCP#2]].
- Formulário de orçamento processado por **função serverless na Vercel** (ou Edge Function do banco) + Resend.

> **Astro + Cloudflare Pages saiu.** Era a recomendação inicial deste documento, descartada porque o site é cinematográfico (GSAP/Spline/storytelling em 4 atos) e o fluxo de produção é Lovable-first.

## 3. Catálogo (dados)

- O catálogo vive no **banco de dados** (tabela `products`). O banco pode ser **Supabase ou Neon** — ambos servem, ver [[10 - Toolchain Premium e Workflow MCP#6. Banco como CMS leve — Supabase ou Neon]]. A escolha entre os dois e o conflito do banco compartilhado da ForYou estão em [[17 - Status do Projeto (Live)]].
- O painel nativo do banco já funciona como **CMS leve** — a AG aprende a editar peças em ~15 min.
- Fase 2 (evolução): painel custom mais amigável, se a AG precisar. Ver [[05 - Roadmap e Próximos Passos]].

## 4. Conversão — WhatsApp e formulário

### Botões de WhatsApp

- Link `https://wa.me/55DDDNUMERO?text=<mensagem>` — **número oficial da AG é pendência do cliente**.
- Na página de produto, a mensagem vem **pré-preenchida** com o nome do modelo.
- Botão flutuante de WhatsApp visível em todas as páginas.

### Formulário de orçamento

- Campos: nome, WhatsApp, cidade, tipo de peça/interesse, mensagem, modelo de referência (opcional, preenchido quando vem de uma página de produto).
- Envio processado por **função serverless na Vercel** (ou Edge Function do banco):
  - notificação por **e-mail** para a AG (via Resend — já usado em outro projeto ForYou);
  - opcional: encaminhar resumo para o WhatsApp da loja.
- Proteção anti-spam: honeypot + Cloudflare Turnstile.
- Mensagem de confirmação + opção de continuar a conversa direto no WhatsApp.

## 5. SEO

Prioridade do projeto — a AG quer ser **encontrada no Google da região**.

- **SEO local:** palavras-chave como "estofados sob medida Patos de Minas", "sofá sob medida Patos de Minas", "reforma de estofados Patos de Minas".
- `title` e `meta description` únicos por página; páginas de produto e categoria indexáveis.
- **Schema.org:** `LocalBusiness` (endereço, horário, geo) na Home/Contato; `Product` nas páginas de produto.
- **Google Business Profile** — vincular o perfil da loja ao site (ação de marketing, fora do código, mas registrar no roadmap).
- `sitemap.xml` e `robots.txt` automáticos.
- URLs limpas e semânticas (`/catalogo/sofas`, `/produto/sofa-modular-toscana`).
- Open Graph para bons previews ao compartilhar no WhatsApp/Instagram.

## 6. Performance e qualidade

- Meta Lighthouse: 90+ em Performance, SEO, Acessibilidade e Boas Práticas.
- Imagens otimizadas (WebP/AVIF, `srcset`, lazy-load) — crítico, pois o site é fotográfico.
- Mobile-first: a maior parte do tráfego vem do link da bio do Instagram.
- Acessibilidade: contraste do texto sobre fundo preto, navegação por teclado, `alt` em todas as imagens.

## 7. Domínio, infraestrutura e analytics

- Domínio sugerido: **`agestofados.com.br`** (verificar disponibilidade no Registro.br) — registro e DNS geridos pela ForYou Code no Cloudflare.
- Repositório Git privado (padrão ForYou Code), deploy automático no push.
- E-mail transacional: Resend.
- Analytics: Cloudflare Web Analytics (sem cookies) ou Google Analytics 4 — definir com o cliente.
- SSL automático via Cloudflare.

## 8. Fora de escopo nesta fase

- Pagamento online / e-commerce.
- Login, área do cliente, orçamento automatizado com valores.
- Multi-idioma (site só em PT-BR).
- Blog (pode entrar como Fase 2 para reforço de SEO).
