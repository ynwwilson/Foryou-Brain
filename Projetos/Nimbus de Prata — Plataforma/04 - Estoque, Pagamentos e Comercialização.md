---
tipo: doc-projeto
projeto: Nimbus de Prata
doc: 04 — Estoque, Pagamentos e Comercialização
data: 2026-06-26
---

# 04 — Estoque, Pagamentos e Comercialização

[[Nimbus de Prata — Índice|← Índice]]

## Controle de estoque e disponibilidade

Cada item tem status + disponibilidade atualizados.

**Status possíveis:** Disponível · Em negociação · Reservado · Pagamento pendente · Vendido · Indisponível · Sob consulta · Em avaliação · Destaque · Lançamento.

### Regras de estoque
- **Itens únicos** (alguns animais e cavalos): sistema **impede que duas pessoas comprem/reservem o mesmo item ao mesmo tempo** → trava de concorrência (lock / reserva com expiração).
- **Itens com quantidade** (embriões, sêmen): controle de **estoque real**. Após pagamento confirmado → **baixa automática** de estoque.
- Status comercial atualizado automaticamente após confirmação.

> Reduz erro, evita venda duplicada, torna a operação confiável.

## Pagamentos — integração Asaas

Pagamento online quando a empresa liberar a opção por item. Conforme configuração de cada item, o cliente pode: comprar · reservar · pagar via **Pix** · **boleto** · **cartão** · receber **link de pagamento** · acompanhar status · ver pedido · ver reserva · receber atualização comercial.

## Fluxo pós-pagamento confirmado

Ao confirmar um pagamento, a plataforma deve:

1. Atualizar o pedido
2. Atualizar o status comercial
3. Reduzir estoque
4. Marcar item como vendido/indisponível quando necessário
5. Registrar movimentação
6. Notificar administração
7. Notificar vendedor ou veterinário responsável
8. Notificar o cliente

Manter **histórico comercial completo**: o quê foi vendido, por quem, para quem, em qual condição, em qual momento.

### Notas de implementação (rascunho — validar)
- Asaas via **webhook** de confirmação → dispara o fluxo de 8 passos (idempotente, para não baixar estoque duas vezes).
- Reserva de item único = registro com `expira_em`; libera automaticamente se não pago no prazo.
- Notificações: definir canais (e-mail, WhatsApp, in-app). WhatsApp é o canal natural do público agro.
- Configuração "comprável online" é **por item** — nem tudo vende com checkout; muito é "sob consulta / proposta".
