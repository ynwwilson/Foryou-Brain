---
type: index
project: Totus Cenografia IA
date: 2026-05-18
tags: [totus, ia-atendimento, index]
---

# 📁 Totus Cenografia IA — Documentação completa

Pasta de notas no vault sobre o sistema de IA de atendimento da Totus.

## Navegação rápida

1. [[00 - Overview]] — Sumário executivo e arquitetura geral
2. [[01 - Credenciais e Acessos]] — 🔐 Todos logins, tokens, senhas (sensível)
3. [[02 - Infraestrutura]] — Mapa Vercel/Neon/VPS/Redis/Cloudflare
4. [[03 - Arquitetura]] — Fluxos detalhados (mensagem, handoff, cron)
5. [[04 - Backend API]] — 27 endpoints + arquivos Python
6. [[05 - Frontend Painel]] — 11 páginas Next.js
7. [[06 - Chatwoot Self-hosted]] — Como administrar
8. [[07 - Comandos e Scripts]] — Cheatsheet operacional
9. [[08 - Pendências e Próximos Passos]] — Bugs, melhorias, checklist GO LIVE

## Status atual (2026-05-18)

✅ Sistema **no ar** e estável
✅ 6 fases iniciais (A–F) + Fase G completa
✅ Chatwoot self-hosted funcionando
✅ Health check todos verdes
⏳ Aguardando plugar Meta API (decisão do Guilherme)
⚠️ 14 pendências identificadas (ver [[08 - Pendências e Próximos Passos]])

## URLs essenciais (cole no navegador)

- Painel: https://totus-cenografia-ia.vercel.app
- Chatwoot: https://atendimento.totuscenografia.com.br
- Repo: https://github.com/ynwwilson/totus-cenografia-ia
- Health: https://totus-cenografia-ia.vercel.app/api/health/full

## Quando precisar mexer

| Quero... | Vou em... |
|---|---|
| Login/senha | [[01 - Credenciais e Acessos]] |
| Comando do dia-a-dia | [[07 - Comandos e Scripts]] |
| Lista de o-que-falta | [[08 - Pendências e Próximos Passos]] |
| Entender fluxo da IA | [[03 - Arquitetura]] |
| Endpoint específico | [[04 - Backend API]] |
| Página específica | [[05 - Frontend Painel]] |
| Mexer no Chatwoot | [[06 - Chatwoot Self-hosted]] |

## Relacionado no vault

- [[IA de Atendimento Rodrigo]] — projeto de referência (Concretize)
- [[ForYou Code]] — empresa que está construindo

## Atualizacao 2026-05-22

- Sistema ainda online: painel HTTP 200, Chatwoot HTTP 200, health `status=ok`.
- WhatsApp Meta segue pendente: `meta_configured=false`.
- Evolution fallback aparece configurado.
- OpenAI fallback nao configurado.
- Repo certo: `C:\Users\ynwwi\Projects\totus-cenografia-ia`.
- Repo antigo `totus-ai-concierge` e legado e nao deve guiar a continuacao.
- Ver detalhes em [[09 - Retomada 2026-05-22 - Status completo e memoria]].
