---
type: architecture
project: Totus Cenografia IA
tags: [architecture, totus, fluxo]
---

# Arquitetura & Fluxos

## Fluxo principal: mensagem do cliente

```
                                    [CLIENTE WhatsApp]
                                           │ (futuro: Meta API)
                                           ▼
                              ┌─────────────────────────┐
                              │   Webhook recebe        │
                              │   POST /api/webhook/    │
                              │       message           │
                              └────────────┬────────────┘
                                           │
                              ┌────────────▼────────────┐
                              │  Upstash Redis          │
                              │  • is_duplicate?  → 200 │
                              │  • rate_limited?  → 200 │
                              │  • enqueue_message      │
                              │  • acquire_lock         │
                              │     └─ falhou? → queued │
                              └────────────┬────────────┘
                                           │ (com lock)
                              ┌────────────▼────────────┐
                              │  BATCH_WINDOW 10s       │
                              │  (drain_queue)          │
                              └────────────┬────────────┘
                                           │
                              ┌────────────▼────────────┐
                              │  Chatwoot sync incoming │
                              │  (cria contato + conv)  │
                              └────────────┬────────────┘
                                           │
                              ┌────────────▼────────────┐
                              │  Verifica:              │
                              │  • is_ai_active?        │
                              │  • automation_disabled? │
                              │  • business_hours?      │
                              └────────────┬────────────┘
                                           │ (todas OK)
                              ┌────────────▼────────────┐
                              │  Claude Sonnet 4.6      │
                              │  + system prompt 37 sec │
                              │  + histórico 20 msgs    │
                              └────────────┬────────────┘
                                           │
                              ┌────────────▼────────────┐
                              │  Guardrails             │
                              │  • Remove emojis        │
                              │  • Remove clichês       │
                              │  • Fatia em até 5 partes│
                              │  • Detecta R$ alto      │
                              └────────────┬────────────┘
                                           │
                       ┌───────────────────┴───────────────────┐
                       │                                       │
                ┌──────▼──────┐                         ┌──────▼──────┐
                │ Aprovação?  │                         │ Resposta    │
                │ (financial  │                         │ normal      │
                │  ou crítica)│                         │             │
                └──────┬──────┘                         └──────┬──────┘
                       │                                       │
                ┌──────▼──────┐                         ┌──────▼──────┐
                │ Cria follow │                         │ Envia parts │
                │ _up status= │                         │ via WhatsApp│
                │ pending     │                         │ + Chatwoot  │
                │ + nota priv │                         │ sync OUT    │
                │ Chatwoot    │                         │             │
                └─────────────┘                         └──────┬──────┘
                                                               │
                                                        ┌──────▼──────┐
                                                        │ Extração de │
                                                        │ lead +      │
                                                        │ sentiment   │
                                                        └─────────────┘
```

## Fluxo: Guilherme responde manualmente

```
[Guilherme abre Chatwoot inbox]
       │
       │ vê conversa, digita resposta
       ▼
[Chatwoot dispara webhook]
       │ POST /api/webhook/chatwoot
       │ event: message_created, type: outgoing, sender: User
       ▼
[Backend detecta]
       │ "humano respondeu → desativa IA aqui"
       ▼
[UPDATE conversations SET automation_disabled=TRUE]
       │
       │ IA para naquela conversa específica
       │ próxima msg do cliente: SEM resposta automática
```

## Fluxo: Cron follow-up 48h

```
[Vercel Cron 13h ou 18h seg-sex]
       │ GET /api/cron/follow-up
       │ Authorization: Bearer ${CRON_SECRET}
       ▼
[Verifica AI ativa + business hours]
       │
       ▼
[Query Neon: conversas com última msg user > 48h E < 7d]
       │
       │ para cada conversa:
       ▼
[Não duplicar — pular se follow-up pendente nas últimas 24h]
       │
       ▼
[Claude gera 1 msg curta de follow-up]
       │ "Voltei aqui pra retomar. Conseguiu evoluir...?"
       ▼
[INSERT totus.follow_ups status=pending]
       │ "TODOS na fila de aprovação" (decisão)
       ▼
[Nota privada no Chatwoot: aguarda aprovação]
       │
       ▼
[Guilherme aprova no painel /approvals]
       │
       ▼
[Envia mensagem ao cliente]
```

## Padrão de aprovações

### Triggers automáticos

```python
# Em api/_agent.py — detect_approval_needed()

FINANCIAL_KEYWORDS = [
    "proposta", "orçamento final", "pix", "boleto",
    "transferência", "contrato", "assinatura",
    "preço final", "valor final", ...
]

CRITICAL_KEYWORDS = [
    "garanto", "prometo", "100%", "com certeza absoluta",
    "reclamação", "problema sério", "processo", ...
]

PRICE_REGEX = r"R\$\s*\d{1,3}(?:\.\d{3})+(?:,\d{2})?"
# Detecta R$ 1.000+ (valor com ponto separador de milhar)
```

Se IA gerar resposta com `R$ 50.000` ou "prometo entregar" → **não envia**, cria follow_up.

## Camadas de proteção da IA

1. **Toggle global** (`ai_settings.is_active`) — pausa tudo
2. **Toggle por conversa** (`conversations.automation_disabled`) — pausa só essa
3. **Business hours** (`ai_settings.business_hours_*`) — fora do horário, envia msg padrão
4. **`fromMe` detection** — humano responde via Chatwoot → desativa IA automaticamente
5. **Aprovações** — mensagens com keywords financeiras/críticas vão pra fila

## Persona — 37 seções do Manual Mestre

Arquivo: `api/_persona.py` (`SYSTEM_PROMPT`)

Seções principais:
1. Identidade Totus
2. Posicionamento (não-montadora, especialista premium)
3. Tom de voz
4. Papel da IA
5. Neuroarquitetura (8 princípios)
6. 5 estímulos neurossensoriais
7. Funil comportamental do visitante
8. 9 padrões de stand (R$ 1.497/m² → R$ 3.477+/m²)
9. Glossário (corredor, esquina, ilha)
10. Ativações comerciais
11. Categorias de área (até 30m², 30-100m², 100m²+)
12. Fluxo comercial 11 passos
13. Regra de apresentação dos padrões (4, 6, 8 primeiro)
14. 30 perguntas qualificadoras
15. Sistema 3-tier (cold/warm/hot)
16. 7 objeções + respostas
17. Simulador de orçamento
18. Gerador automático de conceito
19. Manual de personalidade IA
20. **REGRAS DE APARÊNCIA HUMANA** (adicionado fase G):
    - Zero emojis
    - Sem clichês ("Perfeito", "Entendo")
    - Mirroring de tom
    - Fatiamento `\n\n`
    - Sem markdown
    - Sem promessas vazias
    - Respostas curtas
21. Objetivo final: reunião com arquiteto + produtor

## Padrões Totus em produção

Cadastrados em `totus.products` (9 linhas):

| # | Nome | R$/m² | Brain context |
|---|---|---|---|
| 1 | Estrutura | 1.497 | Cliente testando feira pela 1ª vez |
| 2 | Estrutura+ | 1.697 | Cliente já participou de outras feiras |
| 3 | Profissional | 1.897 | B2B em feiras setoriais |
| 4 | **Intermediário** ⭐ | 2.240 | REFERÊNCIA PRINCIPAL (apresentar primeiro) |
| 5 | Tech | 2.487 | Cliente quer destacar produto tech |
| 6 | **Interativo** ⭐ | 2.735 | Feiras grandes >5000 visitantes |
| 7 | Sensorial | 2.982 | Luxo, gastronomia, perfumaria |
| 8 | **Imersivo** ⭐ | 3.230 | Grandes marcas, tecnologia imersiva |
| 9 | Full Experience | 3.477+ | Top-of-mind, projeto sob medida |

**Logística fora de SP**: R$ 22/km (ida+volta) + R$ 200/m² logística equipe
