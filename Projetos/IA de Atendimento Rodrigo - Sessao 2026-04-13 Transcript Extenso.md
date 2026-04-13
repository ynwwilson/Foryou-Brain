# Sessão 2026-04-13 — Registro Extenso da Conversa

## Objetivo desta nota
Registrar de forma extensa e operacional a conversa desta sessão para que o trabalho possa ser retomado mesmo se a aba/sessão for fechada. Esta nota não é uma transcrição literal palavra por palavra, mas tenta preservar praticamente todo o conteúdo relevante, decisões, nuances, riscos, intenções e próximos passos discutidos.

---

## Contexto inicial da retomada
O usuário informou que havia fechado a aba anterior sem querer. A última lembrança era que eu havia pedido algo relacionado a instalar Vercel CLI e ter CLI disponível.

A partir disso, foi feito trabalho de reconstrução do contexto diretamente do ambiente local do projeto, dos arquivos do repositório, do histórico git, do estado da Vercel CLI e da memória no Obsidian.

---

## O que foi reconstruído no ambiente
### Projeto e contexto local
- Projeto: `C:\Users\ynwwi\Projects\concretize-ia-webhook`
- Foi lido o `CLAUDE.md` local para recuperar as diretrizes do projeto.
- A referência a `RTK.md` não existia no repositório local; o contexto principal estava em `CLAUDE.md` e na nota do Obsidian.

### Vercel
Foi confirmado que:
- A Vercel CLI já estava instalada.
- `npx vercel --version` retornou `41.7.8`.
- `npx vercel whoami` retornou `ynwwilson-9617`.
- O projeto local já estava linkado à Vercel via `.vercel/project.json`.
- Foi possível listar deployments recentes do projeto `concretize-ia`.

### Onde havíamos parado antes
O ponto operacional anterior era: diagnosticar a falha de mídia em produção consultando os logs reais da Vercel.
O motivo pelo qual havia sido pedido Vercel CLI/login era justamente acessar logs de produção e ver o erro real do runtime.

---

## Reconstrução do objetivo real do trabalho
Durante a sessão, o usuário esclareceu que o objetivo verdadeiro não era apenas uma otimização parcial de custo, mas sim uma migração arquitetural mais forte.

### Objetivo final alinhado
- `Gemini` deve ser a IA principal para tudo.
- `OpenAI` deve ser o fallback completo.
- `Claude` deve sair totalmente do runtime e idealmente do código útil.
- O fallback deve preservar o mesmo contexto.
- O cliente não pode sentir a falha operacional.

O usuário também esclareceu que já havia passado a API do Gemini em conversa anterior e que a intenção era usar Gemini em tudo com OpenAI como fallback.

---

## Estado atual do código no momento da sessão
Foi identificado que o repositório está em estado híbrido.

### O que já existe
- `Gemini` já entrou no caminho principal de resposta ao cliente.
- `OpenAI` já existe como fallback em partes do sistema, especialmente em mídia e resposta.
- `lib/gemini.ts` foi criado com funções para:
  - geração de resposta
  - extração de contexto de imagem
  - transcrição de áudio
- `api/status.ts` já expõe sinais de configuração para Gemini e OpenAI.

### O que ainda está incompleto / híbrido
- `Claude` ainda aparece em fluxos auxiliares importantes:
  - evolução da memória do lead
  - análise de intenção comercial
  - sugestão de follow-up
- Testes ainda refletem em vários pontos a arquitetura anterior com Claude.
- A migração total ainda não foi concluída.

---

## Diagnóstico técnico consolidado
Foi discutido que a arquitetura correta não pode assumir ingenuamente que Gemini e OpenAI “não falham”, mesmo sendo multimodais.

### Motivos técnicos de falha que continuam possíveis
- timeout
- rate limit
- resposta malformada
- erro temporário do provedor
- payload de mídia inválido
- arquivo corrompido
- limite de tamanho
- instabilidade de rede entre Vercel e API
- erro de configuração/env
- mudança de comportamento do modelo

### Conclusão técnica
A arquitetura correta não é “eles não falham”. A arquitetura correta é:
- `Gemini` como primário confiável
- `OpenAI` como fallback confiável
- preservação do mesmo contexto no fallback
- logs estruturados para diagnosticar problemas
- guardrails comerciais fortes
- resposta operacional segura se ambos falharem

---

## Sobre “perfeição” do sistema
O usuário perguntou explicitamente se, após tudo isso, o sistema estaria “100% pronto e perfeito”.

Foi alinhado de forma explícita que:
- Não é sério prometer “100% perfeito” para um sistema desse tipo.
- O que é possível entregar é:
  - arquitetura correta
  - produção forte
  - fallback real
  - menor risco operacional
  - menor chance de erro
  - menor chance de perda de contexto
  - consistência comercial muito maior
  - observabilidade para evolução contínua

### Formulação acordada
A resposta correta não é “perfeito para sempre”.
A formulação correta é:
- profissional
- forte
- blindado
- pronto para produção séria
- com manutenção contínua apoiada em logs

### Fatores que impedem a ideia de “perfeição eterna”
- comportamento dos modelos muda
- catálogo/RAG pode ficar desatualizado
- processo comercial pode evoluir
- há sempre casos de borda
- há dependência de APIs externas
- dados de entrada podem ser ruins
- prompts envelhecem

### Conclusão sobre perfeição
- `100% perfeito`: não
- `100% profissional e forte para operar bem`: sim, esse é o alvo correto

---

## Blindagem discutida na sessão
Foi consolidado que a blindagem deve ter 6 camadas principais.

### 1. Blindagem de entrada
Antes de chamar modelo, validar e normalizar:
- texto
- histórico
- mídia
- tamanho
- integridade
- respostas estruturadas

### 2. Fallback real com contexto idêntico
O `OpenAI` precisa receber o mesmo pacote do `Gemini`:
- prompt forte
- histórico recente
- memória persistente do lead
- contexto RAG
- guardrails
- contexto de mídia

### 3. Resiliência de execução
- timeout por operação
- retry controlado só para erro transitório
- sem retry para erro inválido que só queima token
- logs do motivo da troca para fallback
- contingência final se ambos falharem

### 4. Guardrails de qualidade
Bloquear, entre outros:
- cálculo de frete
- desconto não autorizado
- confirmação falsa de pagamento
- recomendação de concorrente
- invenção de produto/medida/prazo
- fingir entendimento de mídia

### 5. Degradação elegante
Se ambos falharem, o cliente não pode perceber colapso. O sistema deve responder com mensagem operacional curta, útil e segura, sem inventar.

### 6. Observabilidade contínua
Logs e métricas de:
- provedor usado
- fallback acionado
- motivo do fallback
- tempo de resposta
- falhas de mídia
- guardrails acionados
- contingência final acionada
- rota usada (regra/cache/FAQ/Gemini/OpenAI)

---

## Regras de negócio já reconstruídas do código
Sem depender ainda das respostas finais do usuário, foi possível reconstruir várias regras a partir do código e da memória do projeto.

### Regras já observadas
- Não usar emoji.
- Espelhar o tom do cliente.
- Não usar frases genéricas de IA como “Perfeito”, “Entendo”, “Ótimo”, “Como posso ajudar?”.
- Evitar textão.
- Dividir resposta apenas quando necessário.
- Nunca calcular frete.
- Não calcular orçamento total automaticamente.
- Não conceder desconto automaticamente.
- Não confirmar pagamento agendado como pago.
- Não recomendar concorrente.
- Não fingir que entendeu áudio/imagem/documento quando falhou.
- Usar contexto de mídia quando a leitura funcionar.
- Tentar conduzir sempre a próxima ação comercial.

---

## Template que foi entregue ao usuário
Foi entregue ao usuário um template com os seguintes blocos:
- `PROMPT`
- `REGRAS COMERCIAIS`
- `GUARDRAILS`
- `MEMORIA DO LEAD`
- `PRODUTOS/RAG`

Depois, foi entregue novamente um template já pré-preenchido com base no código e nas notas locais.

### O que o usuário precisa me trazer depois
O usuário deverá corrigir, complementar ou substituir principalmente:
1. `REGRAS COMERCIAIS`
2. `GUARDRAILS`
3. `PRODUTOS/RAG`
4. `MEMORIA DO LEAD`
5. `PROMPT`

### O que mais importa o usuário definir
- política exata de preço, frete, desconto, prazo e pagamento
- o que a IA nunca pode fazer
- critérios de lead quente/frio/perdido/pronto para humano
- melhor definição dos produtos e aliases reais usados pelos clientes

---

## Plano de implementação consolidado
Foi alinhado um plano em alto nível para a execução técnica.

### O que eu devo fazer
1. Mapear e remover dependências restantes de `Claude`.
2. Criar uma camada unificada `Gemini -> OpenAI` com o mesmo contexto.
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
- Principalmente regras comerciais e guardrails.
- Refinar memória do lead.
- Refinar RAG/produtos.

---

## Como a arquitetura final deve funcionar
### Fluxo alvo de decisão
1. Regras diretas
2. Cache
3. FAQ/RAG
4. Se precisar IA: `Gemini`
5. Se `Gemini` falhar: `OpenAI`
6. Se ambos falharem: resposta operacional segura

### Princípio de contexto
O fallback deve preservar:
- histórico recente
- memória persistente do lead
- contexto de produto/RAG
- regras comerciais e prompt
- contexto de mídia

### O mesmo vale para
- texto
- visão
- transcrição
- memória
- análise de intenção
- follow-up

---

## Resultado final esperado após implementação completa
- IA mais barata
- IA mais robusta
- menor dependência de provedor único
- menor risco comercial
- menor chance de perda de contexto
- comportamento mais previsível
- mais facilidade para manutenção futura

---

## Sobre o que eu poderia adiantar enquanto o usuário está fora
Foi alinhado que, enquanto o usuário estivesse fora, eu poderia adiantar:
- auditoria completa do estado atual da IA
- mapa do que ainda usa Claude
- arquitetura técnica final `Gemini -> OpenAI fallback`
- lista dos arquivos que precisam mudar
- riscos reais de produção
- checklist de execução
- preparação estrutural segura
- organização do contexto no Obsidian

### O que ainda faltará do usuário mesmo assim
- `PROMPT` final
- `REGRAS COMERCIAIS` finais
- `GUARDRAILS` finais
- `MEMORIA DO LEAD` refinada
- `PRODUTOS/RAG` refinado

---

## Sobre auto-approve / full-auto no Codex CLI
O usuário perguntou como configurar o Codex CLI para operar com menos confirmações.

### O que foi descoberto
- O usuário está usando o Codex via terminal.
- Foi consultado `codex --help`.
- As opções relevantes são:
  - `--sandbox`
  - `--ask-for-approval`
  - `--full-auto`
  - `--dangerously-bypass-approvals-and-sandbox`
  - `--search`
  - `-C` / `--cd`

### Recomendação feita
Usar no projeto da Concretize:

```powershell
cd C:\Users\ynwwi\Projects\concretize-ia-webhook
codex --full-auto --search
```

### Motivo
Isso dá um modo mais automático sem cair no bypass total e perigoso.

### O que não foi recomendado
Não usar:

```powershell
codex --dangerously-bypass-approvals-and-sandbox
```

porque isso removeria proteção demais.

### Regra operacional combinada
Mesmo em `--full-auto`, ações destrutivas relevantes, banco de dados e exclusões importantes ainda devem ser tratadas com confirmação explícita e explicação clara.

---

## Instrução de retomada para a próxima sessão
Foi combinado que, na nova sessão, o usuário pode pedir algo como:

```txt
Continue da nota do Obsidian "Projetos/IA de Atendimento Rodrigo - Sessao 2026-04-13 Gemini Plano.md" e avance em tudo que der sem depender de mim.
```

Ou uma versão mais controlada que exija aprovação antes da implementação:
- recuperar o contexto
- entregar diagnóstico
- entregar plano
- esperar a palavra `APROVO` para implementar

---

## Onde paramos exatamente no fim desta sessão
Paramos antes da implementação completa.

### Próximo passo exato quando retomar
1. Ler a nota desta sessão e a nota resumida principal.
2. Recuperar diagnóstico e plano.
3. Entregar ao usuário um resumo com:
   - contexto
   - objetivo
   - diagnóstico
   - plano
4. Esperar o usuário escrever `APROVO`.
5. Só então iniciar a implementação.

---

## Conclusão consolidada da sessão
Esta sessão serviu para:
- reconstruir contexto perdido da aba anterior
- confirmar o estado real do projeto
- alinhar o objetivo correto (`Gemini + OpenAI fallback`)
- alinhar a visão correta sobre confiabilidade e “perfeição”
- estruturar o plano técnico
- estruturar o que o usuário precisa fornecer
- deixar memória suficiente no Obsidian para retomada futura sem perda operacional
