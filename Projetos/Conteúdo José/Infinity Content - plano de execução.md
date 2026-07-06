---
tipo: plano-execucao
tags: [foryoucode, conteudo, infinity-content, roadmap, execucao]
atualizado: 2026-06-09
status: EXECUTADO (9/9 features deployadas em 2026-06-09)
---

# Infinity Content — Plano de execução (9 features)

## ✅ STATUS DE EXECUÇÃO (2026-06-09)

Todas as 5 fases implementadas, deployadas e commitadas. 6 commits.

| Feat | O quê | Validação ao vivo |
|------|-------|-------------------|
| E | legenda+hashtags+título no dossiê | ✅ dossiê Gemini saiu completo |
| I | gancho no card | ✅ hooks afiados gerados |
| F | capa (vídeo oficial) entregue | ✅ link YouTube real |
| C | roteiro universal (texto/link/imagem) | ✅ texto+link+imagem(vision) — Mestre testou tudo no TG |
| A | busca sob demanda | ✅ 1 card postado |
| D | aprende por exemplo | ✅ dossiê OlmoEarth abriu "a jogada é no custo" — puxou o estilo do seed |
| G | feedback "por quê" | ✅ Mestre testou no TG: Pulei → 4 motivos → grava |
| H | lançamento iminente | ✅ detector roda no refill sem erro (alerta só com teaser) |
| B | resumo semanal | ✅ /test-resumo: saídos=24 gravados=2 perdidos=3 |

**API Anthropic recarregada (conta certa) 2026-06-09 ~22h — geração voltou.** Exemplo-seed (Fable 5, calibre aprovado) inserido em `exemplos` pra bootstrapar Feature D.

### 🔴 2 ACHADOS que precisam de AÇÃO do Mestre
1. **OPENAI_API_KEY inválida (401)** — o fallback NÃO funciona. Quando Anthropic cai, não tem reserva. Gerar nova key e `wrangler secret put OPENAI_API_KEY`.
2. **Anthropic em limite** (resets ~20:40 BRT 2026-06-09) — geração parada até resetar. A blindagem alertou no chat (api-anthropic + api-down) — funcionou em condição real.

### Gatilhos novos no canal (decididos na execução)
- `gerar roteiro` + texto/link/imagem → roteiro universal
- `buscar <termo>` → busca sob demanda (1 card)
- reply a um dossiê com `padrão` + roteiro corrigido → vira exemplo de ouro (Feature D)
- 👎 Pulei → botões de motivo (Feature G)
- resumo de domingo → botões "Gerar dossiê" nos temas perdidos (Feature B)

### Pendências de validação (quando API voltar)
- D: gerar dossiê com exemplo salvo, confirmar que puxa o estilo.
- G: clicar Pulei → motivo → confirmar `feedback.reason` gravado.
- H: teaser de fonte oficial → confirmar alerta "vem aí".
- C-vision: mandar print no TG → confirmar roteiro da imagem.

---

# Infinity Content — Plano de execução (9 features) — original abaixo

> Plano pra MIM (Claude) executar quando Mestre liberar. NÃO iniciar sem ordem explícita.
> Base: sistema já operacional e blindado (ver [[Infinity Content - pendências]]).
> Features detalhadas na seção "Planejado" de [[Infinity Content - pendências]].

## Princípios de execução (valem pra TODA feature)

1. **Incremental:** 1 feature por vez → `tsc --noEmit` → `wrangler deploy` → testar AO VIVO (endpoint debug ou clique) → `commit` → atualizar vault. Só então a próxima.
2. **Reusar infra existente:** fila `dossie-queue` (trabalho pesado nunca no webhook ~30s), `notifyOps` (todo erro novo vira alerta no chat), `ROTEIRO_RULES` + `MODO LANCAMENTO`, `selectCardable` (oficial-first), `generateDossie`.
3. **Não regredir a blindagem:** cada caminho novo precisa de try/catch + `notifyOps` no erro. Nada falha mudo.
4. **Trabalho >~20s vai pra fila**, nunca no webhook. Busca web / vision / classificação = fila.
5. **Validar com endpoint key-gated** antes de expor no Telegram (padrão `/test-*`).
6. **Custo sob controle:** features que gastam LLM só disparam por ação do Mestre (não em loop).

## Ordem das fases (por dependência + valor + risco)

```
Fase 1 (saída, prompt-only)      → E, I, F      [baixo risco, ganho diário]
Fase 2 (entrada do Mestre)       → parser, C, A [infra compartilhada]
Fase 3 (loop de aprendizado)     → D, G         [muda o jogo a longo prazo]
Fase 4 (proativo)                → H            [standalone]
Fase 5 (visão semanal)           → B            [capstone, usa dados da Fase 3]
```

---

## FASE 1 — Ganhos rápidos de saída (prompt-only)
**Por quê primeiro:** sem infra nova, baixo risco, valor imediato todo dia. Só mexe em prompt/saída.

### E — Legenda + hashtags + título no dossiê
- **Onde:** `src/dossie.ts` `DOSSIE_INSTRUCTION` — novo bloco de saída no fim do formato.
- **O quê:** depois do roteiro, gerar `📱 LEGENDA` (texto do post), `🏷️ HASHTAGS` (5-8), `✏️ TÍTULO`.
- **Regra:** legenda no MESMO tom (lofi/humano), hashtags do nicho (IA/builder/vibecoding).
- **Validar:** `/gen-dossie` num item → conferir que sai legenda+hashtags+título coerentes.
- **Risco:** baixo. Só aumenta a saída (cuidado com limite 4096 do Telegram — `splitText` já trata).

### I — Hook/gancho no card
- **Onde:** `src/pipeline.ts` (classificador cospe um campo `hook` curto) + `src/cycle.ts` `formatCard` (mostra o hook).
- **O quê:** classificador gera 1 gancho de Reels (≤90 chars) junto da classificação. Card passa a exibir.
- **Validar:** refill → ver cards no canal com linha de gancho.
- **Risco:** baixo. Token a mais no classificador (haiku, barato).

### F — Tela de cima entregue pronta
- **Onde:** `src/dossie.ts` (já tem o bloco 🖥️ TELA DE CIMA via web search). Reforçar pra ENTREGAR link de vídeo oficial validado, não só sugerir.
- **O quê:** prompt exige URL real (do input ou da busca); validar que é link de vídeo/página oficial. Marcar [VIDEO]/[PÁGINA].
- **Validar:** gerar dossiê de lançamento → conferir link real e clicável.
- **Risco:** médio (LLM pode inventar URL — regra anti-alucinação já existe no prompt, reforçar).

---

## FASE 2 — Camada de entrada (input do Mestre vira conteúdo)
**Por quê junto:** A e C compartilham o MESMO encanamento novo no `handleTelegramUpdate` (hoje só trata `callback_query` e reply de texto — não trata comando de texto solto nem foto).

### Infra compartilhada (fazer 1x antes de C e A)
- **Onde:** `src/cycle.ts` `handleTelegramUpdate`.
- **O quê:** detectar mensagem de texto/foto no canal e rotear por prefixo:
  - contém `gerar roteiro` → Feature C
  - começa com `buscar ` → Feature A
- **Foto:** ler `message.photo` (maior resolução) → `getFile` → download `api.telegram.org/file/bot<token>/<path>` → base64.
- **Tudo pesado vai pra FILA** (vision/web/LLM): novo `kind` na `QueueJob`.

### C — Roteiro universal (`gerar roteiro` + link/texto/imagem)
- **Onde:** novo `QueueJob {kind:'roteiro', payload}`; consumer chama gerador novo `gerarRoteiroDeInput(env, {texto?, url?, imagemBase64?})`.
- **Fluxo:**
  - imagem → Claude **vision** lê o post → roteiro
  - url → busca conteúdo (Jina/web) → roteiro
  - texto → direto → roteiro
  - usa `ROTEIRO_RULES` + `MODO LANCAMENTO` (detecta se é lançamento pelo conteúdo)
- **Saída:** mesmo formato do dossiê (+ legenda/hashtags da Fase 1).
- **Validar:** `/test-roteiro` (texto), depois imagem real no canal.
- **Risco:** médio. Vision = formato de mensagem Anthropic com block de imagem. Custo: 1 Sonnet (+imagem/+web).

### A — Busca sob demanda (`buscar X`)
- **Onde:** novo `QueueJob {kind:'busca', termo}`; consumer: web search sobre o termo → monta 1 candidato → classifica → posta 1 card (botão Gerar dossiê).
- **Reusa:** `callLLM` com `webSearch`, `classifyBatch`, `sendCard`.
- **Validar:** `buscar higgsfield` → 1 card coerente.
- **Risco:** médio. Termo vago = card fraco (classificador filtra). ~US$0,10/busca.

---

## FASE 3 — Loop de aprendizado (sistema melhora sozinho)
**Por quê depois da Fase 2:** precisa do encanamento de reply/mensagem maduro. É a alavanca de longo prazo.

### D — Aprende por exemplo (PRIORIDADE estratégica)
- **Onde:** nova tabela `exemplos` (D1); captura de reply; injeção no `DOSSIE_INSTRUCTION`.
- **Fluxo:**
  1. Mestre responde (reply) a um dossiê com o roteiro CORRIGIDO + marca (ex: reply começando com `padrão` ou botão "✅ esse é o padrão").
  2. Bot salva o texto corrigido em `exemplos` (com tema/categoria).
  3. Gerador injeta os N melhores exemplos como few-shot no prompt ("roteiros que o Mestre aprovou: …").
- **Decisão pendente:** gatilho exato (reply com palavra-chave vs botão no dossiê).
- **Validar:** salvar 1 exemplo → gerar novo dossiê → confirmar que o estilo puxou pro exemplo.
- **Risco:** médio. Prompt cresce (limitar a ~3 exemplos, rotacionar por categoria). Cuidado pra não estourar contexto/custo.

### G — Feedback "por quê" (sem fricção)
- **Onde:** `src/telegram.ts` `sendDossie` (sub-botões ao pular) + `src/cycle.ts` feedback handler + coluna `reason` em `feedback` (D1 migration manual no SQL Editor — ver gotcha de migrations).
- **Fluxo:** clicar 👎 Pulei → aparecem 4 botões: técnico demais / já vi / fraco / não é minha praia → grava `reason`.
- **Alimenta:** afinidade (`feedbackAffinity`) e o resumo (Fase 5).
- **Validar:** pular um card com motivo → conferir `reason` no D1.
- **Risco:** baixo. Migration manual em prod (lembrar: migrations não aplicam sozinhas — rodar no SQL Editor).

---

## FASE 4 — Inteligência proativa

### H — Detector de lançamento iminente
- **Onde:** `src/pipeline.ts` (classificador marca teaser/"vem aí") + `src/cycle.ts` (no refill, se achar teaser forte → `notifyOps` tipo `iminente`).
- **O quê:** tag `rumor` + sinais de teaser ("coming soon", "next week", "teaser", contagem regressiva) em fonte oficial → alerta "fica de olho, X vem aí".
- **Validar:** simular item teaser → conferir alerta no chat.
- **Risco:** baixo-médio (falso positivo = ruído; throttle no alerta).

---

## FASE 5 — Visão semanal (capstone)

### B — Resumo semanal
- **Por quê por último:** fica muito melhor com o feedback rico da Fase 3 (G) e os dados acumulados.
- **Onde:** novo cron (domingo 21h BRT = dom 00h UTC já existe; ou domingo específico) → função `resumoSemanal(env)` → posta no canal.
- **Conteúdo:** temas que saíram, quantos Mestre gravou (👍), temas que bombaram (corroboração 3+) e ele NÃO tocou — com botão `📝 Gerar dossiê` nos perdidos (acionável).
- **Decisão pendente:** foco principal — (a) o que perdeu, (b) ritmo/estatística, (c) temas mais fortes. (Mestre ainda não decidiu; default sugerido: a+c.)
- **Base:** tabela `feedback` (gravado/pulado) + `items`/`dossies`. Dados já coletados.
- **Validar:** `/test-resumo` → conferir resumo + botões funcionando.
- **Risco:** baixo. Cron já existe (ajustar dia/hora).

---

## Resumo de dependências e infra nova

| Fase | Feature | Infra nova | Migration D1 | Fila |
|------|---------|-----------|--------------|------|
| 1 | E, I, F | nenhuma (prompt) | não | não |
| 2 | parser, C, A | handler de texto/foto, getFile, vision | não | sim (kind roteiro/busca) |
| 3 | D | tabela `exemplos`, captura reply | sim (`exemplos`) | não |
| 3 | G | sub-botões, coluna `reason` | sim (`reason`) | não |
| 4 | H | detector teaser | não | não |
| 5 | B | função resumo + cron | não | não |

## Decisões pendentes do Mestre (resolver antes da fase respectiva)
- **C/A:** confirmar prefixos exatos (`gerar roteiro`, `buscar`) — JÁ decidido `gerar roteiro` (qualquer payload).
- **D:** gatilho de "esse é o padrão" (reply com palavra vs botão).
- **B:** foco do resumo (perdeu / ritmo / mais fortes).

## Ordem recomendada de ataque (quando liberar)
1. **Fase 1 inteira** (E+I+F num lote — ganho imediato, baixo risco).
2. **Fase 2** (parser → C → A).
3. **Fase 3** (D primeiro = maior retorno, depois G).
4. **Fase 4** (H).
5. **Fase 5** (B).

Cada item: deploy + teste vivo + commit + atualizar [[Infinity Content - pendências]] antes do próximo.

## Links
- [[Infinity Content - pendências]]
- [[Infinity Content]]
- [[Infinity Content - arquitetura tecnica]]
