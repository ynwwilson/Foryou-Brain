---
data: 2026-05-18
sessao: ForYou Leads — sistema completo + auditoria + roadmap
projeto: "[[Pipeline de Leads ForYou]]"
tags: [foryou, leads, automacao, instagram, adspower, worker, claude-vision]
duracao: ~10h (várias iterações ao longo do dia)
---

# ForYou Leads — Construção, debug, auditoria, roadmap

> Sessão maratona. Saímos do "app que captura leads" pra "sistema que envia DMs automaticamente com worker AdsPower + Claude Vision + biblioteca de vídeos locais". No fim, auditoria completa e roadmap de 5 fases.

---

## 🎯 Onde começamos / onde chegamos

### Estado no início do dia
- App Next.js no Vercel com captura automática de leads via Apify + Claude funcionando
- Pipeline UI, dashboard, métricas
- Envio de DMs era 100% MANUAL ("Abrir IG + Copiar" no card)

### Estado no fim do dia
- ✅ Sistema completo de envio automatizado funcionando
- ✅ Worker AdsPower com Playwright, Vision fallback, recovery automático
- ✅ Biblioteca de vídeos locais sincronizada
- ✅ Mensagem unificada gerada pelo Claude
- ✅ Detecção real de envio (poll DOM por `<video>`)
- ✅ Auditoria de 55 melhorias mapeadas em 5 fases
- ✅ Notas Obsidian atualizadas

---

## 🛠 O que construímos hoje (cronológico)

### Manhã/tarde — features de produto
1. **Mudança de design completo do app** (já parcial, mas refinamos contrastes, glassmorphism, dark mode)
2. **Botões de descartar/snooze inline** no `/enviar`
3. **Mensagem única `msg_unified`** com CTA fixa do vídeo do Dr. Eder
4. **Biblioteca de vídeos**: Primeira tentativa via Vercel Blob (deu CORS, abandonado)
5. **Migration pra vídeos locais** — worker scaneia `scripts/videos/` e reporta pra API

### Tarde — sistema de envio
6. **Tabela `send_jobs`** com lifecycle (pending → running → done/cancelled/failed)
7. **Página `/enviar`** com preview, dropdown de vídeo, botão Iniciar, progresso live
8. **Worker AdsPower** (`scripts/worker-adspower.mjs`):
   - Conecta AdsPower API local (port 50325)
   - Playwright via CDP `connectOverCDP`
   - Profile `k1cn2qmx` em modo `visible` (depois `background`)
   - Polls API a cada 5s
   - Auto-cleanup de jobs órfãos no startup + a cada 30s
9. **Instalador Windows** (`install-adspower.bat`):
   - Configura env vars (CRON_SECRET, ADSPOWER_PROFILE_ID)
   - Instala deps e Playwright Chromium
   - Cria VBS na pasta Startup pra rodar hidden no boot

### Noite — debug e robustez
10. **Múltiplas iterações** do worker pra resolver problemas:
    - Worker abria Explorer do Windows (fix: não clica botão visível, marca input direto)
    - Mini chat só aceitava imagem (fix: `expandMiniChat` pra ir pro `/direct/t/`)
    - Limite de 50MB do `setInputFiles` via CDP (fix: HTTP server local + DataTransfer + CSP bypass)
    - `findInput` pegando campo de Notes em vez de composer (fix: scoring inteligente)
    - Job órfão bloqueando novos jobs (fix: removido heartbeat refresh no poll)
    - `dismissPopups` clicando coisa errada (fix: `text-is` em vez de `has-text`)
    - Status update SQL falhava com NULL parameter (fix: branchear SQL)
    - Vídeo "enviado" sem confirmação real (fix: poll DOM por `<video>` 8s pós-Send)

11. **Claude Vision como fallback inteligente**:
    - Endpoint `/api/cron/vision/click-target`
    - Função `findElementInImage` em `lib/claude.ts`
    - Worker tira screenshot + manda pro Claude pedindo coordenadas
    - Cai em ação quando seletores DOM falham

### Madrugada — auditoria e planejamento
12. **Auditoria ultrathink** — mapeei 55 melhorias:
    - 7 itens críticos (Fase 1) — anti-detection, HMAC, backup
    - 8 itens reliability (Fase 2)
    - 8 itens UX (Fase 3)
    - 5 itens inteligência (Fase 4)
    - 6 itens escala (Fase 5)

13. **Roadmap em 5 fases** salvo em [[ForYou Leads — Roadmap Pós-Auditoria]]

---

## 💥 Bugs marcantes resolvidos

### 1. Vídeo de 175MB não enviava
**Causa**: Playwright via CDP transfere bytes via WebSocket → limite 50MB.
**Solução**: HTTP server local na máquina (worker hosta o vídeo em 127.0.0.1:PORT), JS injetado na página `fetch + DataTransfer` no `input[type="file"]`. Bypassa CDP. Funcionou pra qualquer tamanho.

### 2. CSP do Instagram bloqueava fetch de localhost
**Causa**: IG tem `Content-Security-Policy: connect-src 'self'`.
**Solução**: `Page.setBypassCSP({ enabled: true })` via CDP session no startup do browser.

### 3. Vercel Blob v2.x dava CORS
**Causa**: URL `vercel.com/api/blob/...` bloqueado por CORS pra subdomínios `.vercel.app`. Bug conhecido v2.x.
**Solução**: Abandonado. Migramos pra vídeos locais sincronizados via worker.

### 4. Job 'running' órfão bloqueava todos os novos
**Causa**: Poll endpoint refrescava heartbeat de jobs running EM TODA chamada. Worker novo morre, worker novo vê job running falso vivo, claim falha pra sempre.
**Solução**: Removido o `UPDATE last_heartbeat_at` do poll. Só worker ativo que está processando atualiza via `/progress` event.

### 5. Botão "Adicionar foto" abria File Explorer
**Causa**: Worker clicava no botão visível "📷 Adicionar foto" do IG, que dispara `input.click()` do file input. CDP não interceptava → SO abria dialog.
**Solução**: Worker procura `<input type="file">` no DOM diretamente (sem clicar em nada visível) e marca com `data-foryou-file`. `setInputFiles` direto via Playwright.

### 6. PostgreSQL "could not determine data type of parameter $2"
**Causa**: SQL com `CASE WHEN ${x} IS NOT NULL THEN ${x} ELSE col END` falhava quando `x` era sempre NULL em ambas referências.
**Solução**: Branchear o SQL — se `variant_sent` fornecido, inclui na lista de colunas; senão, exclui da SQL inteira.

### 7. Worker mentia "✓ Vídeo enviado"
**Causa**: Após `setInputFiles`, worker logava sucesso sem verificar.
**Solução**: Poll DOM por 8s buscando `<video>` ou `[aria-label*="video"]` na conversa. Se não aparecer → throw "vídeo não enviou de fato".

### 8. Mini chat do IG não aceita vídeo
**Causa**: O popup mini chat (lateral direita) tem input file `accept="image/jpeg"`. Aceita só imagem.
**Solução**: `expandMiniChat()` clica no ícone ↗ pra navegar pra `/direct/t/THREAD_ID` (DM completo, aceita vídeo).

### 9. findInput pegava campo de Notes em vez de composer
**Causa**: `[contenteditable="true"]` pegava o primeiro encontrado — que era o "Conte as novidades" das Notes do IG, não o composer.
**Solução**: Scoring inteligente. Penaliza textos "novidade" / "Conte as novidades" (-50), bonus pra `role="textbox"` (+20) e posição inferior da viewport (+30), bonus máximo (+100) pra aria-label "message"/"mensagem".

---

## 🧠 Decisões importantes da sessão

1. **Worker DEVE rodar local** — Vercel é datacenter, Instagram bana IP de datacenter. Worker no PC do Wilson com IP residencial é única opção segura.

2. **Vídeos locais > cloud** — depois das brigas com Vercel Blob (CORS), decidimos sync local. Worker scaneia `scripts/videos/`, reporta pra API. Zero upload.

3. **AdsPower em vez de Chrome puro** — começamos com Chrome via Playwright launchPersistentContext, migramos pra AdsPower CDP. Anti-detect melhor.

4. **Claude Vision como fallback, não primário** — vision é caro e lento. Usar SÓ quando seletores DOM falham nos pontos historicamente problemáticos (expand mini chat, send button, find input).

5. **Sucesso parcial = enviado** — se texto foi mas vídeo falhou, lead conta como enviado. Wilson pode reenviar vídeo manualmente depois. Conforme escolha do usuário.

6. **Variação de mensagem virou prioridade** — Wilson enfatizou que tudo igual é detectável. Marquei como item 1.1 do roadmap (prioridade máxima).

---

## 📦 Arquitetura final do dia

```
USER clica "Iniciar envio" no foryou-leads.vercel.app/enviar
  ↓
API cria send_job em status=pending
  ↓ (poll a cada 5s)
Worker local (Node.js) pega job
  ↓
AdsPower API → abre profile k1cn2qmx
  ↓ (Playwright CDP)
Pra cada lead:
  - Navega pro perfil
  - Clica "Enviar mensagem" → mini chat
  - expandMiniChat (3 estratégias: DOM → header link → Vision)
  - findInput (scoring + Vision fallback)
  - typeHumanInPage (execCommand insertText, 45-140ms/char)
  - Enter
  - Espera 5s
  - attachVideo (setInputFiles ou HTTP local + DataTransfer)
  - clickSendButton (estrito + Vision fallback)
  - Verifica <video> na conversa
  - markLeadSent (status=enviado + snooze 3d)
  - Espera 3-8 min aleatórios
  ↓
Job marcado done. Worker volta a polar.
  ↓
USER vê progresso live no dashboard.
ManyChat webhook avisa quando lead responde → status auto vira respondeu/quente.
Telegram avisa Wilson.
```

---

## 🚨 Riscos remanescentes (vide roadmap)

1. **CTA hardcoded** = padrão detectável pelo IG
2. **Sem detecção de Action Blocked** → worker continua mandando após IG flag
3. **Sem warm-up** de conta antes do batch
4. **Mesmo vídeo sempre** → fingerprint
5. **Sem janela horária** → DMs às 3am
6. **Webhook ManyChat sem auth** → poluível
7. **Sem backup** do Neon
8. **CRON_SECRET único** → vazou, perdeu tudo
9. **Sem audit log** de status
10. **Sem rate limit** em endpoints
11. **`document.activeElement` no Vision fallback** pode ser body se IG defocus rápido

---

## ✏️ Próxima sessão deve atacar

Fase 1 do roadmap, em ordem:
1. **Variação de mensagem** (CTA + estrutura) — Claude gera mensagens diferentes baseadas em hash do username
2. **Detecção de bloqueio** do IG — pausa worker 24h se ver "Action Blocked"
3. **HMAC no webhook** ManyChat — segurança do dado
4. Rotação de vídeo, warm-up, janela horária, backup

---

## 🔗 Links

- [[Pipeline de Leads ForYou]] (nota mãe, atualizada hoje)
- [[ForYou Leads — Roadmap Pós-Auditoria]] (criada hoje)
- Plan file de trabalho: `C:\Users\ynwwi\.claude-nova\plans\eager-wondering-nygaard.md`
- App: foryou-leads.vercel.app

---

## 🧰 Stack consolidada após hoje

| Camada | Tech |
|--------|------|
| Frontend + API | Next.js 15 App Router |
| Hosting | Vercel (free) |
| Banco | Neon Postgres |
| IA | Claude Sonnet 4.6 + Vision |
| Scraping | Apify (2 tasks) |
| Browser local | AdsPower V2 (profile k1cn2qmx) |
| Automação | Playwright via CDP |
| Webhook resposta | ManyChat |
| Notificação | Telegram bot custom |
| Vídeos | Pasta local sincronizada |

---

## 📊 Métricas da sessão

- **Commits hoje**: ~25+ (sem contar)
- **Bugs corrigidos**: 9 marcantes
- **Features novas**: 12 (Vision fallback, biblioteca de vídeos, scoring inteligente, etc.)
- **Migrations rodadas**: 005, 006, 007, 008 (pelo usuário no Neon)
- **Custo Claude API**: estimado ~$2-3 hoje (várias iterações de teste)
- **Linhas de código tocadas**: provavelmente 3000+ entre adds/edits

---

## 💡 Coisas pra lembrar

- Worker tem `dump de estado` quando findInput falha — usar pra diagnosticar IG mudando UI
- `Page.setBypassCSP` + `Page.setInterceptFileChooserDialog` no startup → resolve CSP e File Explorer
- `text-is()` > `has-text()` sempre que possível pra seletores precisos no IG
- Migrações são MANUAIS no Neon hoje — Fase 2.5 do roadmap resolve isso
- ManyChat tem signature disponível no header que NÃO usamos — Fase 1.6

---

> Sessão fechada às ~22h com auditoria completa + notas atualizadas. Próxima sessão: implementar Fase 1.
