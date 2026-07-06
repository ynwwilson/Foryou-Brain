---
title: IA Concretize - Status Atual 2026-05-27
type: status-operacional
project: Concretize / IA de Atendimento Rodrigo
date: '2026-05-27'
updated: '2026-05-28 11:45'
status: superado-por-arquivamento
tags:
  - concretize
  - ia-atendimento
  - whatsapp
  - meta-cloud-api
  - vercel
  - midia
  - multimodal
  - media-understanding
  - handoff
  - status
---
# IA Concretize - Status Atual 2026-05-27

> Superado em 28/05/2026 por [[IA Concretize - Arquivado 2026-05-28]]. A IA foi parada/arquivada e Rodrigo voltou para atendimento manual no WhatsApp Business padrao.

## Resumo executivo
A IA da Concretize esta em producao no ambiente PROD2 com Meta WhatsApp Cloud API oficial, backend e painel publicados, catalogo com 30/30 imagens e pipeline multimodal endurecido.

O trabalho desta rodada fechou a camada de midia: imagem, audio, video, PDF, PDF escaneado, DOCX e documentos nao suportados agora passam por um contrato estruturado de entendimento antes de a IA responder. Quando entende, a IA pode usar o conteudo. Quando nao entende ou a confianca e baixa, a conversa deve ir para revisao humana sem inventar, sem pedir reenvio em loop e sem repetir frase de instabilidade.

Tambem foi adicionado no painel um indicador operacional que mostra se a midia foi entendida, qual a confianca e se precisa revisao humana.

## Ambiente atual validado
| Item | Estado | Detalhe |
|---|---|---|
| Backend PROD2 | OK | `https://concretize-ia-prod2.vercel.app` |
| Painel PROD2 | OK | `https://concretize-insight-hub-prod2.vercel.app` |
| Alias curto do painel | OK historico | `https://centralconcretize.vercel.app` foi usado nas rodadas anteriores; confirmar se segue apontando para o deploy desejado antes de entregar ao Rodrigo. |
| WhatsApp | OK | Meta Cloud API oficial, numero `+55 34 9718-3001`, provider ativo `meta-whatsapp`. |
| Catalogo | OK | 30 produtos, 30 com imagem, nenhum produto sem imagem no status. |
| IA | OK | Gemini primario/fallback conforme status, OpenAI fallback/texto/transcricao configurado, `aiCanProcessReplies=true`. |
| Midia recebida | OK tecnico | Arquivos renderizaveis no painel quando chegam do provedor com URL recuperavel. |
| Entendimento de midia | OK tecnico | Contrato `status/confidence/action` gravado em `media_contextos`. |
| Painel de entendimento | OK tecnico | Faixa `Midia analisada` / `IA liberada` / `Revisao humana` no Inbox. |
| URL antiga backend | Bloqueada | `https://concretize-ia.vercel.app` retornou `DEPLOYMENT_DISABLED / Payment required`; nao usar como producao atual. |

## URLs corretas
- Backend canonico atual: `https://concretize-ia-prod2.vercel.app`
- Painel PROD2: `https://concretize-insight-hub-prod2.vercel.app`
- Projeto backend local: `C:\Users\ynwwi\Projects\concretize-ia-webhook`
- Projeto painel local: `C:\Users\ynwwi\Projects\concretize-insight-hub`
- Status local complementar: `C:\Users\ynwwi\Concretize IA\LATEST-STATUS.md`

## Como a IA entende midias
Fluxo comum:
1. WhatsApp/Meta envia evento com metadados da mensagem.
2. Backend baixa o arquivo real quando a URL/ID de midia e recuperavel.
3. Backend salva uma copia renderizavel para o painel.
4. Backend interpreta conforme o tipo.
5. Resultado vira `MediaUnderstanding` com `kind`, `status`, `confidence`, `action`, `summary`, `evidence`, `extractedText`, `provider` e `failureReason`.
6. Se `action=reply`, a IA pode usar o conteudo para responder.
7. Se `action=human_review`, a conversa deve ficar para humano; a IA nao deve inventar.

Por tipo:
- Imagem: Gemini tenta descrever produto, medidas visiveis, contexto e evidencias. Se falhar ou vier sem arquivo, fica `unavailable/human_review`.
- Audio: OpenAI `gpt-4o-transcribe` com prompt de vocabulario da Concretize; fallback Gemini. Ha filtro contra transcricao alucinada/repetitiva.
- PDF: primeiro `pdf-parse` tenta texto selecionavel. Se nao houver texto ou falhar, Gemini tenta leitura visual do PDF escaneado.
- DOCX: `mammoth` extrai texto e entra como documento entendido.
- Video: tenta contexto visual/audiovisual via Gemini e tambem transcricao de audio. Com ambos, confianca maior; com apenas um, confianca media.
- Documento nao suportado: fica `unsupported`, sem resposta automatica baseada nele.

## Mudancas principais feitas nesta rodada
### Renderizacao e anexos no painel
- Imagens recebidas passaram a renderizar como imagem real.
- Audio recebido passou a renderizar com player.
- Video recebido passou a renderizar como video quando o arquivo chega renderizavel.
- PDF/documentos passaram a aparecer como card clicavel, nao so `[Documento Recebido]`.
- Envio manual de anexos pelo painel foi adicionado: imagem, audio, video, PDF, DOC e DOCX.

### Fotos de perfil
- Backend ganhou endpoint admin para buscar foto de perfil por telefone.
- Painel tenta renderizar avatar do contato e cai para iniciais se a URL falhar.
- Foi criada migration para `contact_avatar_url`; confirmar aplicacao no Supabase se quiser persistencia direta da coluna. O painel nao depende dela para funcionar, pois busca via endpoint.

### Exclusao de contato/conversa
- Painel ganhou opcao destrutiva de excluir contato/conversa/memoria, com confirmacao forte.
- A exclusao remove dados relacionados por telefone: conversas, mensagens, memoria, lead e registros associados.
- Se o cliente mandar nova mensagem depois, nova conversa sera criada.

### Loops ruins da IA
- Bloqueadas respostas publicas com frase de instabilidade ou pedido de reenvio em loop.
- Se a midia falha e o cliente diz apenas `esse`, `quanto fica esse`, `olha aqui`, etc., a IA nao deve responder tentando adivinhar.
- Se houver texto concreto independente da midia, a IA pode responder usando esse texto.
- Marcadores internos de midia indisponivel deixaram de instruir a IA a pedir reenvio ao cliente.

### Multimodal
- PDF escaneado agora tenta leitura visual pelo Gemini.
- DOCX agora e extraido com `mammoth`.
- Video tenta contexto visual e transcricao de audio.
- Audio usa `gpt-4o-transcribe` com prompt de dominio da Concretize.
- `/api/status?debug=1` declara entradas suportadas: `image`, `audio`, `video-audio-track`, `video-visual-context`, `pdf`, `scanned-pdf`, `docx`.

### Contrato estruturado de midia
- Criado `lib/mediaUnderstanding.ts` no backend.
- `api/webhook.ts` passou a persistir entendimento em `media_contextos`.
- Criado eval estrutural `npm run eval:media` com casos de audio curto, imagem indisponivel, PDF texto, PDF escaneado, video e documento nao suportado.

### Painel de entendimento
- Criado endpoint admin `/api/admin/media-understanding`.
- Painel consulta esse endpoint ao abrir conversa e quando chega nova mensagem.
- A faixa do Inbox mostra resumo e ate 5 midias recentes com tipo, status, confianca e resumo.

### Configuracao e dominios
- Fallback do painel em `src/lib/backendApi.ts` aponta para `https://concretize-ia-prod2.vercel.app`.
- `scripts/reset-for-rodrigo.mjs` deixou de usar URL antiga bloqueada.
- `.vercel/project.json` local do backend aponta para `concretize-ia-prod2`.
- `.vercel/project.json` local do painel foi alinhado para `concretize-insight-hub-prod2`, para evitar deploy manual no projeto errado.

## Commits relevantes da rodada de midia
Backend `ynwwilson/Concretize-IA`:
- `a468eef` - `fix: stop media failure reply loops`
- `8ea7edb` - `feat: improve multimodal media understanding`
- `138cd3b` - `fix: harden media reply understanding`
- `77c2720` - `chore: report transcription provider status`
- `20e4db2` - `feat: add structured media understanding`
- `47aa90c` - `feat: expose media understanding status`

Painel `ynwwilson/concretize-insight-hub`:
- `f465395` - `feat: add destructive contact delete`
- `6539f1b` - `feat: show media understanding status`

Commits de midia/painel imediatamente anteriores e relacionados:
- Backend `17d4afe` - persistir imagens recebidas.
- Painel `e6eb643` - renderizar imagens recebidas.
- Backend `40f1613` - manter previews renderizaveis mesmo se interpretacao falhar.
- Backend `416832b` - persistir midias recebidas e avatars.
- Painel `e64711f` - renderizar avatars e midias no Inbox.
- Backend `fe14e6c` - permitir envio de midia pelo painel.
- Painel `5124f29` - botao de anexo no Inbox.

## Deploys finais confirmados
- Backend: `concretize-ia-prod2`, deployment `dpl_Sf4uhDz8MPkJJvrU2cN6zEMyF4WH`, estado `READY`, commit `47aa90c`.
- Painel PROD2: `concretize-insight-hub-prod2`, deployment `dpl_JDBTp4LTxKfpHLp5ThEzAbukJcGx`, estado `READY`, commit `6539f1b`.
- Painel espelho/legado: `concretize-insight-hub`, deployment `dpl_3yMQ4zME4DJFRxbGRNSowJ6ZHoV3`, estado `READY`, commit `6539f1b`.

## Validacoes executadas
Backend:
- `npm run eval:media`: 6 casos carregados e estruturalmente validos.
- `npm run build`: passou.
- `npm test`: 200/200 passando.
- `git diff --check`: passou.
- `/api/status?debug=1`: `status=ok`, WhatsApp conectado, IA pronta, entradas de midia suportadas confirmadas.
- `/api/admin/media-understanding` sem sessao: HTTP 401, esperado para rota admin protegida.

Painel:
- `npm run build`: passou.
- `npm test`: 22/22 passando.
- `git diff --check`: passou.
- Browser local em `http://127.0.0.1:5174`: login renderizou sem erro de console, apenas avisos futuros do React Router.
- `https://concretize-insight-hub-prod2.vercel.app/login`: HTTP 200.
- `https://concretize-insight-hub-prod2.vercel.app/inbox`: HTTP 200.

Repos:
- Backend limpo em `main...origin/main`.
- Painel limpo em `main...origin/main`.

## O que foi observado pelo Wilson durante a rodada
- Audio inicialmente nao tocava no painel; depois passou a tocar.
- Documento inicialmente nao abria/renderizava; depois passou a abrir/renderizar.
- Um audio curto com tres `oi` chegou a ser transcrito de forma alucinada/repetitiva; isso motivou troca para transcricao moderna e filtro anti-alucinacao.
- O painel mostrava placeholders como `[Documento Recebido]` sem card util; isso foi corrigido.
- Fotos de perfil nao apareciam; fluxo de avatar foi implementado.
- IA repetia frases como `Tive uma instabilidade rapida aqui, pode me mandar novamente?`; isso foi bloqueado.
- IA pedia `Me fala qual produto ou modelo voce quer ver` quando nao entendia midia; esse loop foi bloqueado quando a pergunta dependia da midia.
- Wilson pediu exclusao de contato/conversa/memoria como no WhatsApp; foi implementado com confirmacao forte.

## Estado honesto: chegamos no limite?
Dentro da arquitetura atual e sem novos dados reais, foi feito tudo que era seguro fazer em codigo: ingestao, renderizacao, entendimento, contrato de confianca, guardrails, painel operacional, testes, build, deploy e status.

Nao existe perfeicao absoluta em midia. A IA ainda pode nao entender quando:
- a Meta/WhatsApp nao entrega o arquivo recuperavel;
- o arquivo esta corrompido, grande demais ou inacessivel;
- o audio esta inaudivel;
- a imagem/video nao mostra o produto com clareza;
- o PDF esta ilegivel mesmo visualmente;
- o cliente usa referencia deitica sem a midia estar disponivel.

O comportamento correto nesses casos e: nao inventar, nao mandar loop de reenvio, marcar para humano e mostrar no painel que precisa revisao.

## Pendencias ativas
Ver nota dedicada: [[IA Concretize - Pendencias e Proximos Passos 2026-05-27]].

## Sessao completa
Ver memoria detalhada da execucao: [[2026-05-27 23h46 - Concretize IA memoria completa midia painel e pendencias]].
