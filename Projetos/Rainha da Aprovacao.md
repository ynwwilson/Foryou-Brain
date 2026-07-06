---
title: "Rainha da Aprovacao"
type: projeto
created: 2026-03-26
atualizado: 2026-05-27
tags: [projeto, entregue, educacao, case]
status: entregue
---

# Rainha da Aprovação

## Cliente
Dayane Alemar — Salinha / Rainha da Aprovação. Escola física com **200+ alunos**, foco em vestibular/ENEM.

## Status
**Entregue em 20 de março de 2026.** Em produção em https://metodorainhadaaprovacao.vercel.app (migração futura para `metodorainhadaaprovacao.com.br`). Manutenção ativa — correções pontuais e aprimoramentos rolando até hoje (entrega não foi um corte definitivo, é evolução contínua).

## Valor
R$27.000 — **não divulgar valor cobrado em material público** (valor correto seria R$50k+, contrato fechado por dentro do padrão de mercado). Usar como case sem mencionar número. Dayane não paga mensalidade — só infraestrutura (Supabase, Vercel, etc).

## Stack
Lovable + Supabase + Vercel + Cloudflare + Autentique (contrato com cláusula de omissões customizada)

## Construído por
José (vibe coding, solo)

## URL pública
- **Atual:** https://metodorainhadaaprovacao.vercel.app
- **Definitiva (futura):** https://metodorainhadaaprovacao.com.br

## Autorização para uso comercial
**Autorizado.** Dayane liberou uso do nome, marca e plataforma como case público. Regra: **não mencionar valor cobrado** (R$27k é valor de portfólio inicial, fora do padrão atual de mercado). Liberado para gravação como Asset 2 no Plano Comercial 2026.

---

## O que é o produto

Plataforma educacional multi-perfil com **multi-login** — um único produto onde o login direciona automaticamente pra área correta conforme o papel do usuário.

**Perfis de acesso:**
- **Aluno** — área de estudo e acompanhamento individual
- **Professor** — área de operação pedagógica e acompanhamento de turmas
- **Diretor** — área gerencial, acadêmica e financeira/operacional
- **Admin** — painel administrativo complementar

---

## Escopo entregue por perfil

### Aluno
- Dashboard do aluno
- Banco de questões
- Revisões + retry list (repetição de listas de erro)
- Caderno de erros automático
- Listas de exercício
- Simulados + histórico de simulados
- Redação (envio + recebimento corrigido)
- Flashcards (repetição espaçada)
- Planner / agenda de estudos
- Meta / objetivo
- Resultados e evolução
- Conquistas / ranking
- Biblioteca de material
- Método de estudo
- Histórico
- Configurações
- Troca de turno / turma

### Professor
- Dashboard do professor
- Correção e gestão de redações
- Turmas / classes
- Provas / exames + listas de prova
- Banco de questões + importação de questões
- Desempenho geral
- Análise individual de aluno
- Listas manuais customizadas
- Materiais
- Configurações

### Diretor
- Dashboard executivo
- Visão geral de desempenho
- Desempenho da equipe
- Hall of Fame
- Broadcast / comunicação em massa
- **Análise de retenção**
- Simulados e listas de prova
- Planner do aluno com intervenção gerencial
- Detalhe individual do aluno
- **X-Ray do aluno**: evolução, erros, revisões, heatmap
- Detalhe de performance por pessoa
- Grupos de turma
- Solicitações de troca de turma
- **Assinaturas / subscriptions**
- **Contratos** integrados
- Banco de questões e importação
- Configurações

### Admin
- Dashboard admin
- Questões e importação em massa
- E-mails

---

## Como usar como case (pitch pronto)

> "A gente construiu uma plataforma completa para uma escola com 200+ alunos — com app do aluno, painel do professor, dashboard executivo do diretor e controle administrativo, tudo num sistema só com a marca deles. O aluno entra e vê banco de questões, simulados, caderno de erros, flashcards e o próprio planner. O diretor vê retenção, desempenho, contratos e até o X-Ray de cada aluno. Um produto, vários perfis, uma marca."

## Demo recomendada (3 min)

1. **Fluxo do aluno:** dashboard → simulado → caderno de erros → flashcard
2. **Painel do professor:** turmas → análise individual
3. **Dashboard do diretor:** X-Ray do aluno + retenção + contratos

---

## Por que importa para a ForYou Code

- **Validação técnica:** plataforma multi-perfil complexa entregue solo via vibe coding (Lovable + Supabase)
- **Validação de nicho:** educação é nicho de alta complexidade — entregar prova capacidade
- **Asset visual forte:** painel da diretora é o que mais vende (X-Ray, retenção, contratos)
- **ROI defensável em proposta:** R$30k de projeto se paga em 6 meses se reduzir 30% do churn de uma escola com 200 alunos × R$800/mês (ver Plano Comercial fórmula 3)

---

## Sessões e auditorias

- [[2026-05-27 Rainha Sessao Completa]] — registro completo da sessão de 27/05/2026 (10 PRs, fundação de enforcement, BUG-06 corrigido, auditoria dos 42 bugs, plano LGPD).
- [[2026-05-27 Rainha Super-Analise e Verificacao]] — relatório técnico da auditoria por camadas (código/deploy/runtime).
- [[2026-04-18 Rainha Diagnostico Definitivo v2]] — diagnóstico estratégico (Fase 4 LGPD, Fase 7 migração Lovable).

## Estado de enforcement (após 27/05)

- CI gate ativo: `tsc --noEmit` + `npm run test` em todo PR (era só `build`).
- Branch protection no `main` (GitHub Pro) — PR obrigatório + check verde, sem push direto.
- `tests/unit/blindagemInvariants.test.ts` — testes ratchet travam `.neq summation` (totalmente) e `getClaims` (11 offenders documentados).
- Regra-de-ouro: edge functions deployam da `dev` (Lovable); frontend deploya da `main` (Vercel). Mudança em function → PR pra `dev` primeiro.

## Pendências críticas (após 27/05)

- 🔴 **Rotacionar 5 tokens** (estavam em texto plano; movidos para `C:\Users\ynwwi\Secrets\rainha\`).
- 🔴 **Plano LGPD/ECA** (`docs/LGPD_ECA_PLANO.md` no repo) — risco nº1, precisa advogado EdTech + Dayane decidir base legal/textos.
- 🟡 Apagar aluno teste `ZZ TESTE QA DEPLOY` (ID `dde11ab1-d0fa-4c90-989e-5be712fec5c1`) — inofensivo.
- 🟠 Sentry: conta + DSN (`sentry.ts` já wirado, falta ativar).

## Relacionado

- [[ForYou Code]]
- [[knowledge/Rainha da Aprovacao e uma plataforma educacional entregue para Salinha Dayane Alemar por R$27k|Nota knowledge complementar]]
- [[knowledge/Catalogo de entregas ForYou Code|Catálogo de entregas]]
- [[knowledge/Cases ForYou Code|Cases consolidados]]
- [[knowledge/Plano Comercial ForYou Code 2026|Plano Comercial 2026]]
