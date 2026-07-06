---
title: "Site ForYouCode — Dívida visual (pendente Antigravity)"
type: tracking
created: 2026-05-05
tags: [projeto, site, foryoucode, divida-visual, antigravity]
status: ativo
---

# Dívida visual — pendente Antigravity

> Lista viva. Tudo que o **Lovable não consegue** entregar fica registrado aqui pra ser implementado nas Fases 3-4 (Antigravity, Prompts 8-12) ou Fase 6 (Antigravity, Prompts 16-17).
> Atualizar a cada nova pendência identificada.

---

## D1 — Seção "Dor" (P3 → upgrade no P9)

**Estado atual no Lovable:** 7 ícones dispersos, pulso suave, linhas SVG falhando, gradient de fundo.

**Efeito desejado (Antigravity):**
- Ícones nascem **juntos no centro** (sobrepostos)
- Ao entrar na viewport / scrollar, **explodem** pra suas posições finais
- Linhas pontilhadas tentam conectá-los, falham (algumas tracejadas)
- Headline "Você está rodando seu negócio em 7 ferramentas que não conversam." **sobe** com scroll progress
- Counter sobe junto: 1 → 7 ferramentas

**Por que Lovable não consegue:** `useScroll` + `useTransform` + posições absolute calculadas + timing coordenado de múltiplos elementos.

**Onde implementar:** Prompt 9 (Antigravity) — já estava previsto no roadmap como "Sacada Mobbin".

---

## D2 — Seção "Como funciona" (P4 → upgrade no P10)

**Estado atual no Lovable:** 3 cards lado a lado em grid 3 colunas (versão limpa, revertida após tentativa assimétrica falhar).

**Efeito desejado (Antigravity):**
- Estado inicial (antes da viewport): **3 cards empilhados no centro**, levemente sobrepostos
  - Card central em destaque (frente, opacidade 100%, brilho)
  - Cards laterais atrás, levemente rotacionados (~-8° à esquerda, +8° à direita)
  - Opacidade reduzida (~40%), escala menor (~0.92)
  - Borda fina translúcida com pontos nos cantos (corner markers)
  - Glow sutil purple atrás do card central
- Quando entra na viewport: cards **afastam horizontalmente** sem rotação extra
  - Esquerdo desloca pra esquerda, direito pra direita, central permanece
  - Conforme afastam, opacidade dos laterais sobe pra 100%, escala iguala
- Linhas pontilhadas verticais/horizontais no fundo (grid sutil tech blueprint)

**Referência visual:** WorkOS + Radix login boxes (screenshot enviado por Mestre 2026-05-05 21:20).

**Por que Lovable não consegue:** Timeline coordenada `x` / `opacity` / `scale` em 3 elementos com scroll trigger. Tentativa em 2026-05-05 falhou (saiu horizontal longe, sem efeito empilhado).

**Onde implementar:** Prompt 10 (Antigravity) — ampliar do "pin scroll Como Funciona" pra incluir esse efeito de cards empilhados que se afastam.

---

## D3 — Seção "Quem constrói" (P5 → assets pendentes)

**Estado atual no Lovable:** 3 cards limpos com placeholders gradient roxo no lugar das fotos.

**Pendência:**
- Substituir placeholders pelas **fotos reais** dos sócios (José, Marco, Eduardo) — ainda não temos os arquivos
- Confirmar handles sociais reais (atual: `@wilsonads.ia`, `@yngomesmarco`, `@eduardo` — esse último é placeholder)

**Onde implementar:** não é Antigravity — é tarefa de assets. Lovable mesmo resolve quando tivermos fotos. Anotar pra não esquecer antes do launch.

---

## 📐 REFERÊNCIAS VISUAIS ABSOLUTAS (definidas 2026-05-05 22:08)

> Mestre enviou 21 screenshots em `C:\Users\ynwwi\Downloads\refs`. 3 referências foram identificadas e travadas como DNA visual do site.

### Ref 1 — Sites that Move (Dylan Brouwer / Webflow portfolio)
- Dark luxo metálico, editorial pesado
- Headlines display gigantes mix sans bold + serif italic
- Eyebrows mono uppercase ("DESIGN BY DYLAN · 03:06 CET" → bate com nosso relógio)
- Cases com mockups 3D de devices sobre gradient
- Tags badge canto inferior cases ("DAPPER · DESIGN")
- Botão `● MENU` com bolinha laranja live
- Grid SHOW ALL com logos colaboradores fileira inclinada
- Marcadores `+` cruzamentos blueprint
- Ícones 3D metálico chumbo

### Ref 2 — Mobbin
- Claro, espaçamento generoso
- Headlines bold sans grandes
- CTAs duplo pílula (preta cheia + outline)
- **Logos de marcas espalhados em layout orgânico** (Twitch, ChatGPT, Dropbox, Mistral, Apple)
- Counters destacados ("1.647 apps · 609.600 screens · 139.300 flows")
- Mockups apps 3D centralizados
- Tabs em pílula (Screens / UI Elements / Flows)
- Header pílula

### Ref 3 — WorkOS AuthKit + Radix
- Dark deep tech, glow seletivo
- Headlines display brancas GIGANTES
- **Login boxes com corner markers (4 cantos) + dotted border** ← base D2
- Card central com glow purple radial atrás
- Grid capabilities com ícones tech
- **Linhas pontilhadas conectando elementos** ← base D1
- Cards seção com eyebrow mono ("Shine bright" / "Framework freedom")
- Color customizer com swatches + radius slider ← base D5

### Blend ForYou Code — quem manda em cada seção

> **Decisão 2026-05-05 (Mestre):** relógio mono no header foi REMOVIDO (Lovable). Manter assim. Header passa a ser só Mobbin (pílula limpa), sem o detalhe Sites that Move.

| Seção | Referência dominante |
|---|---|
| Header | Mobbin (pílula limpa, sem relógio) |
| Hero | WorkOS AuthKit (display gigante + glow purple radial) |
| Dor (P3 → upgrade D1) | WorkOS Radix (linhas pontilhadas conectando) |
| Como funciona (P4 → upgrade D2) | WorkOS AuthKit (cards empilhados com corner markers) |
| Quem constrói (P5) | Sites that Move (Dylan card editorial) |
| Cases (P6 → upgrade D4) | Sites that Move (mockups 3D + tag canto) |
| Sacada Mobbin (P9 — upgrade D1) | Mobbin literal (logos espalhados + counters) |
| Customizer (P16 — D5) | WorkOS Radix customizer |
| CTA final (P7) | Mobbin (CTAs pílula + headline display) |

---

## D4 — Seção "Cases" (P6 → vídeos loop no P17 + assets)

**Estado atual no Lovable:** Bento grid 4 cards (Operacional ForYou destaque, Salinha + SmartCell direita, Totus largura total embaixo). Mockups internos = placeholders gradient roxo.

**Pendência 1 (Antigravity, P17):** vídeos em loop dentro dos cards (IntersectionObserver + lazy load + perf mobile + poster fallback).

**Pendência 2 (assets — não-Antigravity):**
- Screenshots/mockups reais de cada produto
- Páginas internas de case (link "Ver case →" hoje aponta pra nada)
- Atenção: **Totus Cenografia "IA do Rodrigo" NÃO ESTÁ EM PRODUÇÃO** (ver memória `project_totus_cenografia.md`). Não citar como case entregue. Considerar trocar por outro case ou mover pra "em construção".

**Onde implementar:** P17 (Antigravity) + sessão dedicada de assets antes do launch.

---

## D5 — Customizer ao vivo (P16 — Antigravity)

**Estado atual:** ainda não construído.

**Efeito desejado (base WorkOS Radix customizer):**
- Painel lateral com swatches de cor (paleta: roxo, preto, azul, verde, vermelho)
- Slider de border-radius (0px → 16px)
- Toggle dark/light
- Campo upload de logo
- Mockup de app reagindo em tempo real (login box / dashboard) à medida que altera os controles
- Linha pontilhada com corner markers no mockup (estilo AuthKit)

**Onde implementar:** Prompt 16 (Antigravity).

---

## D6 — Mobile completo (todas as seções, < 768px)

**Pendência ampla:** mobile precisa estar 100% alinhado, centralizado, sem scroll horizontal acidental, sem texto cortado, com tipografia hierárquica preservada, padding consistente, tap targets ≥44x44px.

**Atenção referências:** mobile da Mobbin é o gabarito (espaçamento generoso, headlines respiram, CTAs em pílula full-width centralizados). Sites that Move como segunda referência (eyebrows mono, layout editorial mesmo em mobile).

**Onde implementar:** prompt mobile-fix no Lovable (já redigido) ANTES de partir pro Antigravity. Detalhes finos de mobile podem voltar como ajuste no Antigravity também.

---

**Última atualização:** 2026-05-05 noite — Phase 2 fechada. D1-D6 registradas. Referências visuais absolutas (Sites that Move + Mobbin + WorkOS AuthKit/Radix) travadas como DNA do site. Próxima ação: prompt mobile-fix no Lovable, depois Antigravity (P8).
