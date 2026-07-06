---
type: pending-issues
project: Totus Cenografia IA
date: 2026-05-18
tags: [pendencias, bugs, totus, roadmap]
---

# Pendências, Bugs e Próximos Passos

Relatório da auditoria de 2026-05-18 (após Fase G).

## 🔴 CRÍTICOS (resolver antes de ir pra produção)

### 1. WhatsApp ainda não plugado (esperado)
- **Status**: Esperando decisão do Guilherme sobre Meta API
- **Impacto**: Sistema funciona localmente mas não recebe mensagens reais ainda
- **Como resolver**: configurar `META_ACCESS_TOKEN`, `META_PHONE_NUMBER_ID`, `META_APP_SECRET` no Vercel e apontar webhook na Meta para `https://totus-cenografia-ia.vercel.app/api/webhook/message`
- **Verify token** já configurado: `totus-webhook-verify-2026`

### 2. Business hours desligado (configuração de teste)
- **Estado atual**: `respect_business_hours=False`, `0:00-23:59` em todos os dias
- **Como verificar**: SELECT * FROM totus.ai_settings;
- **Como corrigir**: via painel `/settings` ou direto no Neon:
```sql
UPDATE totus.ai_settings 
SET respect_business_hours = TRUE,
    business_hours_start = '08:00',
    business_hours_end = '20:00',
    business_days = ARRAY[1,2,3,4,5];
```

### 3. Conta Chatwoot duplicada
- **Sintoma**: Account 1 (Totus IA correta) + Account 2 (sobra, sem inbox)
- **Causa**: Alguém fez signup em `guilhermepcamargo@gmail.com` antes de eu fechar `ENABLE_ACCOUNT_SIGNUP`
- **Como decidir**: 
  - Apagar account 2 + user 2 (mais limpo)
  - OU mover user 2 (gmail) para account 1 como agent adicional
- **Como apagar (via Rails console)**:
```ruby
# SSH no VPS, depois:
cd /opt/chatwoot-totus && docker compose exec rails bundle exec rails console
# No console:
Account.find(2).destroy!
User.find_by(email: 'guilhermepcamargo@gmail.com').destroy!
```

## 🟡 IMPORTANTES (não bloqueiam, mas precisam atenção)

### 4. `chatwoot_synced` flag não atualizada
- **Sintoma**: 16/16 mensagens com `chatwoot_synced=FALSE` no Neon
- **Impacto**: Métricas/observability — sync acontece mas DB local não rastreia
- **Onde corrigir**: `api/_database.py::save_message` ou criar `mark_synced(msg_id)`
- **Severidade**: baixa (sync acontece, só não temos histórico)

### 5. Concretize Chatwoot em loop de restart
- **Sintoma**: `concretize-chatwoot-web-1 | Restarting (1) X seconds ago`
- **Por que importa**: Compartilha VPS conosco. Pode estar consumindo memória/CPU
- **Como verificar**: 
```bash
docker logs concretize-chatwoot-web-1 --tail 50
```
- **Ação**: AVISAR o Rodrigo (não tocar nessa stack)

### 6. SDK Anthropic removido (cliente HTTP próprio)
- **O que aconteceu**: SDK estourou 250MB do bundle Vercel
- **Solução implementada**: `api/_anthropic.py` com httpx direto
- **Limitação**: Não suporta streaming, prompt caching, vision (não usamos hoje)
- **Quando preocupar**: Se precisar de features avançadas Claude, considerar voltar SDK + lambda em vez de Vercel

### 7. Imports cross-folder no Vercel Python
- **Histórico**: Tentei criar `api/cron/follow-up.py` separado mas Vercel deu error
- **Solução**: Mantém tudo em `api/index.py` (cron + webhook + endpoints juntos)
- **Limitação**: Arquivo `index.py` está crescendo (~700 linhas)
- **Quando preocupar**: Se passar de 1500 linhas, refatorar em routers

## 🟢 MELHORIAS (futuro)

### 8. Sem fallback de IA
- **Atual**: Só Claude Sonnet 4.6. Se Anthropic cair, IA não responde
- **Sugestão Rodrigo**: Gemini 2.5 Flash-Lite como principal + OpenAI como fallback
- **Effort**: 1h pra implementar cadeia de fallback

### 9. Sem typing indicator
- **Atual**: Cliente envia → 10s batch + ~5s Claude → resposta aparece. Sem feedback intermediário
- **Como fazer**: Usar Meta API `messaging_product=whatsapp, status=typing` 
- **Effort**: 30 min quando Meta API estiver plugada

### 10. Sem image/audio handling
- **Atual**: Se cliente mandar foto, ignora
- **Próximo passo**: Claude Sonnet suporta vision — basta passar imagem como content
- **Effort**: 2h

### 11. SQL schema.sql desatualizado
- **Sintoma**: O arquivo `sql/schema.sql` tem só as 5 tabelas originais; as 8 novas (follow_ups, brain_versions, products, etc.) foram criadas via migration ad-hoc
- **Risco**: Quem clonar o repo não consegue recriar o banco
- **Como corrigir**: Gerar `pg_dump` do schema atual e substituir o `schema.sql`
```bash
pg_dump -s "postgresql://neondb_owner:..." -n totus > sql/schema.sql
```

### 12. Sem testes automatizados
- **Atual**: Tudo testado manualmente via curl/painel
- **Sugestão**: pytest para backend + Playwright para frontend
- **Effort**: 1-2 dias

### 13. Frontend SSR não bloqueia totalmente
- **Sintoma**: Painel carrega o HTML antes do redirect pra `/login`
- **Risco**: Mínimo (apenas flash visual, dados protegidos via API)
- **Como corrigir**: Middleware Next.js para SSR auth check

### 14. Exceções silenciosas
- **Padrão**: `except Exception: pass` em sentiment, lead extraction
- **Onde**: `api/_agent.py`
- **Risco**: Erros passam batidos
- **Sugestão**: Logar via Vercel logs (`print(f"[error] {e}")`)

## 📋 Checklist antes do GO LIVE com WhatsApp real

- [ ] Restaurar business_hours (8:00-20:00, dias úteis)
- [ ] Apagar account 2 do Chatwoot (decisão)
- [ ] Avisar Rodrigo sobre `concretize-chatwoot-web-1`
- [ ] Configurar Meta API:
  - [ ] Criar app em developers.facebook.com
  - [ ] WhatsApp → Cloud API → setup
  - [ ] Webhook URL: `https://totus-cenografia-ia.vercel.app/api/webhook/message`
  - [ ] Verify token: `totus-webhook-verify-2026`
  - [ ] Subscribe: `messages`
  - [ ] Capturar: `META_ACCESS_TOKEN`, `META_PHONE_NUMBER_ID`, `META_APP_SECRET`
  - [ ] Adicionar env vars no Vercel
- [ ] Trocar senha do painel (atualmente `Totus@2026!` — vazada nesta documentação)
- [ ] Trocar senha do Chatwoot (atualmente `Totus@Cenografia#2026!`)
- [ ] Trocar JWT_SECRET por outro (mais conservador)
- [ ] Adicionar fotos REAIS dos padrões 4, 6 e 8 em `/catalog`
- [ ] Validar persona da IA com Guilherme (`/brain`)
- [ ] Atualizar `sql/schema.sql` com schema atual completo
- [ ] Documentar política de retenção de dados (LGPD)

## 🚀 Roadmap pós-WhatsApp

1. **Tracking de leads no Chatwoot**: usar custom attributes para sincronizar lead memory
2. **Templates aprovados Meta**: botões interativos (sim/não, agendar reunião)
3. **Áudios**: transcrição automática via Whisper
4. **Imagens**: análise de fotos enviadas pelo cliente (referências visuais)
5. **Integração CRM externo**: HubSpot ou RD Station via webhook
6. **Dashboard advanced**: análise de sentimento ao longo do tempo, taxa de conversão por padrão
7. **Multi-user**: se Totus crescer e ter equipe atendendo
8. **A/B test**: variantes de mensagem da IA

## Atualizacao 2026-05-22 - estado verificado

Verificacao feita antes de continuar:

- Painel `https://totus-cenografia-ia.vercel.app`: HTTP 200.
- Chatwoot `https://atendimento.totuscenografia.com.br`: HTTP 200.
- `/api/health/full`: `status=ok`.
- Checks: Neon ok, Anthropic ok, Redis ok, Chatwoot ok.
- WhatsApp: `meta_configured=false`; `evolution_configured=true`.
- OpenAI fallback: `not_configured`.
- Repo correto: `C:\Users\ynwwi\Projects\totus-cenografia-ia`.
- Repo antigo/legado: `C:\Users\ynwwi\Projects\totus-ai-concierge`.
- Nova nota de memoria/retomada: [[09 - Retomada 2026-05-22 - Status completo e memoria]].

### Novo critico de seguranca

- O remote Git local do repo atual contem um GitHub PAT embutido na URL. Nao copiar o valor para chat/documentos.
- Acao antes de entrega: trocar o remote para URL limpa e rotacionar o PAT no GitHub.
- Existem segredos em notas operacionais antigas. Antes de compartilhar qualquer nota com Guilherme/terceiros, rotacionar senhas/tokens e mover segredos para um gerenciador seguro.
