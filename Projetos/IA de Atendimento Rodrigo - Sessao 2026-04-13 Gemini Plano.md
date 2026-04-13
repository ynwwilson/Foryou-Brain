# Sessão 2026-04-13 — Gemini como primário + OpenAI fallback

## Contexto desta sessão
O usuário retomou o trabalho após fechar a aba anterior sem querer. Foi necessário reconstruir o contexto local do projeto e o ponto exato onde o trabalho havia parado.

## O que foi confirmado no ambiente
- Projeto local: `C:\Users\ynwwi\Projects\concretize-ia-webhook`
- A Vercel CLI já está instalada no projeto.
- `npx vercel --version` retornou `41.7.8`.
- `npx vercel whoami` retornou `ynwwilson-9617`.
- O projeto local já está linkado à Vercel via `.vercel/project.json`.
- Foi listado o histórico recente de deployments do projeto `concretize-ia`.

## Onde havíamos parado antes
O bloqueio operacional anterior era o diagnóstico da falha de mídia em produção via logs da Vercel. O pedido anterior para instalar/logar Vercel CLI existia para conseguir consultar logs reais da função em produção e capturar a causa da falha de mídia.

## Reconstrução do objetivo real da arquitetura
Após inspeção do código local e dos diffs recentes, ficou claro que o objetivo correto não é apenas usar uma IA mais barata de forma parcial.

### Objetivo final alinhado com o usuário
- Usar `Gemini` como IA principal para tudo.
- Usar `OpenAI` como fallback completo.
- Remover `Claude` totalmente do runtime e, idealmente, do código útil.
- Preservar o mesmo contexto no fallback.
- O cliente não pode sentir falha operacional.

## Estado atual do código no momento desta sessão
### O que já existe
- `Gemini` já entrou no fluxo principal de resposta ao cliente.
- `OpenAI` já existe em partes do fallback, especialmente em resposta e mídia.
- Há implementação nova em `lib/gemini.ts`.
- `api/status.ts` já expõe indicadores relacionados a Gemini/OpenAI.

### O que ainda está híbrido / incompleto
- `Claude` ainda aparece em fluxos auxiliares:
  - evolução da memória do lead
  - análise de intenção comercial
  - sugestão de follow-up
- Testes ainda refletem em partes a arquitetura antiga com Claude.
- A migração total para `Gemini + OpenAI fallback` ainda não foi concluída.

## Diagnóstico técnico consolidado
A arquitetura correta não deve assumir que Gemini e OpenAI nunca falham. Mesmo sendo multimodais, podem falhar por timeout, rate limit, resposta malformada, erro temporário do provedor, payload inválido, arquivo corrompido, limite de tamanho, instabilidade de rede, erro de env/configuração e mudanças de comportamento dos modelos.

### Princípio de produção definido
A blindagem correta é:
- `Gemini` como primário confiável.
- `OpenAI` como fallback confiável.
- Mesmo contexto no fallback.
- Logs estruturados para diagnóstico.
- Guardrails fortes.
- Resposta operacional segura se ambos falharem.

### Meta operacional correta
Não prometer “perfeição absoluta”, e sim:
- produção forte
- baixo risco operacional
- fallback real
- baixa degradação para o cliente
- manutenção contínua orientada por logs

## O que foi definido sobre blindagem
As camadas de blindagem que devem existir:
1. Validação e normalização de entrada.
2. Fallback real com contexto idêntico.
3. Resiliência de execução com timeout/retry/fallback corretos.
4. Guardrails de qualidade e de negócio.
5. Estratégia de degradação elegante para o cliente.
6. Observabilidade de longo prazo.

## Regras de negócio já reconstruídas do código
- Não usar emoji.
- Espelhar o tom do cliente.
- Não usar frases genéricas de IA como “Perfeito”, “Entendo”, “Ótimo”, “Como posso ajudar?”.
- Evitar textão; respostas curtas e naturais no WhatsApp.
- Nunca calcular frete.
- Não calcular orçamento total automaticamente.
- Não conceder desconto automaticamente.
- Não confirmar pagamento agendado como pagamento concluído.
- Não recomendar concorrente.
- Não fingir que entendeu áudio/imagem/documento quando falhou.
- Usar contexto de mídia quando a extração/transcrição funcionar.

## O que o usuário precisa me trazer depois
O usuário vai voltar com material mais completo para começar 100% do plano. Os blocos que preciso, preferencialmente corrigidos e completados pelo usuário, são:

1. `PROMPT`
2. `REGRAS COMERCIAIS`
3. `GUARDRAILS`
4. `MEMORIA DO LEAD`
5. `PRODUTOS/RAG`

### Ordem ideal de prioridade para o usuário preencher/corrigir
1. `REGRAS COMERCIAIS`
2. `GUARDRAILS`
3. `PRODUTOS/RAG`
4. `MEMORIA DO LEAD`
5. `PROMPT`

## Template pré-preenchido que foi entregue ao usuário
Foi entregue um template com esses blocos já parcialmente preenchidos a partir do código e da memória local:
- `PROMPT`
- `REGRAS COMERCIAIS`
- `GUARDRAILS`
- `MEMORIA DO LEAD`
- `PRODUTOS/RAG`

O usuário deve editar/corrigir/complementar esses blocos e trazer na próxima sessão.

## Plano de implementação definido
### O que eu devo fazer
1. Mapear e remover dependências restantes de `Claude`.
2. Criar a camada unificada `Gemini -> OpenAI` com o mesmo contexto.
3. Migrar para essa camada:
   - resposta principal
   - memória do lead
   - análise de intenção
   - follow-up
   - visão de imagem
   - transcrição de áudio
4. Reforçar o pipeline de mídia.
5. Aplicar guardrails de entrada e saída.
6. Implementar contingência final segura.
7. Reescrever testes para a nova arquitetura.
8. Validar build/testes localmente.
9. Validar em produção com logs reais da Vercel.
10. Limpar legado e documentar a arquitetura final.

### O que o usuário deve fazer
- Trazer os blocos de negócio refinados.
- Principalmente política exata de preço, frete, desconto, prazo e pagamento.
- Definir melhor critérios de lead quente/frio/perdido/pronto para humano.
- Enriquecer a base de produtos/RAG com nomes reais, aliases e atributos úteis.

## Como a arquitetura final deve funcionar
### Fluxo alvo
- Regras diretas / cache / FAQ / RAG tentam resolver primeiro.
- Se precisar IA, `Gemini` responde.
- Se Gemini falhar, `OpenAI` assume com o mesmo contexto.
- Se ambos falharem, o cliente recebe uma resposta operacional segura e curta.
- O mesmo princípio vale para texto, visão, transcrição, memória, análise e follow-up.

### Resultado final esperado
- IA mais barata.
- IA mais robusta.
- Menor dependência de um único provedor.
- Menor chance de erro comercial.
- Menor chance de perda de contexto.
- Maior consistência de comportamento.
- Melhor capacidade de manutenção futura.

## Onde paramos exatamente
Paramos antes da implementação completa. O próximo passo quando o usuário voltar é:
1. receber os blocos de negócio refinados;
2. consolidar a especificação operacional final;
3. iniciar a implementação da migração total para `Gemini + OpenAI fallback`.

## Observação importante para a próxima sessão
Não afirmar que o sistema ficará “100% perfeito”. A formulação correta acordada foi:
- não perfeito para sempre
- mas profissional, forte, blindado e pronto para produção séria
- com manutenção contínua apoiada em logs
