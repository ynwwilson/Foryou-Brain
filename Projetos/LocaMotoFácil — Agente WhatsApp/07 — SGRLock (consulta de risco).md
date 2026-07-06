---
projeto: LocaMotoFácil — Agente WhatsApp
nota: SGRLock (consulta de risco)
status: credencial recebida e VALIDADA na API — falta gravar env + redeploy
---

# SGRLock — consulta de risco (Banned List / BGCL)

## CREDENCIAL RECEBIDA (2026-06-09) ✅
Email da Odeen (pro Guilherme). Login de painel que **TAMBÉM funciona na API**:
- `user`: `guilhermepcamargo@gmail.com`
- `password`: `#Glhrm#adm123`
- Painéis web: admin `https://admin.sgrloc.com.br/inicio` · consultas `https://balcao.sgrloc.com.br/balcao`
- **Teste de login na API (POST /session/) = HTTP 200 `result:"success"`**, devolveu token+refresh JWT.
- `companyId: 382`, `companyName: "GC LOCAÇÃO DE MOTOS LTDA"`.
- **`credentialLifeProof: false`** → biometria/prova de vida DESLIGADA → consulta NÃO exige imagem (código atual serve).
- `expiresIn: "15m"` (bate com o cache/refresh do client).
- Observação Odeen: consultas que retornam FALHA não são cobradas. Consumo mínimo R$50/mês.

**Feito 2026-06-09:** env gravadas no Vercel prod + .env, painel redeployado.

## TESTE REAL (2026-06-09) — 2 bugs de código achados+corrigidos + 1 bloqueio externo
Wilson mandou a CNH no WhatsApp de teste; IA respondeu "deixa eu confirmar..." e ficou muda. Investigação no backend (`risk_checks` vazio, `error_log`):

**Bug 1 — turno `risk_check` rejeitado pelo schema (zod).** A visão lia a data da CNH em formato ≠ `DD/MM/YYYY` (ex ISO `2005-12-20`) e o turno era recusado; o retry cego re-emitia o mesmo turno inválido → `throw "no parseable agent turn"` → `safeBridge` escalava sem nunca chamar o SGRLock. Reproduzido com gpt-4o (falha determinística). **Fix:** `RiskCheckAction` normaliza `birthDate` (ISO/traço/ponto→DD/MM/YYYY) e coage `document` p/ só dígitos; `think()` agora faz retry informando o erro exato do zod e loga o raw do modelo no fail. (commit `23db28f`)

**Bug 2 — `result:"warn"` tratado como reprovado.** A consulta real retornou `result:"warn"` + `"Problemas criação consulta Background Check Light. Tente novamente."` (4/4). O mapeamento antigo (`ok: res.ok || result==="error"`) marcava warn como ok→approved=false → orchestrator tratava como **REPROVADO** (falso apontamento). **Fix:** só `success`/`error` são veredito; `warn`/desconhecido → `ok:false` → escala verificação **manual**, nunca reprova por engano; `validate()` reexecuta até 2x. (commit `0387eb3`)

**`warn` — NÃO é Odeen caída (corrigi conclusão anterior).** Sondagem com vários CPF mostrou que é **determinístico por CPF**, não instabilidade:
- CPF válido `111.444.777-35` → `success` **6/6**.
- CPF válido `529.982.247-25` → `warn` **6/6**.
- CPF que eu tinha usado pro "José" (`010.181.937-72`) → `warn`; mas **esse CPF eu li ERRADO da foto escura — dígito verificador inválido, nem é o CPF real do José.** Todo meu teste "do José" foi com dado inventado → descartado.
- Hipótese provável: `warn "Problemas criação consulta Background Check Light"` = CPF válido em dígito mas **sem registro real na base do BCL** (CPF de teste/fake). CPF de pessoa real (o do José de verdade) deve voltar veredito. **Falta confirmar com o CPF real.**

**Bug 3 — foto ruim quebra tudo (resolvido com fluxo novo).** Fotos de CNH vêm ruins → leitura erra CPF/data. Decisão (Wilson): **ler foto + CONFIRMAR antes de consultar**. Implementado (commit `f66d133`):
- Prompt: fluxo 2 passos — IA lê a CNH, repete "CPF X, nascimento Y, confirma? se errado manda digitado", só emite `risk_check` após confirmar/digitar; foto ilegível → pede digitado; dica de foto ao pedir o doc.
- `util/cpf.ts` `isValidCpf` (dígito verificador); `runRiskCheck` **bloqueia consulta de CPF inválido** e pede o número digitado (sem pausar) — nunca gasta consulta em leitura ruim.

**CONFIRMADO FUNCIONANDO (2026-06-09 20h12).** Wilson reenviou a CNH; fluxo rodou: IA leu → confirmou (Nome/CPF `124.948.086-85`/nasc 25/05/2007) → "Certinho" → consulta SGRLock → **`result:"success"`, `approved:true`** gravado em `risk_checks`. O `warn` anterior era 100% por CPF mal lido (o real é `124.948.086-85`, não o que eu chutei). **Não há nada pendente com a Odeen.**

**Bug 4 — silêncio após "vou analisar" (resolvido).** No aprovado o código não mandava nada pro cliente (só breadcrumb); no não-verificado/reprovado pausava sem avisar. Cliente ficava no vácuo. **Fix (commit `b7a50cd`):** `runRiskCheck` retorna o desfecho; `sendRiskFollowup` fecha o ciclo — **aprovado → IA continua a venda com o próximo passo** (combinar retirada), **não-verificado/reprovado → mensagem neutra calorosa + humano assume**. Fallback fixo garante que algo sempre chega. Validado com gpt-4o.

**Status final:** SGRLock 100% funcional ponta-a-ponta (lê CNH → confirma → consulta → veredito → continua atendimento). 112 testes verdes, no ar. Pendência SGRLock = **nenhuma**.

## O que é
Serviço da **Odeen & Co** ("Intelligence for Security") — API de consulta de risco pro setor de locação. Manda CPF+nome+nascimento, devolve se a pessoa está **limpa** ou tem **apontamento** (lista negra / BGCL). Escopo inicial do LocaMotoFácil (por email da Odeen): **só Banned List + BGCL**.

## A API
- Base URL: `https://api-external-client-rjwxsrqe6q-rj.a.run.app/v1`
- **Login:** `POST /session/` `{user, password}` → `token` + `refresh_token` (JWT Bearer)
- **Consulta:** `POST /validationrequest` (Bearer) `{document, birth_date:"dd/mm/yyyy", name, document_type:1}` (CPF=1)
- **Refresh:** `POST /session/refresh-token` `{token: REFRESH_TOKEN}`

## Resposta (decisão simples)
- Limpo: `{"result":"success","service":null,...}` → **aprovado**
- Apontamento: `{"result":"error","message":"Reprovado","transactionId":"...","service":null}` → **reprovado**
- Regra: `result === "success"` → ok; qualquer outro → reprovado. Falha de rede/auth → **escala** (nunca aprova no erro).

## Como foi integrado (commit 3687d9f)
- **Core:** `packages/core/src/sgrlock/client.ts` (SgrlockClient: login/refresh/validate + cache de token). Config loader `loadSgrlockConfig` (SGRLOCK_USER/PASSWORD/BASE_URL).
- **Banco:** tabela `risk_checks` (migration 0008, RLS single-owner). Store: insertRiskCheck/listRiskChecks/latestRiskCheck.
- **Auto (no cadastro):** ação `risk_check` no AgentTurn. A IA lê nome/CPF/nascimento da **CNH** e emite a ação. Orchestrator (`runRiskCheck`): consulta → grava → se reprovado OU falha → **escala pra humano + pausa + alerta**. **Nunca expõe o resultado pro cliente** (system prompt instrui). Aprovado → segue.
- **Manual (painel):** componente `RiskCheckPanel` na página do lead (seção "Análise de risco (SGRLock)") — form CPF/nome/nascimento + botão + histórico. Server action `runRiskCheck`.
- **Off-safe:** sem credencial → escala pra verificação manual (não quebra).

## Decisões
- Reprovado → escala pra humano (não recusa seca; LGPD, evitar falso positivo).
- IA nunca fala "lista negra/consulta/score" pro cliente — é interno. Diz só "vou analisar seu cadastro".
- Data de nascimento: lida da CNH; se ilegível, a IA pede.

## Falta (do dono)
**Credencial `user`+`senha`** — a Odeen emite (não dá pra criar sozinho). Email enviado pro Julio Machado (julio.machado@odeen.com.br). Quando chegar:
1. `vercel env add SGRLOCK_USER production` + `SGRLOCK_PASSWORD` (e no .env local)
2. redeploy painel
3. testar consulta manual + automático pela CNH

## Contatos Odeen
- Julio Machado (TI): julio.machado@odeen.com.br
- Caline Costa (Comercial): caline.costa@odeen.com.br · (11) 99930-3927
- thread: comercial2@odeen.com.br
