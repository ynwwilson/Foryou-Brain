---
date: '2026-05-27 23:46'
tool: codex
title: Concretize IA memoria completa midia painel e pendencias
model: openai
project: Concretize / IA de Atendimento Rodrigo
tags:
  - codex
  - sessão
  - concretize
  - ia-atendimento
  - midia
  - handoff
---
# Concretize IA memoria completa midia painel e pendencias

> Ferramenta: Codex
> Data: 2026-05-27 23:46 BRT
> Diretório inicial: `C:\Users\ynwwi`
> Repos trabalhados: backend `C:\Users\ynwwi\Projects\concretize-ia-webhook`; painel `C:\Users\ynwwi\Projects\concretize-insight-hub`.

## Pedido do Wilson
Wilson pediu para salvar absolutamente tudo no Obsidian: tudo que foi feito, o que aconteceu, cada passo, pendencias e estado final, criando/atualizando o que fosse preciso.

## Contexto da rodada
A conversa comecou com a pergunta sobre onde paramos na IA da Concretize e evoluiu para uma auditoria/fix de producao sobre midias no WhatsApp e no painel.

Problemas relatados por Wilson:
1. Audio nao tocava no painel.
2. PDF/documentos nao abriam/renderizavam como no WhatsApp.
3. Audio passou a tocar, mas uma fala simples com tres `oi` foi transcrita como repeticao enorme; transcricao alucinada.
4. Documento continuava sem abrir em um momento intermediario.
5. Depois audio e documento foram dados como funcionando.
6. Fotos de perfil dos contatos nao apareciam.
7. IA respondia muitas vezes com `tive uma instabilidade rapida aqui, pode me mandar novamente?`.
8. Quando recebia audio, video, documento ou imagem que nao entendia, a IA repetia `me fala qual produto/modelo voce quer ver`.
9. Wilson pediu opcao de excluir contato/conversa/memoria, como no WhatsApp.
10. Wilson perguntou se a IA agora entendia perfeitamente midias; resposta honesta: nao existe perfeicao absoluta, mas da para melhorar ate o limite pragmatico.
11. Wilson pediu para fazer o que fosse preciso para chegar perto da perfeicao.
12. Wilson perguntou se faltava algo; foram listados teste real WhatsApp, URL/config, painel com status, dataset/evals e fila assincrona.
13. Wilson respondeu `entao faca`; foi executado o que era possivel sem depender de novo envio manual.

## Passos executados antes do ultimo bloco
### 1. Exclusao de contato
Foi implementada opcao destrutiva no painel para excluir contato/conversa/memoria.

Commit painel:
- `f465395 feat: add destructive contact delete`

Validacoes registradas:
- Backend `node --test tests/webhook-source.test.js tests/catalog-media.test.js`: 121/121.
- Backend `npm test`: 193/193.
- Backend `npm run build`: passou.
- Painel teste direcionado: 16/16.
- Painel suite: 21/21.
- Painel build: passou.
- Deploy backend: `dpl_A7GxzvxaZQYQpsj99AiskfA3jm6u`, `READY`.
- Deploy painel: `dpl_FXnwTHs9eHPvTet8mzYqQDg7PCzr`, `READY`.

Risco documentado:
- Exclusao e destrutiva por telefone; remove conversas, mensagens, memoria, lead e relacionados. Se cliente mandar mensagem de novo, nova conversa sera criada.

### 2. Hotfix de loops de falha de midia
Problema:
- IA ainda podia repetir instabilidade, pedir reenvio ou perguntar produto/modelo quando midia falhava.

Causa raiz:
- Guardrail final substituia algumas saidas ruins por outra pergunta generica.
- Texto deitico com marcador de midia indisponivel ainda era tratado como suficiente para resposta.
- Prompt continha frase literal proibida de instabilidade, podendo contaminar saida.

Correcoes:
- `lib/replyGuardrails.ts`: suprimiu frases publicas de instabilidade/reenvio; promessa vazia de midia sem acao deixou de virar pergunta generica.
- `api/webhook.ts`: detecta referencias fracas a midia (`esse`, `essa`, `isso`, `quanto fica esse`, `foto`, `imagem`, `documento`, etc.).
- Se ha midia indisponivel e o texto depende dela, conversa vai para humano sem resposta automatica.
- Se ha texto concreto independente, IA pode responder ao texto.
- `lib/ai.ts`, `lib/openai.ts`, `lib/brainConfig.ts`: prompt deixou de pedir reenvio em loop.

Commit backend:
- `a468eef fix: stop media failure reply loops`

Validacao:
- Backend testes direcionados/suite: 194/194.
- Backend build: passou.
- Deploy: `dpl_BPURE2hHeUL17VvHcxCC7pf89xaU`, `READY`.
- `/api/status`: ok, WhatsApp conectado, `activeProvider=meta-whatsapp`, `officialCloudApiReady=true`, `aiCanProcessReplies=true`.

### 3. Melhoria multimodal
Objetivo:
- Aumentar entendimento automatico de imagem, audio, video, PDF e DOCX sem deixar a IA inventar.

Correcoes:
- PDF: continua usando `pdf-parse`; se nao extrai texto, tenta Gemini visual para PDF escaneado.
- DOCX: adicionada dependencia `mammoth`; DOCX entra como `[DOCUMENTO DOCX]`.
- Video: tenta contexto visual/audiovisual pelo Gemini e transcricao de audio.
- Prompts passam a reconhecer `CONTEXTO DO VIDEO` e `DOCUMENTO DOCX`.
- `/api/status?debug=1` declara `supportedInputs` incluindo `scanned-pdf` e `docx`.

Commit backend:
- `8ea7edb feat: improve multimodal media understanding`

Validacao:
- Backend `npm test`: 195/195.
- Backend `npm run build`: passou.
- Deploy: `dpl_EKe7aBQNiJbTzeUsKheypR45Y1Mf`, `READY`.

### 4. Hardening de audio e midia indisponivel
Objetivo:
- Melhorar audio e reduzir loops/respostas ruins.

Correcoes:
- `lib/openai.ts`: transcricao de `whisper-1` para `OPENAI_TRANSCRIPTION_MODEL || gpt-4o-transcribe`.
- Adicionado prompt de transcricao com vocabulario Concretize: cobogo, paver/peyver, bloquete, bloco, canaleta, mourao, Patos de Minas, Artur Magalhaes, medidas, valores e entrega.
- `api/webhook.ts`: `getReplyableProcessedMessages`.
- Midia indisponivel + texto concreto: IA recebe apenas texto concreto.
- Midia indisponivel + pergunta deitica: humano/pendente, sem automatico.
- Marcadores internos deixaram de pedir para cliente reenviar.
- `api/status.ts`: debug exibe provider de transcricao.

Commits backend:
- `138cd3b fix: harden media reply understanding`
- `77c2720 chore: report transcription provider status`

Validacao:
- Backend `npm test`: 196/196.
- Backend build: passou.
- Deploy final: `dpl_BJZZUXkU3Y5hMBqNGVeEDDCtv4mY`, `READY`.
- `/api/status?debug=1`: `transcriptionProvider.primary=gpt-4o-transcribe`, fallback Gemini, prompt de dominio habilitado.

### 5. Contrato estruturado de entendimento de midia
Objetivo:
- Cada midia recebida ter status/confianca/acao antes de a IA responder.

Correcoes:
- Criado `lib/mediaUnderstanding.ts`.
- Contrato `MediaUnderstanding`: `kind`, `status`, `confidence`, `action`, `summary`, `evidence`, `extractedText`, `provider`, `failureReason`.
- `status`: `understood`, `unavailable`, `unsupported`.
- `confidence`: `high`, `medium`, `low`, `none`.
- `action`: `reply`, `reply_text_only`, `human_review`.
- `api/webhook.ts`: persiste entendimento em `media_contextos`.
- Audio transcrito: `understood/high/reply`.
- PDF/DOCX lido: `understood/medium/reply`.
- Video com audio+visual: `high`; com apenas um caminho: `medium`.
- Falha real: `unavailable/none/human_review`.
- Documento nao suportado: `unsupported/none/human_review`.
- Evals: `scripts/evals/media-understanding-cases.json` e `npm run eval:media`.

Commit backend:
- `20e4db2 feat: add structured media understanding`

Validacao:
- `npm run eval:media`: 6 casos validos.
- `npm run build`: passou.
- `npm test`: 199/199.
- Deploy: `dpl_giAtotyST5DrjgwZvp51k5ZKS1nq`, `READY`.
- API PROD2 debug: ok, WhatsApp conectado, supportedInputs confirmados.

Observacao importante:
- URL antiga `https://concretize-ia.vercel.app/api/status` retornou bloqueio por pagamento. Producao validada passou a ser `https://concretize-ia-prod2.vercel.app`.

## Ultimo bloco executado apos `entao faca`
### Objetivo
Resolver o que ainda era acionavel sem depender de um novo teste manual no WhatsApp:
- verificar producao/configuracoes;
- mostrar no painel status/confianca/acao da midia;
- criar endpoint admin de leitura de entendimento;
- corrigir URL canonica;
- validar, commitar, pushar e confirmar deploy.

### 1. Checagem de estado inicial
Backend estava limpo em `main...origin/main`.
Painel estava limpo em `main...origin/main`.

### 2. Busca de referencias antigas
Encontrada referencia antiga no backend em `scripts/reset-for-rodrigo.mjs`, apontando para URL antiga bloqueada.
Foi alterada para `https://concretize-ia-prod2.vercel.app/api/status` sem query key local.

No painel, `src/lib/backendApi.ts` tinha fallback antigo/de deployment especifico.
Foi alterado para `https://concretize-ia-prod2.vercel.app`.

### 3. TDD backend
Teste novo em `tests/webhook-source.test.js` verificou que existe endpoint admin de media-understanding com:
- `requireAdminUser`;
- `conversation_id`;
- `contact_phone`;
- leitura de `media_contextos`;
- normalizacao de linha;
- `humanReviewRequired`;
- `items` e `summary`.

O teste falhou inicialmente porque `api/admin/media-understanding.ts` ainda nao existia. Esse foi o RED do TDD.

### 4. TDD painel
Teste novo em `src/test/leadMemorySource.test.ts` verificou:
- fallback canonico `https://concretize-ia-prod2.vercel.app`;
- existencia de `MediaUnderstandingItem`;
- chamada `fetchMediaUnderstanding`;
- endpoint `/api/admin/media-understanding`;
- textos `Midia analisada`, `Revisao humana`;
- uso de `humanReviewRequired`.

O teste falhou inicialmente porque o painel ainda nao tinha a faixa de entendimento. Esse foi o RED do TDD.

### 5. Implementacao backend
Arquivo novo:
- `api/admin/media-understanding.ts`

O endpoint:
- aceita `GET` e `OPTIONS`;
- exige admin via `requireAdminUser`;
- aceita `phone` ou `conversation_id`;
- se recebe `conversation_id`, busca `contact_phone` em `conversations`;
- consulta `media_contextos` por telefone;
- normaliza cada registro para o contrato usado pelo painel;
- retorna `{ phone, summary, items }`;
- `summary` conta `total`, `understood`, `unavailable`, `unsupported`, `humanReviewRequired`.

### 6. Implementacao painel
Arquivo alterado:
- `src/pages/Inbox.tsx`

Adicoes:
- interfaces `MediaUnderstandingItem`, `MediaUnderstandingSummary`, `MediaUnderstandingState`;
- helper de label por status/confianca/tipo;
- componente `MediaUnderstandingPanel`;
- estado `mediaUnderstanding` e `loadingMediaUnderstanding`;
- funcao `fetchMediaUnderstanding(convId)`;
- chamada ao abrir conversa;
- chamada apos nova mensagem via realtime;
- renderizacao da faixa logo abaixo do header da conversa.

Textos da UI:
- `Midia analisada`
- `IA liberada`
- `Revisao humana`

### 7. Configuracao local corrigida
Painel:
- `.vercel/project.json` local foi alterado para o projeto `concretize-insight-hub-prod2`.

Motivo:
- O repo deploya em dois projetos Vercel; o `prod2` e o alvo operacional atual.
- Isso evita que um deploy manual local mire o projeto antigo.

### 8. Validacoes antes de commit
Backend:
- `rtk npm test -- tests/webhook-source.test.js`: passou, suite total 200/200.

Painel:
- `rtk npm test -- src/test/leadMemorySource.test.ts`: passou, 17 testes direcionados.

Validacao completa via Context-Mode:
- Backend `rtk npm run eval:media`: passou.
- Backend `rtk npm run build`: passou.
- Backend `rtk npm test`: 200/200.
- Painel `rtk npm run build`: passou.
- Painel `rtk npm test`: 22/22.

Observacoes de build do painel:
- Browserslist desatualizado.
- Chunk maior que 500 kB.
Esses eram warnings, nao falhas.

Browser local:
- servidor iniciado em `http://127.0.0.1:5174`;
- login do painel renderizou;
- console sem erros, apenas warnings futuros do React Router;
- servidor local encerrado depois.

`git diff --check` passou nos dois repos.

### 9. Commits criados
Backend:
- `47aa90c feat: expose media understanding status`

Painel:
- `6539f1b feat: show media understanding status`

### 10. Push
Push para `origin/main` passou nos dois repos.

### 11. Deploys verificados
Backend:
- Projeto: `concretize-ia-prod2`
- Deployment: `dpl_Sf4uhDz8MPkJJvrU2cN6zEMyF4WH`
- Commit: `47aa90c6164ec19400261af869fdf7925799bf49`
- Estado: `READY`
- Aliases: inclui `concretize-ia-prod2.vercel.app`

Painel PROD2:
- Projeto: `concretize-insight-hub-prod2`
- Deployment: `dpl_JDBTp4LTxKfpHLp5ThEzAbukJcGx`
- Commit: `6539f1b19c2c7fbf4149cebc9379f31761d67b09`
- Estado: `READY`
- Aliases: inclui `concretize-insight-hub-prod2.vercel.app`

Painel espelho/legado:
- Projeto: `concretize-insight-hub`
- Deployment: `dpl_3yMQ4zME4DJFRxbGRNSowJ6ZHoV3`
- Commit: `6539f1b19c2c7fbf4149cebc9379f31761d67b09`
- Estado: `READY`

### 12. Sondagens finais
Backend:
- `https://concretize-ia-prod2.vercel.app/api/status?debug=1` respondeu `status=ok`.
- WhatsApp conectado.
- `activeProvider=meta-whatsapp`.
- `officialCloudApiReady=true`.
- `aiCanProcessReplies=true`.
- Entradas suportadas confirmadas.

Endpoint novo:
- `/api/admin/media-understanding?conversation_id=test` sem sessao retornou HTTP 401.
- Isso e esperado porque rota administrativa exige autenticacao.

Painel:
- `https://concretize-insight-hub-prod2.vercel.app/login`: HTTP 200.
- `https://concretize-insight-hub-prod2.vercel.app/inbox`: HTTP 200.

Repos:
- backend limpo em `main...origin/main`.
- painel limpo em `main...origin/main`.

## Arquivos principais alterados no ultimo bloco
Backend:
- `api/admin/media-understanding.ts`
- `tests/webhook-source.test.js`
- `scripts/reset-for-rodrigo.mjs`

Painel:
- `src/pages/Inbox.tsx`
- `src/lib/backendApi.ts`
- `src/test/leadMemorySource.test.ts`
- `.vercel/project.json` local ignorado, alinhado para prod2.

Status local:
- `C:\Users\ynwwi\Concretize IA\LATEST-STATUS.md` atualizado com a nova secao.

Obsidian nesta solicitacao:
- Criada nota canônica [[IA Concretize - Status Atual 2026-05-27]].
- Criada nota de pendencias [[IA Concretize - Pendencias e Proximos Passos 2026-05-27]].
- Criada esta nota de memoria completa.
- Atualizados indice e nota historica do projeto.

## Estado final honesto
Foi feito tudo que era seguro e acionavel em codigo sem novos dados reais:
- midia renderizavel no painel;
- audio/documento/imagem/video com caminhos de renderizacao;
- PDF texto e PDF escaneado com caminhos de leitura;
- DOCX com extracao;
- audio com transcricao moderna e prompt de dominio;
- contrato de entendimento de midia;
- bloqueio de loops de instabilidade/reenvio;
- comportamento humano quando a midia nao pode ser entendida;
- painel mostrando status/confianca/revisao;
- exclusao de contato/conversa/memoria;
- testes, build, push e deploys verificados.

Nao da para declarar perfeicao absoluta porque midia depende de qualidade do arquivo, entrega da Meta, legibilidade e dados reais.
O proximo salto depende de teste real com WhatsApp e dataset de falhas reais.

## Pendencias resumidas
Ver nota detalhada: [[IA Concretize - Pendencias e Proximos Passos 2026-05-27]].

Essenciais:
- teste real WhatsApp com imagem, audio, PDF texto, PDF escaneado, DOCX, video e arquivo ruim;
- confirmar faixa de `Midia analisada` no painel com dados reais;
- confirmar que a IA nao usa mais instabilidade/reenvio/pergunta generica em loop;
- criar dataset real e eval semantico;
- considerar fila assincrona para midias pesadas;
- confirmar/aplicar migration de avatar se ainda pendente;
- rotacionar qualquer segredo exposto em sessoes antigas;
- confirmar dominio oficial/persistente do painel.

## Onde retomar
1. Abrir `https://concretize-insight-hub-prod2.vercel.app/inbox`.
2. Mandar midias reais para o WhatsApp da Concretize.
3. Para cada midia, conferir no painel: renderizacao, status da faixa, resumo, confianca e se a IA respondeu ou segurou para humano.
4. Se houver falha, capturar horario exato, telefone e tipo de midia; procurar logs do backend `concretize-ia-prod2` no deployment atual.
5. Converter qualquer falha em teste/eval antes de mexer no pipeline.
