# 02 — Arquitetura e Catálogo

> Voltar ao [[AG Estofados — Índice]]

## 1. Sitemap

```
/                         Home
/catalogo                 Catálogo (todas as categorias)
/catalogo/[categoria]     Categoria (ex.: /catalogo/sofas)
/produto/[slug]           Página de produto individual
/sobre                    Sobre / Nossa História (desde 1997)
/projetos                 Projetos 3D / Portfólio
/depoimentos              Depoimentos de clientes
/contato                  Contato e Localização
/orcamento                Formulário de orçamento
```

Depoimentos pode também ser uma **seção** dentro da Home + Sobre, em vez de página própria — decisão a confirmar conforme volume de material.

## 2. Estrutura das páginas

### Home

1. **Header fixo** — logo AG dourado · menu (Início, Catálogo, Sobre, Projetos 3D, Contato) · botão WhatsApp dourado.
2. **Hero** — imagem grande de ambiente real · headline da marca · subheadline · CTAs **"Solicitar orçamento"** + **"Ver catálogo"**.
3. **Faixa de credibilidade** — ícones: *Desde 1997 · Feito à mão · 100% sob medida · Projetos 3D · Entrega na região*. (Inspirado na grade de ícones da referência COCO HOME.)
4. **Categorias em destaque** — cards com foto: Sofás, Poltronas, Cabeceiras, Sofás Automatizados, etc.
5. **Peças em destaque** — carrossel de cards de produto (foto + nome + categoria + "Solicitar orçamento"). **Sem preço.**
6. **Como funciona o sob medida** — 4 passos: 1) Conversa e medidas · 2) Projeto 3D · 3) Produção artesanal · 4) Entrega e instalação.
7. **Bloco Sobre** — resumo da história desde 1997 + foto da loja/equipe + link para [[#Sobre / Nossa História]].
8. **Projetos 3D / Portfólio** — galeria curta + link.
9. **Depoimentos** — 3 a 5 depoimentos de clientes.
10. **CTA final** — faixa "Vamos criar a sua peça?" com WhatsApp + formulário.
11. **Footer** — endereço, mapa, redes sociais, horário, navegação.

### Catálogo e Categoria

- Grade de cards de produto, filtrável por categoria.
- Card: foto · nome · categoria · botão "Ver detalhes".
- Topo da categoria: foto-banner + texto curto sobre aquele tipo de peça (bom para SEO).

### Página de Produto

Como **não há preço**, a página é uma vitrine + gatilho de orçamento:

1. **Galeria de fotos** — várias imagens, incluindo detalhes de acabamento.
2. **Nome + categoria**.
3. **Descrição / história da peça** — para quem é, o que a torna especial.
4. **Opções de personalização** — tecidos, medidas, acabamentos, versão automatizada (quando aplicável). Apresentadas como possibilidades, não como seletor de compra.
5. **CTA "Solicitar orçamento deste modelo"** — abre WhatsApp com mensagem pré-preenchida (ex.: *"Olá! Tenho interesse no modelo [Nome]"*) e link para o formulário.
6. **Bloco de confiança** — "feito à mão · sob medida · desde 1997".
7. **Peças relacionadas** — 3 cards da mesma categoria.

### Sobre / Nossa História

História desde 1997, o ofício artesanal, a equipe, os bastidores da produção, a loja física. Página de **autoridade** — converte o público de arquitetos.

### Projetos 3D / Portfólio

Galeria de projetos 3D e ambientes entregues. Quando houver, usar formato **antes/depois** ou *render 3D × peça real*.

### Depoimentos

Depoimentos reais (texto, foto do cliente/ambiente, idealmente vídeo). Reforça prova social.

### Contato / Localização

Endereço (Rua Silva Guerra, 140, Centro — Patos de Minas), mapa incorporado, WhatsApp, telefone, e-mail, horário de funcionamento, redes sociais.

### Orçamento

Formulário: nome, WhatsApp, cidade, tipo de peça/interesse, mensagem, (opcional) modelo de referência. Envio cai no WhatsApp e/ou e-mail da AG. Detalhes técnicos em [[04 - Especificação Técnica]].

## 3. Modelo de catálogo

Catálogo inicial **enxuto: 8 a 15 peças**. Sugestão de distribuição por categoria (a confirmar com o cliente):

| Categoria | Slug | Peças (estimativa) |
|---|---|---|
| Sofás | `sofas` | 3–4 |
| Sofás Automatizados | `sofas-automatizados` | 1–2 |
| Poltronas | `poltronas` | 2–3 |
| Cabeceiras e Camas | `cabeceiras` | 2–3 |
| Banquetas e Pufs | `banquetas-pufs` | 1–2 |

> Mesas/cadeiras, almofadas e decoração podem entrar em uma fase posterior — manter o lançamento enxuto.

### Campos de cada produto

```
nome              ex.: "Sofá Modular Toscana"
slug              ex.: "sofa-modular-toscana"
categoria         sofas | sofas-automatizados | poltronas | cabeceiras | banquetas-pufs
descricao         texto curto (2–4 parágrafos)
fotos[]           galeria (mínimo 3, ideal 5+)
personalizacao[]  tecidos / medidas / acabamentos / automatizado
destaque          true/false (aparece na Home)
relacionados[]    slugs de peças da mesma categoria
```

Nesta fase o catálogo é **conteúdo gerido em código** (coleção de dados no projeto). Um painel/CMS para a AG editar sozinha fica como evolução de Fase 2 — ver [[05 - Roadmap e Próximos Passos]].
