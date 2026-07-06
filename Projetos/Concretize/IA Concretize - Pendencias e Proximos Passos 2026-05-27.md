---
title: IA Concretize - Pendencias e Proximos Passos 2026-05-27
type: pendencias
project: Concretize / IA de Atendimento Rodrigo
date: '2026-05-27'
updated: '2026-05-27 23:46'
status: pendencias-pos-midia-estruturada
tags:
  - concretize
  - ia-atendimento
  - pendencias
  - whatsapp
  - midia
  - qa
  - proximos-passos
---
# IA Concretize - Pendencias e Proximos Passos 2026-05-27

## Prioridade 0 - teste real indispensavel
- [ ] Enviar pelo WhatsApp real uma imagem nova de produto e confirmar: aparece no painel, fica renderizavel e gera entendimento estruturado.
- [ ] Enviar audio curto real e confirmar: player aparece no painel, transcricao nao alucina repeticao e IA usa o texto correto.
- [ ] Enviar PDF com texto selecionavel e confirmar: card abre no painel e IA entende o conteudo.
- [ ] Enviar PDF escaneado/foto dentro de PDF e confirmar: Gemini tenta contexto visual; se nao entender, marca revisao humana.
- [ ] Enviar DOCX e confirmar: texto extraido com `mammoth`, resumo aparece no painel.
- [ ] Enviar video curto com fala/produto e confirmar: tenta audio + visual; se nao entender, nao inventa.
- [ ] Enviar documento nao suportado ou arquivo ruim e confirmar: `unsupported/unavailable`, sem resposta automatica ruim.
- [ ] Conferir no painel a faixa de status: `Midia analisada`, `IA liberada` ou `Revisao humana`.

## Prioridade 1 - validar comportamentos que motivaram os fixes
- [ ] Confirmar que a IA nao fala mais `tive uma instabilidade rapida` ou variantes.
- [ ] Confirmar que a IA nao pede `me manda novamente` em loop quando a midia falha.
- [ ] Confirmar que a IA nao responde `me fala qual produto/modelo voce quer ver` quando o cliente disse apenas `esse` e a midia nao foi entendida.
- [ ] Confirmar que texto concreto ainda funciona mesmo com midia falhada. Exemplo: cliente manda arquivo ruim + texto com produto, quantidade e cidade; IA deve responder sobre o texto.
- [ ] Confirmar que conversa com `action=human_review` fica operacionalmente facil para humano assumir.

## Prioridade 2 - operacao do painel
- [ ] Testar exclusao de contato em um contato de teste, nunca em lead real sem backup/confirmacao.
- [ ] Testar envio manual de anexo pelo painel para WhatsApp real: imagem, audio, PDF e video pequeno.
- [ ] Confirmar que foto de perfil aparece para contatos com avatar publico no WhatsApp.
- [ ] Confirmar fallback de iniciais quando nao ha foto ou a URL falha.
- [ ] Confirmar se `centralconcretize.vercel.app` ainda aponta para o deploy/projeto desejado; se for URL oficial do cliente, tornar dominio persistente no projeto certo.

## Prioridade 3 - dados reais e evals
- [ ] Criar dataset real com conversas/midias anonimizadas: audio curto, audio com ruido, imagem clara, imagem ruim, PDF texto, PDF escaneado, DOCX, video, documento nao suportado.
- [ ] Criar eval semantico alem do eval estrutural atual. O eval atual garante formato/casos; o proximo deve julgar resposta correta, nao so estrutura.
- [ ] Medir taxa de `human_review`, `unavailable`, `unsupported`, falsos positivos e falsos negativos.
- [ ] Transformar falhas reais em testes regressivos antes de mexer no prompt ou pipeline.

## Prioridade 4 - arquitetura futura se volume exigir
- [ ] Fila assincrona para midias pesadas, evitando depender de uma unica execucao do webhook para baixar, renderizar, interpretar e responder.
- [ ] Estado visual de `processando midia` no painel, caso a fila assincrona seja criada.
- [ ] Busca visual/catalogo: usar imagem recebida para comparar com catalogo e sugerir produto provavel quando fizer sentido.
- [ ] Melhorar observabilidade por midia: tempo de download, provider usado, motivo exato de falha, tamanho e MIME.
- [ ] Dashboard de qualidade: quantas midias entendidas, quantas revisoes humanas, quais tipos mais falham.

## Prioridade 5 - infraestrutura e seguranca
- [ ] Rotacionar qualquer token/segredo que tenha sido colado em sessoes antigas ou notas antigas.
- [ ] Evitar registrar segredos em Obsidian; manter somente IDs nao secretos, URLs e comandos sem credenciais.
- [ ] Confirmar se migration `contact_avatar_url` foi aplicada no Supabase; aplicar se a persistencia direta de avatar for desejada.
- [ ] Monitorar Chatwoot/VPS; houve historico de 502 e indisponibilidade em sessoes anteriores.
- [ ] Monitorar quota OpenAI/Gemini e custo de transcricao/visao.
- [ ] Confirmar perfil comercial do WhatsApp com dados oficiais: foto, descricao, endereco, email/site. Nao inventar dados.

## Criterio para chamar de quase perfeito
A IA so deve ser considerada quase perfeita quando passar por uma bateria real com pelo menos:
- 10 imagens reais;
- 10 audios reais;
- 5 PDFs texto;
- 5 PDFs escaneados;
- 3 DOCX;
- 3 videos;
- 5 arquivos ruins/nao suportados;
- 20 conversas de texto normais misturadas com midia.

Aprovacao esperada:
- quando entende, responde util e sem alucinar;
- quando nao entende, nao inventa;
- painel mostra claramente o motivo/status;
- humano consegue assumir sem precisar adivinhar o que aconteceu;
- nao ha loop de instabilidade, reenvio ou pergunta generica repetida.

## Estado atual das pendencias
Nao ha pendencia de codigo imediata que eu consiga resolver sem novos dados reais. A proxima melhoria real depende de teste WhatsApp real e coleta de casos.
