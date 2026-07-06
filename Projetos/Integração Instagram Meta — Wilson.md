---
projeto: Integração Instagram Meta — Wilson
owner: Wilson (Mestre)
instagram: "@ynwwilson"
status: 🟡 em auditoria
criado: 2026-05-08
atualizado: 2026-05-08
tags: [projeto, instagram, meta, api, automação]
---

# Integração Instagram Meta — Wilson

> Painel mestre da integração entre o Instagram **@ynwwilson** e o Claude (via Meta for Developers + Composio).
> Toda rodada de auditoria, execução e credencial fica registrada aqui.

---

## 🎯 Objetivo final

Controle total do Instagram via API:
- Insights gerais da conta + por vídeo/post/reel/story
- Leitura e automação de DMs
- Publicação programada
- Moderação de comentários
- Relatórios automáticos
- Integração com o stack ForYou Code (Supabase, Vercel, Composio)

---

## 🧭 Estado atual

| Frente | Status | Última atualização |
|---|---|---|
| App no Meta for Developers | 🔴 a verificar | 2026-05-08 |
| Conta Instagram em modo Business/Creator | 🔴 a verificar | — |
| Página Facebook vinculada | 🔴 a verificar | — |
| Business Manager + Verification | 🔴 a verificar | — |
| Permissões aprovadas (App Review) | 🔴 a verificar | — |
| Tokens (App, User Long-Lived, Page) | 🔴 a verificar | — |
| Webhooks configurados | 🔴 a verificar | — |
| Conexão via Composio | 🔴 a verificar | — |

Legenda: ✅ Pronto · ⚠️ Parcial · 🔴 Falta · ⛔ Bloqueador

---

## 🔄 Fluxo macro

1. **Auditar** o que já existe → preencher tabela de status
2. **Roadmap** do que falta, em ordem de dependência
3. **Executar** prompt a prompt na extensão do Claude
4. **Coletar credenciais** (App ID, Secret, tokens, IDs)
5. **Plugar no Composio** + testar leitura de insights e DMs
6. **Ativar webhooks** para automação em tempo real
7. **Construir relatórios** em cima da API

---

## 📋 Prompt 1 — AUDITORIA (rodar primeiro)

> Cole inteiro na extensão do Claude com `developers.facebook.com` aberto e logado.

```text
# AUDITORIA META FOR DEVELOPERS — INSTAGRAM @ynwwilson

Sou Wilson (Mestre). Instagram: @ynwwilson.
Objetivo final: controle total do meu Instagram via API — insights gerais e por vídeo,
DMs (leitura, automação de respostas), publicação, comentários, relatórios.

## SUA TAREFA NESTA PASSADA
AUDITORIA COMPLETA. NÃO altere NADA. Só verifique, registre evidência e reporte.
Use screenshots em telas críticas (Dashboard, App Review, Permissions, Token Debugger).

## ROTEIRO — passe por CADA item, nesta ordem:

### 1. Apps existentes
- Liste todos os apps na minha conta de developer
- Para o app dedicado ao Instagram: ID, nome, tipo (Business?), modo (Development/Live),
  data de criação, dono
- Se não existir → marcar 🔴 [CRIAR APP BUSINESS]

### 2. Configurações > Básico
- App Domains
- URL Política de Privacidade
- URL Termos de Serviço
- Ícone (1024x1024)
- Categoria
- Email de contato verificado
- Business Account vinculado ao app

### 3. Produtos adicionados (verificar se cada um está adicionado)
- [ ] Instagram (Instagram API with Instagram Login OU Instagram API with Facebook Login)
- [ ] Facebook Login for Business
- [ ] Webhooks
- [ ] Messenger Platform (para Instagram Messaging)
- [ ] Marketing API (futuro: ads)

### 4. Permissões e Funcionalidades
Status de cada uma (None / Standard Access / Advanced Access):
- instagram_business_basic
- instagram_business_content_publish
- instagram_business_manage_messages
- instagram_business_manage_comments
- instagram_business_manage_insights
- instagram_basic
- instagram_manage_insights
- instagram_manage_comments
- instagram_manage_messages
- instagram_content_publish
- pages_show_list
- pages_read_engagement
- pages_manage_metadata
- business_management

### 5. App Review
- O que já foi submetido
- O que foi aprovado
- O que ainda falta solicitar
- Vídeos screencast já gravados? Quais permissions exigem screencast?

### 6. Conta Instagram (@ynwwilson)
- Aparece conectada ao app?
- Está em modo Business ou Creator? (Personal não serve — trocar)
- Tem Página do Facebook vinculada?
- A Página está no Business Manager?

### 7. Business Manager / Meta Business Suite
- Business Manager existe?
- Conta verificada (Business Verification)?
- Domínio verificado?
- Data Use Checkup em dia?
- 2FA ativo nos admins?

### 8. Tokens e credenciais (só checar existência/validade, NÃO copiar valor agora)
- App ID
- App Secret (existe? última rotação?)
- User Access Token (existe? long-lived? expira quando?)
- Page Access Token
- Instagram Business Account ID identificado
- Token Debugger: rodar em cada token e reportar scopes + validade

### 9. Webhooks
- Configurado?
- Callback URL
- Verify Token configurado
- Subscriptions ativas: messages, messaging_postbacks, comments, mentions,
  story_insights, message_reactions, message_reads, live_comments
- Última entrega bem-sucedida?

### 10. Roles e acesso
- Quem tem acesso ao app (Admins, Developers, Testers)
- Test users configurados (se app em Dev Mode)

### 11. Configurações avançadas
- Server IP Allowlist
- Update Notifications email
- Data Protection Officer
- Restrições de plataforma (iOS/Android/Web)

## OUTPUT OBRIGATÓRIO

### Parte 1 — Tabela de status
| # | Item | Status | Evidência | Detalhe |
|---|---|---|---|---|
Status: ✅ Pronto / ⚠️ Parcial / 🔴 Falta / ⛔ Bloqueador

### Parte 2 — Roadmap do que falta
Lista numerada por DEPENDÊNCIA (o que precisa vir antes do quê) até chegar a 100%.

### Parte 3 — Configurações benéficas NÃO ativadas
- Webhooks que poderia ligar
- Permissões adicionais úteis para insights/DM/automação
- Métricas extras (reels insights, stories insights, audience demographics)
- Recursos da Meta Business Suite

### Parte 4 — Riscos detectados
Token exposto, App Secret antigo, app Live sem proteção, permissions a mais que o
necessário, etc.

### Parte 5 — Credenciais a extrair (em prompt seguinte)
- App ID
- App Secret (regenerar se for o caso)
- User Access Token (long-lived, 60d)
- Page Access Token
- Page ID
- Instagram Business Account ID
- Webhook Verify Token

### Parte 6 — Próximo prompt
Me entregue o TEXTO do próximo prompt que devo colar em você, em ordem,
para resolver o item de maior prioridade detectado.

## REGRAS DURAS
- NÃO altere nada nesta passada. Só audite.
- NÃO cole valores de App Secret nem tokens completos no relatório (use ••••últimos 4 chars).
- Se cair login ou permission for negada, avise e continue de onde der.
- Em cada bloqueador, indique o passo manual exato (clique a clique) que destrava.
```

---

## 📥 Resultado da auditoria

> Cole aqui o output que a extensão devolver. Eu uso isso pra atualizar a tabela de
> estado atual e gerar o próximo prompt.

```
[a preencher após rodar Prompt 1]
```

---

## 🧱 Próximos prompts (versionados)

> Cada nova passada vira um Prompt 2, 3, 4… aqui embaixo. Sempre indicando objetivo,
> pré-requisito e regra de segurança.

### Prompt 2 — [a definir após auditoria]
Pré-requisito: Prompt 1 executado.
Objetivo: a definir.

```
[a gerar com base no resultado da auditoria]
```

---

## 🔐 Cofre de credenciais

> ⚠️ NÃO colar tokens completos aqui no vault. Apenas referências e últimos 4 chars.
> Tokens completos vão pra `.env` local + Composio (vault deles).

| Credencial | Local seguro | Últimos 4 chars | Expira em | Última rotação |
|---|---|---|---|---|
| App ID | público (pode ficar aqui) | — | — | — |
| App Secret | .env + Composio | `••••` | — | — |
| User Long-Lived Token | Composio | `••••` | — | — |
| Page Access Token | Composio | `••••` | — | — |
| Page ID | aqui (público) | — | — | — |
| IG Business Account ID | aqui (público) | — | — | — |
| Webhook Verify Token | .env + servidor | `••••` | — | — |

---

## 📚 Recursos úteis

- Meta for Developers: https://developers.facebook.com/
- Meta Business Suite: https://business.facebook.com/
- Token Debugger: https://developers.facebook.com/tools/debug/accesstoken/
- Graph API Explorer: https://developers.facebook.com/tools/explorer/
- Instagram Graph API docs: https://developers.facebook.com/docs/instagram-api/
- Webhooks for Instagram: https://developers.facebook.com/docs/instagram-api/guides/webhooks
- Composio: https://composio.dev/

---

## 🗓 Histórico de execuções

- **2026-05-08** — Painel criado. Prompt 1 (auditoria) preparado, aguardando execução na extensão Claude.
