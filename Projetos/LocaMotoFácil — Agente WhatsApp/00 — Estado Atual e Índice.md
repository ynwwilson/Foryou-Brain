---
projeto: LocaMotoFácil — Agente WhatsApp com IA
atualizado: 2026-06-09
status: EM PRODUÇÃO (número de teste) — pendências externas
---

# LocaMotoFácil — Agente WhatsApp com IA · ESTADO ATUAL

> Handoff completo. Tudo que foi feito, onde estamos, o que falta. Pode dar `/clear` depois de ler isto.

## TL;DR
Agente de atendimento no WhatsApp para a **LocaMotoFácil** (locadora de moto delivery, Campinas). Atende sozinho por texto/áudio/imagem/documento/comprovante, com painel de controle estilo fintech. **Está no ar e funcionando** num número de TESTE da Meta. Falta: credencial SGRLock (Odeen), crédito Anthropic, template PT aprovado, e migrar pra número real de produção.

## Onde está tudo
- **Código:** `C:\Users\ynwwi\Projects\whatsapp-ai-agent` — monorepo npm (branch `build-b`). Backup no GitHub **privado**: https://github.com/ynwwilson/whatsapp-ai-agent (.env não sobe).
- **Painel (no ar):** https://waa-panel.vercel.app
- **Gateway (no ar):** https://waa-gateway.ynwwilson.workers.dev
- **Vault Obsidian:** esta pasta. Notas 00–07.

## Notas deste projeto
- [[01 — Arquitetura e Stack]]
- [[02 — Timeline do que foi feito]]
- [[03 — Deploy, Acessos e Segredos]]
- [[04 — Erros, Acertos e Decisões]]
- [[05 — O que falta + Como retomar]]
- [[06 — Negócio LocaMotoFácil (regras travadas)]]
- [[07 — SGRLock (consulta de risco)]]

## O que está PRONTO e FUNCIONANDO ✅
- Atendimento IA por **texto** (preço R$427, cores, FAQ, tom humano sem travessão) — testado E2E no WhatsApp
- Entende **áudio** (transcreve→responde), **imagem/comprovante** (lê valor/recebedor/efetuado vs agendado, flag destino errado), **documento PDF** (lê o corpo)
- **Pagamento só na retirada, anti-golpe** — IA nunca pede Pix adiantado, tranquiliza contra golpe, sabe o CNPJ
- **Memória** (recente + resumo rolante + fatos pgvector), idempotência, failover OpenAI→Anthropic, escalação
- **Reengajamento proativo** (template + cron Vercel /15min) — testado, chegou no zap
- **Painel redesenhado** (Revolut Dark laranja) — dashboard, conversas (chat ao vivo + assumir), pagamentos (agrupado por lead), custo, saúde, config, mídia, templates. Mobile 100% responsivo.
- **SGRLock** (consulta de risco Banned List/BGCL) — código completo, off-safe; falta só credencial

## O que FALTA (pendências externas / do dono)
1. ~~**SGRLock**~~ ✅ **100% FUNCIONANDO 2026-06-09** — credencial validada, no Vercel prod + .env. Teste real ponta-a-ponta OK: CPF do José → `success`/aprovado. Corrigidos 4 bugs no caminho (parse de data, `warn`→reprovado, foto ruim/CPF inválido, silêncio pós-análise). Fluxo: lê CNH → confirma dados → consulta → continua a venda. Ver [[07 — SGRLock (consulta de risco)]].
2. **Crédito na Anthropic** — fallback do LLM (hoje só OpenAI tem crédito).
3. **Template PT aprovado na Meta** — pra ligar o proativo de verdade (hoje só hello_world de teste).
4. **Número real de produção** — sair do número de teste (+1 555 636 0545). Ver [[05 — O que falta + Como retomar]].
5. **Refinar locamoto.md** — condição jurídica "a moto fica sua" (opcional).

## Cliente / negócio
LocaMotoFácil. Moto Yamaha Factor 150 0km, R$427/semana, retirada R$676, caução R$997 (4×249), plano 36 meses (moto vira do locatário). **Pagamento SÓ na retirada, presencial, nada adiantado.** CNPJ 00.971.610/0001-32. Detalhes em [[06 — Negócio LocaMotoFácil (regras travadas)]].
