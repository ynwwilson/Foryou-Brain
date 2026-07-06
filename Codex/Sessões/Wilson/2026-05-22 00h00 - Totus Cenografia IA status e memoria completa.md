---
date: 2026-05-22
tool: codex
title: "Totus Cenografia IA - status e memoria completa"
model: openai
tags: [codex, sessao, totus, obsidian, memoria]
---

# Totus Cenografia IA - status e memoria completa

## Pedido do Mestre

Salvar no Obsidian tudo sobre o estado da IA Totus Cenografia, incluindo o que fizemos, erros, correcoes, descobertas, pendencias e como continuar depois.

## O que foi verificado nesta sessao

- Lida a nota global mais recente de `Codex/Sessões/`.
- Buscadas referencias a Totus, Guilherme e Cenografia no vault.
- Identificado que existem dois repos locais:
  - `C:\Users\ynwwi\Projects\totus-ai-concierge` = legado/antigo.
  - `C:\Users\ynwwi\Projects\totus-cenografia-ia` = projeto atual correto.
- Verificado que o repo atual esta em `main...origin/main`.
- Ultimo commit atual: `12d450d fix: harden totus ai operations`.
- Verificado painel em producao: `https://totus-cenografia-ia.vercel.app` retornou HTTP 200.
- Verificado Chatwoot: `https://atendimento.totuscenografia.com.br` retornou HTTP 200.
- Verificado health: `https://totus-cenografia-ia.vercel.app/api/health/full` retornou `status: ok`.

## Estado tecnico atual

- Neon: ok.
- Anthropic/Claude: ok/configurado.
- Redis/Upstash: ok.
- Chatwoot: ok.
- Meta WhatsApp: `meta_configured=false`.
- Evolution fallback: `evolution_configured=true`.
- OpenAI fallback: `not_configured`.

Conclusao: plataforma esta online e pronta em estrutura, mas WhatsApp real via Meta ainda nao esta plugado.

## Arquivos atualizados/criados no Obsidian

- Criado: `Projetos/Totus Cenografia IA/09 - Retomada 2026-05-22 - Status completo e memoria.md`.
- Atualizado: `Projetos/Totus Cenografia IA/00 - Overview.md`.
- Atualizado: `Projetos/Totus Cenografia IA/08 - Pendências e Próximos Passos.md`.
- Atualizado: `Projetos/Totus Cenografia IA/README.md`.
- Atualizado: `Projetos/Totus Cenografia IA/07 - Comandos e Scripts.md`.
- Atualizado: `Caminhos.md`.

## O que ficou registrado

- Status real de producao.
- Repositorio correto.
- Aviso de que `totus-ai-concierge` e legado.
- URLs vivas.
- Health checks.
- Entregas ja feitas.
- Decisoes de arquitetura e negocio.
- Descobertas sobre Totus, Manual Mestre, site, padroes e fluxo comercial.
- Erros tecnicos encontrados e correcoes feitas.
- Pendencias bloqueantes para go-live.
- Pendencias importantes nao bloqueantes.
- Alerta de seguranca sobre segredos em notas e token embutido no Git remote local.
- Como continuar na proxima sessao.

## Proximo passo recomendado

Antes de go-live:

1. Remover token do remote local e rotacionar o PAT.
2. Rotacionar senhas/tokens que aparecem em notas operacionais.
3. Configurar Meta WhatsApp Cloud API no Vercel.
4. Configurar webhook Meta para `/api/webhook/message`.
5. Restaurar business hours real.
6. Resolver conta duplicada do Chatwoot.
7. Validar persona com Guilherme.
8. Fazer teste end-to-end com WhatsApp real.

Nota principal para abrir primeiro:

```txt
Projetos/Totus Cenografia IA/09 - Retomada 2026-05-22 - Status completo e memoria.md
```
