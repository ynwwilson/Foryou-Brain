---
type: cheatsheet
project: Totus Cenografia IA
tags: [comandos, devops, totus]
---

# Comandos & Scripts úteis

## Diretórios locais

| Local | Caminho |
|---|---|
| Repositório código | `C:\Users\ynwwi\Projects\totus-cenografia-ia` |
| Notas vault Obsidian | `C:\Users\ynwwi\Projects\claude-novo\stark\Stark\Projetos\Totus Cenografia IA\` |
| Plano arquivado | `C:\Users\ynwwi\.claude\plans\wise-knitting-brooks.md` |

## Git / Deploy

```bash
cd C:/Users/ynwwi/Projects/totus-cenografia-ia

# Status
rtk git status

# Commit + push (auto-deploy Vercel)
rtk git add -A
rtk git commit -m "feat: descrição"
rtk git push origin main

# Ver últimos deploys
# (Vercel dashboard: https://vercel.com/yngomesmarco-hues-projects/totus-cenografia-ia)
```

## SSH no VPS

```bash
ssh root@76.13.166.51
# Senha: REy9LxN7fajG7.JK&t8B
```

## Migrations Neon (Python script)

```python
import psycopg2
conn = psycopg2.connect("postgresql://neondb_owner:npg_jQC7Ylp5iZdz@ep-shiny-cell-ac9qba4n-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require")
cur = conn.cursor()
cur.execute("ALTER TABLE totus.messages ADD COLUMN ...")
conn.commit()
```

## Testar endpoints

### Health
```bash
curl https://totus-cenografia-ia.vercel.app/api/health/full
```

### Login
```bash
curl -X POST https://totus-cenografia-ia.vercel.app/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"guilherme@totus.com","password":"Totus@2026!"}'
```

### Webhook (simular WhatsApp incoming)
```bash
curl -X POST https://totus-cenografia-ia.vercel.app/api/webhook/message \
  -H "Content-Type: application/json" \
  -d '{
    "phone": "5511999998888",
    "text": "Quero stand pra feira em SP",
    "name": "Cliente Teste",
    "message_id": "manual_test_001"
  }'
```

### Cron manual (precisa do CRON_SECRET)
```bash
# Pegar secret do Vercel via API
# Authorization: Bearer <CRON_SECRET>
curl -X POST https://totus-cenografia-ia.vercel.app/api/cron/follow-up \
  -H "Authorization: Bearer ab206e0d72339e2e575b..."
```

## VPS: gerenciar Chatwoot

```bash
# Status
docker ps --filter "name=totus-chatwoot"

# Restart
cd /opt/chatwoot-totus && docker compose restart

# Logs ao vivo
docker logs -f totus-chatwoot-web
docker logs -f totus-chatwoot-sidekiq

# Postgres
docker exec -it totus-chatwoot-db psql -U postgres chatwoot
# Comandos PSQL: \dt, \du, SELECT * FROM accounts;

# Rails console (debug)
cd /opt/chatwoot-totus && docker compose exec rails bundle exec rails console
```

## VPS: nginx

```bash
# Test config
nginx -t

# Reload
systemctl reload nginx

# Vhost da Totus
cat /etc/nginx/sites-enabled/totus

# Logs nginx
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

## VPS: SSL renew

```bash
# Verificar certificados
certbot certificates

# Renovar
certbot renew

# Renovar específico
certbot renew --cert-name atendimento.totuscenografia.com.br
```

## Redis (Upstash): consultar via curl

```bash
# PING
curl -X POST https://precious-flea-91141.upstash.io \
  -H "Authorization: Bearer gQAAAAAAAWQFAAIncDIwZDM2Zjc3OGI4Mjg0NGIwOTExMmE4NmJjNjcwMzAwYnAyOTExNDE" \
  -H "Content-Type: application/json" \
  -d '["PING"]'

# Listar todas chaves totus:
curl -X POST https://precious-flea-91141.upstash.io \
  -H "Authorization: Bearer gQAAAAAAAWQFAAIncDIwZDM2Zjc3OGI4Mjg0NGIwOTExMmE4NmJjNjcwMzAwYnAyOTExNDE" \
  -H "Content-Type: application/json" \
  -d '["KEYS","totus:*"]'

# Limpar fila (DEBUG)
curl -X POST https://precious-flea-91141.upstash.io \
  -H "Authorization: Bearer ..." \
  -d '["DEL","totus:msgs:5511999998888"]'
```

## Chatwoot API

```bash
# Listar contatos
curl https://atendimento.totuscenografia.com.br/api/v1/accounts/1/contacts \
  -H "api-access-token: pWGdmnFhVrZJCfa914FXFxLm"

# Criar mensagem manual
curl -X POST https://atendimento.totuscenografia.com.br/api/v1/accounts/1/conversations/1/messages \
  -H "api-access-token: pWGdmnFhVrZJCfa914FXFxLm" \
  -H "Content-Type: application/json" \
  -d '{"content":"Mensagem teste","message_type":"outgoing","private":false}'
```

## Cloudflare DNS

```bash
# Listar records
CF_TOKEN=[REDACTED-CLOUDFLARE]
ZONE=17c89f9ee2f60ba8779fb7ecb8fa8c92

curl https://api.cloudflare.com/client/v4/zones/$ZONE/dns_records \
  -H "Authorization: Bearer $CF_TOKEN"
```

## Vercel: redeploy manual

Via dashboard: https://vercel.com/yngomesmarco-hues-projects/totus-cenografia-ia → Deployments → Redeploy

Via API:
```bash
VERCEL_TOKEN=[REDACTED-VERCEL]
TEAM=team_uZU2DYDtmcTe4QYFnquE3EqJ
PROJECT=prj_1uOKfMMIOdCcjePb4PMgGWHAbnLZ

curl -X POST "https://api.vercel.com/v13/deployments?teamId=$TEAM" \
  -H "Authorization: Bearer $VERCEL_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"name\":\"totus-cenografia-ia\",
    \"project\":\"$PROJECT\",
    \"target\":\"production\",
    \"gitSource\":{\"type\":\"github\",\"repoId\":1242536912,\"ref\":\"main\"}
  }"
```

## Debug rápido

### Painel não autentica
- Limpar `localStorage.totus_token` no browser
- Verificar `/api/auth/login` retorna 200 + token
- Verificar `/api/auth/me` valida (com Bearer)

### Chatwoot retorna 401
- Header deve ser `api-access-token` (hífen, não underscore)
- Token: `pWGdmnFhVrZJCfa914FXFxLm`

### Mensagem não responde
1. Verificar `is_ai_active` em `totus.ai_settings`
2. Verificar `automation_disabled` na conversa específica
3. Verificar business hours
4. Verificar Redis lock pendurado: `DEL totus:lock:{phone}`

### IA respondendo errado
1. Editar `/brain` no painel
2. Publicar nova versão em `/publication`
3. Se necessário, rollback para versão anterior

### VPS sem RAM
```bash
free -h
docker stats --no-stream
# Se concretize-chatwoot-web continua em loop de restart, está consumindo memória
```

## ALERTA 2026-05-22 - sensivel

Esta nota contem comandos historicos com tokens/senhas. Nao compartilhar fora do vault. Antes de entregar o projeto ao Guilherme ou a terceiros:

1. Rotacionar senhas do painel e Chatwoot.
2. Rotacionar JWT secret, tokens Vercel/Cloudflare/Upstash/Chatwoot.
3. Trocar o remote Git local para URL sem token.
4. Mover segredos para gerenciador seguro.
