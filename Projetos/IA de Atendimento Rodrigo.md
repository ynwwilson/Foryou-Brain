---
title: IA de Atendimento Rodrigo
type: projeto
created: 2026-03-26T00:00:00.000Z
updated: '2026-04-18T00:00:00.000Z'
tags:
  - projeto
  - cliente
  - ia-atendimento
  - crm
  - whatsapp
  - chatwoot
  - megaapi
  - vendedor-3.0
status: quase-pronto-validacao-final
---

# IA de Atendimento — Rodrigo (Concretize Pré Moldados)

## Objetivo
IA de atendimento via WhatsApp com CRM integrado. Automação de atendimento qualificado, integração com Chatwoot e suporte 24/7.

## Cliente
- [[Rodrigo]]
- Empresa: Concretize Pré Moldados

---

## Status Técnico (15/04/2026) — estado atual real

| Item | Status | Detalhe |
|---|---|---|
| **Backend** | ✅ Online | https://concretize-ia.vercel.app — cérebro configurável, publicação e catálogo vivo ativos |
| **WhatsApp** | ✅ Conectado | Instância operacional e status ajustado para refletir prontidão real |
| **Supabase** | ✅ Atualizado | migration do cérebro da IA e catálogo vivo aplicada manualmente |
| **Frontend** | ✅ Online | https://concretize-insight-hub.vercel.app com `Catálogo Vivo`, `Cérebro da IA`, `Publicação` e `Status` |
| **Cérebro da IA** | ✅ Validado manualmente | rascunho, publicação e rollback funcionando |
| **Catálogo Vivo** | ✅ Validado manualmente | salvar e sincronizar produto funcionando |
| **Status operacional** | ✅ Corrigido | deixou de reportar degradação falsa |
| **Impacto de publicação** | ✅ Corrigido | agora usa diff real da mudança atual |
| **Observabilidade básica** | ✅ Fechada | `failed_messages` criada no Supabase, monitor UptimeRobot configurado e status básico operacional |
| **SSH no VPS** | ✅ Fechado | acesso por chave funcionando no Hostinger (`ssh -i ~/.ssh/hostinger_ed25519 root@76.13.166.51`) |
| **PDF** | 🟡 Pendente por decisão | continua como item a configurar no painel |
| **Teste real em conversa** | 🟡 Falta validar | último passo relevante para chamar de 100% |

## Onde paramos de verdade
- A arquitetura principal do painel da IA já está pronta e publicada.
- Quase tudo que foi definido sobre contexto, nome, regras, tom, guardrails, memória, handoff, imagem, links e catálogo já foi refletido no painel.
- As notas antigas que diziam que ainda faltava definir quase tudo do negócio ficaram desatualizadas.
- O que falta agora não é mais desenhar a estrutura principal; é validar a IA em conversa real e decidir a política final de PDF.

## Erros importantes encontrados nesta fase e já resolvidos
- telas pretas nas rotas novas do painel
- status operacional mostrando degradação falsa
- divergência de impacto entre `Cérebro da IA` e `Publicação`
- erro ao publicar depois de rollback por repetição de `version_number`
- cérebro em modo emergência: ambas as versões em `ai_brain_versions` tinham `is_current: false` (teste de rollback feito antes do code fix ser deployado) — corrigido via PATCH no Supabase em 15/04

## Como o Claude deve interpretar este projeto agora
- tratar o `concretize-insight-hub` como painel mestre real da IA da Concretize
- considerar que o cérebro configurável já existe e está funcional
- não voltar a tratar a parte principal de negócio como pendência ampla
- focar em validação final, refinamento fino e teste real da IA

## Pendências atuais reais (15/04/2026)
### O que ainda falta de verdade
- teste real final da IA em conversa de produção
- política final de PDF

### Itens técnicos já fechados nesta fase
- tabela `failed_messages` criada manualmente no Supabase SQL Editor
- SSH com chave no VPS Hostinger funcionando
- monitor HTTP do UptimeRobot criado/configurado para `https://concretize-ia.vercel.app/api/status`

### O que NÃO deve mais ser tratado como pendência principal
- calibração ampla de prompt/cérebro: já foi feita em grande parte e já está refletida no painel
- regras comerciais, guardrails, memória do lead, tom e boa parte do comportamento: já foram definidos e migrados para a central da IA
- criação da estrutura principal do cérebro/publicação/catálogo vivo: já foi implementada e validada manualmente

### Pendências técnicas antigas que já foram resolvidas nesta fase
- tabela `failed_messages` no Supabase
- SSH com chave no VPS Hostinger
- UptimeRobot monitorando `/api/status`

Esses itens não devem mais aparecer como pendência ativa do projeto.

## Status Técnico (13/04/2026)

| Item | Status | Detalhe |
|---|---|---|
| **Backend** | ✅ Online | https://concretize-ia.vercel.app — 61/61 testes locais passando |
| **WhatsApp** | ✅ Conectado | Instância `megastart-Mg0tnMyPBvv` em `apistart02.megaapi.com.br` |
| **Chatwoot** | ✅ Corrigido | DeviseTokenAuth com refresh automático via Redis continua no ar |
| **Supabase** | ✅ Funcional | `lead_memory` + RAG de produtos/FAQ já integrados ao backend |
| **Frontend** | ✅ Online | https://concretize-insight-hub.vercel.app |
| **IA ativa** | ⚠️ Verificar | Confirmar `is_active` no painel e envs novas da rota barata |
| **Roteamento de IA** | ✅ Implementado no código | Router já decide entre regra/cache/FAQ, `local_llm`, `remote_fallback` e `premium_exception` |
| **Migração off-Claude** | 🟡 Parcial | Resposta principal de texto já pode sair por Groq/Ollama; memória, análise, follow-up e visão ainda usam Claude |
| **Download de Mídia** | 🟡 Parcialmente corrigido | Pipeline e retries melhoraram; ainda precisa validar em produção com logs reais |

---

## Auditoria / Evolução (06/04/2026) — Vendedor 3.0 ✅
### Pontos Corrigidos & Implementados
1. **Toque Humano:** IA simula digitação com delays naturais.
2. **Redundância Total:** Fallback automático Claude → OpenAI.
3. **Fatiamento de Mensagens:** Até 3 balões curtos, sem textão.
4. **Mirroring:** IA replica tom do cliente.
5. **Banimento de Emojis:** 100% removido.
6. **Otimização de Custos:** Auditoria de CRM ignorada para msgs curtas (<15 chars).

---

## Sessão 08/04/2026 — O que foi feito, o que deu errado, onde paramos

### 1. Chatwoot — Erro 401 Recorrente ✅ CORRIGIDO

**Problema:** Chatwoot retornava 401 continuamente. A causa raiz era que a coluna `access_token` não existia na tabela `users` do Chatwoot (migration nunca rodou), então o `api_access_token` estava sempre nulo/inválido.

**Solução implementada (lib/chatwoot.ts — reescrito completo):**
- Removido uso de `api_access_token` (que dependia da coluna ausente)
- Implementado autenticação via DeviseTokenAuth: faz login com email/senha, cacheia os tokens `access-token + client + uid` no Redis com TTL de 23h
- Tokens rotativos: a cada resposta da API, os novos tokens são salvos no Redis automaticamente
- Em caso de 401: limpa cache, faz re-login, tenta uma vez mais
- Adicionadas env vars `CHATWOOT_EMAIL` e `CHATWOOT_PASSWORD` no Vercel

**Por que é estável:** Os tokens do DeviseTokenAuth rodam a cada request mas são rastreados e atualizados. Nunca mais vai expirar silenciosamente.

---

### 2. maxDuration Vercel ✅ CORRIGIDO
**Problema:** Webhook tinha `maxDuration: 30s` no vercel.json — insuficiente para o pipeline completo com delays de humanização (10s batch window + processamento de mídia + geração de resposta).

**Solução:** `api/webhook.ts` mudou para `maxDuration: 60`.

---

### 3. lead_memory — Tabela criada ✅ CORRIGIDO
**Migration aplicada via Supabase SQL Editor em 08/04/2026.** Sistema usa `lead_memory` dedicada.

---

### 4. Download de Mídia — BUG ENCONTRADO, FIX PARCIALMENTE DEPLOADO

#### Histórico do bug
A feature de áudio/imagem/PDF foi adicionada em commit `d7c0c75` ("Adicionados Superpoderes") mas **nunca funcionou em produção desde o primeiro deploy**.

#### Causa raiz identificada (4 bugs simultâneos em `lib/media.ts`)

O endpoint MegaAPI correto é:
```
POST https://{HOST}/rest/instance/downloadMediaMessage/{INSTANCE_KEY}
```

Corpo esperado pela API:
```json
{
  "messageKeys": {
    "url": "...",
    "mediaKey": "...",
    "directPath": "...",
    "mimetype": "...",
    "messageType": "image|audio|video|document"
  }
}
```

Resposta de sucesso:
```json
{ "error": false, "message": "...", "data": "base64string" }
```

Resposta de erro (HTTP 200 mesmo com erro):
```json
{ "error": true, "name": "...", "message": "...", "statusCode": 400 }
```

**Os 4 bugs que existiam antes:**
1. Body era plano `{ url, mediaKey, directPath, mimeType }` — faltava o wrapper `messageKeys`
2. Campo `mimeType` (camelCase) — API exige `mimetype` (lowercase)
3. Campo `messageType` obrigatório estava AUSENTE (precisa ser `"image"/"audio"/"video"/"document"`)
4. `responseType: 'arraybuffer'` — API retorna JSON com base64, não binário. `Buffer.from(res.data)` processava os bytes do JSON de erro como se fossem mídia

#### Fix aplicado — commit `5e3c00f` (deploado com sucesso)
```typescript
// ANTES (quebrado):
axios.post(url, { url, mediaKey, directPath, mimeType }, { responseType: 'arraybuffer' })
// Buffer.from(res.data) — processava bytes do JSON de erro

// DEPOIS (corrigido):
function mimeTypeToMessageType(mimeType: string): string {
  if (mimeType.startsWith('image/')) return 'image';
  if (mimeType.startsWith('audio/')) return 'audio';
  if (mimeType.startsWith('video/')) return 'video';
  return 'document';
}

axios.post(url, {
  messageKeys: {
    url: keys.url,
    mediaKey: keys.mediaKey,
    directPath: keys.directPath,
    mimetype: keys.mimeType,          // lowercase
    messageType: mimeTypeToMessageType(keys.mimeType),  // novo campo obrigatório
  }
})
// Buffer.from(res.data.data, 'base64') — extrai base64 da resposta JSON
```

#### Status após o fix: AINDA FALHANDO

O usuário testou (screenshot às 10:00 AM, deploy às 9:55 AM) e o áudio ainda retornou `[AUDIO_INDISPONIVEL]`. O fix está deploado mas ainda há um erro desconhecido.

#### Tentativas de diagnóstico
1. **Vercel CLI:** Não logado — sem acesso aos logs (`vercel whoami` falhou)
2. **Endpoint de diagnóstico `api/admin/test-media.ts`:** Criado mas o deploy `db583e1` FALHOU na Vercel por motivo desconhecido (build error não identificado). Arquivo removido.
3. **saveFailedMessage para Supabase:** Adicionado ao `processMedia` para capturar o erro real — mas a tabela `failed_messages` não existe no Supabase (RLS/tabela ausente)
4. **Supabase REST API com anon key:** Não tem permissão de leitura nas tabelas relevantes (RLS bloqueia)
5. **dev-browser para acessar Vercel dashboard:** Tentativas falharam (`newPage` não abre no Opera correto)

#### Estado atual do código (commit `de46655`, deploado com sucesso)
- `lib/media.ts`: Logs melhorados — captura `err.response?.data` (body completo do erro MegaAPI), `err.response?.status`, inclui tudo na mensagem de erro propagada
- `api/webhook.ts`: `processMedia` tenta salvar erro em `saveFailedMessage('_diag_media', ...)` — mas como a tabela não existe, falha silenciosamente

#### O que ainda NÃO sabemos
O erro real que a MegaAPI retorna quando tenta fazer o download. Pode ser:
- 401: token inválido para o endpoint `downloadMediaMessage` (token correto para `sendMessage` mas talvez diferente para download)
- 404: endpoint não existe nessa instância/plano
- 400: campo inválido (ex: `mimetype` com codec info como `audio/ogg; codecs=opus`)
- 500: erro no servidor MegaAPI

#### O que falta fazer (PRIORIDADE 1)
1. **Ver o erro real.** Opções:
   - Logar no Vercel CLI (`npx vercel login`) e rodar `npx vercel logs concretize-ia --follow` enquanto envia áudio
   - OU: O usuário abre Vercel dashboard → projeto concretize-ia → Functions → webhook → logs
   - OU: Criar tabela `failed_messages` no Supabase e retestar
   
2. **Depois de ver o erro:** Corrigir a causa raiz específica

---

## Infraestrutura

### Backend
- **Repo:** `ynwwilson/Concretize-IA` (branch main)
- **Deploy:** Vercel (auto-deploy em push para main)
- **URL:** https://concretize-ia.vercel.app
- **Env vars:** MEGAAPI_HOST, MEGAAPI_INSTANCE_KEY, MEGAAPI_TOKEN, CHATWOOT_URL, CHATWOOT_EMAIL, CHATWOOT_PASSWORD, CHATWOOT_ACCOUNT_ID, CHATWOOT_INBOX_ID, OPENAI_API_KEY, ANTHROPIC_API_KEY, UPSTASH_REDIS_REST_URL, UPSTASH_REDIS_REST_TOKEN, SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY
- **Instância MegaAPI:** `megastart-Mg0tnMyPBvv` em `apistart02.megaapi.com.br`

### Frontend (Central de Gestão)
- **Repo:** `ynwwilson/concretize-insight-hub` (branch main)
- **URL:** https://concretize-insight-hub.vercel.app
- **Login:** concretizepatos@gmail.com / Concretize123
- **Stack:** React + Vite + Tailwind + Shadcn

### Supabase
- **Projeto:** `wxjoezbysbtbotwjvaxl`
- **Tabelas:** conversations, messages, leads, ai_config, products, lead_memory, conversations_intelligence
- **Tabela `failed_messages`:** NÃO EXISTE (função `saveFailedMessage` falha silenciosamente)
- **Anon key:** `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind4am9lemJ5c2J0Ym90d2p2YXhsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxODA3NjIsImV4cCI6MjA5MDc1Njc2Mn0.Q9RugEf_RTyIIb75WFOJrBGs4CqDRHLQ58ZFWk5zbJ0`

### VPS (Chatwoot)
- **Host:** Hostinger Ubuntu 22.04
- **Acesso:** Terminal web Hostinger (SSH com chave não configurado ainda)
- **Docker:** containers `concretize-chatwoot-web-1`, `sidekiq-1`, `redis-1`, `db-1`
- **PostgreSQL:** user=chatwoot, pass=99511638Ab, db=chatwoot
- **URL Chatwoot:** https://aiagentconcretize.com.br
- **Login Chatwoot:** concretizepatos@gmail.com / Concretize2024!

### Redis (Upstash)
- BATCH_WINDOW = 10s, LOCK_TTL = 30s, QUEUE_TTL = 30s

---

## Commits desta sessão (08/04/2026)

| Commit | O que fez | Status |
|---|---|---|
| `5e3c00f` | Fix 4 bugs no downloadMedia MegaAPI | Deploado ✅ — mas mídia ainda falha |
| `db583e1` | Endpoint diagnóstico + log melhorado | Deploy FALHOU ❌ na Vercel |
| `de46655` | Log erro completo MegaAPI + remove test-media.ts | Deploado ✅ |

---

## Fluxo de Mídia (como funciona quando funciona)

1. WhatsApp → MegaAPI webhook → `parseWebhookEvent` extrai `mediaKeys` (`url, mediaKey, directPath, mimeType`)
2. `enqueueMessage` + `enqueueMediaKeys` → Redis (TTL 30s)
3. `waitUntil(processMessage(...))` inicia em background
4. `drainQueue` espera 10s (BATCH_WINDOW) para acumular mensagens consecutivas
5. `drainMediaQueue` pega as chaves de mídia do Redis
6. `processQueuedMedia` → `processMedia` → `downloadMedia(mediaKeys)`
7. `downloadMedia` chama `POST https://{HOST}/rest/instance/downloadMediaMessage/{INSTANCE_KEY}` com `{ messageKeys: { url, mediaKey, directPath, mimetype, messageType } }`
8. Resposta: `{ error: false, data: "base64..." }` → `Buffer.from(base64, 'base64')`
9. **Áudio:** Whisper transcreve → `[AUDIO TRANSCRITO]: texto` vai para o Claude
10. **Imagem:** base64 vai como bloco multimodal para o Claude
11. **PDF:** `pdf-parse` extrai texto → `[DOCUMENTO PDF]: texto` vai para o Claude

---

## Sessão 13/04/2026 — Onde paramos na troca do Claude

### O que o repositório mostra hoje
- Os commits `08bed92` e `5f5cd6e` adicionaram uma camada de roteamento de IA com caminho barato.
- O fluxo principal de resposta ao cliente agora passa por `routeAiReply`, que tenta nesta ordem: regra direta, cache Redis, FAQ RAG, LLM local (`Ollama`), fallback remoto barato (`Groq`) e só então exceção premium (`Claude`).
- Em outras palavras: a troca do Claude para outra IA já foi parcialmente implementada no código.

### Qual IA substituta entrou de fato no código
- A lembrança de "talvez era Gemini" nao bate com o estado atual do repositório.
- Nao existe integração `Gemini` implementada neste backend.
- O que foi implementado de verdade foi:
  - `Groq` como fallback remoto barato para respostas de texto
  - `Ollama` como opção local/primária de baixo custo, pensado para rodar fora da Vercel

### O que ainda continua no Claude
- Exceções premium da resposta principal
- Evolução da `lead_memory`
- Avaliação de intenção comercial
- Sugestão de follow-up
- Extração de contexto visual de imagens/comprovantes

### Conclusão prática
- A base para sair do Claude já existe e está verde nos testes.
- A troca total ainda nao aconteceu.
- O próximo passo operacional mais seguro é ativar `Groq` em produção para o caminho principal de texto e manter Claude só nas exceções premium.
- `Ollama` só faz sentido se houver endpoint acessível pela Vercel; `127.0.0.1` nao serve em produção.
- Se a meta continuar sendo `Gemini`, isso exigirá nova integração; hoje nao há código pronto para isso.

## Próximos Passos (em ordem de prioridade)

1. **URGENTE:** Ver o erro real do download de mídia
   - Opção A: abrir `npx vercel logs <deployment-url>` ao vivo enquanto um teste real de áudio/imagem é enviado
   - Opção B: Abrir Vercel dashboard (https://vercel.com/ynwwilson-9617s-projects/concretize-ia) → Functions → webhook → logs recentes
   - Opção C: Criar tabela `failed_messages` no Supabase SQL Editor e retestar

2. Consolidar a especificação operacional da nova arquitetura de IA:
   - `Gemini` como primário
   - `OpenAI` como fallback completo
   - mesmo contexto no fallback
   - `Claude` removido do runtime

3. Executar a migração total dos fluxos ainda híbridos:
   - memória do lead
   - análise de intenção
   - follow-up
   - mídia, visão e transcrição com blindagem completa

4. Criar tabela `failed_messages` no Supabase (a função já existe no código, só falta a tabela)

5. Configurar SSH com chave para o VPS Hostinger

6. Configurar UptimeRobot para monitorar https://concretize-ia.vercel.app/api/status

## Sessão 13/04/2026 — Continuação: decisão final da arquitetura de IA

### Decisão consolidada com o usuário
O objetivo final foi definido assim:
- `Gemini` deve ser a IA principal para tudo
- `OpenAI` deve ser o fallback completo
- `Claude` deve sair totalmente do runtime e idealmente do código útil
- o fallback deve preservar o mesmo contexto
- o cliente não pode sentir falha operacional

### Diagnóstico consolidado
A arquitetura não deve assumir que provedores multimodais nunca falham. Mesmo com Gemini e OpenAI, ainda existem riscos de timeout, rate limit, resposta malformada, falha temporária, payload inválido, arquivo corrompido, limite de tamanho, instabilidade de rede, erro de env e mudanças de comportamento do modelo.

### Princípio técnico aprovado
A blindagem correta deve ter:
- validação de entrada
- `Gemini` primário
- `OpenAI` fallback
- mesmo contexto para ambos
- guardrails fortes
- logs estruturados
- resposta operacional segura se ambos falharem

### Status da implementação hoje
O repositório está híbrido:
- Gemini já entrou na resposta principal
- OpenAI já existe em parte do fallback
- Claude ainda está presente em memória, análise e follow-up
- testes ainda refletem em partes a arquitetura anterior

### O que o usuário vai trazer na próxima sessão
O usuário vai retornar com material refinado para completar a especificação operacional da IA nos blocos:
- `PROMPT`
- `REGRAS COMERCIAIS`
- `GUARDRAILS`
- `MEMORIA DO LEAD`
- `PRODUTOS/RAG`

### Próximo passo exato quando a próxima sessão começar
1. receber os blocos refinados do usuário
2. consolidar a especificação final
3. iniciar a implementação completa da migração `Gemini + OpenAI fallback`

---

## 16/04/2026 — Incidente real em produção: roteamento, nomes e isolamento entre contatos

### O que deu errado de verdade
- O sistema foi tratado como \"100%\" cedo demais com base em testes de source/build, sem validação suficiente do fluxo real MegaAPI -> webhook -> Supabase -> Chatwoot -> WhatsApp.
- O parser do webhook aceitava `jid` do topo cedo demais; na MegaAPI o número real do lead pode vir em `key.remoteJid`. Isso fazia inbound colapsar para o número da própria instância/contato errado.
- Houve contaminação de nome do contato: o mesmo telefone podia ficar com nome antigo/incorreto no backend e no Chatwoot.
- O endpoint manual de envio (`api/send.ts`) usava `agent_name` como se fosse nome do cliente, o que contaminava memória e nome do contato.
- O painel e o WhatsApp mostraram sintomas diferentes do mesmo problema estrutural: identidade do lead (telefone + nome) não estava suficientemente blindada no pipeline.
- Em uso real apareceram sinais de mistura entre contatos e histórico, então a validação final anterior deve ser considerada insuficiente.

### O que foi corrigido nesta sessão
- Parser do webhook corrigido para priorizar `key.remoteJid` / `messageData.key.remoteJid` antes do `jid` do topo.
- Parser mantido por envelope coerente para não misturar `message`, `key` e `jid` de objetos diferentes.
- `contact_name` agora é atualizado quando chega um nome real novo para o mesmo telefone.
- Chatwoot agora também atualiza o nome do contato encontrado pelo mesmo telefone quando o nome real muda.
- `api/send.ts` deixou de usar `agent_name` como nome do cliente; agora usa o `contact_name` real da conversa.
- Feature nova entregue: pausa de automação por contato, com toggle individual e seleção em massa no painel.
- Migration do Supabase aplicada em produção: `automation_disabled` em `conversations` + índice por `contact_phone`.

### O que foi validado nesta sessão
- Backend: testes passaram `94/94` e `npm run build` limpo após os fixes finais.
- Frontend da pausa de automação: teste-source passou e build passou.
- Migration do Supabase executada manualmente no dashboard logado do Opera com retorno `Success. No rows returned`.
- Commits publicados:
  - `0ece857` — pausa de automação por contato
  - `054a4ee` — prioriza `remoteJid` do lead no webhook
  - `ccf7e16` — corrige contaminação de nome do contato
- Frontend publicado com seleção em massa / toggle de automação:
  - `44384f2`

### O que ainda NÃO pode ser tratado como 100% provado
- Ainda precisa de reteste real em produção com pelo menos:
  - 1 áudio do Eduardo
  - 1 áudio do Marco
  - 1 contato pessoal do próprio Rodrigo/José
- Se ainda houver erro após esses fixes, o próximo suspeito principal é o pareamento texto/mídia por lote no Redis/webhook.
- A qualidade semântica das respostas de áudio ainda pode precisar refinamento fino mesmo com o roteamento corrigido.

### Leitura correta do estado atual após 16/04/2026
- O sistema está mais correto do que estava antes, mas não deve ser chamado de \"100%\" sem a nova rodada de teste real.
- Os maiores erros desta fase foram de identidade do contato, não de infraestrutura principal.
- A próxima prioridade operacional é provar isolamento entre contatos em produção real.

## 17–18/04/2026 — Anti-invenção de produto, fluidez e handoff restrito

### Problema que motivou a sessão
Nos prints reais de conversa, a IA insistia em oferecer "Cobogó Éter" mesmo quando o cliente só tinha falado em "cobogó" genérico — produto que **não existe no catálogo**. Pior: se o cliente mudava de assunto, a IA teimava; se mencionava produto inexistente, a IA confirmava com "vou verificar". Handoff também estava largo demais (passava pro Rodrigo em qualquer dúvida).

### Causa raiz identificada
- O catálogo real do Supabase **nunca era injetado no prompt**. A função `getProducts()` existia mas não era chamada no caminho de produção; o brain só tinha "Cobogós" genérico no `identity`, sem nomes exatos. A IA inventava pra preencher a lacuna.
- `lib/brainConfig.ts` tinha literais "Eter do Muno" em 2 pontos (linhas 1393 e 1442) ancorando o modelo na hallucination.
- Pré-marker polluído no `ai_brain_versions` carregava regras antigas de versões anteriores do patch.
- A regra anti-invenção existia mas era específica pra Éter — não generalizava pra qualquer produto.
- Não havia guardrail determinístico: se o modelo inventava, passava direto.

### O que foi implementado

**Pipeline de catálogo**
- `lib/supabase.ts`: novo `getCatalogSnapshot()` retornando prompt rico (nome, dimensões, aplicações, argumentos, brain_context) agrupado por categoria, cache de 60s.
- `lib/aiRouter.ts`: catálogo injetado em **todo** request de IA.

**Validador determinístico (novo arquivo)**
- `lib/responseValidator.ts`: regex detecta menções a produtos, Levenshtein fuzzy match com tolerância de 1–2 chars (suporta transcrição tipo "Fenestraa" → "Fenestra").
- `generateWithValidation()` roda em cada provider: se inventa, refaz 1x com alerta corretivo; loga `double_miss` se falha de novo.
- `scanHistoryForInvalid()` varre assistente em turnos anteriores e injeta `[AVISO DE CONTEXTO]` quando detecta invenção passada — quebra ciclo de auto-reforço.
- `tests/response-validator.test.js`: 8 testes, todos verdes.

**Regras do brain (v10 publicada)**
- Literais "Eter do Muno" removidos de `lib/brainConfig.ts`.
- `POSTURA PARA PRODUTO FORA DO CATÁLOGO` genérica: qualquer produto ausente vira "esse a gente não trabalha, temos X/Y/Z, quer ver?".
- `REGRA DE FLUIDEZ DA CONVERSA`: segue última mensagem do lead, não insiste em assunto abandonado, volta quando o lead volta, espelha ritmo/tom/formato.
- `handoff` com **LISTA FECHADA** — passa pro Rodrigo **só** em:
  - desconto
  - fechamento
  - comprovante/pix/agendamento
  - orçamento total com frete
  - **NUNCA passa**: dúvida técnica, reclamação genérica, projeto grande sem sinal de fechamento, pedido de catálogo/foto/vídeo/link, cliente pedindo genericamente "falar com alguém", horário/localização.

**Robustez do roteador**
- `lib/ai.ts`: `isRetryableProviderError()` pula retry em 429/quota do Gemini — vai direto pro OpenAI fallback.
- `lib/aiRouter.ts`: length cap por sinal — ≤8 palavras → 2 blocos; ≤20 → 4 blocos; else sem cap. Evita textão em resposta a mensagem curta.

**Patch script**
- `scripts/patch-brain-config.mjs`: `LEGACY_PATCH_HEADERS` stripa conteúdo pré-marker poluído; `HANDOFF_RULES` aplicado em main (`ai_brain_versions`) e fallback (`analytics_v2`).
- Utilitários novos: `dump-brain-sections.mjs`, `dump-identity.mjs`, `dump-product-schema.mjs`, `hunt-eter.mjs` (confirmou que "Eter do Muno" nunca existiu no DB — era só hallucination do LLM), `verify-brain-config.mjs`.

### Deploy
- Commit `736613c` em main, push feito, Vercel auto-deploy.
- Brain v10 já estava publicada no Supabase (org `ccf52483-3e36-4a1d-8e7a-b2d9e107a36d`), `is_current=true`, com marker `__PATCH_V2__` em guardrails, tone_style, sales_rules e handoff.

### Validações
- `rtk npm test` → 114/114 passando.
- `rtk tsc --noEmit` → limpo.
- Verificação via dump confirmou que `handoff` tem o marker `__PATCH_V2__` seguido da LISTA FECHADA.

### Pendências pós-deploy
- **Monitorar logs** `[validator:invalid]` e `[validator:double_miss]` primeiras horas — se double_miss for frequente, ajustar prompt do retry.
- **Testar em conversa real** se a fluidez funciona (lead muda assunto → IA acompanha; lead volta → IA volta).
- **Reconectar WhatsApp** na MegaAPI (item operacional do Rodrigo).
- **Observar volume de 429 do Gemini** — se persistir, avaliar subir quota ou inverter ordem (OpenAI principal).
- **Dashboard de hoje** — item antigo ainda pendente.

### Leitura correta do estado atual após 18/04/2026
- A parte de **qualidade de resposta** avançou bastante: catálogo sempre presente, guardrail determinístico, regras de fluidez genéricas, handoff restrito ao que o Rodrigo realmente quer ver.
- A parte de **infra e identidade de contato** continua nos fixes do 16/04 (roteamento `remoteJid`, pausa por contato, contaminação de nome corrigida).
- Ainda precisa de validação em produção real — código está mais correto mas não "100% provado" até rodar com conversas vivas.

---

## Relacionado
- [[Rodrigo]]
- [[ForYou Code]]
- [[Guia de Clonagem IA de Atendimento]]
