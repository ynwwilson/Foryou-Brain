---
title: IA de Atendimento Rodrigo
type: projeto
created: 2026-03-26T00:00:00.000Z
updated: '2026-05-28'
tags:
  - projeto
  - cliente
  - ia-atendimento
  - crm
  - whatsapp
  - chatwoot
  - meta-cloud-api
  - vendedor-3.1
  - concretize
  - midia
  - multimodal
  - media-understanding
  - prod2
  - arquivado
status: arquivado-sem-ia
---

# IA de Atendimento — Rodrigo (Concretize Pré Moldados)

## Status atual canônico - 28/05/2026
A IA da Concretize foi arquivada a pedido do Wilson. Rodrigo voltou para atendimento manual no WhatsApp Business padrão, sem agente de IA.

Fonte atual:
- [[IA Concretize - Arquivado 2026-05-28]]

Resumo: backend PROD2 preservado, histórico/banco/código não apagados, mas runtime em `ARCHIVE_MODE=1`. `/api/status?debug=1` retorna `status=archived`, `service=Rodrigo - arquivado`, telefone placeholder `+1 555 0100`, `activeProvider=archived`, `webhookCanProcess=false` e `aiCanProcessReplies=false`. Webhook Meta retorna `ignored=archived`. Env secrets antigas continuam guardadas no Vercel, mas não são usadas enquanto `ARCHIVE_MODE=1`.

Para reativar no futuro, não inventar: primeiro remover/desligar `ARCHIVE_MODE`, redeployar, validar status, e só então revisar Meta/WhatsApp/Chatwoot.

## Status anterior canônico - 27/05/2026
A fonte atual para retomada da IA da Concretize é:
- [[IA Concretize - Status Atual 2026-05-27]]
- [[IA Concretize - Pendencias e Proximos Passos 2026-05-27]]
- [[2026-05-27 23h46 - Concretize IA memoria completa midia painel e pendencias]]

Resumo: backend PROD2, painel PROD2, Meta WhatsApp Cloud API, mídia estruturada, painel mostrando entendimento/confiança/revisão humana e deploys validados. A próxima etapa real depende de testes WhatsApp com mídias reais e dataset/eval semântico.

As seções antigas abaixo ficam como histórico. Não usar URLs antigas como produção atual sem validar; a produção validada nesta rodada é `https://concretize-ia-prod2.vercel.app` e o painel PROD2 é `https://concretize-insight-hub-prod2.vercel.app`.

## Objetivo
IA de atendimento via WhatsApp com CRM integrado. Automação de atendimento qualificado, integração com Chatwoot e suporte 24/7.

## Cliente
- [[Rodrigo]]
- Empresa: Concretize Pré Moldados

---

## Status Técnico (25/05/2026) — PROD2 operacional validado

Fonte operacional mais recente:
- `C:\Users\ynwwi\Concretize IA\LATEST-STATUS.md`
- `C:\Users\ynwwi\Concretize IA\PRODUCTION-READINESS-AUDIT-2026-05-25.md`

| Item | Status | Detalhe |
|---|---|---|
| **Backend PROD2** | ✅ Operacional | `https://concretize-ia-prod2-yngomesmarco-hues-projects.vercel.app` retornando `/api/status` com `status=ok`. |
| **Painel PROD2** | ✅ Operacional | `https://concretize-insight-hub-prod2-yngomesmarco-hues-projects.vercel.app` abre com HTTP 200 e aponta para backend PROD2. |
| **Meta Cloud API** | ✅ Ativa | Webhook salvo na Meta em `/webhook/meta-whatsapp`; verify token corrigido e aceito. |
| **WhatsApp real** | ✅ Validado | Mensagem real enviada para o número da Concretize chegou via POST Meta e a IA respondeu no WhatsApp. |
| **Número conectado** | ✅ Conectado | `+55 34 9718-3001`, provider ativo `meta-whatsapp`. |
| **IA generativa** | ✅ Pronta | `primaryAiReady=true`, `fallbackAiReady=true`, `aiCanProcessReplies=true`. Gemini foi restaurado no PROD2; OpenAI deve continuar sendo monitorada por alertas anteriores de quota. |
| **Catálogo e mídia** | ✅ Completo | 30 produtos, 30 com imagem, `catalogMedia.ok=true`, nenhum produto sem imagem. |
| **Fotos por contexto** | ✅ Corrigido | Pedido "foto dos dois" agora prioriza produtos recém recomendados, como Infinity e Topázio, em vez de produto antigo do histórico. |
| **Cotação direta** | ✅ Corrigido | Regra de cotação não usa mais histórico antigo para responder pergunta aberta. Follow-up de frete/entrega continua usando contexto quando a pergunta atual exige. |
| **Painel visual** | ✅ Polido | Acentuação e labels administrativos corrigidos; console em produção sem erros/warnings na validação final. |
| **Repos GitHub** | ✅ Conectados | Backend `ynwwilson/Concretize-IA`; painel `ynwwilson/concretize-insight-hub`; deploys PROD2 validados via Git. |
| **Chatwoot** | 🟡 Monitorar | Teve alerta anterior de indisponibilidade/502; na janela final de validação não apareceu erro novo. |
| **Perfil comercial WhatsApp** | 🟡 Pendente manual | Falta preencher foto, descrição, endereço, email/site com dados oficiais. Não inventar dados. |
| **PDF** | 🟡 Pendente de decisão | Política final de PDF ainda precisa ser definida. |

### Confirmações finais de 25/05/2026
- Meta salvou e validou o webhook PROD2.
- `POST /webhook/meta-whatsapp` recebeu mensagem real com HTTP 200.
- IA respondeu no WhatsApp real.
- Painel PROD2 mostrou conversa de teste.
- Backend `/api/status` confirmou WhatsApp conectado, Cloud API pronta, IA apta a responder e catálogo com 30/30 imagens.
- Logs finais de 20 minutos: backend e painel sem erros/warnings.

### Commits relevantes desta retomada
- Backend `76ce193` — `fix: harden Meta production recovery`
- Backend `cc75041` — `chore: trigger prod2 git deployment`
- Backend `edd0915` — `fix: keep quote rules out of open advice`
- Backend `a713d65` — `fix: send recently recommended product photos`
- Painel `cdcf6ef` — `fix: point panel to prod2 backend`
- Painel `1b640fc` — `fix: configure Vercel Vite output`
- Painel `f1303fb` — `fix: polish production panel text`

### Onde paramos de verdade
A IA da Concretize voltou a operar no ambiente novo PROD2, com Meta Cloud API oficial, backend e painel publicados, repositórios conectados, catálogo com mídia completo e teste real de WhatsApp respondido.

O projeto não está mais no estado "pendente de subscribed_apps" nem "aguardando mensagem real". Isso ficou superado em 25/05/2026.

### Próximos passos corretos
1. Fazer mais testes reais no WhatsApp com perguntas abertas, objeções, preço, frete, fotos e troca de assunto.
2. Preencher o perfil comercial do WhatsApp somente com dados oficiais da Concretize.
3. Definir a política final de PDF.
4. Monitorar OpenAI/Chatwoot em janela maior.
5. Não trocar webhook, domínios, billing ou projetos antigos sem decisão separada.

### Incidente corrigido — resposta manual pelo painel não chegava no WhatsApp
Data/hora: 25/05/2026, 13h45 BRT.

Problema:
- Ao responder pelo Inbox do painel, a mensagem podia aparecer como resposta no painel, mas não chegar no WhatsApp real.
- Esse era um problema crítico porque o painel é o lugar principal de controle humano da operação.

Causa raiz:
- `api/send.ts` ainda enviava por `lib/megaapi.ts`.
- O ambiente PROD2 atual usa Meta Cloud API oficial (`activeProvider=meta-whatsapp`).
- Além disso, o painel mascarava falha: se `/api/send` retornasse erro, `Inbox.tsx` gravava a mensagem manualmente no Supabase como `agent`, dando falsa impressão de envio.
- O mesmo risco de provider errado existia em aprovação de follow-up e follow-up automático.

Correção aplicada:
- Criado `lib/whatsappOutbound.ts`, adaptador único de envio.
- Quando `META_WHATSAPP_TOKEN` e `META_PHONE_NUMBER_ID` estão configurados, o envio sai pela Meta Cloud API.
- Se Meta não estiver configurada, mantém MegaAPI como fallback legado.
- `api/send.ts`, `api/admin/approve-follow-up.ts` e `api/cron/follow-up.ts` passaram a usar o adaptador.
- `Inbox.tsx` não grava mais mensagem no Supabase quando o envio falha; agora mostra erro e mantém o texto para tentar de novo.

Commits:
- Backend `e0a67f8` — `fix: route manual sends through active WhatsApp provider`
- Painel `141815f` — `fix: stop masking failed inbox sends`

Validação:
- Backend: `rtk npm test` passou com 183/183; `rtk npm run build` passou.
- Painel: `rtk npm test` passou com 13/13; `rtk npm run build` passou; `rtk npm run lint` sem erros, apenas 8 warnings antigos de Fast Refresh.
- Deploy backend PROD2: `dpl_99Hpefn9GkV94u45F2wrRyuUgFNM`, status `READY`.
- Deploy painel PROD2: `dpl_EJjZWmBZKXz15jv345UqvZqAnd8U`, status `READY`.
- `/api/status` segue `status=ok`, `activeProvider=meta-whatsapp`, `officialCloudApiReady=true`, `aiCanProcessReplies=true`.

Próxima validação real:
- Responder pelo painel para um número de teste e confirmar no celular que a mensagem chegou.
- Se não chegar, pegar o horário exato e consultar logs do deployment `dpl_99Hpefn9GkV94u45F2wrRyuUgFNM`.

### Não fazer agora
- Não apagar projetos antigos.
- Não mexer no workspace antigo/billing sem plano separado.
- Não trocar novamente o webhook da Meta.
- Não remover MegaAPI ou Chatwoot sem auditoria de dependências.
- Não registrar tokens, chaves ou segredos nesta nota.

---

## Status Técnico (19/05/2026) — Migração Meta WhatsApp Cloud API

> Histórico superado pelo status de 25/05/2026. Esta seção deve ser lida como registro do caminho até o PROD2, não como estado atual.

Nota operacional completa: [[WhatsApp Cloud API — Migração Meta 2026-05-19]].

| Item | Status | Detalhe |
|---|---|---|
| **Backend Meta Cloud API** | ✅ Implementado | Novo conector `lib/metaWhatsapp.ts`, rota `/webhook/meta-whatsapp`, envio Cloud API e validação HMAC. |
| **Deploy Vercel** | ✅ Online | `https://concretize-ia.vercel.app`; GET verify retornou challenge corretamente. |
| **Webhook Meta - teste do painel** | ✅ Chegou | Meta enviou `POST /webhook/meta-whatsapp`, backend respondeu `200` e IA foi acionada. |
| **Webhook Meta - mensagem real** | 🔴 Não chegou ainda | Meta mostrou payload real do José, mas Vercel não recebeu novo POST correspondente. |
| **Causa provável atual** | 🟡 Meta/WABA | Falta assinar a WABA `2013351966214745` no App via `POST /{WABA_ID}/subscribed_apps` com token permanente. |
| **Envio Cloud API** | 🟡 Parcial | Token temporário causou 401 antes; teste fictício causou `#131030 recipient not in allowed list`. Precisa reteste com token permanente. |
| **Integração antiga MegaAPI** | ✅ Intacta | Mantida como fallback; não remover até a oficial estar provada. |
| **Número real Concretize** | ⏸️ Não migrar ainda | `+55 34 99718-3001` só deve entrar depois do teste completo com número de teste Meta. |

### Próximo passo exato
Criar token permanente de System User no Business Manager com `whatsapp_business_messaging` e `whatsapp_business_management`, assinar a WABA no App via `POST /v25.0/2013351966214745/subscribed_apps`, confirmar com `GET /subscribed_apps`, atualizar `META_WHATSAPP_TOKEN` na Vercel e redeploy.

### Alerta de segurança
Tokens e App Secret foram expostos no chat durante a operação. Não registrar valores. Rotacionar antes de produção real.

---

## Status Técnico (12/05/2026) — estado atual real

| Item | Status | Detalhe |
|---|---|---|
| **Backend** | ✅ Online | https://concretize-ia.vercel.app — commit `32899b7`, 161 testes |
| **WhatsApp** | 🔴 Desconectado | MegaAPI HTTP 404. Aguardando reconexão via QR (última decisão: fazer quando for testar de verdade) |
| **OpenAI** | ✅ Funcionando | Primário — gpt-4o-mini, ~1.5s de latência. Chave rotacionada em 12/05. |
| **Gemini** | ✅ Funcionando (fallback) | Invertido para fallback em 12/05. Chave nova mas free tier (20 req/dia) — insuficiente como primário. |
| **Supabase** | ✅ Completo | Todos os campos dos 30 produtos preenchidos (imagem, contexto, aplicações, embeddings) |
| **Catálogo** | ✅ Completo | 30/30 produtos com foto, aplicações, brain_context, sales_arguments, catalog_link_url. 150 embeddings. sync_status=synced. |
| **Imagens** | ✅ Upload feito | 28 imagens subidas do catalogoconcretize.vercel.app pra Supabase Storage. 30/30 com image_url. |
| **Brain v12** | ✅ Publicada | Persona Carlão, lista negra expandida, 12 few-shots, regra 1 pergunta/vez, fallback estruturado, zero markdown. |
| **Humanity Validator** | ✅ Ativo | lib/humanityValidator.ts detecta 7 categorias de vício (abertura-robô, fechamento corp, markdown, etc) com retry automático. |
| **Testes** | ✅ 161/161 | Inclui 21 novos testes de humanidade. |
| **Frontend** | ✅ Online | https://concretize-insight-hub.vercel.app — todos 30 produtos visíveis e sincronizados |
| **Redis** | ✅ | LOCK_TTL=60s (ajustado), QUEUE_TTL=180s, BATCH_WINDOW=10s |
| **Chatwoot (VPS)** | ✅ Online | Docker rodando em 76.13.166.51. Bug do PID órfão documentado (ver nota). |

### O único passo que falta pra testar de verdade
Reconectar o WhatsApp na MegaAPI (gerar QR, escanear no celular do Rodrigo). Depois disso, sistema está pronto para conversa real.

### Alertas
- **Gemini free tier:** chave nova é gratuita (limite 20 req/dia). Se quiser Gemini como primário futuramente, precisa upgrade pra paid no Google AI Studio.
- **ANTHROPIC_API_KEY:** ainda presente nas envs da Vercel (Production) mas Claude saiu do runtime. Candidata a remoção.

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
- **Login:** removido da nota; usar vault seguro.
- **Stack:** React + Vite + Tailwind + Shadcn

### Supabase
- **Projeto:** `wxjoezbysbtbotwjvaxl`
- **Tabelas:** conversations, messages, leads, ai_config, products, lead_memory, conversations_intelligence
- **Tabela `failed_messages`:** NÃO EXISTE (função `saveFailedMessage` falha silenciosamente)
- **Anon key:** `[REDACTED-JWT]`

### VPS (Chatwoot)
- **Host:** Hostinger Ubuntu 22.04
- **Acesso:** Terminal web Hostinger (SSH com chave não configurado ainda)
- **Docker:** containers `concretize-chatwoot-web-1`, `sidekiq-1`, `redis-1`, `db-1`
- **PostgreSQL:** user=chatwoot, pass=99511638Ab, db=chatwoot
- **URL Chatwoot:** https://aiagentconcretize.com.br
- **Login Chatwoot:** concretizepatos@gmail.com / [removido]

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

---

## 08–09/05/2026 — Codex: Guardrails determinísticos de mídia (PR #6)

### Problema que motivou a sessão
Diagnóstico revelou que a IA prometia enviar foto mas nunca enviava. Causa raiz: `products.image_url` existia mas o catálogo no prompt não incluía a URL; RAG ficava abaixo do threshold (0.65). IA inventava a promessa sem ter capacidade real de executá-la.

### O que foi implementado

**`lib/catalogMedia.ts` (300 linhas — novo):**
- Detecta intenção de mídia ("tem foto?", "manda imagem", "mostra", "tem vídeo?") **antes** da IA responder
- Consulta `products` direto (não depende de RAG/threshold)
- Se existe `image_url`: emite `[SEND_MEDIA: image, <url>]` na resposta — backend intercepta e envia pela MegaAPI antes da IA falar
- Se não existe: IA responde honestamente "não tenho foto cadastrada"

**`lib/replyGuardrails.ts` (guardrail inicial):**
- Bloqueia promessas vazias de mídia ("já vou te enviar" sem action executada)
- Detecta re-pergunta de qualificação quando cliente já deu a info

**`sql/products_catalog_runtime_columns.sql`:**
- Adiciona `image_url`, `video_url`, `document_url`, `catalog_link_url`, `use_image_when`, `use_video_when`, `use_link_when` em `products`

**`api/status?debug=1`:**
- Novo bloco `catalogMedia` mostrando produtos com/sem mídia cadastrada

### Bugs corrigidos 09/05 (pós-PR#6)
- `d289e96`: IA enviava foto E DEPOIS dizia "vou te enviar a foto" — bug de ordem/semântica
- `07605ba`: cliente dizia "20 unidades, rua X" e IA re-perguntava — `replyGuardrails.ts` expandido (+181 linhas), novo `lib/replyGuardrails.ts:repairRedundantQualificationAsk`

### Teste real confirmado
Usuário promoveu deploy manualmente na Vercel (CLI sem permissão de prod). Enviou "Tem foto do Cobogó 4 Pontas?" — sistema enviou a foto corretamente.

---

## 12/05/2026 — Sessão longa: catálogo completo, humanização Carlão, inversão de providers

### 1. Chaves de API rotacionadas
- `GEMINI_API_KEY`: chave anterior havia sido marcada como "leaked" pelo Google (403). Nova chave gerada em aistudio.google.com (free tier — atenção ao limite).
- `OPENAI_API_KEY`: 401 na chave anterior. Nova chave gerada em platform.openai.com.
- Ambas validadas com chamadas reais antes de publicar na Vercel. Deploy automático após `vercel env add`.

### 2. Catálogo completo — 30 produtos
Todos os 30 produtos foram preenchidos via script Supabase:

**Imagens (28 subidas):**
- Source: catalogoconcretize.vercel.app (SPA Lovable). JS bundle inspecionado pra extrair mapeamento `produto → arquivo hashed`
- Download dos assets e upload pra Supabase Storage em `product-media/<product_id>/<timestamp>-<slug>.png`
- `products.image_url` atualizado. Total: 30/30 com imagem (eram 2/30).

**Conteúdo (todos os 30):**
- `applications` (array): 4-5 usos por produto, específicos por categoria
- `brain_context` (texto): contexto comercial, quem compra, diferenciais
- `sales_arguments` (array): 4-5 argumentos por produto
- `catalog_link_url`: `https://catalogoconcretize.vercel.app/produto/<slug>`
- `use_image_when`: gatilho genérico — "Quando cliente pedir foto, imagem, 'mostra'..."
- `use_link_when`: gatilho genérico — "Quando cliente pedir catálogo, ver online..."

**Embeddings:**
- 150 linhas em `product_embeddings` (30 produtos × ~5 chunks cada)
- 14 FAQs reindexadas
- `sync_status=synced` em todos os 30

### 3. Humanização — persona Carlão (brain v12)

**Brain v12 publicada via `scripts/patch-brain-config.mjs`:**
- **QUEM É VOCÊ — CARLÃO DA CONCRETIZE:** atendente da Concretize, interior MG, direto, sem firula. Responde "aqui é o Carlão da Concretize" quando perguntam o nome. NUNCA se apresenta como IA/bot/assistente.
- **Lista negra expandida:** "Claro!", "Aqui está", "Se precisar me avise", "Estou à disposição", "Espero ter ajudado", "Para que eu possa", "Gostaria de auxiliar", "Em relação ao", e mais.
- **Regra de 1 pergunta por vez:** nunca 2-3 demandas numa só resposta.
- **Fórmula 5 passos:** reconhece → dado → 1 pergunta → próximo passo → fechamento curto.
- **Small talk só em bordas:** saudação, fechamento, transição — nunca no meio.
- **12 few-shot examples "RUIM vs BOM"** pra ancorar o tom.
- **Mirroring estrito:** IA só usa gíria se cliente usar primeiro. Cliente neutro → IA neutra.
- **Variação lexical:** mesma pergunta nunca tem mesma resposta literal.
- **Fallback estruturado:** mensagem vaga → chuta objetivo → 2 opções → pede detalhe. NUNCA "não entendi, tente novamente".
- **Zero markdown (reforçado):** sem `**`, `__`, blocos de código, listas com `-` ou `*`.

**`lib/humanityValidator.ts` (novo):**
- Detecta 7 categorias de vício: `abertura_robo`, `fechamento_corp`, `linguagem_corp`, `auto_apresentacao_ia`, `markdown`, `lista_com_marcador`, `multiplas_pergs`
- `buildHumanityCorrection()`: prompt de correção customizado por vício encontrado
- Integrado em `lib/aiRouter.ts:generateWithValidation` — combina checagem de invenção + humanidade em 1 único retry (não 2)
- Loga `[humanity:invalid]` e `[humanity:double_miss]` pra monitoramento

**`lib/replyGuardrails.ts:sanitizeCustomerReply`:**
- Expandido pra cortar: "Claro,", "Certo,", "Com certeza,", "Aqui estão", "Sim claro", "Eis"

### 4. Inversão de providers — OpenAI primário, Gemini fallback
**Motivação:** Gemini free tier (20 req/dia) estourava em qualquer uso real. OpenAI estava sendo usado como fallback 100% das vezes de qualquer jeito — com latência 12× maior pelo overhead do retry.

**4 lugares invertidos (mesmo padrão em todos — try OpenAI → catch Gemini):**
- `lib/ai.ts:generatePrimaryReply` — resposta principal ao cliente
- `lib/ai.ts:generateStructuredOutput` — lead memory, intent eval, follow-up
- `lib/media.ts:extractImageContext` — visão de imagens recebidas
- `api/webhook.ts:transcribeAudioWithFallback` — áudio do WhatsApp (Whisper já era padrão-ouro pra PT-BR)

**Resultado em produção:**
- OpenAI: 1.5s latência
- Gemini: 18.8s (throttled no free tier)

**CLAUDE.md atualizado** com a nova arquitetura.

### 5. Melhorias técnicas menores
- `LOCK_TTL`: 30s → 60s (alinhado com `maxDuration=60s` do webhook — lock não expira mais mid-processing)
- `QUEUE_TTL`: 90s → 180s (mantém 3× LOCK_TTL)
- `drainQueue` aceita `skipWait=true` no retry (pula os 10s redundantes pra segunda mensagem)
- `.gitignore` agora ignora `.env*.local`
- `scripts/reset-for-rodrigo.mjs`: script pra zerar dados de teste antes de entregar ao Rodrigo (Supabase + Redis + Chatwoot + MegaAPI logout). Tem `--dry-run` e exige "RESET" digitado.
- `tsx` adicionado como devDependency (permite `npx tsx scripts/*.ts` diretamente)
- Diagnóstico completo via `/api/status?debug=1` sem key em nota.

### Commits desta sessão (12/05/2026)
| Commit | O que fez |
|---|---|
| `3f59f2e` | Script reset-for-rodrigo + .gitignore |
| `4788c06` | Lock e retry de batching mais robustos |
| `83cf7ae` | tsx como devDependency |
| `5fa8c63` | Proíbe markdown na resposta — brain v11 |
| `28a5cdd` | Persona Carlão + humanity validator + brain v12 |
| `32899b7` | Inverte providers — OpenAI primário, Gemini fallback |

---

## Arquitetura de IA vigente (12/05/2026)

```
WhatsApp (MegaAPI)
    → webhook.ts
    → batching 10s (Redis LOCK_TTL=60s, QUEUE_TTL=180s)
    → processMessage
        → catalogMedia (detecta intenção de mídia ANTES da IA)
            → envia [SEND_MEDIA] se product.image_url presente
        → generateReply (lib/ai.ts)
            1. OpenAI gpt-4o-mini (primário, ~1.5s)
               └── retry 1× se transient error
               └── fallback Gemini 2.5 Flash-Lite se falhar
        → generateWithValidation (lib/aiRouter.ts)
            → validateResponse (anti-invenção, Levenshtein)
            → validateHumanity (anti-robô, 7 vícios)
            └── 1 retry combinado se qualquer validador falhar
        → prepareReplyForSending
            → sanitizeCustomerReply (remove markdown, aberturas-robô)
            → replyGuardrails (promessa vazia? re-pergunta?)
        → envio via MegaAPI
        → sync Chatwoot
```

**Brain v12 ativa** em `ai_brain_versions` (org `ccf52483-3e36-4a1d-8e7a-b2d9e107a36d`), `is_current=true`.

---

## Infraestrutura atual (12/05/2026)

### Backend
- **Repo:** `ynwwilson/Concretize-IA` (branch main, commit `32899b7`)
- **Deploy:** Vercel (auto-deploy em push para main)
- **URL:** https://concretize-ia.vercel.app
- **Diagnóstico:** `/api/status?debug=1` sem key em nota.
- **Instância MegaAPI:** `megastart-Mg0tnMyPBvv` em `apistart02.megaapi.com.br`
- **Env vars relevantes:**
  - `OPENAI_API_KEY` — primário (rotacionado 12/05)
  - `GEMINI_API_KEY` — fallback (rotacionado 12/05, free tier)
  - `ANTHROPIC_API_KEY` — presente mas Claude saiu do runtime (candidata a remoção)
  - `CRON_SECRET` — criado, protege endpoint de follow-up
  - `ADMIN_EMAIL=concretizepatos@gmail.com`

### Frontend (Central de Gestão)
- **Repo:** `ynwwilson/concretize-insight-hub` (branch main)
- **URL:** https://concretize-insight-hub.vercel.app
- **Login:** removido da nota; usar vault seguro.

### Supabase
- **Projeto:** `wxjoezbysbtbotwjvaxl`
- **Brain org:** `ccf52483-3e36-4a1d-8e7a-b2d9e107a36d`
- **Tabelas:** conversations, messages, leads, ai_config, products, lead_memory, failed_messages, media_contextos, product_embeddings, ai_brain_versions, ai_brain_drafts, analytics_v2
- **Bucket:** `product-media` (público) — 30 pastas com imagem de cada produto

### Redis (Upstash)
- `BATCH_WINDOW=10s`, `LOCK_TTL=60s`, `QUEUE_TTL=180s`, `DEDUP_TTL=60s`

### VPS (Chatwoot)
- **Host:** Hostinger Ubuntu 22.04, IP `76.13.166.51`
- **Acesso:** credencial removida da nota; usar vault seguro.
- **Docker:** `concretize-chatwoot-web-1`, `sidekiq-1`, `redis-1`, `db-1`
- **URL Chatwoot:** https://aiagentconcretize.com.br
- **Login:** removido da nota; usar vault seguro.
- **⚠️ Bug do PID órfão:** se Chatwoot der 502, rodar: `docker exec concretize-chatwoot-web-1 rm /app/tmp/pids/server.pid && docker restart concretize-chatwoot-web-1`

---

## Pendências pós 12/05/2026

### Única pendência para ir a ar
- [ ] **Reconectar WhatsApp** — gerar QR via painel MegaAPI ou `/api/status`, escanear no celular do Rodrigo.

### Para fazer após reconectar (por ordem)
- [ ] Rodar 5 mensagens de teste reais (pede preço, pede foto, curta, gíria, fora do catálogo)
- [ ] Monitorar logs Vercel por `[humanity:invalid]`, `[humanity:double_miss]`, `[validator:invalid]`
- [ ] Confirmar que foto chega quando cliente pede
- [ ] Upgrade chave Gemini pra paid tier se quiser voltar Gemini como primário
- [ ] Rodar `node scripts/reset-for-rodrigo.mjs --dry-run` e depois sem flag quando for entrega oficial ao Rodrigo

### Nice-to-have (ciclo de melhoria contínua)
- [ ] Ciclo semanal: converter 3 casos de `[humanity:double_miss]` em novos few-shot examples → brain v13+
- [ ] Subir fotos dos produtos pra ter vídeos (`video_url`) — zero vídeos hoje
- [ ] Documentar PDFs (`document_url`) — zero documentos hoje
- [ ] Substituir testes de string por testes de comportamento real (10 cenários priorizados)
- [ ] Upgrade Gemini pra paid se volume justificar

---

## Relacionado
- [[Rodrigo]]
- [[ForYou Code]]
- [[Guia de Clonagem IA de Atendimento]]

---

## Atualizacao - auditoria de falso sucesso no painel

Data/hora: 2026-05-25 14:10 BRT

Objetivo:
- Depois de corrigir a resposta manual do Inbox, auditei outras acoes do painel que poderiam mostrar sucesso sem confirmar persistencia/envio real.

Correcoes aplicadas no painel:
- Dashboard: limpar mensagem com falha agora so remove o alerta local depois de `DELETE /api/admin/failed-messages` responder OK; se falhar, mostra erro.
- Leads: notas, cerebro/memoria, status e criacao de lead agora checam erro de Supabase/backend antes de mostrar sucesso ou fechar o fluxo.
- Produtos: upload de imagem agora salva a URL no produto via `/api/admin/catalog-products`, recarrega a lista e sincroniza o catalogo usado pela IA antes de mostrar sucesso.
- Produto: mensagem de erro do upload ficou generica para cobrir falha no bucket ou na sincronizacao do catalogo.

Commit:
- Painel: `bac730b fix: prevent false success in panel actions`

Validacao:
- Painel `rtk npm test`: 16/16 passando.
- Painel `rtk npm run build`: passou.
- Painel `rtk npm run lint`: 0 erros; 8 warnings antigos de Fast Refresh.
- Painel `rtk git diff --check`: passou.
- Backend `rtk npm test`: 183/183 passando.
- Backend `rtk npm run build`: passou.
- Deploy painel PROD2 `concretize-insight-hub-prod2-34f4xna3v`: READY.
- Smoke HTTP do painel estavel: 200 OK.
- Smoke HTTP do deployment novo: 200 OK.
- `/api/status`: `status=ok`, `activeProvider=meta-whatsapp`, `officialCloudApiReady=true`, `catalogMedia.ok=true`, `aiCanProcessReplies=true`.

Proximos testes manuais recomendados:
- No painel, tentar salvar nota/status/memoria em um lead real e confirmar persistencia apos recarregar.
- Subir imagem em um produto de teste e confirmar que a IA usa a imagem nova quando o cliente pedir foto.

---

## Atualizacao - imagens recebidas renderizadas no painel

Data/hora: 2026-05-25 16:20 BRT

Problema:
- Fotos enviadas por clientes nao apareciam como imagem na conversa do painel.
- No PROD2 com Meta Cloud API, o webhook da Meta estava normalizando principalmente texto; imagem recebida via `messages[0].image.id` nao era baixada/persistida como midia do painel.
- O Inbox tambem renderizava `messages.content` como texto puro, entao URLs/marcadores de midia nao viravam imagem.

Correcoes:
- Backend agora aceita eventos de midia da Meta, baixa a midia via Graph API, salva preview publico no bucket `inbound-media` e grava a mensagem como `[Imagem recebida] + URL + legenda`.
- Backend nao ignora mais mensagem sem texto quando ela tem midia.
- Painel agora detecta mensagens de imagem e renderiza `<img>` real com link "Visualizar imagem".
- Adicionado script `scripts/backfill-inbound-image-previews.mjs` para tentar recuperar placeholders antigos via anexos do Chatwoot quando o Chatwoot estiver acessivel.

Commits:
- Backend: `17d4afe fix: persist inbound customer images`
- Painel: `e6eb643 fix: render inbound images in inbox`

Validacao:
- Backend `rtk npm test`: 185/185 passando.
- Backend `rtk npm run build`: passou.
- Painel `rtk npm test`: 17/17 passando.
- Painel `rtk npm run build`: passou.
- Painel `rtk npm run lint`: 0 erros; 8 warnings antigos de Fast Refresh.
- `rtk git diff --check`: passou nos dois repos.
- Deploy backend PROD2 `concretize-ia-prod2-8sofeplkq-yngomesmarco-hues-projects.vercel.app`: READY.
- Deploy painel PROD2 `concretize-insight-hub-prod2-6q7423bpk.vercel.app`: READY.
- Smoke painel estavel: HTTP 200.
- `/api/status`: `status=ok`, `activeProvider=meta-whatsapp`, `officialCloudApiReady=true`, `catalogMedia.ok=true`, `aiCanProcessReplies=true`.

Caso Fernanda Santos:
- Conversa localizada: `𝙁𝙚𝙧𝙣𝙖𝙣𝙙𝙖 𝙎𝙖𝙣𝙩𝙤𝙨`, telefone `553492051375`.
- No Supabase nao existe placeholder de imagem nem registro em `media_contextos` para essa foto antiga; existem apenas textos como "Vocês tem essa pedra pra vender ?" e "E esse ?".
- Isso indica que a foto antiga foi ignorada antes da correcao e nao foi arquivada no Supabase.
- Backfill por Chatwoot ficou bloqueado porque `https://aiagentconcretize.com.br` esta retornando `502 Bad Gateway` e SSH na VPS `76.13.166.51:22` deu timeout.

Proximo teste real:
- Pedir para um numero de teste enviar uma foto nova no WhatsApp e confirmar que ela aparece renderizada no painel.
- Para recuperar fotos antigas, primeiro restaurar o Chatwoot/VPS; depois rodar o backfill por anexos do Chatwoot.

---

## Atualizacao - alias curto do painel

Data/hora: 2026-05-25 16:33 BRT

Alias criado:
- `https://centralconcretize.vercel.app`

Destino:
- Deployment atual do painel `concretize-insight-hub-prod2-6q7423bpk.vercel.app`
- Projeto Vercel `concretize-insight-hub-prod2`
- Commit `e6eb643 fix: render inbound images in inbox`

Validacao:
- `GET/HEAD https://centralconcretize.vercel.app`: HTTP 200.
- HTML carregado com titulo `Concretize Command Center`.
- Nao houve alteracao no webhook da Meta nem no backend.

Observacao:
- Este alias aponta para o deployment atual do painel. Para tornar `centralconcretize.vercel.app` o dominio automatico de todos os proximos deploys, o caminho mais limpo e renomear o projeto Vercel do painel para `centralconcretize` ou configurar um dominio persistente no projeto.

---

## Atualizacao - retomada correta do backfill de imagens antigas

Data/hora: 2026-05-25 16:45 BRT

Correcao de contexto:
- A frente que ainda estava aberta nao era a URL curta; era o backfill das imagens antigas recebidas de clientes, principalmente o caso Fernanda Santos.

Estado verificado:
- Chatwoot voltou a responder: `https://aiagentconcretize.com.br` com HTTP 200.
- Painel curto segue online: `https://centralconcretize.vercel.app` com HTTP 200.
- Backend segue saudavel: `/api/status` com `status=ok`, `activeProvider=meta-whatsapp`, `officialCloudApiReady=true`, `catalogMedia.ok=true`, `aiCanProcessReplies=true`.

Backfill:
- Script `scripts/backfill-inbound-image-previews.mjs` foi corrigido para tentar `CHATWOOT_TOKEN` e, se receber 401, autenticar via `CHATWOOT_EMAIL`/`CHATWOOT_PASSWORD` com cache de headers.
- Commit backend: `7846ad0 fix: allow chatwoot login for image backfill`.

Caso Fernanda Santos:
- Supabase: sem placeholder de imagem e sem `media_contextos` para a foto antiga.
- Chatwoot: com servico online, nao foram encontrados contatos/anexos de imagem correspondentes aos telefones investigados.
- Conclusao atual: a foto antiga nao tem fonte recuperavel nos armazenamentos atuais. A correcao de midia vale para novas imagens recebidas daqui para frente.

Validacao:
- Backend `rtk npm test`: 185/185 passando.
- Backend `rtk npm run build`: passou.
- Backend `rtk git diff --check`: passou.

---

## Atualizacao - placeholder de imagem do painel recuperado

Data/hora: 2026-05-25 17:07 BRT

Problema observado:
- Uma foto nova enviada no WhatsApp apareceu no painel apenas como `[Imagem Recebida]`, sem renderizar a imagem.

Causa raiz:
- O backend salvava o preview no bucket `inbound-media`, mas a etapa seguinte de interpretacao da imagem pela IA ficava no mesmo bloco de erro.
- Se a interpretacao falhasse, o preview era descartado do fluxo de persistencia da mensagem e o painel recebia so o placeholder.

Correcoes:
- `api/webhook.ts`: preview da imagem agora e persistido e usado no painel mesmo se a IA falhar ao interpretar a foto.
- `scripts/backfill-inbound-image-previews.mjs`: backfill agora tambem recupera placeholders usando previews ja salvos no bucket `inbound-media`, sem depender do Chatwoot.
- Backfill executado no telefone `553491036586`: 1 placeholder atualizado; depois da execucao, placeholders pendentes nesse contato ficaram em 0.

Commit:
- Backend: `40f1613 fix: keep inbound image previews renderable`
- Deploy backend PROD2: `dpl_J3L62RqZip32GH2tJAy8fJoqDsWn`, status `READY`.

Validacao:
- Backend `rtk npm test`: 186/186 passando.
- Backend `rtk npm run build`: passou.
- Backend `rtk git diff --check`: passou.
- `/api/status`: `status=ok`, `activeProvider=meta-whatsapp`, `officialCloudApiReady=true`, `catalogMedia.ok=true`, `aiCanProcessReplies=true`.
- `https://centralconcretize.vercel.app`: HTTP 200.
- `https://aiagentconcretize.com.br`: HTTP 200.

Teste manual:
- Recarregar o painel e abrir a conversa `Jose Wilson`/`553491036586`; a bolha que era `[Imagem Recebida]` deve aparecer como imagem.
- Enviar outra foto nova pelo WhatsApp para confirmar o fluxo corrigido daqui para frente.

---

## Atualizacao - fotos de perfil e qualquer midia renderizavel no Inbox

Data/hora: 2026-05-25 17:30 BRT

Problema:
- O painel ainda dependia de iniciais para contatos, mesmo quando havia foto de perfil disponivel.
- O Inbox renderizava imagem, mas nao tratava audio, video, documento e link como anexos visuais.
- O backend persistia preview publico para imagem, mas audio/video/documento ficavam como transcricao ou placeholder sem URL renderizavel.

Correcoes:
- Backend: `api/admin/profile-picture.ts` criado para buscar foto de perfil por telefone com autenticacao admin.
- Backend: `getOrCreateConversation` tenta guardar `contact_avatar_url` quando a coluna existir, mas continua funcionando se a migration ainda nao estiver aplicada.
- Backend: midias recebidas agora usam `persistInboundMediaPreview` para imagem, audio, video e documentos suportados, salvando URL publica no bucket `inbound-media`.
- Painel: Inbox renderiza foto de perfil do contato com fallback para iniciais se a URL falhar.
- Painel: mensagens com marcador e URL agora renderizam como `<img>`, `<audio>`, `<video>`, card de documento ou card de link.
- Alias `centralconcretize.vercel.app` foi reapontado para o deploy novo do painel.

Commits:
- Backend: `416832b fix: persist inbound media and profile avatars`
- Painel: `e64711f fix: render avatars and media in inbox`

Validacao:
- Backend `rtk npm test`: 188/188 passando.
- Backend `rtk npm run build`: passou.
- Painel `rtk npm test`: 19/19 passando.
- Painel `rtk npm run build`: passou.
- Painel `rtk npm run lint`: 0 erros; 8 warnings antigos de Fast Refresh.
- `rtk git diff --check`: passou nos dois repos.
- Deploy backend PROD2 `dpl_CKEDQu8oJWpE48CgfeLbAUCMMohX`: READY.
- Deploy painel PROD2 `dpl_BSfhKveK5ZFnwuEQv1NYHk2qgQvP`: READY.
- `/api/status`: `status=ok`, `activeProvider=meta-whatsapp`, `officialCloudApiReady=true`, `catalogMedia.ok=true`, `aiCanProcessReplies=true`.
- `https://centralconcretize.vercel.app`: HTTP 200 apontando para o deploy novo.

Observacao:
- Migration criada: `supabase/migrations/20260525171500_add_conversation_contact_avatar_url.sql`.
- Ela ainda precisa ser aplicada quando o Supabase CLI estiver autenticado. O fluxo de producao nao depende dela, porque o painel busca avatar pelo endpoint admin quando a coluna nao existe ou vem vazia.

Teste manual recomendado:
- Dar refresh forte no painel e abrir o Atendimento.
- Enviar pelo WhatsApp uma foto, audio, video e PDF de teste; todos devem aparecer como anexo renderizado no Inbox.
- Conferir se contatos com foto publica no WhatsApp aparecem com foto; se um contato nao tiver foto publica ou o provedor nao retornar avatar, o painel mostra as iniciais.

---

## Atualizacao - pausa e reativacao da IA auditadas

Data/hora: 2026-05-25 17:55 BRT

O que foi verificado:
- Pausa global da IA: `ai_config.is_active=false` e o webhook para antes de gerar resposta, mas continua atualizando inteligencia do lead quando aplicavel.
- Pausa por contato: `automation_disabled=true` e o webhook bloqueia resposta antes de qualquer envio da IA.
- Assumir conversa: `status=pending` e `is_ai_handled=false`; o webhook nao responde enquanto estiver pendente.
- Resolver conversa: `status=resolved`; o webhook nao responde enquanto estiver resolvida.

Lacuna encontrada:
- Reativar uma conversa que estava pendente/assumida e tambem com `automation_disabled=true` podia limpar apenas parte do bloqueio, dependendo do botao usado.

Correcao:
- `return_to_ai` agora tambem limpa `automation_disabled=false`.
- `Ativar automacao` por contato/bulk agora tambem coloca conversas nao resolvidas em `status=open` e `is_ai_handled=true`.
- Conversas resolvidas nao sao reabertas automaticamente pelo bulk toggle.

Commit:
- Backend: `a9d08f5 fix: fully resume ai automation controls`

Validacao:
- Backend `rtk npm test`: 188/188 passando.
- Backend `rtk npm run build`: passou.
- Backend `rtk git diff --check`: passou.
- Deploy backend PROD2 `dpl_8pD739s1ejCtguShsiZpE4sWMCdV`: READY.
- `/api/status`: `status=ok`, `activeProvider=meta-whatsapp`, `officialCloudApiReady=true`, `catalogMedia.ok=true`, `aiCanProcessReplies=true`.

Conclusao:
- Pausar funciona e reativar volta ao caminho normal da IA para conversas nao resolvidas.
- Se a conversa estiver resolvida, ela continua resolvida por seguranca; para reabrir, usar o botao `IA`/retornar para IA na conversa.

---

## Atualizacao - auditoria de midia e resposta com anexos no painel

Data/hora: 2026-05-25 18:22 BRT

Problema encontrado:
- O Inbox ja conseguia enviar texto pelo painel, mas nao tinha botao/fluxo para o atendente enviar anexos nativos como no WhatsApp normal.
- Isso era uma lacuna funcional real: recebimento/renderizacao de imagem/audio/video/documento foi corrigido antes, mas resposta manual com anexo pelo painel ainda nao existia.

Correcoes:
- Backend: criado `api/send-media.ts`, com autenticacao admin, bucket publico `outbound-panel-media`, envio via provedor ativo do WhatsApp, persistencia em `messages` e sync basico com Chatwoot.
- Backend: `sendOutboundMediaUrl` e MegaAPI wrapper passaram a aceitar `audio`.
- Painel: Inbox ganhou botao de clipe para enviar imagem, audio, video, PDF, DOC e DOCX.
- Painel: o texto digitado no input vira legenda do anexo. Se o backend falhar, o painel mostra erro e nao salva sucesso falso.

Commits:
- Backend: `fe14e6c fix: allow panel media replies`
- Painel: `5124f29 fix: add inbox attachment replies`

Validacao:
- Backend `rtk npm test`: 189/189 passando.
- Backend `rtk npm run build`: passou.
- Backend `rtk git diff --check`: passou.
- Painel `rtk npm test`: 20/20 passando.
- Painel `rtk npm run build`: passou.
- Painel `rtk npm run lint`: 0 erros; 8 warnings antigos de Fast Refresh.
- Painel PROD2: deploy `concretize-insight-hub-prod2-lezf2bmok.vercel.app` ficou `READY`.
- Alias curto `https://centralconcretize.vercel.app` foi reapontado para `concretize-insight-hub-prod2-lezf2bmok.vercel.app`.
- `HEAD https://centralconcretize.vercel.app` e `HEAD https://concretize-insight-hub-prod2-lezf2bmok.vercel.app` retornaram HTTP 200 com o mesmo `Etag` e `Last-Modified`, confirmando que o alias curto esta no deploy novo.
- Backend PROD2: `/api/status` respondeu `status=ok`, `activeProvider=meta-whatsapp`, `officialCloudApiReady=true`, `catalogMedia.ok=true`, `aiCanProcessReplies=true`.
- Backend PROD2: `OPTIONS /api/send-media` respondeu HTTP 200; `GET /api/send-media` respondeu HTTP 401 por falta de autenticacao, esperado.

Caso Fernanda Santos:
- Supabase: sem placeholder, URL, media_contexto ou imagem arquivada para a foto antiga.
- Chatwoot: contato existe, mas a API retorna zero conversas para ele.
- Conclusao: aquela imagem antiga especifica nao e recuperavel pelo sistema; precisa ser reenviada pela cliente se ainda for necessaria.

Cobertura atual:
- Cliente -> painel: imagem, audio, video, PDF/documentos suportados renderizam como anexos quando a midia chega pelo provedor.
- Painel -> cliente: texto, imagem, audio, video, PDF, DOC e DOCX.
- IA/catalogo -> cliente: imagem/video/documento/link por `SEND_MEDIA` quando ha URL cadastrada.

Limites conhecidos:
- Midia antiga nunca salva no Supabase/Chatwoot nao pode ser reconstruida.
- Upload do painel usa base64 e limite logico de 20 MB; arquivos muito grandes podem bater em limite da plataforma antes disso.
- Ainda falta um teste manual real de envio de anexo pelo painel para confirmar entrega ponta a ponta na Meta.
