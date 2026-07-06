# 15 — Skills Anti-Slop

> Voltar ao [[AG Estofados — Índice]]
>
> 5 skills (Claude Code) que formam **pipeline de defesa em 5 camadas** contra "AI slop" — designs genéricos que IA gera por padrão. Custo: R$ 0. Impacto: o site da AG sai do nível "ok" pro nível "agência premium".

## As 5 skills

| Skill | Stars | Função |
|---|---|---|
| **Impeccable** | 15K (Paul Bakaus) | **Auditor.** 20 comandos (`/audit`, `/polish`, `/critique`), detecta 24 anti-padrões (purple gradients, dark glows, bounce easing, cramped padding) |
| **Huashu-Design** | 662 (alchaincyf, MIT) | **Prototipador HTML nativo.** 20 design philosophies + 5 review dimensions + animation pipeline exportando MP4 |
| **UI/UX Pro Max** | 71K (nextlevelbuilder) | **Cérebro de design system.** 67 UI styles, 161 paletas, 57 pares tipográficos, 99 guidelines UX, 161 reasoning rules |
| **Taste** | (leonxlnx) | **Regras de bom gosto.** Bane emojis, neon glows, fake stats, hero centralizado. Força assimetria, fontes reais, spacing premium |
| **Playwright skill** | (lackeyjb) | **Olho real no DOM.** Claude opera browser, escreve tests do que existe (não da memória), visual regression, screenshot diff |

## Pipeline de defesa em 5 camadas

```
1. PROJETAR        →  UI/UX Pro Max
   gera design system contextualizado (paleta, tipografia, padrões, anti-patterns)
   ↓
2. REGRAS LIGADAS  →  Taste (main + soft + output)
   ativa em toda geração: sem clichês, sem placeholders, fonts reais
   ↓
3. PROTOTIPAR      →  Huashu-Design
   gera HTML nativo pra revisar antes de virar código React
   exporta MP4 das animações pra aprovar visualmente
   ↓
4. CONSTRUIR       →  Lovable + Claude Code (MCPs)
   código real, animação GSAP, integração Neon, deploy Vercel
   ↓
5. AUDITAR         →  Impeccable
   /audit detecta os 24 anti-padrões
   /polish refina, /critique avalia direção
   ↓
6. VERIFICAR       →  Playwright skill
   Claude opera o browser real, screenshot diff, visual regression
   flagra bug ANTES do deploy ir pra produção
   ↓
PRODUÇÃO ✅
```

Cada camada é filtro. Slop só passa se atravessar 5 redes.

## Como entra na AG Estofados

### Etapa 1 — Disparo do Lovable

Rodo `UI/UX Pro Max --design-system` com briefing AG. Volta:
- Pattern: `editorial-luxury`
- Style: `dark-premium-cinematic`
- Palette: filtrada das 161 → 1 vencedora cruzada com nossos tokens
- Typography: 57 pares → cruzados com PP Editorial + Inter
- Anti-patterns vertical estofado: [...]

Cruzo com [[09 - Design System — Fontes e Tokens]] e mando o **prompt sistema do Lovable já com Taste skill ativa**.

### Etapa 2 — Lovable gera a base

Lovable usa briefing reforçado. Taste impede:
- Emoji em CTAs
- Hero centralizado
- Neon glow
- `// TODO` ou `/* placeholder */` (output-skill)

### Etapa 3 — Prototipagem de seção complexa

Antes de mandar o Hero pro Lovable, rodo Huashu-Design pra gerar **HTML nativo + animação MP4** do hero proposto. Mestre vê o vídeo em 30s. Aprova ou ajusta. Só então vai pro Lovable.

### Etapa 4 — Auditoria pós-geração

Toda vez que Lovable ou eu mexo num componente, rodo `Impeccable /audit`. Detecta:
- Dourado em mais de 3 lugares na mesma tela? Flag.
- Padding cramado? Flag.
- Touch target < 44px no mobile? Flag.
- Linha de texto > 75 chars? Flag.
- Heading skipping (H2 → H4)? Flag.

Corrijo com `/polish`.

### Etapa 5 — Verificação visual antes de deploy

Antes do `vercel --prod`, rodo Playwright skill:
- Abre o preview URL
- Compara screenshot atual vs baseline aprovada
- Detecta regressões pixel-perfect
- Testa interação real (botão WhatsApp, form, hero anima)
- Roda em Chrome + Firefox + Safari + mobile (iOS/Android emulado)
- Lighthouse 90+ obrigatório

## Ordem de instalação

```
1. Taste              → instala primeiro (regras valem desde a 1ª geração)
2. UI/UX Pro Max      → segundo (gera o system base)
3. Huashu-Design      → terceiro (protótipos rápidos)
4. Impeccable         → quarto (audita o que já foi gerado)
5. Playwright skill   → quinto (substitui/complementa gstack que já temos)
```

## Comandos de instalação

| Skill | Como instalar |
|---|---|
| **Taste** | `git clone https://github.com/leonxlnx/taste-skill ~/.claude/skills/taste` |
| **UI/UX Pro Max** | `git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill ~/.claude/skills/ui-ux-pro-max` (depois copiar `.claude/skills/ui-ux-pro-max` interno) |
| **Impeccable** | `npx impeccable install` no diretório do projeto |
| **Huashu-Design** | Conforme README: `npx -y @huashu-design/cli install` |
| **Playwright skill** | `git clone https://github.com/lackeyjb/playwright-skill ~/.claude/skills/playwright-skill` |

Exatos comandos confirmados nos README de cada repo.

## Custo

| Skill | Custo |
|---|---|
| Todas as 5 | R$ 0 (open source) |

Único custo é tempo de instalação (~5 min cada).

## Sources

- [Impeccable — GitHub](https://github.com/pbakaus/impeccable)
- [Impeccable review (apidog)](https://apidog.com/blog/impeccable-claude-code-skill/)
- [Huashu Design — GitHub](https://github.com/alchaincyf/huashu-design)
- [UI/UX Pro Max — GitHub](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [Taste Skill](https://www.tasteskill.dev/)
- [Playwright Skill — GitHub](https://github.com/lackeyjb/playwright-skill)
