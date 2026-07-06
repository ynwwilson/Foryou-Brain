---
tipo: doc-projeto
projeto: Nimbus de Prata
doc: 07 — Design e Posicionamento Visual
data: 2026-06-26
---

# 07 — Design e Posicionamento Visual

[[Nimbus de Prata — Índice|← Índice]]

> Visualmente: **premium, natural, elegante e vivo**. NÃO pode parecer sistema agro comum, portal de plantio, página rural genérica ou dashboard corporativo frio.

## A estética deve comunicar
Tradição · excelência · natureza · genética · qualidade · organização · confiança · sofisticação · comercialização de alto padrão.

## Direção do site público
Claro, leve e **editorial**. A sensação desejada é uma mistura de:
- Haras premium
- Marca de luxo
- Empresa de genética
- Showroom de alto padrão
- Hotel boutique
- Catálogo editorial
- Plataforma digital moderna

## Princípios
- **Fotografia é protagonista** — cavalos, gado, paisagens, manejo, estrutura, animais, luz natural, campo, detalhes técnicos e materiais reais conduzem a experiência.
- Muito **espaço em branco**.
- **Tipografia sofisticada**.
- **Cores naturais**, detalhes discretos.
- **Animações suaves** — vivo, mas não exagerado.

## Alinhamento com a direção do Mestre (ForYou Code)
> Ver memória `feedback_design_taste_sites`: P&B real (sem marrom), full-bleed editorial, sem grade genérica de cards, pouco texto. Marrom + cards = "cara de IA genérica". Casa perfeitamente com o brief da Nimbus.

### Toolchain provável (quando for construir — NÃO agora)
- **context7** → doc atual das libs.
- **ui-ux-pro-max** → plano de estilo/paleta/fonte/layout.
- **GSAP + ScrollTrigger / Lenis** → animação editorial suave, parallax, pin de seções de genética.
- **Three.js / R3F** (opcional) → hero ou apresentação 360° de animal de destaque, se valer o esforço.
- **shadcn + magicui** → base de UI e componentes animados (catálogo, filtros, cards de métrica).
- **impeccable + web-design-guidelines** → polir e auditar a11y antes de entregar.
- **playwright/dev-browser** → validar responsivo + 60fps.

### Riscos de design a evitar
- Catálogo virar "grade de cards genérica" → usar layout editorial, full-bleed, hierarquia forte.
- Excesso de texto técnico afogando a foto → dados em camadas (resumo + "ver detalhes").
- Painel admin parecer dashboard frio → mesma linguagem visual da marca, mesmo sendo ferramenta.
