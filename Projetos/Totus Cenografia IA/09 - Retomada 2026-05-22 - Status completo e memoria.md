---
type: session-memory
project: Totus Cenografia IA
date: 2026-05-22
status: live-platform-whatsapp-pending
tags: [totus, memoria, retomada, erros, producao, whatsapp]
---

# Retomada 2026-05-22 - Status completo e memoria

Esta nota consolida o estado real da IA da Totus para continuarmos depois sem depender do chat.

## Resumo executivo

A IA da Totus Cenografia esta no ar como plataforma: painel administrativo, API, banco Neon, Redis/Upstash, Chatwoot self-hosted, brain/versionamento, catalogo, leads, aprovacoes, dashboard, health checks, guardrails e fluxo de follow-up.

O sistema ainda nao esta em producao real no WhatsApp porque a Meta API oficial ainda nao foi plugada. O health atual confirma que a Meta nao esta configurada, mas a Evolution aparece configurada como fallback.

Status correto: **plataforma production-ready, aguardando plugar WhatsApp Meta e fazer homologacao real com Guilherme**.

## Projeto correto

Repositorio atual:

```txt
C:\Users\ynwwi\Projects\totus-cenografia-ia
```

GitHub:

```txt
https://github.com/ynwwilson/totus-cenografia-ia
```

Branch:

```txt
main...origin/main
```

Ultimo commit verificado:

```txt
12d450d fix: harden totus ai operations
```

Importante: existe um repo antigo chamado `totus-ai-concierge`. Ele foi uma versao anterior/legada e **nao deve ser tratado como fonte de verdade do projeto atual**.

## URLs vivas verificadas

Verificado em 2026-05-22:

```txt
https://totus-cenografia-ia.vercel.app
HTTP 200 OK
Servidor: Vercel
```

```txt
https://atendimento.totuscenografia.com.br
HTTP 200 OK
Servidor: nginx/Ubuntu + Chatwoot
```

```txt
https://totus-cenografia-ia.vercel.app/api/health/full
status: ok
neon: ok
anthropic: ok
redis: ok
chatwoot: ok
whatsapp.meta_configured: false
whatsapp.evolution_configured: true
openai: not_configured
```

## O que ja foi entregue

- Painel administrativo Next.js 14 no Vercel.
- Backend FastAPI Python serverless em `api/index.py`.
- Auth JWT para Guilherme.
- Banco Neon com schema `totus.*`.
- Chatwoot self-hosted proprio em `atendimento.totuscenografia.com.br`.
- Redis/Upstash com prefixo `totus:*`.
- BATCH_WINDOW de 10s para juntar mensagens.
- Deduplicacao por message id.
- Rate limit por telefone.
- Lock por telefone.
- Bloqueio de echo/outgoing.
- Brain da IA com rascunho, publicacao, versionamento e rollback.
- Persona baseada no Manual Mestre da Totus, com 37 secoes.
- Catalogo com 9 padroes Totus e precificacao por m2.
- Leads com memoria estruturada.
- Inbox/painel com conversas.
- Toggle global da IA.
- Toggle por conversa.
- Business hours configuravel.
- Fila de aprovacoes para mensagens financeiras/criticas.
- Cron de follow-up 48h, sempre indo para aprovacao.
- Dashboard com KPIs e graficos.
- Health check completo.
- Meta Cloud API implementada no codigo, aguardando env vars reais.
- Evolution fallback existente/configurado.
- Guardrails de aparencia humana: sem emojis, sem cliches, respostas curtas, sem markdown desnecessario.

## Decisoes importantes que tomamos

- Nao copiar a operacao do Rodrigo; reaproveitar arquitetura e aprendizados, mas com operacao separada.
- A Totus deve ter contexto, credenciais, branding, banco, Chatwoot, webhooks e memoria separados.
- O aprovador principal e Guilherme.
- O objetivo da IA nao e fechar contrato sozinha: ela qualifica, educa, sugere caminho e conduz para reuniao com arquiteto/produtor.
- Mensagens com valor alto, promessa critica, contrato, pagamento ou garantia devem ir para aprovacao humana.
- O Chatwoot e a caixa de atendimento unificada.
- Resposta manual humana no Chatwoot deve desativar a automacao naquela conversa.
- Follow-up automatico existe, mas deve cair em fila de aprovacao antes de enviar.
- WhatsApp real deve ser pela Meta API oficial quando Guilherme decidir.

## Coisas que descobrimos juntos

- O Manual Mestre da Totus tinha material suficiente para uma IA especializada, nao generica.
- O site da Totus confirmou posicionamento, portfolio, cases, marcas, promessa de prazo e fluxo comercial.
- A Totus precisa vender valor e experiencia, nao "stand barato".
- A IA deve usar os padroes 4, 6 e 8 como principais pontos de conversa.
- Estimativa pode existir, mas nao deve virar orcamento final nem promessa de fechamento.
- A IA deve puxar para reuniao com arquiteto/produtor quando o lead estiver quente.
- O projeto atual correto e `totus-cenografia-ia`, nao `totus-ai-concierge`.
- O health mostra que o sistema esta vivo, mas o WhatsApp Meta ainda esta desligado.
- OpenAI nao esta configurado como fallback hoje.
- O banco Neon e compartilhado com ForYou Leads, mas o isolamento acontece pelo schema `totus.*`.
- O VPS tambem tem stack do Rodrigo; nao tocar nos containers/configs da Concretize.

## Erros/problemas que tivemos e como corrigimos

### 1. Risco de clonar errado a IA do Rodrigo

Problema: no inicio a ideia parecia "copiar a IA para outro cliente".

Correcao: definimos a regra correta: copiar arquitetura e aprendizados, mas criar operacao nova e isolada para Totus.

### 2. Repo legado confundindo o estado

Problema: `totus-ai-concierge` existe localmente e tem estrutura antiga Vite/Lovable/FastAPI com persona superficial.

Correcao: identificamos que a fonte atual e `C:\Users\ynwwi\Projects\totus-cenografia-ia` e documentamos isso no vault.

### 3. Vercel function_size_exceeded / bundle perto de 250MB

Problema: SDK Anthropic deixou a funcao serverless grande demais para o limite do Vercel.

Correcao: removemos o SDK e usamos cliente HTTP direto em `api/_anthropic.py`.

Commit relacionado:

```txt
02fdccd perf: substituir SDK anthropic por client HTTP leve (resolve function_size_exceeded 250MB)
```

### 4. Chatwoot exigia source_id correto

Problema: criar conversa no Chatwoot falhava por requisito da API do inbox/contact_inbox.

Correcao: passamos a usar `source_id` vindo do `contact_inbox`.

Commit relacionado:

```txt
9b8a6ca fix(chatwoot): usar source_id do contact_inbox ao criar conversa (API inbox requirement)
```

### 5. create_task nao funcionava bem em serverless

Problema: sync do Chatwoot podia nao finalizar porque serverless encerra o ciclo da request.

Correcao: `sync_message` passou a ser aguardado diretamente com `await`.

Commit relacionado:

```txt
75a05fa fix(agent): await sync_message direto - create_task nao funciona em serverless
```

### 6. Mutacao com fetch_one precisava de commit

Problema: INSERT/UPDATE com RETURNING podia executar sem persistir corretamente.

Correcao: `fetch_one` passou a dar commit quando usado para mutation.

Commit relacionado:

```txt
e10df1a fix(db): commit em fetch_one quando for mutation (INSERT/UPDATE com RETURNING)
```

### 7. Header do Chatwoot com underscore era rejeitado

Problema: usar `api_access_token` quebrava porque Nginx/Chatwoot esperam header com hifen.

Correcao: usar `api-access-token`.

Commit relacionado:

```txt
a205eaf fix(chatwoot): usar api-access-token (hifen) - nginx rejeita underscores
```

### 8. Cron separado quebrou por import cross-folder no Vercel Python

Problema: `api/cron/follow-up.py` separado deu problema de imports no ambiente Vercel.

Correcao: cron ficou dentro de `api/index.py`.

Commit relacionado:

```txt
8e2ec71 fix(fase-g): cron follow-up movido para api/index.py (evita problema de imports cross-folder)
```

### 9. Business hours ficou aberto para teste

Problema: `respect_business_hours=False`, com janela 00:00-23:59 para todos os dias.

Correcao pendente: antes do go-live, reativar horario comercial real no painel ou no Neon.

### 10. Conta duplicada no Chatwoot

Problema: existe account correta da Totus e uma conta criada acidentalmente.

Correcao pendente: decidir se remove a account duplicada ou se move o usuario para a account correta.

### 11. chatwoot_synced nao reflete sync real

Problema: mensagens aparecem com `chatwoot_synced=false`, embora o sync aconteca.

Correcao pendente: criar `mark_synced(msg_id)` ou ajustar `save_message`.

### 12. sql/schema.sql desatualizado

Problema: arquivo de schema do repo nao representa todas as 13 tabelas atuais.

Correcao pendente: gerar dump do schema `totus` atual e atualizar `sql/schema.sql`.

### 13. Sem testes automatizados

Problema: validacao foi majoritariamente manual via curl, painel e logs.

Correcao pendente: adicionar pytest para backend e Playwright para frontend.

### 14. Sem fallback de IA configurado

Problema: Anthropic/Claude e o motor atual; OpenAI aparece `not_configured`.

Correcao pendente: implementar fallback Gemini/OpenAI antes de depender comercialmente da IA em alto volume.

### 15. Segredos espalhados em notas operacionais

Problema: notas de comandos/acessos guardam segredos operacionais. Isso ajuda a retomar, mas aumenta risco se o vault for compartilhado.

Correcao pendente: antes de entregar para Guilherme ou compartilhar qualquer nota, rotacionar senhas/tokens e mover segredos para gerenciador seguro.

### 16. Git remote local com token embutido

Problema descoberto em 2026-05-22: o remote `origin` local do repo `totus-cenografia-ia` contem um GitHub PAT embutido na URL.

Correcao pendente: trocar o remote para URL sem token e rotacionar o PAT. Nao registrar o token em chat nem em nova documentacao.

### 17. Erro de comando nesta sessao

Problema: uma busca em PowerShell falhou porque variaveis como `$file` e `$_.Name` foram interpoladas antes de chegar ao `rtk powershell.exe`.

Correcao: escapar variaveis com crase no comando interno, por exemplo `` `$file `` e `` `$_.Name ``.

## Pendencias bloqueantes antes do go-live

1. Configurar Meta WhatsApp Cloud API no Vercel:
   - `META_ACCESS_TOKEN`
   - `META_PHONE_NUMBER_ID`
   - `META_APP_SECRET`
2. Configurar webhook na Meta:
   - URL: `https://totus-cenografia-ia.vercel.app/api/webhook/message`
   - Verify token: `totus-webhook-verify-2026`
   - Subscribe: `messages`
3. Restaurar business hours real.
4. Resolver conta duplicada no Chatwoot.
5. Rotacionar senha do painel, senha Chatwoot, JWT secret, tokens e PAT GitHub.
6. Remover token embutido do remote Git local.
7. Validar persona da IA com Guilherme.
8. Fazer teste real end-to-end com WhatsApp.

## Pendencias importantes, mas nao bloqueantes

- Atualizar `sql/schema.sql`.
- Adicionar fotos reais dos padroes 4, 6 e 8 no catalogo.
- Corrigir `chatwoot_synced`.
- Adicionar logs em exceptions silenciosas.
- Adicionar testes automatizados.
- Implementar fallback Gemini/OpenAI.
- Implementar typing indicator quando Meta estiver plugada.
- Implementar tratamento de imagem/audio.
- Documentar politica de retencao/LGPD.

## Como continuar

1. Abrir o repo certo:

```powershell
cd C:\Users\ynwwi\Projects\totus-cenografia-ia
```

2. Checar estado:

```powershell
rtk git status
rtk curl.exe -sS https://totus-cenografia-ia.vercel.app/api/health/full
```

3. Antes de qualquer entrega para cliente, resolver seguranca:

```powershell
rtk git remote set-url origin https://github.com/ynwwilson/totus-cenografia-ia.git
```

Depois rotacionar o PAT no GitHub, senhas do painel/Chatwoot, JWT secret e tokens expostos em notas.

4. Proximo trabalho recomendado:

- Fase GO-LIVE WhatsApp Meta.
- Depois UAT com Guilherme.
- Depois hardening de seguranca/documentacao.

## Regra de ouro para proximas sessoes

Nao usar `totus-ai-concierge` como fonte. Sempre usar:

```txt
C:\Users\ynwwi\Projects\totus-cenografia-ia
```

E sempre abrir primeiro:

- [[00 - Overview]]
- [[08 - Pendências e Próximos Passos]]
- [[09 - Retomada 2026-05-22 - Status completo e memoria]]
