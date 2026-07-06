---
tipo: referência
criado: 2026-05-27
atualizado: 2026-05-27
fonte: sessão "[[2026-05-27 23h45 - Aprimoramento Arsenal IA + Empresa-IA ForYou Code]]"
status: 0/26 coletadas
---

# Credenciais a Coletar

26 credenciais que Mestre precisa coletar **offline** e salvar no **Bitwarden**. Nunca passar por chat IA.

## ⚠️ Regras de ouro

1. **Nunca** colar credencial em chat de IA — vault auto-sync expõe pra Marco/Eduardo
2. **Nunca** commitar arquivo `.env` no git
3. **Sempre** usar `.gitignore` blindando `.env`
4. **Variáveis sensíveis** marcar com "Resolicitar senha principal" no Bitwarden
5. **Anotações**: data criação + validade + scopes + URL pra regenerar

## Onde guardar

- **Cofre humano mestre:** Bitwarden Free (https://bitwarden.com/pricing/)
- **Por projeto local:** `.env` na raiz, listado no `.gitignore`
- **Globais (várias projetos):** variáveis de ambiente Windows via `[Environment]::SetEnvironmentVariable(...)`
- **Futuro (empresa-IA 24/7):** Doppler ou Infisical

---

## Lista completa

### 🔴 Essenciais — tech/infra (8)

| # | Plataforma | Tipo | Onde pegar | ✓ |
|---|---|---|---|---|
| 1 | GitHub | Personal Access Token (PAT) | https://github.com/settings/tokens → Generate (classic) → scope `repo` + `workflow` | ☐ |
| 2 | Vercel | API Token | https://vercel.com/account/tokens | ☐ |
| 3 | Cloudflare | API Token | https://dash.cloudflare.com/profile/api-tokens → template "Edit zone DNS" | ☐ |
| 4 | Resend | API Key | https://resend.com/api-keys | ☐ |
| 5 | Supabase | Service Role Key + Project URL | https://supabase.com/dashboard/project/_/settings/api | ☐ |
| 6 | Modal (Imerso) | Token ID + Secret | https://modal.com/settings/tokens | ☐ |
| 7 | Anthropic | API Key | https://console.anthropic.com/settings/keys | ☐ |
| 8 | OpenAI (Codex) | API Key | https://platform.openai.com/api-keys | ☐ |

### 🟡 Telegram (3)

| # | Plataforma | Tipo | Onde pegar | ✓ |
|---|---|---|---|---|
| 9 | Telegram Bot | Bot Token | Conversar com **@BotFather** → `/newbot` | ☐ |
| 10a | Telegram | Seu Chat ID | Conversar com **@userinfobot** | ☐ |
| 10b | Telegram | Chat ID do Marco | (Marco conversa com @userinfobot) | ☐ |
| 10c | Telegram | Chat ID do Eduardo | (Eduardo conversa com @userinfobot) | ☐ |

### 🟡 Social (pra automação marketing — 6)

| # | Plataforma | Tipo | Onde pegar | ✓ |
|---|---|---|---|---|
| 11 | Meta (Instagram + Facebook + Threads) | Long-Lived User Access Token (60 dias) | https://developers.facebook.com/apps → criar app → Graph API Explorer | ☐ |
| 12 | TikTok | Business API Access Token | https://business-api.tiktok.com/portal/apps | ☐ |
| 13 | YouTube | Data API v3 Key + OAuth Client | https://console.cloud.google.com/apis/credentials | ☐ |
| 14 | LinkedIn | API Access Token | https://www.linkedin.com/developers/apps | ☐ |
| 15 | Reddit | API Client ID + Secret | https://www.reddit.com/prefs/apps → create app (script) | ☐ |
| 16 | X / Twitter (US$100/mês básico) | API v2 Bearer Token | https://developer.twitter.com/en/portal/dashboard | ☐ |

### 🟡 Comercial / CRM (4)

| # | Plataforma | Tipo | Onde pegar | ✓ |
|---|---|---|---|---|
| 17 | Okara | API Key | https://okara.ai → criar conta Free → Settings/API | ☐ |
| 18 | Zernio | API Key | https://zernio.com → criar conta → Settings/API | ☐ |
| 19 | HubSpot | Private App Token | https://app.hubspot.com → Settings → Integrations → Private Apps | ☐ |
| 20 | DocuSign | Integration Key + User ID | https://account.docusign.com/admin/api-and-keys | ☐ |

### 🟢 Monitoramento (2)

| # | Plataforma | Tipo | Onde pegar | ✓ |
|---|---|---|---|---|
| 21 | UptimeRobot | API Key (Main) | https://uptimerobot.com/dashboard.php#mySettings | ☐ |
| 22 | Better Uptime (alternativa) | API Token | https://betteruptime.com/team-billing | ☐ |

### 🟢 Opcionais (4)

| # | Plataforma | Tipo | Onde pegar | ✓ |
|---|---|---|---|---|
| 23 | QuickBooks (via Anthropic SMB) | OAuth Client | https://developer.intuit.com | ☐ |
| 24 | Sentry (error tracking) | DSN | https://sentry.io → Project Settings → SDK Setup | ☐ |
| 25 | Calendly | Personal Access Token | https://calendly.com/integrations/api_webhooks | ☐ |
| 26 | Canva | Connect API | https://www.canva.com/developers/apps | ☐ |

---

## Padrão de salvamento no Bitwarden

Modelo de Anotações (copia e ajusta):

```
Criado: AAAA-MM-DD
Expira: AAAA-MM-DD (ou "nunca")
Scopes/Permissões: <lista>
Usado por: <agentes/projetos>
Como regenerar: <URL exata>
Observação: <qualquer alerta>
```

Sugestão de pastas no Bitwarden:
- `ForYou Code / Tech` (1-8, 21-22)
- `ForYou Code / Telegram` (9, 10a/b/c)
- `ForYou Code / Marketing` (11-16)
- `ForYou Code / Comercial` (17-20)
- `ForYou Code / Opcionais` (23-26)

---

## Cuidado especial

⚠️ **NÃO** colar credencial em:
- Chat de IA (Claude Code, Claude.ai, ChatGPT, Codex, etc)
- Markdown aberto no vault
- Issue/PR público no GitHub
- WhatsApp/Telegram do trio (auto-save salva!)
- Print de tela compartilhado

⚠️ **NUNCA** compartilhar com Marco/Eduardo:
- Banco
- Anthropic API Key
- Cartão de crédito
- Acesso admin do GitHub
- Acesso admin Vercel

Eles têm escopo limitado de operação (CMO/CRO).

---

## Conexões

- Sessão origem: [[2026-05-27 23h45 - Aprimoramento Arsenal IA + Empresa-IA ForYou Code]]
- Estrutura empresa-IA: [[Empresa-IA ForYou Code — Estrutura]]
- Arsenal: [[Arsenal IA ForYou Code]]
