---
title: IA Concretize — Handoff Produção Meta e Entrega 2026-05-22
type: handoff-tecnico
project: Concretize / IA de Atendimento Rodrigo
date: '2026-05-22'
status: producao-meta-cloud-api-conectada-regras-entrega-publicadas
tags:
  - concretize
  - ia-atendimento
  - whatsapp
  - meta-cloud-api
  - vercel
  - frete
  - entrega
  - debug
  - handoff
---
# IA Concretize — Handoff Produção Meta e Entrega 2026-05-22

## Resumo executivo
Em 2026-05-22 a IA da Concretize saiu do estado de migração pendente e passou a operar em produção com WhatsApp Cloud API oficial da Meta.

Estado atual validado após deploy:
- Backend: `https://concretize-ia.vercel.app`
- Painel: `https://concretize-insight-hub.vercel.app`
- Provider ativo: `meta-whatsapp`
- WhatsApp: conectado
- Número conectado: `+55 34 9718-3001`
- Catálogo: 30 produtos, 30 com imagem
- IA principal e fallback: prontos
- Webhook: processando mensagens reais

O trabalho também corrigiu envio de imagem pela Meta, duplicidade de respostas, uso de histórico em follow-up e regras comerciais de entrega/frete.

## Segurança e secrets
Durante a sessão foram usados tokens técnicos de Vercel e Meta. Eles NÃO devem ser salvos em notas, código, commits ou logs permanentes.

Ação obrigatória depois:
- Revogar/rotacionar o token da Vercel usado na sessão.
- Revogar/rotacionar tokens temporários Meta colados durante a sessão.
- Manter na Vercel apenas envs criptografadas.
- Não registrar `META_WHATSAPP_TOKEN`, `META_APP_SECRET`, App Secret, tokens de System User ou tokens temporários no Obsidian.

## Identificadores operacionais conhecidos
IDs não secretos relevantes para retomada:
- App Meta: `IA CONCRETIZE`
- App ID: `1330367675744725`
- WABA real que estava sendo trabalhada no fluxo técnico: `1555241252688170`
- WABA/conta Concretize observada em diagnóstico anterior: `1002016869183160`
- Phone Number ID real validado na configuração de produção: `1159981177197401`
- Número real em produção: `+55 34 9718-3001`
- Nome de exibição: `Concretize Pré Moldados`
- Business/System User citado: `concretize_admin`
- ID do System User: `61589978737217`
- App/ativos com controle total: IA CONCRETIZE, WhatsApp ForYouCode, WhatsApp Concretize Pré Moldados, Test WhatsApp Business Account

Observação: houve confusão entre WABA sandbox/teste e WABA real. A retomada deve sempre validar no painel da Meta qual WABA está selecionada antes de trocar envs.

## Linha do tempo curta
1. Início: backend estava tecnicamente pronto, mas o WhatsApp aparecia `disconnected` pelo status público.
2. Foi confirmado que existiam dois caminhos no código: MegaAPI legado e Meta Cloud API oficial.
3. A Meta exigia resolver registro/controle do número real e conexão à Cloud API.
4. O número `+55 34 9718-3001` apareceu no Gerenciador do WhatsApp como `Concretize Pré Moldados`, primeiro com status offline/em análise.
5. Foi concluído o fluxo de registro do número real na Meta.
6. A produção foi atualizada para usar Meta Cloud API oficial.
7. O status público passou a confirmar `activeProvider: meta-whatsapp` e `officialCloudApiReady: true`.
8. Mensagens reais passaram a chegar no painel da Concretize.
9. Surgiram problemas reais de comportamento: imagem registrada no painel mas não entregue, respostas duplicadas, entrega para hoje mal formulada, IA perguntando cidade mesmo com rua informada e não aplicando regra de entrega.
10. Foram feitos fixes sistêmicos e publicados em produção.

## Estado atual do endpoint de status
Após o deploy final, `GET https://concretize-ia.vercel.app/api/status` retornou:
- `status: ok`
- `whatsapp.status: connected`
- `whatsapp.phone: +55 34 9718-3001`
- `whatsapp.activeProvider: meta-whatsapp`
- `whatsapp.officialCloudApiReady: true`
- `catalogMedia.ok: true`
- `catalogMedia.totalProducts: 30`
- `productsWithoutImage: []`
- `readiness.webhookCanProcess: true`
- `readiness.primaryAiReady: true`
- `readiness.fallbackAiReady: true`
- `readiness.aiCanProcessReplies: true`

## Problema 1 — WhatsApp/Meta não estava claro
Sintoma:
- O usuário queria colocar o número real da Concretize para rodar com API oficial.
- Havia dúvida se a IA rodaria dentro do WhatsApp Business App ou fora.
- Havia dúvida entre usar Cloud API oficial, coexistência ou conector por QR/MegaAPI.

Descoberta:
- A IA não roda dentro do app WhatsApp Business.
- A IA roda no backend `concretize-ia.vercel.app` e usa o WhatsApp como canal.
- Cloud API oficial normalmente exige que o número esteja registrado na plataforma; o atendimento manual precisa ser por painel/inbox, salvo coexistência oficial.
- Conector tipo MegaAPI permite manter o app no celular, mas é menos estável e estava desconectado.

Decisão:
- Usar API oficial Meta Cloud API para produção.
- Manter MegaAPI como fallback legado, sem remover agora.
- Controlar pelo painel/inbox, não depender do celular como operação principal.

## Problema 2 — Confusão entre WABA sandbox e WABA real
Sintoma:
- A tela API Setup mostrava o número sandbox `+1 555 632-3563`.
- O WABA `2013351966214745` era o sandbox/teste.
- O número brasileiro não aparecia no seletor da etapa de teste.

Descoberta:
- O número real da Concretize precisava estar registrado/conectado à Cloud API.
- O app e System User precisavam de acesso correto aos ativos.
- O fluxo `Adicionar novo número` era o caminho prático para levar o número real até verificação.
- O número real apareceu no Gerenciador do WhatsApp em `Phone numbers` como `Concretize Pré Moldados`.

Erro importante:
- Tentamos pensar em `vincular uma conta do WhatsApp Business` como se fosse o caminho principal, mas o caminho correto para esse caso era registrar/adicionar o número na conta do WhatsApp Business certa e concluir verificação.

Estado final:
- Número real conectado.
- Status no Gerenciador: conectado.
- Mensagens reais chegando no painel.

## Problema 3 — Token Vercel e CLI
Sintomas:
- Vercel CLI local antigo falhava com `The specified token is not valid`.
- Ao tentar usar token sem aspas no PowerShell, o shell interpretou o token como comando.
- `--token` sem valor gerou erro `ARG_MISSING_REQUIRED_LONGARG`.
- `npx vercel deploy --prod` com CLI antigo falhou dizendo que o endpoint exigia versão `47.2.2` ou posterior.
- `rtk npx vercel@latest` foi interpretado errado como script npm em um momento.

Como foi resolvido:
- Token foi definido corretamente no PowerShell com aspas.
- Para deploy final, funcionou usando `npx vercel@latest` dentro de wrapper PowerShell e `--token=...` no formato com `=`.
- Deploy final produziu:
  - deployment id: `dpl_Hr1EKVaMmN54i7uZci4hzdPKYMin`
  - URL de deploy: `https://concretize-fltaun1yc-ynwwilson-9617s-projects.vercel.app`
  - alias de produção: `https://concretize-ia.vercel.app`

Não salvar o token usado.

## Problema 4 — Imagem aparecia no painel, mas não chegava no WhatsApp
Sintoma:
- No painel apareceu:
  - `[Imagem enviada]: Cobogó 4 Pontas https://...webp`
- No WhatsApp real, a imagem não chegava.

Causa raiz:
- A Meta Cloud API recusava mídia `image/webp`.
- Logs indicavam erro Meta `131053: Media upload error: Unsupported Image mime type image/webp. Please use one of image/png, image/jpeg.`
- O painel registrava a intenção/registro de envio, mas a Meta não entregava a imagem por incompatibilidade de formato.

Correção:
- `lib/metaWhatsapp.ts` passou a normalizar URLs públicas WebP do Supabase Storage para endpoint renderizado compatível com Meta.
- URLs `/storage/v1/object/public/...webp` passaram a ser convertidas para `/storage/v1/render/image/public/...webp?width=1200&format=origin`, fazendo a resposta vir como JPEG.
- Testes adicionados em `tests/meta-whatsapp.test.js`.

Estado final:
- Envio de imagem pela Meta foi corrigido e validado em uso real depois da correção.

## Problema 5 — Respostas duplicadas
Sintoma:
- Cliente mandava várias mensagens seguidas.
- A IA respondia duas vezes com textos muito parecidos ou iguais.
- Exemplo observado:
  - `Boa, ja tenho aqui a entrega para Hoje...`
  - Depois repetia uma variação quase igual.

Causa raiz:
- O webhook recebia mensagens agrupadas/retry em janela curta.
- A fila/batch não esperava suficientemente quando chegavam mensagens consecutivas.
- Não havia supressão forte para resposta recente idêntica da IA.

Correção:
- `lib/redis.ts` adicionou mecanismo de espera da janela de batch e checagem de duplicidade recente.
- `api/webhook.ts` passou a aguardar a janela completa em retries e suprimir resposta de IA recente/duplicada.
- Testes adicionados em `tests/webhook-source.test.js`.

Resultado esperado:
- Quando o cliente dispara várias mensagens rápidas, a IA deve esperar o agrupamento e responder uma vez só com contexto completo.

## Problema 6 — Frase ruim sobre entrega para hoje
Sintoma:
- IA respondeu algo como:
  - `Boa, ja tenho aqui a entrega para Hoje...`
- Isso parecia confirmar disponibilidade imediata sem base real.

Causa raiz:
- O prompt/regra permitia linguagem que soava como promessa operacional.
- A IA precisava tratar urgência como possibilidade a confirmar, não como garantia.

Correção:
- `lib/replyGuardrails.ts` recebeu regra para bloquear/ajustar promessa insegura de entrega hoje.
- Prompts/contexto foram reforçados para dizer que entrega no mesmo dia depende de confirmação do responsável.
- Testes em `tests/reply-guardrails.test.js`.

Resultado esperado:
- A IA pode dizer que tenta verificar/confirmar, mas não pode prometer entrega hoje automaticamente.

## Problema 7 — Regras comerciais de entrega/frete não estavam no cérebro
Regras fornecidas pelo Wilson:
- Blocos e canaletas: taxa de R$ 70,00 para entrega dentro da cidade.
- Bloquetes e pavers: taxa de R$ 700,00 dentro da cidade até 50 metros; a partir de 100 metros o frete é grátis.
- Cobogós: taxa de entrega de R$ 70,00 até 15 cobogós; acima disso é grátis.
- Pisos de passeio: taxa de entrega de R$ 70,00 até 30 metros de pisos; acima disso é grátis.

Correção:
- `lib/replyRules.ts` recebeu regras determinísticas para frete local antes da IA generativa.
- `lib/ai.ts`, `lib/openai.ts`, `lib/context.ts`, `lib/brainConfig.ts`, `lib/rag.ts` receberam reforços para a IA respeitar essas regras no raciocínio.
- Testes criados em `tests/reply-rules.test.js`.

Resultado esperado:
- A IA deve aplicar a regra específica por categoria quando já há produto e quantidade.
- Quando a regra exige confirmação do responsável, a IA deve pedir o dado mínimo sem inventar prazo.

## Problema 8 — IA perguntou cidade mesmo com rua informada
Sintoma observado em print:
- Cliente disse: `Quanto fica aqui na artur magalhaes 1350 20 unidades do 4 pontas`
- Depois perguntou: `E quanto é a entrega?`
- IA respondeu pedindo cidade da obra, mesmo já tendo rua/endereço.
- Mais tarde, ao perguntar taxa, respondeu que dependia da distância e pediu cidade novamente.

Causa raiz:
- `resolveDirectReply()` olhava somente a mensagem atual.
- Quando a última mensagem era `E quanto é a entrega?`, a função não via o histórico com produto, quantidade e endereço.
- A detecção de grupo de frete dependia de termos explícitos como `cobogo`; se o cliente falava só `4 pontas`, a regra de frete não ligava isso ao produto do catálogo.
- O extrator de quantidade podia pegar o primeiro número da frase; em endereço, isso poderia confundir rua `1350` com quantidade se a quantidade viesse depois.

Correção publicada:
- `lib/aiRouter.ts` passou a montar contexto recente com as últimas mensagens e passar isso para `resolveDirectReply`.
- `lib/replyRules.ts` agora aceita `conversationContext` além da mensagem atual.
- O motor direto combina mensagem atual + histórico recente para resolver follow-up.
- A detecção local entende sinais como `aqui na`, `rua`, `avenida`, `bairro`, `Patos de Minas`, `dentro da cidade`.
- O parser de catálogo liga `4 pontas` a `Cobogó 4 Pontas` pelo contexto do catálogo.
- `extractQuantity()` passou a preferir quantidade com unidade (`unidades`, `m²`, `metros`, `peças`) antes de número solto.

Comportamento esperado agora:
- Se cliente disser `Quanto fica aqui na artur magalhaes 1350 20 unidades do 4 pontas`, a IA deve entender:
  - produto: `Cobogó 4 Pontas`
  - quantidade: `20 unidades`
  - total produto: `20 x R$ 43,00 = R$ 860,00`
  - endereço local informado: sim
  - entrega: grátis, porque cobogós acima de 15 têm frete grátis
- Se depois o cliente perguntar `E quanto é a entrega?`, a IA deve usar o histórico e não perguntar cidade de novo.

## Comportamento esperado para o caso do print
Entrada do cliente:
```text
Quanto fica aqui na artur magalhaes 1350 20 unidades do 4 pontas
E quanto é a entrega?
```

Resposta esperada após a correção:
```text
20 unidades do Cobogó 4 Pontas ficam R$ 860,00.

Para essa quantidade, a entrega dentro da cidade fica grátis.
```

A IA não deve:
- perguntar cidade se já recebeu rua/endereço local;
- dizer que depende da distância sem aplicar a regra conhecida;
- prometer entrega hoje sem confirmação;
- responder duas vezes a mesma coisa.

## Arquivos alterados no backend
Projeto: `C:\Users\ynwwi\Projects\concretize-ia-webhook`

Diff estatístico capturado antes do handoff:
```text
api/status.ts                  |  70 +++++++++++-----
api/webhook.ts                 |   9 +-
lib/ai.ts                      |   8 +-
lib/aiRouter.ts                |  12 ++-
lib/brainConfig.ts             |   6 +-
lib/context.ts                 |  10 +--
lib/leadMemory.ts              |   1 -
lib/metaWhatsapp.ts            |  26 +++++-
lib/openai.ts                  |   4 +-
lib/rag.ts                     |   4 +-
lib/redis.ts                   |  15 ++++
lib/replyGuardrails.ts         |  34 ++++++++
lib/replyRules.ts              | 185 ++++++++++++++++++++++++++++++++++++++++-
lib/supabase.ts                |   1 -
tests/meta-whatsapp.test.js    |  11 +++
tests/reply-guardrails.test.js |  20 +++++
tests/webhook-source.test.js   |  28 ++++++-
17 files changed, 396 insertions(+), 48 deletions(-)
```

Novo arquivo local observado:
- `tests/reply-rules.test.js`

## Detalhes técnicos das mudanças principais
### `api/status.ts`
- Status público passou a preferir Meta Cloud API quando configurada.
- Expõe `activeProvider`, `officialCloudApiReady` e readiness sem vazar secrets.

### `api/webhook.ts`
- Mensagens Meta e MegaAPI seguem o mesmo pipeline de IA, mas a resposta usa o provider correto.
- Adicionadas proteções de batching/retry/duplicidade.

### `lib/metaWhatsapp.ts`
- Adapter oficial Meta Cloud API.
- Envio de texto/mídia pela Cloud API.
- Normalização de imagem WebP Supabase para formato aceito pela Meta.
- Sanitização de status sem vazar token.

### `lib/replyRules.ts`
- Regras determinísticas de frete e orçamento.
- Interpretação de histórico recente.
- Match de produto do catálogo por tokens significativos, exemplo `4 pontas` -> `Cobogó 4 Pontas`.
- Quantidade com unidade tem prioridade sobre número solto.

### `lib/replyGuardrails.ts`
- Bloqueia promessa automática de entrega hoje.
- Corrige resposta para pedir confirmação operacional quando necessário.

### `lib/redis.ts`
- Suporte à drenagem da fila dentro da janela de batch.
- Supressão de resposta recente duplicada.

### `lib/leadMemory.ts` e `lib/supabase.ts`
- Removido uso de coluna inexistente `source` em inserts/updates de leads.

## Validações executadas
Antes do deploy final, foram executados:
- `rtk npm test -- tests/reply-rules.test.js`
- `rtk npm test -- tests/webhook-source.test.js`
- `rtk npm run build`

Resultado observado:
- Testes passaram.
- Build TypeScript passou.
- Deploy de produção passou.
- Status público confirmou Meta conectada.

Também havia validação anterior do backend:
- `npm test -- tests/webhook-source.test.js` rodou a suíte e passou com `169` testes.
- `npm run build` passou.

Após a última rodada, a suíte estava com aproximadamente `180` testes passando, conforme saída do runner durante o trabalho.

## Deploy final
Comando funcional usado na sessão foi via `npx vercel@latest deploy --prod` com token fornecido em tempo de execução.

Resultado:
- Deployment: `dpl_Hr1EKVaMmN54i7uZci4hzdPKYMin`
- URL: `https://concretize-fltaun1yc-ynwwilson-9617s-projects.vercel.app`
- Alias de produção: `https://concretize-ia.vercel.app`
- Build Vercel: `npm run build` / `tsc --noEmit`
- Estado: `READY`

## Painel da Concretize
Painel informado pelo Wilson:
- `https://concretize-insight-hub.vercel.app`
- Deploy também visto em Vercel como `concretize-insight-1qdqxge73-ynwwilson-9617s-projects.vercel.app`

Observação:
- As mensagens da Meta real já aparecem no painel.
- O painel registrava envio de imagem antes da correção, mas o WhatsApp não recebia devido ao mime WebP rejeitado pela Meta.

## Decisões operacionais importantes
- API oficial Meta é o caminho de produção.
- MegaAPI fica como fallback legado por enquanto.
- Não remover integração antiga sem nova etapa de estabilização.
- Atendimento manual deve acontecer pelo painel/inbox, não pelo WhatsApp Business App comum, salvo se coexistência oficial for confirmada.
- Para urgência de entrega no mesmo dia, IA não promete; confirma com responsável.
- Para frete local com regra conhecida, IA calcula e responde direto.
- Quando cliente fornece rua/local, isso conta como contexto de cidade/local e a IA não deve pedir cidade de novo.

## Próximos testes recomendados
Testar em conversa real no WhatsApp:

1. Produto + imagem:
```text
quero ver foto do cobogo 4 pontas
```
Esperado: imagem chega no WhatsApp, não só no painel.

2. Cobogó com frete grátis:
```text
Quanto fica aqui na artur magalhaes 1350 20 unidades do 4 pontas?
```
Esperado: total R$ 860,00 e entrega grátis.

3. Follow-up de entrega:
```text
E quanto é a entrega?
```
Esperado: usa histórico e diz que para 20 cobogós é grátis, sem perguntar cidade.

4. Cobogó com taxa:
```text
Preciso de 10 cobogós 4 pontas aqui na artur magalhaes 1350
```
Esperado: produto `10 x R$ 43,00 = R$ 430,00`; entrega R$ 70,00; total com entrega R$ 500,00 se a resposta somar tudo.

5. Blocos/canaletas:
Esperado: taxa R$ 70,00 dentro da cidade.

6. Bloquete/paver até 50m²:
Esperado: taxa R$ 700,00 dentro da cidade.

7. Bloquete/paver a partir de 100m²:
Esperado: frete grátis.

8. Piso passeio até 30m²:
Esperado: taxa R$ 70,00.

9. Piso passeio acima de 30m²:
Esperado: frete grátis.

10. Urgência:
```text
preciso pra hoje
```
Esperado: não prometer entrega hoje; pedir quantidade/dados se faltarem ou dizer que confirma com responsável.

## Riscos restantes
- Tokens usados em chat devem ser revogados/rotacionados.
- Algumas regras de frete dependem de interpretação de unidade: metros, m², unidades. Continuar testando frases reais.
- Se cliente não informar quantidade, a IA deve pedir quantidade antes de calcular entrega.
- Se cliente informar endereço fora da cidade, a regra local pode não se aplicar; nesse caso deve pedir confirmação/detalhe.
- O painel pode precisar de melhorias específicas para exibir erro real de mídia quando Meta rejeitar envio, embora o principal problema de WebP tenha sido corrigido.

## Estado para próxima sessão
Retomar daqui:
- Produção conectada via Meta oficial.
- Deploy final já publicado.
- Primeiro foco: testar as frases acima no WhatsApp real e observar se a IA aplica frete sem perguntar cidade.
- Se falhar, buscar logs Vercel do horário exato e comparar com `resolveDirectReply`/histórico recebido.
- Se funcionar, próximo passo é estabilizar operação, rotacionar tokens e decidir commit/PR/limpeza da árvore local.
