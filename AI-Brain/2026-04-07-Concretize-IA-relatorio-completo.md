---
project: Concretize IA
date: '2026-04-07'
status: published-connected-status-fixed
tags:
  - concretize-ia
  - webhook
  - vercel
  - megaapi
  - chatwoot
  - codex-handoff
---
# Relatório completo - Concretize IA - 2026-04-07

## Resumo executivo

A estabilização principal foi concluída e publicada.

O webhook foi reescrito para resiliência, o dashboard foi corrigido para passar lint/build, o `CHATWOOT_TOKEN` foi atualizado no Vercel, os dois projetos foram publicados, e o bug do `/api/status` mostrando WhatsApp desconectado foi corrigido.

Estado final verificado:

- Webhook produção: `https://concretize-ia.vercel.app/api/status` retorna `status: ok` e `whatsapp.status: connected`.
- Dashboard produção: `https://concretize-insight-hub.vercel.app` retorna HTTP 200 e carrega a tela de login.
- Vercel production deployment do webhook está Ready.
- Vercel production deployment do dashboard está Ready.
- Git tracked limpo nos dois repositórios.
- Untracked preexistentes mantidos sem mexer no webhook: `docs/`, `old_vercel.json`, `tmp_check_db.js`.

## Regras operacionais confirmadas

- Sempre usar `rtk ` antes de comandos de terminal/shell.
- Sempre ler antes de agir: `AI-Brain/00-OVERVIEW.md`, `AI-Brain/01-STATUS.md`, `AI-Brain/02-REGRAS.md`.
- Atualizar AI-Brain após etapas importantes.
- Usar Opera como navegador padrão quando tecnicamente possível.
- Como o Opera já aberto não expunha CDP/DevBrowser, foi usada automação de UI do Windows sobre a janela Opera existente e logada.
- Não gravar credenciais sensíveis em claro nas notas. `CHATWOOT_TOKEN` foi atualizado no Vercel com o valor informado pelo usuário, mas não foi registrado aqui em texto claro.

## Repositórios envolvidos

- Webhook: `C:\Users\ynwwi\Projects\concretize-ia-webhook`
- Dashboard: `C:\Users\ynwwi\Projects\concretize-insight-hub`
- AI-Brain: `C:\Users\ynwwi\Projects\claude-novo\stark\Stark\AI-Brain\`

## Commits finais

Webhook:

- `cbe1591 fix(webhook): harden message processing`
- `1c5f634 fix(webhook): include resilience helpers`
- `c825692 fix(status): detect megaapi connection states`
- `d8cb801 fix(status): use megaapi instance endpoint`

Dashboard:

- `e934c51 fix(dashboard): clear blocking lint errors`

## O que foi mudado no webhook

Arquivo principal: `api/webhook.ts`

A reescrita incluiu:

- Parsing centralizado de evento de webhook.
- Aceite de payload MegaAPI top-level (`instance_key`) e payload de simulação `ReceivedCallback`.
- Deduplicação por `messageId` via Redis.
- Rate limit por telefone via Redis.
- Fila por telefone e lock por telefone.
- `releaseLock` garantido em `finally`.
- `sendPresence` protegido por `safeSendPresence` com `try/catch`.
- Chatwoot isolado em `try/catch`, sem derrubar o fluxo principal.
- Fallback Claude -> OpenAI -> mensagem de handoff humano.
- `saveFailedMessage` em falhas de envio/processamento.
- Tratamento de `fromMe` para registrar handoff humano e desativar IA na conversa se um humano responder pelo WhatsApp conectado.
- Resposta HTTP 200 mesmo em erro interno do webhook para evitar retries agressivos do provedor.
- Correção de `logObjection`: passou a usar `conversation.id`, não telefone.

Arquivos auxiliares do webhook:

- `lib/redis.ts`: adicionadas exports necessárias `isDuplicate` e `isRateLimited`.
- `lib/supabase.ts`: adicionada export `saveFailedMessage` e ajuste em `logObjection` para `conversationId`.
- `tests/webhook-source.test.js`: adicionado teste de regressão estrutural do webhook.
- `package.json`: adicionado script de teste.

Erro no caminho:

- Primeiro commit `cbe1591` não incluiu `lib/redis.ts` e `lib/supabase.ts` porque esses arquivos estavam modificados localmente e não foram adicionados no commit inicial.
- O build local passava porque a árvore local tinha os helpers, mas o Vercel compilou só o commit sem eles.
- Vercel falhou com `Build Failed`, comando `npm run build` saiu com código 2.
- Causa raiz: exports novas usadas por `api/webhook.ts` ainda não estavam no commit remoto.
- Correção: commit `1c5f634 fix(webhook): include resilience helpers` adicionou os helpers faltantes e o deploy seguinte ficou Ready.

## O que foi mudado no dashboard

Projeto: `concretize-insight-hub`

Correções:

- `src/components/ui/command.tsx`: corrigido erro de lint `no-empty-object-type` com type alias para props.
- `src/components/ui/textarea.tsx`: corrigido erro de lint `no-empty-object-type` com type alias para props.
- `src/pages/Inbox.tsx`: removido `as any` em insert de messages.
- `tailwind.config.ts`: trocado `require` por `import` para eliminar erro de lint.

Verificação do dashboard:

- `rtk npm test`: passou 1/1.
- `rtk npm run lint`: passou com 0 erros e 9 warnings conhecidos.
- `rtk npm run build`: passou; warnings restantes de Browserslist desatualizado e chunk maior que 500 kB.
- Produção: `https://concretize-insight-hub.vercel.app` retornou HTTP 200 e carregou tela de login.

Warnings conhecidos do dashboard:

- `react-refresh/only-export-components` em alguns componentes UI/contextos.
- `react-hooks/exhaustive-deps` em `SettingsPage.tsx` para dependência `fetchConfig`.
- Browserslist/caniuse-lite desatualizado.
- Chunk JS grande após minificação.

Esses warnings não bloquearam build nem deploy.

## Vercel e Opera

Situação inicial:

- Vercel CLI não tinha credenciais locais: `No existing credentials found`.
- `VERCEL_TOKEN` e `CHATWOOT_TOKEN` não existiam no ambiente local.
- DevBrowser abriu navegador gerenciado/isolado sem sessão Vercel.
- Usuário pediu explicitamente usar a única janela Opera já aberta e logada.

Solução:

- A janela Opera existente não expunha CDP/DevBrowser na porta 9222.
- Foi usada automação de UI do Windows com clique, clipboard, teclas e screenshots.
- Vercel Dashboard logado foi acessado pela janela Opera existente.
- `CHATWOOT_TOKEN` foi atualizado no projeto `concretize-ia` / webhook pelo formulário de Environment Variables da Vercel.
- Vercel confirmou: `Updated Environment Variable successfully`; novo deploy era necessário.
- Redeploy do webhook foi iniciado pelo botão `Redeploy` da UI.

Erro no caminho:

- O primeiro redeploy do webhook falhou com build remoto por causa dos helpers faltantes em `lib/redis.ts` e `lib/supabase.ts`.
- Após commit/push dos helpers, o deploy automático ficou Ready.

## Correção do status WhatsApp / MegaAPI

Problema observado:

- Mesmo após o usuário conectar o WhatsApp, `/api/status` retornava `whatsapp.status: disconnected`.
- Primeiro diagnóstico com `?debug=1` mostrou provider HTTP 404, `state: null`, `matchedInstance: null`.

Primeira melhoria:

- `api/status.ts` foi alterado para reconhecer vários formatos possíveis de estado: `open`, `connected`, `online`, `ready`, `authenticated`.
- Também passou a ler campos aninhados alternativos como `instance.status`, `connectionStatus`, `connection_state`, `connected === true`, etc.
- Adicionado debug sanitizado com `?debug=1`, sem expor token.
- Commit: `c825692 fix(status): detect megaapi connection states`.

Causa real final:

- O endpoint usado para consultar status da MegaAPI estava incorreto para este ambiente.
- Código antigo usava: `/rest/instance/fetchInstances/{instance_key}`.
- Esse endpoint retornava HTTP 404.
- O endpoint correto para a MegaAPI foi: `/rest/instance/{instance_key}`.

Correção final:

- `api/status.ts` agora consulta primeiro `https://${HOST}/rest/instance/${INSTANCE_KEY}`.
- Se receber 404, faz fallback para `https://${HOST}/rest/instance/fetchInstances/${INSTANCE_KEY}`.
- Commit: `d8cb801 fix(status): use megaapi instance endpoint`.

Resultado final:

- `/api/status?debug=1` retornou provider HTTP 200, `state: connected`, `matchedInstance: megastart-Mg0tnMyPBvv`.
- `/api/status` sem debug retornou `whatsapp.status: connected`.

Exemplo final verificado:

```json
{
  "status": "ok",
  "service": "Concretize IA Webhook",
  "whatsapp": {
    "status": "connected",
    "phone": null,
    "instance": "megastart-Mg0tnMyPBvv"
  }
}
```

Observação: `phone` ficou `null` porque a resposta da MegaAPI não trouxe número nos campos atualmente lidos, mas o estado conectado foi confirmado.

## Testes em produção sem mensagem externa

Testes básicos:

- `GET https://concretize-ia.vercel.app/api/webhook` -> HTTP 200 `{ ok: true }`.
- `POST https://concretize-ia.vercel.app/api/webhook` com `{}` -> HTTP 200 `{ ignored: true }`.
- `OPTIONS https://concretize-ia.vercel.app/api/status` -> HTTP 200.
- `GET https://concretize-ia.vercel.app/api/status` -> HTTP 200 e depois da correção retornou `connected`.
- `HEAD https://concretize-insight-hub.vercel.app` -> HTTP 200.

Simulações de webhook:

- Grupo simulado -> HTTP 200 `{ ignored: "group" }`.
- Mensagem `fromMe` simulada -> HTTP 200 `{ ok: true, queued: "fromMe" }`.
- Primeira mensagem com `messageId` -> HTTP 200 `{ ok: true }`.
- Segunda mensagem com mesmo `messageId` -> HTTP 200 `{ ignored: "duplicate" }`.
- Incoming `ReceivedCallback` simulado -> HTTP 200 `{ ok: true }`.
- Formato MegaAPI top-level simulado -> HTTP 200 `{ ok: true }`.

Erro no caminho:

- A primeira bateria simulada retornou `{ ok:false, error:"webhook_error" }`.
- Runtime Logs da Vercel mostraram `[webhook error] Invalid JSON`.
- Causa: arquivo temporário de payload foi gravado com BOM/encoding que o runtime não aceitava como JSON válido.
- Correção: gerar payload temporário UTF-8 sem BOM.
- Depois disso a simulação passou.

Logs observados depois da correção:

- Não apareceu novo `[webhook error]` visível na captura depois da simulação corrigida.
- Apareceram logs normais como `processMessage starting` para telefones falsos de teste.
- Apareceu `handoff AI disabled` em conversa fake criada por teste `fromMe`, esperado para o fluxo de handoff humano.

## Verificações finais executadas

Webhook:

- `rtk npm test` -> 4/4 testes passaram.
- `rtk npm run build` -> passou com `tsc --noEmit`.
- `rtk curl.exe -s https://concretize-ia.vercel.app/api/status` -> retornou `whatsapp.status: connected`.
- Git tracked limpo após commits.

Dashboard:

- `rtk npm test` -> 1/1 teste passou.
- `rtk npm run lint` -> 0 erros, 9 warnings conhecidos.
- `rtk npm run build` -> passou com warnings conhecidos.
- `rtk curl.exe -I https://concretize-insight-hub.vercel.app` -> HTTP 200.
- Git tracked limpo.

## O que ainda não foi testado por limitação real

Não foi possível testar entrega visual no WhatsApp sem uma mensagem real externa.

Ainda não foi provado por teste real:

- Se a MegaAPI entrega evento real ao webhook quando alguém manda mensagem.
- Se o payload real em produção vem exatamente em um dos formatos simulados.
- Se `sendText` entrega a resposta no WhatsApp conectado.
- Se a resposta da IA aparece no WhatsApp do contato externo.
- Se Chatwoot/Supabase/WhatsApp sincronizam de ponta a ponta com contato real.

## O que testar amanhã ou quando houver um segundo número

Sequência recomendada:

1. Conectar a instância `megastart-Mg0tnMyPBvv` na MegaAPI.
2. Abrir `https://concretize-ia.vercel.app/api/status`.
3. Confirmar `whatsapp.status: connected`.
4. De outro WhatsApp, enviar uma mensagem simples para o número conectado: `oi`.
5. Confirmar se a IA responde no WhatsApp.
6. Conferir no dashboard se a conversa apareceu.
7. Conferir no Chatwoot se a conversa sincronizou.
8. Enviar uma segunda mensagem rápida para observar fila/dedupe/rate limit sem travar.
9. Responder manualmente pelo WhatsApp conectado para confirmar que o handoff humano desativa a IA na conversa.
10. Ver Runtime Logs da Vercel para erros `sendText`, Supabase, Redis, Chatwoot, Claude/OpenAI ou MegaAPI.

## Sobre desconectar hoje

Pode desconectar sem desconfigurar o sistema.

Desconectar o WhatsApp só altera o estado da sessão na MegaAPI. Não desfaz:

- deploy da Vercel;
- variáveis de ambiente;
- atualização do `CHATWOOT_TOKEN`;
- webhook publicado;
- commits no GitHub;
- configuração do dashboard;
- correção do status MegaAPI.

Amanhã, ao reconectar a mesma instância `megastart-Mg0tnMyPBvv`, o `/api/status` deve voltar para `connected` após a MegaAPI atualizar o estado.

## Estado final para próximo agente

- Não reverter mudanças.
- Não commitar untracked preexistentes `docs/`, `old_vercel.json`, `tmp_check_db.js` sem revisar intenção do usuário.
- Para browser, usar Opera quando possível; se a janela existente não expuser CDP, usar UI automation com cuidado e screenshots.
- Vercel CLI local pode continuar sem credenciais; operar pela UI da Vercel no Opera se necessário.
- `CHATWOOT_TOKEN` já foi atualizado no Vercel com valor informado pelo usuário.
- Status WhatsApp foi corrigido e confirmado como `connected` no endpoint público após a correção.
