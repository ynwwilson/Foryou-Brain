# Safety — Red Lines, Confirmação e Tripla Confirmação

> Atualizado 2026-03-31. Regras alinhadas com CLAUDE.md do claude-novo.

## Confirmação simples (toda ação real via Composio, Dev Browser ou Manus)

Antes de qualquer ação externa, mostrar e aguardar:

```
⚠️ VOU EXECUTAR:
[descrição clara]
[alvo: app/conta/destinatário]

Responda CONFIRMO para prosseguir.
```

## Tripla confirmação (ações críticas)

## Quando usar este skill

Este skill é ativado AUTOMATICAMENTE antes de qualquer ação das categorias abaixo.
Não é opcional. Não é ignorável. É parte do protocolo.

---

## Red Lines — Ações Bloqueadas

As seguintes ações **NUNCA** são executadas sem tripla confirmação:

1. Deletar arquivos, pastas ou diretórios (rm, del, rmdir, shutil.rmtree, fs.unlink)
2. Excluir dados em banco de dados (DELETE sem WHERE, DROP TABLE, truncate)
3. Deletar projetos, deployments, DNS records em ferramentas externas
4. Realizar compras, assinar planos, usar cartão
5. Transferir ou movimentar dinheiro
6. Excluir emails, eventos, contatos, arquivos Google
7. Remover domínios ou configs no Cloudflare
8. Cancelar assinaturas ou planos ativos
9. Apagar histórico de conversas ou sessões
10. Modificar openclaw.json ou configs críticas de sistema
11. Qualquer comando com `rm -rf`, `del /f`, `format`, `DROP`, `TRUNCATE`

---

## Protocolo de Tripla Confirmação

Quando detectar ação bloqueada:

### Etapa 1 — Aviso

```
⚠️ AÇÃO IRREVERSÍVEL DETECTADA

Ação: [descrição clara do que vai ser feito]
Alvo: [arquivo/banco/serviço/dados afetados]

Você tem CERTEZA? Responda SIM ou NÃO.
```

→ Aguardar resposta. Se NÃO (ou qualquer outra coisa) → CANCELA + registra em audit.log + para aqui.

### Etapa 2 — Reconfirmação

```
🔴 Esta ação NÃO pode ser desfeita. Dados serão perdidos permanentemente.

Confirma de novo? Responda SIM ou NÃO.
```

→ Aguardar resposta. Se NÃO → CANCELA + registra + para.

### Etapa 3 — Confirmação Final

```
⛔ ÚLTIMA CHANCE. Não há volta.

Digite exatamente: CONFIRMO
(qualquer outra resposta cancela automaticamente)
```

→ Aguardar resposta. Só prossegue se a resposta for exatamente `CONFIRMO` (maiúsculas).
→ Qualquer outra coisa → CANCELA + registra.

---

## Após Executar Ação Irreversível

Depois de executar (se confirmado): registrar no audit log:

```bash
python /root/stark/scripts/audit_log.py log \
  --action "delete_file" \
  --target "/path/to/file" \
  --result "success" \
  --confirmed true
```

---

## Rate Limiter — Verificar antes de Executar

Antes das ações abaixo, verificar se o limite foi atingido:

```bash
# Verificar se pode executar
python /root/stark/scripts/rate_limiter.py check --action exec_shell

# Registrar execução (chamar após executar)
python /root/stark/scripts/rate_limiter.py record --action exec_shell
```

| Ação (--action) | Limite | Período |
|---|---|---|
| api_call | 5 | por minuto |
| subagent_spawn | 1 | por 30 min |
| cron_execution | 3 | por hora |
| file_write | 10 | por hora |
| message_send | 20 | por hora |
| exec_shell | 15 | por hora |

Se o check retornar `LIMIT_REACHED`: esperar até próximo período.
Se for ação crítica (tripla confirmação): executar mesmo com limite, mas registrar em audit.log.

---

## Fluxo Completo (resumo)

```
Receber pedido de ação
  → É Red Line? → SIM → Tripla confirmação → CONFIRMO? → Executa + Audit
                       → NÃO ou sem resposta → Cancela + Audit
  → Não é Red Line → Rate limit check → OK → Executa + Rate record
                                      → LIMIT_REACHED → Aguarda
```

---

## Registrar no Audit Log (sempre)

Qualquer ação importante (executada OU cancelada) deve ser registrada:

```bash
# Ação executada
python /root/stark/scripts/audit_log.py log \
  --action "TIPO" \
  --target "ALVO" \
  --result "success|cancelled|error" \
  --confirmed true|false \
  --details "contexto adicional"

# Ver últimos logs
python /root/stark/scripts/audit_log.py tail --n 20
```

O arquivo de log fica em: `memory/audit.log` (formato JSONL)
