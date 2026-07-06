# 05 — Roadmap e Próximos Passos

> Voltar ao [[AG Estofados — Índice]]
>
> ⚠️ **Stack atualizada (2026-05-21).** As Fases 3 e 4 abaixo já refletem a toolchain final (Lovable + TanStack Start + Vercel) de [[10 - Toolchain Premium e Workflow MCP]]. Referências antigas a Antigravity / Astro / Cloudflare Pages foram corrigidas.

## 1. Visão geral das fases

```
Fase 0 — Planejamento ............ ✅ concluída
Fase 1 — Coleta de inputs ........ ⏳ depende do cliente
Fase 2 — Produção fotográfica .... ⏳ depende de Fase 1
Fase 3 — Design (wireframe → UI) . depende de Fase 1 (texto) + 2 (foto)
Fase 4 — Construção .............. depende de Fase 3
Fase 5 — SEO + Analytics ......... paralelo a Fase 4
Fase 6 — Revisão + handover ...... depende de Fase 4 + 5
Fase 7 — Evolução ................ pós-lançamento
```

**Caminho crítico:** Fotos. Tudo que vier depois do Design fica preso esperando o ensaio fotográfico — esse é o ponto que define a data real de lançamento.

## 2. Fases em detalhe

### Fase 0 — Planejamento ✅

Briefing, arquitetura, identidade, especificação técnica, roadmap, conteúdo/copy, plano fotográfico, wireframes, design system. **Concluída.** Artefatos: docs 01 a 09.

### Fase 1 — Coleta de inputs do cliente

**Objetivo:** destravar produção fotográfica e construção.

Itens a obter da AG:

- [ ] **Número de WhatsApp oficial** (com DDD) — usado em todos os botões e formulário.
- [ ] **Lista das 8–15 peças** que entram no catálogo inicial (com nomes oficiais).
- [ ] **Descrição básica de cada peça** (1–2 frases que o cliente já usa) — vira insumo do copy.
- [ ] **3–5 depoimentos de clientes** reais com autorização de uso (texto + nome + cidade; foto opcional).
- [ ] **Confirmação do domínio** — sugestão `agestofados.com.br`. Conferir disponibilidade no Registro.br.
- [ ] **Acesso ao Google Business Profile** da loja (ou autorização para a ForYou criar/reivindicar).
- [ ] **Material visual existente** — fotos brutas/originais que possam servir de plano B.
- [ ] **E-mail para receber leads** do formulário de orçamento.

**Quem executa:** Mestre conduz a coleta com a AG (1 reunião + grupo de WhatsApp para envio dos arquivos).

### Fase 2 — Produção fotográfica

**Objetivo:** produzir o acervo visual definitivo do site.

Ver briefing completo em [[07 - Plano de Produção Fotográfica]]. Resumo:

- Ensaio na loja física (Rua Silva Guerra, 140).
- 8–15 peças × ~5 ângulos cada + shots institucionais (loja, equipe, processo).
- Edição e entrega em WebP/AVIF + JPG de alta resolução.

**Plano B:** se o ensaio atrasar, lançar com seleção das melhores fotos do Instagram e trocar depois — risco assumido em [[07 - Plano de Produção Fotográfica#5. Plano B]].

### Fase 3 — Design

**Objetivo:** transformar wireframes + copy + fotos em mockup de alta fidelidade pronto para construção.

- Wireframes já definidos em [[08 - Wireframes e Decisões de Layout]].
- Design system definido em [[09 - Design System — Fontes e Tokens]].
- Base do site gerada no **Lovable** (TanStack Start); animação e refino via Claude Code/MCP — ver [[10 - Toolchain Premium e Workflow MCP]].
- Aprovação visual da AG antes de partir para código.

### Fase 4 — Construção

**Objetivo:** site no ar com catálogo, formulário e WhatsApp funcionando.

Conforme [[04 - Especificação Técnica]] e [[10 - Toolchain Premium e Workflow MCP]]:

- Repositório Git privado (padrão ForYou Code).
- **Lovable (TanStack Start) + Vercel**, deploy automático no push; DNS no Cloudflare.
- Catálogo no banco de dados (**Supabase ou Neon**) — tabela `products`.
- Páginas: Home, Catálogo, Categoria, Produto, Sobre, Projetos 3D, Depoimentos, Contato, Orçamento.
- Formulário de orçamento via função serverless na Vercel (ou Edge Function do banco) + Resend (e-mail) + Cloudflare Turnstile (anti-spam).
- Botão de WhatsApp flutuante em todas as páginas, mensagens pré-preenchidas conforme [[06 - Conteúdo e Copy#7. Mensagens de WhatsApp]].

### Fase 5 — SEO + Analytics (em paralelo à Fase 4)

- `title` e `meta description` únicos por página (padrões em [[06 - Conteúdo e Copy#8. Meta tags base]]).
- Schema.org `LocalBusiness` na Home/Contato; `Product` nas páginas de produto.
- `sitemap.xml` + `robots.txt`.
- Open Graph para previews em WhatsApp/Instagram.
- Cloudflare Web Analytics ativado (sem cookies, sem banner).
- Google Business Profile vinculado ao domínio (ação de marketing).

### Fase 6 — Revisão + handover

- QA cruzado: outro membro da ForYou roda checklist (links, formulário, WhatsApp, mobile, Lighthouse 90+).
- Reunião de entrega com a AG: como o site funciona, como ler o e-mail de leads, como pedir alterações.
- Documento `README.md` no repositório com instruções de manutenção.
- Treinamento curto (15–30 min) com a AG.

### Fase 7 — Evolução (pós-lançamento)

Backlog para depois do site no ar:

- **Painel/CMS** mais amigável para a AG editar peças sozinha (painel custom sobre o banco — o painel nativo do Supabase/Neon já cobre o básico desde o lançamento).
- **Blog** para reforço de SEO local ("Como escolher tecido para sofá", "Quanto dura um estofado sob medida", etc.).
- **Multi-idioma** (PT-EN) se aparecer demanda de fora.
- **WhatsApp Business API** + automação básica de primeira resposta.
- **Integração com Instagram** (feed embedado, link tracking).

## 3. Dependências

| Etapa | Bloqueia |
|---|---|
| Lista de peças (Fase 1) | Ensaio fotográfico, copy de produto, catálogo |
| Número de WhatsApp (Fase 1) | Todos os CTAs do site |
| Depoimentos (Fase 1) | Seção de depoimentos e prova social |
| **Fotos (Fase 2)** | **Design final, lançamento sem plano B** |
| Domínio (Fase 1) | Deploy em produção (preview na Cloudflare Pages funciona sem domínio) |
| Design aprovado (Fase 3) | Início da construção |

## 4. Estimativa de prazo

Estimativa **somente do trabalho ForYou** — cada fase começa no dia que recebe os insumos. Não compromete data até a Fase 1 fechar.

| Fase | Tempo útil estimado |
|---|---|
| 1 — Coleta de inputs | Depende da AG (alvo: 1 semana) |
| 2 — Ensaio fotográfico | 1 dia de ensaio + 3–5 dias de edição |
| 3 — Design no Antigravity | 3–5 dias úteis |
| 4 — Construção | 5–8 dias úteis |
| 5 — SEO + Analytics | 1–2 dias úteis (paralelo) |
| 6 — Revisão + handover | 2 dias úteis |

**Total ForYou:** ~3 a 4 semanas de trabalho útil, sem contar a janela do cliente.

## 5. Marcos visíveis

- **M1 — Inputs recebidos** (encerra Fase 1).
- **M2 — Fotos entregues** (encerra Fase 2).
- **M3 — Mockup aprovado pela AG** (encerra Fase 3).
- **M4 — Site no ar em preview** (Cloudflare Pages, sem domínio).
- **M5 — Site em produção** com domínio.com.br ativo.
- **M6 — Handover concluído** — projeto fechado.

## 6. Riscos e mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Ensaio fotográfico atrasar | Alta | Alto | Plano B com fotos do Instagram (qualidade limitada, mas evita travar) |
| AG não conseguir reunir depoimentos | Média | Médio | Lançar com 1–2 depoimentos e crescer com o tempo; ou substituir por "casos" |
| Domínio `agestofados.com.br` indisponível | Baixa | Baixo | Alternativas: `agestofadosmg.com.br`, `agestofadospatos.com.br` |
| Cliente pedir mudanças grandes pós-aprovação | Média | Médio | Aprovação formal de mockup antes da Fase 4; alterações grandes viram Fase 7 |
| AG quiser editar conteúdo sozinha | Alta | Baixo | Já previsto na Fase 7 (CMS) — explicar no handover |
