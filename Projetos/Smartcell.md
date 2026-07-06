---
title: "Smartcell"
type: projeto
created: 2026-03-26
atualizado: 2026-05-06
tags: [projeto, ecommerce, cliente, entregue]
status: entregue
---

# Smartcell — Smartcell Premium Store

## Cliente
Fellipe — loja de eletrônicos premium em Patos-MG

## Status
**Entregue em 25 de abril de 2026.** Em produção em https://smartcellsite.com.br (e mirror Lovable em https://smartcell.lovable.app).

## Norte estratégico (definido 27/05/2026)
> **Site nacional > loja física no médio prazo.** Documento-mãe: [[Projetos/Smartcell - Tese estrategica|Tese estratégica]]. Tudo neste projeto a partir de agora é avaliado contra essa tese.
>
> **Docs operacionais subordinados:**
> - [[Projetos/Smartcell - Plano de crescimento|Plano de crescimento]] — execução tática 30 dias
> - [[Projetos/Smartcell - Cronograma de conteudo|Cronograma de conteúdo]] — estratégia por canal
> - [[Projetos/Smartcell - Estrategia de conteudo e vendas|Estratégia de conteúdo e vendas]] — plano para Reels, carrossel, Stories, VIP e site venderem
> - [[Projetos/Smartcell - Estrategia ampliada|Estratégia ampliada]] — 16 frentes + ondas financiadas pelo caixa
> - [[Projetos/Smartcell - 5 Roteiros venda site|Roteiros venda site]] (em pausa — aguardando referências virais)
> - [[Projetos/Smartcell - SESSAO 2026-05-27 planejamento nacional|Sessão 2026-05-27]] — resumo executivo completo do planejamento estratégico nacional

## Modelo comercial
Participação nos lucros — 20% do lucro de cada produto vendido. Sem cobrança de projeto. **Sem mais nada a ser pago ou contratado** — manutenção, evolução e novos módulos entram no acordo de participação. Split de sócios (José/Marco/Eduardo, soma 100%) virou regra de negócio dentro do admin financeiro.

## Stack final
- **Frontend:** React 18 + Vite 5 + TypeScript 5 + Tailwind 3 + Framer Motion + Embla Carousel + Zod + React Router
- **Backend:** Lovable Cloud (Supabase) — DB, Auth, Storage, Edge Functions, Realtime, RLS
- **IA:** Lovable AI Gateway com Gemini 2.5 Pro/Flash + GPT-5 (fallback configurado)
- **Pagamento:** Mercado Pago (PIX) + Asaas (PIX/Boleto)
- **Outros:** ViaCEP, PWA com service worker próprio, WhatsApp `wa.me` (sem MegaAPI)

## Escopo entregue (consolidado)

### Frontend público (loja)
- 26+ rotas: Home, /iphone, /iphone-17, /iphone-novos, /seminovos, /usados, /mac, /loja/:categoria, /loja/produto/:id, /loja/acessorios + subcategorias, /favoritos, /checkout, /minha-conta, /rastrear-pedido, e 9 institucionais (sobre, garantia, troca, como compramos, pagamento, trabalhe conosco, privacidade, cookies, termos)
- Header glass com drawer mobile, busca global com debounce 300ms, dark mode toggle, footer com newsletter, breadcrumbs, 404 customizada (CSS art iPhone), PageTransitions 300ms, LoadingScreen branded
- Hero com vídeo background loop, parallax 70%, fade-out 25%, gradient title, iPhone 17 Pro Max delayed entry
- Catálogo com ProductCard branco, badges coloridos (Última unidade > Manual > Destaque > Seminovo > Oferta), filtros laterais, sort em tempo real, toggle Novos/Seminovos, skeletons, Embla Carousel, lightbox fullscreen, scroll fade-ins via IntersectionObserver

### Conversão & marketing
- Welcome popup 3s com cupom BEMVINDO 5%
- Urgency triggers: estoque baixo, timer 3h, viewers dinâmicos (8–24)
- Cupons SMARTCELL10, BEMVINDO + frete grátis automático >R$1.000
- Related products (mesma categoria, scroll horizontal mobile)
- Newsletter com Zod
- Notify-me (e-mail para reposição quando stock=0)
- Reviews funcionais (estrelas, distribuição, persistência)
- Comparador (modal 2-3 produtos, diferenças destacadas)
- Favoritos com heart, contador navbar, localStorage
- Busca global agrupada por categoria

### Carrinho & checkout
- CartSidebar (340px desktop, 85vh bottom-sheet mobile)
- Merge por ID/cor/storage
- Calculadora de frete por CEP (ViaCEP)
- **Frete por região MG:** Patos R$9 / Triângulo R$40 / Resto MG R$40 / Grátis >R$1.000 / Bloqueia fora de MG
- Prazo dinâmico (1-3 dias úteis novos, 3-7 seminovos)
- Checkout 4 etapas: Endereço → Entrega → Pagamento → Confirmação
- Pedidos SC-XXXX com persistência localStorage
- Finalização via WhatsApp `wa.me` (553438212212) com mensagem formatada

### Pagamentos
- **PIX Mercado Pago:** QR dinâmico + copia-e-cola + webhook + polling 5s
- **PIX/Boleto Asaas:** edge function + webhook
- Edge function consultar-status-pix

### PWA
- Service worker próprio (`public/sw.js`)
- Offline cache, manifest, install banner 30s, ícones e splash

### Painel Admin (`/admin/*`)
13 módulos: Dashboard (KPIs), Produtos (listagem/novo/editar/variações), **Seminovos (condição, bateria %, IMEI, checklist 30 itens)**, Pedidos (status, ações WhatsApp templates), CRM (funil de leads), **Financeiro (Receita vs Custo, top 10 lucrativos, split sócios José/Marco/Eduardo)**, Categorias, Banners, Galeria com GallerySelector, Avaliações, Usuários, Notificações, Jobs IA, Configurações + DataCleanupSection. AdminGuard, AdminLogin, AdminLayout, AdminSidebar, ConfirmDialog em ações destrutivas, ProductForm reutilizável, drag-and-drop ordering, tabelas mobile responsivas.

### IA & Automações (8 edge functions)
1. `gerar-descricao-produto` — Lovable AI Gateway (Gemini/GPT) gera copy
2. `generate-product-color-images` — gera imagens por cor (Gemini Image)
3. `save-product-color-image`
4. `processar-jobs-ia` — fila assíncrona
5. `criar-pix-mercadopago` + webhook
6. `criar-cobranca-asaas` + webhook
7. `consultar-status-pix`
8. `gerenciar-admin`
+ `_shared/ai-fallback.ts` — fallback entre modelos

### Conta do usuário
Auth localStorage (cadastro, login, logout), endereço com ViaCEP, histórico de pedidos, rastreamento (timeline vertical, valida pedido+CPF), pré-popula SC-0042/SC-0051 se vazio, favoritos persistentes.

### Conformidade & SEO
Cookie consent LGPD, páginas privacidade/cookies/termos, meta tags, JSON-LD, canonical, viewport, lazy loading de todas as rotas, alt text, robots.txt, manifest.json.

### Design system
Tema híbrido: Obsidian (#020202) Hero/Xiaomi + Light/white restante. Primary Apple Blue #0071e3. Montserrat (body) + Akira (highlights). Liquid Glass (Hero), Bento Grid (categorias), Trust marquee velocity scroll (180 dias garantia, 30 itens checklist), hard cuts entre seções, Framer Motion, dark mode com transições 300ms (FOUC prevention inline script), logo textual `smartcell-logo-text.png`.

## Integrações ativas
| Serviço | Uso |
|---|---|
| Mercado Pago | PIX dinâmico + webhook |
| Asaas | PIX/Boleto + webhook |
| ViaCEP | Endereço automático |
| Lovable AI Gateway | Descrições + imagens IA (Gemini + GPT) |
| WhatsApp `wa.me` | Checkout + atendimento (553438212212) |
| Supabase Storage | Imagens de produtos |

## O que NÃO entrou (status revisado 27/05/2026 contra tese nacional)

| Item | Status atual |
|---|---|
| Integração transportadora (Melhor Envio) | ⚠️ **PRIORIDADE MÁXIMA** — bloqueia tese nacional. Implementação semana 1-2. |
| Google Analytics / Meta Pixel + CAPI | ⚠️ **PRIORIDADE MÁXIMA** — sem isso, R$ 2k/mês em ads é cego |
| Catálogo Meta Business | ⚠️ Prioridade alta — destrava Instagram Shopping |
| Programa de pontos / fidelidade | Fase 2 (3-9 meses) |
| Chatbot vendedor IA conversacional | Não entra — atendimento humano + WhatsApp Business resolve |
| E-mail transacional próprio | Fase 1 (semanas 3-4) — pós-venda + carrinho abandonado |
| MegaAPI | Sem necessidade — `wa.me` resolve |

Detalhes em [[Projetos/Smartcell - Plano de crescimento|Plano de crescimento]].

## Status comercial
- ✅ **Em produção desde 25/04/2026**
- ⏳ Faturamento ainda não tem números (loja recém-finalizada)
- ✅ **Fellipe autorizou uso como case público** (nome, marca, número 553438212212)
- ✅ **Disponível para gravar 4º asset de venda** (Plano Comercial 2026 originalmente previa 3 — Rodrigo, Dayane, ForYou Code interno)

## Uso comercial pelo time
- **Asset visual forte:** hero com vídeo, painel admin completo, fluxo PIX automático, IA gerando descrições e imagens — bom material pra demo
- **Nicho de prova:** e-commerce premium / eletrônicos / seminovos com IMEI / loja regional
- **Argumento:** "construímos uma loja completa com checkout PIX automático, IA gerando produto e split de lucro entre sócios — em participação, sem cliente pagar projeto"

## Relacionado
- [[ForYou Code]]
- [[knowledge/Catalogo de entregas ForYou Code|Catálogo de entregas — case validado]]
- [[knowledge/Plano Comercial ForYou Code 2026|Plano Comercial 2026]]
- [[knowledge/Licoes tecnicas e-commerce Smartcell|Lições técnicas Smartcell]]
