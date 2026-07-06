---
projeto: LocaMotoFácil — Agente WhatsApp
nota: Erros, Acertos e Decisões
---

# Erros, Acertos e Decisões (aprendizados)

## Bugs achados e corrigidos
- **panel_users sem RLS** (escalonamento de privilégio) — com os grants amplos do 0001, um usuário authenticated podia se auto-inserir no allowlist. Fix: enable RLS + policy SELECT-only (subselect das outras policies continua funcionando). Crítico, pego no deploy.
- **Colisão de migration** — proactive era 0005, mas 0005 já era observability. Renumerado pra 0006.
- **LLM sem crédito** — OpenAI 429 + Anthropic 400. Não é bug de código; era billing. Dono pôs crédito na OpenAI.
- **Quirk do "9" BR** — Meta normaliza o celular sem o 9 extra; cadastrar as 2 formas no número de teste. Some no número real.
- **Comprovante "agendado" errado** — prompt não passava a data de hoje → modelo achava data de hoje futura. Fix: injetar data atual (Brasília) + regra "data de hoje NÃO é futuro".
- **Visão recusava ler comprovante (~50%)** — gpt-4o às vezes recusa documento financeiro/PII → JSON vazio → fallback "ilegível". Fix: retry 1x + linha no prompt dizendo que o cliente autorizou a leitura.
- **Recebedor não extraído** — comprovante só lia o pagador. Adicionado `recipient` + comparação com LocaMotoFácil/CNPJ → flag "destino errado".
- **Pix destino errado contava como efetuado** — corrigido: `effectivePaymentStatus` sobrescreve pra "destino errado", não conta como efetuado no dashboard.
- **Texto do doc não persistia** — só ia pro prompt. Agora salva em `media.transcription` (painel mostra + verificável).
- **Mobile do painel**: header sobrepondo título com filtros (fix global no `.top`), 2 menus (removido o de cima), "Mais" repetia todos (agora só não-principais), chat header apertado (pill compacto IA on/off), botão "Lead" sobre o composer (subiu), sparklines cruzando texto (escondidas no mobile), recebedor vazando tela (agrupado por lead).
- **Ícone SVG sem fechar `</>`** quebrou typecheck (fragment não fechado).
- **Cache stale `.next/types`** após deletar app/page.tsx — limpar `.next`.

## Decisões importantes
- **Gemini descartado** — key com quota 0 (free tier off). Vídeo passou a ser ffmpeg (áudio) + OpenAI (frames), sem Gemini.
- **Pagamento SÓ na retirada, nada adiantado** (anti-golpe) — correção de negócio crítica do dono. IA nunca pede Pix. Ver [[06 — Negócio LocaMotoFácil (regras travadas)]].
- **Reprovado no SGRLock → escala pra humano** (não recusa seca; LGPD, falso positivo).
- **Painel: Revolut Dark + accent LARANJA** (não roxo) — escolha do dono. CSS Modules, sem Tailwind.
- **Pagamentos agrupado por lead** — não mostrar 5x o mesmo nome; clica → página do lead com tudo.
- **Backward-compat aliases no globals.css** — tokens antigos (--panel etc) apontam pros novos durante a migração, pra não quebrar telas mid-reskin.

## Acertos / o que funcionou bem
- **dev-browser no Opera logado** — fez TODO o setup manual (Supabase SQL, Meta, Vercel root dir, cadastro de número/código) sem o dono mexer. Screenshots da URL logada funcionam (login + viewport mobile/desktop) pra QA visual.
- **Webhook via Graph API** (não pela UI) — mais confiável que clicar na interface nova da Meta.
- **Off-safe features** — SGRLock e proativo degradam com elegância sem credencial/template.
- **Mockup HTML aprovado antes de codar** o redesign — evitou retrabalho.

## Caveats aceitos
- Proativo fora de 24h só via template aprovado. Sem indicador "gravando áudio". Comprovante = leitura+classificação com confiança (não verificação bancária real).
