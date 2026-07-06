---
date: 2026-06-30 21h27
fim: 2026-06-30 22:53:43
tool: claude-nova
title: "Precisamos de um follow-up mínimo no webhook da Eduzz antes "
session_id: 9c189622-ccec-4980-abd6-38a8681dc894
tags: [claude-nova, sessão, completo]
---

# Precisamos de um follow-up mínimo no webhook da Eduzz antes 

> **Ferramenta:** Claude Nova · **Início:** 2026-06-30 21h27 · **Fim:** 2026-06-30 22:53:43
> **Dir:** `C:\Users\ynwwi\Projetos\metodorainha-4fadbe36`

## Objetivo
Precisamos de um follow-up mínimo no webhook da Eduzz antes …

## Conversa

**Mestre:** Precisamos de um follow-up mínimo no webhook da Eduzz antes do deploy. Não fazer deploy. Não mexer no Lovable Cloud. Não alterar secrets. Não alterar banco, migrations, RLS, subscriptions, paywall ou configuração da Eduzz. Contexto: O código HMAC de `main` está correto para payloads reais, mas a Eduzz usa um POST vazio no botão “Verificar URL”. Hoje o fluxo é: ```txt POST vazio → HMAC é exigido primeiro → não existe x-signature → 401 ``` Precisamos aceitar somente o teste vazio, sem enfraquecer a autenticação de eventos reais. ## Mudança exata No `supabase/functions/eduzz-webhook/index.ts`: 1. Ler `rawBody` uma única vez com `await req.text()`. 2. Imediatamente depois, antes de validar HMAC: ```ts if (rawBody.length === 0) {   return new Response(     JSON.stringify({ success: true, message: "Webhook endpoint active" }),     {       status: 200,       headers: { ...corsHeaders, "Content-Type": "application/json" },     },   ); } ``` 3. Esse early return deve ser para corpo exatamente vazio. Não aceitar: * JSON vazio `{}`; * whitespace; * payload parcial; * payload sem assinatura; * evento `ping` com conteúdo sem HMAC. 4. Para qualquer `rawBody.length > 0`: * exigir `x-signature`; * validar HMAC-SHA256(rawBody, EDUZZ_WEBHOOK_SECRET); * manter 401 para ausência ou assinatura inválida; * só fazer parse JSON depois da assinatura válida. 5. O POST vazio não pode: * inserir em `webhook_events`; * consultar ou alterar `subscriptions`; * consumir crédito; * gerar logs de payload; * disparar qualquer efeito colateral. ## Testes obrigatórios Adicionar/ajustar testes para provar: 1. POST com corpo exatamente vazio e sem `x-signature`    * retorna 200;    * não toca no banco;    * não cria evento;    * não cria assinatura. 2. POST com `{}` e sem `x-signature`    * retorna 401;    * não toca no banco. 3. POST com whitespace e sem `x-signature`    * retorna 401;    * não toca no banco. 4. POST não vazio com assinatura inválida    * retorna 401. 5. Evento `invoice.paid` assinado corretamente    * continua processando normalmente. 6. GET health check continua 200. Criar PR separado, pequeno e focado. Rodar: * tsc; * npm test; * npm run build; * eslint nos arquivos tocados. Entregar: * commit/PR; * arquivo alterado; * comportamento exato de POST vazio; * confirmação de que HMAC continua obrigatório para qualquer payload não vazio; * confirmação de que não houve deploy nem alteração no Lovable Cloud.
> 21:27

---

**Mestre:** O PR #186 está correto como conceito, mas a base precisa ser corrigida antes de qualquer merge. Fato confirmado no repositório: ```txt origin/main = 5926bba feat(eduzz-webhook): replace shared-secret auth with HMAC-SHA256 (#185) ``` Portanto, `main` já contém o HMAC, mesmo que o workspace do Lovable ainda estivesse atrasado. Não fazer deploy. Não mexer em Lovable Cloud. Não mexer em secrets. Não alterar Eduzz. Não mexer em banco, migrations, RLS, subscriptions ou paywall. Objetivo: transformar #186 em um follow-up limpo para `main`, trazendo somente o comportamento de POST vazio da verificação de URL. Procedimento: 1. Fazer `git fetch origin`. 2. Confirmar:    * `origin/main` está em `5926bba` ou descendente;    * `ae4459c` é o commit original do HMAC;    * `d4c7e22` é apenas o follow-up de POST vazio. 3. Na branch `fix/eduzz-webhook-empty-ping`, reaplicar somente o commit do follow-up sobre `origin/main`. Como a branch atual tem `ae4459c` como ancestral, usar esta estratégia: ```bash git rebase --onto origin/main ae4459c ``` 4. Se houver conflito:    * preservar o HMAC que já existe em `origin/main`;    * preservar `x-signature`;    * preservar `EDUZZ_WEBHOOK_SECRET`;    * preservar a regra de HMAC obrigatório para qualquer corpo não vazio;    * reaplicar somente este comportamento novo: ```ts const rawBody = await req.text(); if (rawBody.length === 0) {   return Response.json(     { success: true, message: "Webhook endpoint active" },     { status: 200, headers: corsHeaders },   ); } ``` 5. O POST vazio precisa:    * responder 200;    * não exigir assinatura;    * não tocar banco;    * não criar `webhook_events`;    * não alterar subscriptions. 6. `{}`, whitespace e qualquer payload não vazio continuam exigindo `x-signature` e HMAC válido. 7. Atualizar o PR #186 para apontar para `main`. 8. Conferir o diff final contra `origin/main`. O diff final não pode trazer novamente o HMAC inteiro, nem duplicar arquivos já presentes em main. Ele deve conter somente: * ajuste de POST vazio no handler; * testes do handler; * alteração mínima de configuração de testes, apenas se necessária. 9. Rodar: * npm test; * npm run build; * tsc; * eslint nos arquivos tocados. 10. Enviar a branch com `--force-with-lease`, informar: * novo commit; * base final do PR; * diff final contra main; * confirmação de que o PR #186 agora é seguro para merge. Não fazer merge ainda.
> 21:54

---

**Mestre:** O PR #186 está bloqueado no GitHub por um check obrigatório pendente: `Build check — Expected — Waiting for status to be reported` Vercel já concluiu com sucesso. Não fazer merge bypass. Não alterar código ainda. Não fazer deploy. Não mexer no Lovable Cloud, Eduzz, banco ou secrets. Quero apenas diagnosticar por que o check obrigatório `Build check` não foi reportado. Auditar: 1. Qual workflow, GitHub Action, integração ou status check deveria publicar exatamente o nome `Build check`. 2. Se existe workflow em `.github/workflows` relacionado a build/test. 3. Se houve execução de GitHub Actions para o PR #186. 4. Se a execução falhou, ficou cancelada, não disparou ou usa outro nome de check. 5. Quais checks obrigatórios estão configurados para a branch `main`. 6. Se `Build check` é um requisito antigo/stale da proteção de branch. 7. Se os checks atuais que realmente existem possuem outro nome. Entregar: * causa exata; * qual é a menor correção segura; * se precisa ajustar workflow ou regra de proteção da branch; * sem editar nada ainda.
> 22:14

**Claude Nova:** Diagnose only, no edits. Gathering evidence in parallel: workflows on disk, PR checks, runs, and branch protection.
> 22:14

---

**Mestre:** tudo sobre a eduzz feito, testado e finalizado
> 22:53

---

