---
tipo: doc-projeto
projeto: Nimbus de Prata
doc: 06 — CRM, Agenda e Campanhas
data: 2026-06-26
---

# 06 — CRM, Agenda e Campanhas

[[Nimbus de Prata — Índice|← Índice]]

## CRM e relacionamento comercial

> A plataforma ajuda a empresa a **não perder oportunidades**. Todo interessado pode virar **lead** no CRM.

### Campos do lead
Nome · telefone · e-mail · cidade · interesse · origem · produto/categoria de interesse · vendedor responsável · veterinário responsável · histórico · observações · etapa comercial.

### Funil comercial
Novo lead → Em contato → Qualificado → Proposta enviada → Negociação → Reserva → Pagamento pendente → Fechado / Perdido.

### Inteligência que a empresa precisa enxergar
Quais produtos têm mais interesse · quais vendedores convertem mais · quais veterinários geram mais vendas · quais leads estão parados · quais pagamentos estão pendentes.

## Agenda e atendimento

Visitante/cliente pode solicitar: **visita à fazenda** · reunião · atendimento comercial · avaliação · apresentação de animal · conversa com veterinário · conversa com vendedor.

Internamente, a equipe acompanha: visitas · reuniões · retornos · tarefas · compromissos · agenda de vendedores · agenda de veterinários · agenda administrativa.

## Promoções, cupons e campanhas (poder do admin, sem mexer no código)

- Cupons · desconto percentual · desconto em valor
- Validade de promoções · limite de uso
- Promoções por categoria · por item específico
- Produtos em destaque · campanhas sazonais · destaques na Home

> A empresa deve ter liberdade total para campanhas sem alterar código.

### Notas de implementação (rascunho — validar)
- Lead pode nascer de qualquer ação no site (form, "solicitar info", agendamento) → captura automática com `origem` preenchida.
- Atribuição de responsável (vendedor/vet) pode ser manual ou por regra (origem, região DDD 34/Triângulo Mineiro).
- Agendamento conecta com a Agenda interna → notifica o responsável.
- Cupom/campanha precisa respeitar a config "comprável online" do item (ver [[04 - Estoque, Pagamentos e Comercialização]]).
