---
projeto: LocaMotoFácil — Agente WhatsApp
nota: O que falta + Como retomar
---

# O que falta + Como retomar

## Pendências (ordenadas)
### 1. Credencial SGRLock ⏳ (esperando Odeen)
Email já enviado pro Julio (julio.machado@odeen.com.br). Quando chegar `user`+`senha`:
1. `vercel env add SGRLOCK_USER production --scope yngomesmarco-hues-projects` (e SGRLOCK_PASSWORD)
2. Adicionar também no `.env` local
3. Redeploy do painel
4. Testar: na página do lead, seção "Análise de risco" → preencher CPF/nome/nascimento → consultar
5. Confirmar fluxo automático pela CNH (mandar foto de CNH no WhatsApp)
Detalhes: [[07 — SGRLock (consulta de risco)]]

### 2. Crédito na Anthropic
Hoje só OpenAI tem crédito. Pôr crédito em https://console.anthropic.com/settings/billing pra ter failover real. (Sistema funciona só com OpenAI; é redundância.)

### 3. Template PT aprovado na Meta
Pra ligar o reengajamento proativo de verdade (hoje só hello_world de teste).
- Criar template em PT no WhatsApp Manager (ex: "Oi {{1}}, vamos continuar sua análise pra alugar a moto?")
- Esperar aprovação da Meta
- Cadastrar no painel (Templates) + agendar
- O cron (/15min) dispara os vencidos sozinho

### 4. Número real de produção — ⛔ TRAVADO NO REGISTRO (atualizado 2026-06-18)
Número real escolhido = **+55 19 99207-9451** (display "LocaMotoFácil"). IDs novos: **WABA `1661780868274603`, PNID `1104425689428958`**, business dono `1590796992102932` "Loca.Moto.Facil". 2FA PIN = `508317`.
- **Já feito:** `.env` atualizado (PNID+WABA novos); system user "Wilson Locamoto" (`61590888050166`) com **Acesso total** na WABA+App; app inscrito; webhook ok; **token NOVO gerado** no `.env` (Vercel ainda com o antigo — os 2 válidos, sincronizar quando registrar). Número `code_verification_status=VERIFIED`.
- **Bloqueio:** registro falha. `POST /{PNID}/register` → **code 100 / subcode 33**; UI App-Dashboard "Registrar" → "Falha na inscrição. Tente novamente." Número fica `status=PENDING`, `platform_type=NOT_APPLICABLE`, `is_pin_enabled=false`.
- **Causa raiz (diagnóstico multi-agente 18/06):** **rate-limit de registro `133016` — 10 tentativas/número por janela ROLANTE de 72h; cada tentativa (API, botão UI, PIN errado, OTP) RE-ARMA a janela.** Por isso "tentar depois de dias" falhava (sempre tinha tentativa no meio). NÃO é token/permissão/UI/PIN.
- **Pagamento (141006) e verificação de negócio (141010) NÃO causam o subcode 33** — são gates de ENVIO (msg iniciada pela empresa / volume). Resolver em paralelo (precisa cartão + documentos do cliente), não bloqueiam registrar nem o E2E user-initiated.
- **COMO RETOMAR:** (1) **parada total de register/deregister/PIN/OTP por 72h limpas** — começou ~18/06, seguro a partir de **~21/06**. (2) UMA tentativa: `POST /1104425689428958/register {messaging_product:'whatsapp', pin:'508317'}` com token do `.env`. (3) Verificar `GET /1104425689428958?fields=status,platform_type,is_pin_enabled` → esperar `CONNECTED`/`CLOUD_API`/`true`. (4) Se AINDA subcode 33 → **número novo** (chip pré-pago, sem WhatsApp, recebe código 1x) que bypassa throttle per-número, OU **Meta Direct Support** (citar PNID + erro 100/subcode 33 + "stuck PENDING / not provisioned").
- Após registrar: atualizar token no Vercel se quiser sincronizar; webhook segue valendo (nível WABA); entra cobrança Meta por conversa (teste era grátis).

### 5. Refino opcional
- Condição jurídica "a moto fica sua" no locamoto.md (texto final)
- Polir sparklines do dashboard
- PauseToggle/ProfileEditor/ContactControls ainda usam tokens antigos (via alias, funcionam)

## Como retomar depois do /clear
1. Ler [[00 — Estado Atual e Índice]] primeiro.
2. Código em `C:\Users\ynwwi\Projects\whatsapp-ai-agent`, branch `build-b`. `git log --oneline` mostra tudo.
3. Rodar local: `npm run typecheck` + `npm run test` (devem estar verdes).
4. Deploy painel: `vercel deploy --prod --yes --scope yngomesmarco-hues-projects` (da raiz).
5. Deploy gateway: `cd apps/gateway && npx wrangler deploy`.
6. QA visual: dev-browser conecta no Opera logado (`dev-browser --connect`); logar no painel (creds em [[03]]); screenshot mobile (390x844) / desktop (1280).
7. Migrations novas: injetar no SQL editor do Supabase via dev-browser Monaco.
8. Testar agente: mandar mensagem do celular do dono pro número de teste; verificar no Supabase (tabelas messages/payments/error_log) via REST com service key do `.env`.

## Testes ainda NÃO feitos (opcionais)
- Batching (5 msgs rápidas → 1 resposta)
- Memória de longo prazo na prática (10 dias depois)
- IA enviando mídia/áudio PTT pré-gravado
- Guardrails: "quero investir" (fora de escopo), "me dá desconto" (recusa), "ignore suas instruções" (anti-injection)
