# AG Estofados — Site Institucional

> Projeto **ForYou Code** · Cliente: **AG Estofados** (Patos de Minas/MG)
> Status: **Pronto para conectar MCPs e disparar Lovable** — ver [[10 - Toolchain Premium e Workflow MCP]] · 🔴 status vivo em [[17 - Status do Projeto (Live)]]
> Início do planejamento: 2026-05-21

Site institucional + catálogo premium para uma estofaria sob medida de alto padrão, com conversão por WhatsApp e formulário de orçamento.

## Documentos

1. [[01 - Briefing]] — negócio, objetivos, público-alvo, posicionamento e concorrência.
2. [[02 - Arquitetura e Catálogo]] — sitemap, estrutura de cada página e modelo de catálogo.
3. [[03 - Identidade Visual e Tom de Voz]] — paleta preto + dourado, tipografia, componentes e voz da marca.
4. [[04 - Especificação Técnica]] — formulário, SEO local e performance (⚠️ stack sobrescrita pelo [[10 - Toolchain Premium e Workflow MCP]]).
5. [[05 - Roadmap e Próximos Passos]] — fases (0 a 7), dependências, cronograma, marcos e riscos.
6. [[06 - Conteúdo e Copy]] — textos prontos de cada página + meta tags + mensagens de WhatsApp.
7. [[07 - Plano de Produção Fotográfica]] — briefing para o fotógrafo, lista de shots, plano B.
8. [[08 - Wireframes e Decisões de Layout]] — estrutura visual de cada tela + grid + comportamentos.
9. [[09 - Design System — Fontes e Tokens]] — PP Editorial New + Inter + Cormorant italic, tokens, componentes.
10. [[10 - Toolchain Premium e Workflow MCP]] — Lovable + TanStack Start + GSAP + Lenis + Spline + Supabase + Vercel; workflow MCP; setup passo a passo.
11. [[11 - Storytelling em 4 Atos]] — site tratado como filme (Conflito → Revelação → Peça → Convite).
12. [[12 - Immersive Interactions Catalog]] — 18 interações imersivas em 3 tiers + anti-padrões.
13. [[13 - Pipelines Generativos]] — 15 pipelines automatizados via MCP/API (P0-P3).
14. [[14 - Mapa de Conexões]] — 3 portas (MCPs, APIs, Browser) + tudo que Claude orquestra sozinho.
15. [[15 - Skills Anti-Slop]] — Impeccable + Huashu + UI/UX Pro Max + Taste + Playwright (defesa em 5 camadas).
16. [[16 - Setup e Credenciais]] — checklist executável de chaves, MCPs, software e fontes.
17. [[17 - Status do Projeto (Live)]] — 🔴 documento vivo: decisões batidas, tokens testados, tasks, conflitos.

## Decisões fechadas (Fase 0 — planejamento)

| Tema | Decisão |
|---|---|
| Conversão | WhatsApp em todo o site **+ formulário de orçamento** (sem checkout/e-commerce) |
| Visual | **Preto + dourado** — identidade da marca AG |
| Catálogo | **Páginas de produto individuais**, catálogo enxuto (**8–15 peças**) |
| Páginas | Home, Catálogo, Categoria, Produto, Sobre, Projetos 3D, Depoimentos, Contato, Orçamento |
| Stack | **Lovable em TanStack Start** + **Supabase ou Neon** + **Vercel** + **Cloudflare DNS** + Resend |
| Animação | **GSAP 3.13 + Lenis 1.3 + Spline 3D + Framer Motion + Lottie** |
| Fontes | **PP Editorial New** (display) + **Inter** (corpo) + **Cormorant Garamond italic** (citações) |
| Ícones | **Lucide** + **Lottie** animados + SVG oficial WhatsApp |
| Tom | **Afiado, manifesto, ofício** — caixa alta no hero, colchetes nos CTAs |
| Workflow | **Lovable faz base · Claude Code via MCP faz animação/refino** |
| Modelo | Cliente ForYou Code (entrega padrão da empresa) |
| Domínio/host | ForYou Code cuida (registro + Cloudflare Pages) |

## Referência visual

Template **"COCO HOME — Interior Modern"**: estética escura premium, cards arredondados, hero forte, navegação por categorias em ícones. Usado como inspiração de **layout e clima** — não de modelo de negócio (a referência é e-commerce com preço fixo; a AG é sob medida).

## Próximo passo (em execução)

**Setup do ambiente ForYou** (antes/em paralelo à Fase 1 do cliente):

- [x] Mestre tem Lovable Pro
- [ ] Conectar **Lovable MCP** no Claude Code — ver [[10 - Toolchain Premium e Workflow MCP#7.1]]
- [ ] Criar projeto **Supabase** + conectar Supabase MCP — ver [[10 - Toolchain Premium e Workflow MCP#7.2]]
- [ ] Criar conta **Vercel** + conectar Vercel MCP — ver [[10 - Toolchain Premium e Workflow MCP#7.3]]
- [ ] Registrar domínio `agestofados.com.br` no Registro.br
- [ ] Disparar projeto Lovable com prompt sistema completo

**Em paralelo — Fase 1 com o cliente AG:**

- [ ] Número de WhatsApp oficial (com DDD)
- [ ] Lista das 8–15 peças do catálogo inicial (nomes oficiais + 1-2 frases)
- [ ] 3–5 depoimentos reais (texto + autor + cidade + autorização)
- [ ] Acesso ao Google Business Profile (ou autorização para criar/reivindicar)
- [ ] Material visual existente (fotos brutas que possam servir de plano B)
- [ ] E-mail oficial para receber leads do formulário
- [ ] Horário de funcionamento da loja
- [ ] Definição da data do ensaio fotográfico (ver [[07 - Plano de Produção Fotográfica]])

Workflow detalhado em [[10 - Toolchain Premium e Workflow MCP#8. Workflow operacional]].
