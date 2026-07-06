---
type: chatwoot-docs
project: Totus Cenografia IA
tags: [chatwoot, totus, infra, vps]
---

# Chatwoot Self-hosted

URL: https://atendimento.totuscenografia.com.br

## Como acessar

1. Abrir https://atendimento.totuscenografia.com.br
2. Email: `guilherme@totuscenografia.com.br`
3. Senha: `Totus@Cenografia#2026!`

> ⚠️ Existe segunda conta `guilhermepcamargo@gmail.com` que foi criada acidentalmente antes de eu desabilitar signup. Ver pendências em [[08 - Pendências e Próximos Passos]].

## Configuração no VPS

| Item | Valor |
|---|---|
| Diretório | `/opt/chatwoot-totus/` |
| Containers | `totus-chatwoot-{web,sidekiq,db,redis}` |
| Versão | `chatwoot/chatwoot:latest` |
| Porta web (host) | `127.0.0.1:3001` |
| Porta postgres (host) | `127.0.0.1:5433` |
| Porta redis (host) | `127.0.0.1:6380` |
| Network Docker | `totus-chatwoot_totus` |
| Volumes | `totus-chatwoot_storage_data`, `_postgres_data`, `_redis_data` |
| Nginx vhost | `/etc/nginx/sites-enabled/totus` |
| SSL | `/etc/letsencrypt/live/atendimento.totuscenografia.com.br/` |

## Dados iniciais

- **Account ID 1**: "Totus Cenografia"
- **User 1**: Guilherme (SuperAdmin) — guilherme@totuscenografia.com.br
- **Inbox 1**: "Totus IA" (channel: `Channel::Api`)
  - Webhook URL: `https://totus-cenografia-ia.vercel.app/api/webhook/chatwoot`
- **User Access Token**: `pWGdmnFhVrZJCfa914FXFxLm`

## Integração com backend Totus

A IA do Totus espelha **todas as mensagens** (incoming + outgoing) no Chatwoot:

```python
# Em api/_agent.py
await _chatwoot.sync_message(phone, name, content, "incoming")  # cliente
# ... Claude responde ...
await _chatwoot.sync_message(phone, name, part, "outgoing")     # IA
```

E o Chatwoot manda webhook pro Totus quando humano responde:

```
Guilherme digita resposta no Chatwoot
→ Chatwoot dispara event: message_created (type=outgoing, sender.type=User)
→ POST https://totus-cenografia-ia.vercel.app/api/webhook/chatwoot
→ Backend: UPDATE conversations SET automation_disabled = TRUE WHERE phone = ...
→ Próxima msg do cliente NÃO é respondida pela IA (handoff humano)
```

## API Chatwoot — autenticação

⚠️ Header: **`api-access-token`** (com hífen, não underscore — nginx rejeita underscores).

```bash
# Exemplo: listar contatos
curl -H "api-access-token: pWGdmnFhVrZJCfa914FXFxLm" \
  https://atendimento.totuscenografia.com.br/api/v1/accounts/1/contacts
```

## Endpoints úteis Chatwoot API

```
GET  /api/v1/accounts/1/contacts            # listar contatos
GET  /api/v1/accounts/1/conversations       # listar conversas
GET  /api/v1/accounts/1/conversations/{id}/messages
POST /api/v1/accounts/1/conversations       # criar conversa
POST /api/v1/accounts/1/conversations/{id}/messages  # adicionar msg
POST /api/v1/accounts/1/contacts            # criar contato
GET  /api/v1/accounts/1/inboxes             # listar inboxes
```

Estrutura completa: https://www.chatwoot.com/developers/api/

## Comandos úteis no VPS

```bash
# SSH
ssh root@76.13.166.51   # senha: REy9LxN7fajG7.JK&t8B

# Status containers
docker ps --filter "name=totus-chatwoot"

# Logs do web
docker logs totus-chatwoot-web --tail 50 -f

# Logs sidekiq (jobs)
docker logs totus-chatwoot-sidekiq --tail 50

# Restart geral
cd /opt/chatwoot-totus && docker compose restart

# Acessar Rails console (debug)
cd /opt/chatwoot-totus && docker compose exec rails bundle exec rails console

# Postgres CLI direto
docker exec -it totus-chatwoot-db psql -U postgres chatwoot

# Backup volume postgres
docker run --rm -v totus-chatwoot_postgres_data:/data -v $(pwd):/backup alpine tar czf /backup/totus-chatwoot-db-$(date +%F).tar.gz /data

# Renovar SSL (automático mas pode forçar)
certbot renew --cert-name atendimento.totuscenografia.com.br
```

## Manutenção

### Atualizar versão Chatwoot
```bash
cd /opt/chatwoot-totus
docker compose pull
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
docker compose up -d
```

### Resetar senha do Guilherme via Rails
```ruby
# rails console
u = User.find_by(email: 'guilherme@totuscenografia.com.br')
u.password = 'NovaSenha123!'
u.password_confirmation = 'NovaSenha123!'
u.save!
```

### Criar novo access token
```ruby
u = User.find_by(email: 'guilherme@totuscenografia.com.br')
AccessToken.create!(owner: u)
# Pegar o .token gerado
```

## Webhook config (caso precise reconfigurar)

No painel Chatwoot:
1. Settings → Inboxes → Totus IA
2. Configuration → Webhook URL
3. Setar: `https://totus-cenografia-ia.vercel.app/api/webhook/chatwoot`
4. Subscribe to: `message_created`

Ou via API:
```bash
curl -X PUT https://atendimento.totuscenografia.com.br/api/v1/accounts/1/inboxes/1 \
  -H "api-access-token: pWGdmnFhVrZJCfa914FXFxLm" \
  -H "Content-Type: application/json" \
  -d '{"webhook_url":"https://totus-cenografia-ia.vercel.app/api/webhook/chatwoot"}'
```
