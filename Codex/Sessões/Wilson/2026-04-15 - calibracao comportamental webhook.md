# Sessão Codex — 2026-04-15

## Objetivo
Consolidar e implementar a calibração comportamental/comercial da IA do projeto `concretize-ia-webhook`, com foco em tom, persuasão, memória, handoff para humano e regras anti-inferência.

## O que foi decidido com o usuário

### Tom e comportamento
- A IA deve soar humana, tranquila, simpática, educada e persuasiva.
- Deve falar de igual pra igual no WhatsApp.
- Não deve parecer IA nem usar excesso de palavras afirmativas como `Perfeito`, `Ótimo`, `Entendo`.
- Pode usar `Como posso ajudar?`, desde que não seja de forma vazia/solta; precisa vir com contexto ou próximo passo.
- Deve sempre seguir o ritmo e o tom do lead.
- Se o lead for mais direto, a IA deve ser mais direta, sem perder essência comercial.
- A IA pode ser cerca de 1% mais agressiva comercialmente, principalmente para não perder o lead para concorrente.

### Recomendação comercial
- A IA pode recomendar com embasamento.
- Pode sugerir opções prováveis sem inventar e sem confirmar cedo demais.
- Não pode tratar sugestão como certeza.

### Memória do lead
- A memória deve persistir para sempre, salvo exclusão manual.
- Deve sempre se atualizar conforme a conversa e o contexto mudam.
- Deve lembrar o que importa para retomadas futuras.
- Não deve guardar ruído como `oi`, `tchau` etc.
- Campos confirmados/relevantes:
  - nome do lead
  - forma de tratamento
  - tipo de cliente
  - produto de interesse
  - modelo confirmado
  - quantidade ou metragem confirmada
  - local da obra
  - cidade
  - prazo desejado
  - orçamento até o momento
  - status do lead
  - objeção principal
  - preferência relevante
  - última pendência aberta
  - última atualização
- Mídia entra primeiro como sinal; não deve virar fato automaticamente.

### Escalada para humano
Mensagens aprovadas/consolidadas:
- Durante horário:
  - `Vou passar isso pro responsável pra te confirmar certinho. Se quiser, já me manda a quantidade e a cidade da obra que eu deixo isso adiantado.`
- Fora do horário:
  - `Vou deixar isso encaminhado pro time responsável. O atendimento humano funciona de segunda a sexta, das 07:00 às 12:00 e das 13:00 às 17:00. Se quiser, já me manda a quantidade e a cidade da obra que eu deixo tudo organizado pra te responderem mais rápido.`
- Em feriado:
  - `Vou deixar isso encaminhado pro responsável, mas como hoje estamos fora do horário comercial/feriado, o retorno humano acontece no próximo dia útil. Se quiser, já me manda a quantidade e a cidade da obra que eu adianto tudo por aqui.`
- Caso sensível:
  - `Esse ponto eu prefiro passar pro responsável pra te orientar com segurança. O retorno costuma ser bem rápido. Se quiser, já me adianta a quantidade e a cidade da obra que eu deixo tudo mais encaminhado.`
- Estoque/prazo/valor exato:
  - `Pra eu te passar isso do jeito certo, preciso validar com o time responsável. Me confirma a quantidade e a cidade da obra que eu já deixo encaminhado.`

Regra geral aprovada:
- usar sempre `segurança + continuidade + próximo passo`
- nunca dizer só que vai verificar e sumir
- sempre pedir pelo menos quantidade e cidade quando fizer sentido

### Concorrente / preço
Resposta calibrada aprovada:
- `Preço chama atenção mesmo, mas no fim o que pesa é a peça chegar bem feita e não te dar problema depois na obra. Aqui a gente trabalha com padrão forte de qualidade e entrega rápida. Me fala o que você precisa que eu vejo a opção mais certa pra você, antes de você fechar algo só pelo menor preço.`

### Estoque / pronta entrega
- Regra mantida: quase sempre fabricamos sob pedido.
- Ajuste comercial aprovado: deixar claro que a entrega costuma ser rápida.

### Troca e reclamação
- A IA deve acolher, pedir foto e contexto mínimo, não discutir culpa e passar para humano.
- Resposta-base aprovada:
  - `Me manda uma foto pra eu registrar certinho e já passar isso pro responsável. O time humano te atende no horário comercial e vai te orientar da melhor forma.`

## O que foi implementado no código
Arquivos alterados:
- `lib/ai.ts`
- `lib/openai.ts`
- `lib/context.ts`
- `lib/replyRules.ts`
- `tests/webhook-source.test.js`

### Mudanças implementadas
1. Regras de prompt ajustadas para:
- permitir `Como posso ajudar?` com contexto
- reforçar espelhamento do ritmo/tom do lead
- permitir recomendação com embasamento sem confirmação precoce
- reforçar handoff com `segurança + continuidade + próximo passo`
- reforçar que modelo/estoque/prazo/desconto/orçamento total não podem ser confirmados sem validação suficiente

2. Contexto fixo comercial ajustado para:
- condução mais firme em objeção de preço
- condução mais firme em concorrente/preço
- regra explícita de mirroring
- explicação explícita sobre uso contextual de `Como posso ajudar?`
- seção formal de transição para humano por cenário

3. Regras diretas ajustadas para:
- frete pedir quantidade + cidade e encaminhar corretamente
- pronta entrega/estoque responder com verdade operacional + agilidade de entrega

4. Memória reforçada no prompt estruturado para:
- atualizar quando o contexto muda
- não converter mídia ambígua em fato confirmado

## Validação executada
Comandos rodados e aprovados:
- `npm test -- --run`
- `npm run build`

Resultado:
- testes passando `72/72`
- build passando (`tsc --noEmit`)

## Pendência única relevante para amanhã
Falta o bloco de produto/RAG em nível máximo:
- vantagens reais dos produtos prioritários
- quando indicar cada um
- quando não indicar
- como comparar opções

O usuário disse que consegue trazer isso amanhã.

## Estado final ao encerrar hoje
- calibração comportamental principal implementada
- tom, handoff, memória e resposta comercial endurecidos
- base validada por teste e build
- único gap restante: argumentos finos dos produtos prioritários para fechar a camada de RAG/recomendação
