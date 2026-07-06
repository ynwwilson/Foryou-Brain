---
projeto: LocaMotoFácil — Agente WhatsApp
nota: Negócio (regras travadas)
fonte: business/locamoto.md no repo (alimenta o system prompt)
---

# Negócio LocaMotoFácil — regras travadas

> Fonte da verdade que alimenta o agente: `C:\Users\ynwwi\Projects\whatsapp-ai-agent\business\locamoto.md`. Editar lá muda o que a IA sabe (rebuild regenera o knowledge embarcado).

## Quem é
Locadora de moto pra **delivery** em Campinas. Moto 0km pra gerar renda mesmo sem crédito/negativado, com caminho pra **ficar com a moto** ao fim de 36 meses. NÃO vender como "aluguel barato". **Só locação — investidor está FORA de escopo.**

## Dados oficiais
- Empresa: **LocaMotoFácil**
- **CNPJ: 00.971.610/0001-32** (a IA pode informar pra provar legitimidade contra medo de golpe)

## Produto
- **Yamaha Factor 150 UBS 0km / 2026**. Cores: preta, branca, vermelha.
- Processo online pelo WhatsApp, retirada na **concessionária Yamaha em Campinas**.

## Preços (CONFIRMADOS)
- Aluguel semanal: **R$ 427,00**
- Caução: **R$ 997,00** em até **4× R$ 249,00** (semanais)
- Retirada: **R$ 676,00** (1ª semana 427 + 1ª parcela caução 249)
- 4 primeiras semanas: R$ 676/sem; depois R$ 427/sem
- Plano 36 meses → ao fim a moto é do locatário

## ⚠️ PAGAMENTO — REGRA DE OURO (anti-golpe)
**Pagamento SÓ no ato da retirada, presencial, na concessionária. NADA adiantado.**
- A IA **NUNCA** pede Pix/transferência/sinal/taxa/reserva/depósito pra liberar ou garantir a moto.
- Antes da retirada só existe **análise de cadastro (grátis)**.
- Usa isso a favor: "você não paga nada agora, só paga vendo a moto na concessionária no dia da retirada".
- **Quem pedir dinheiro adiantado em nome da LocaMotoFácil é golpista** — a IA alerta o cliente.
- Se o cliente mandar comprovante mesmo assim (caiu em golpe / destino errado): a IA avisa na hora que pode ter sido golpe.
- Testado: "já vou te mandar o pix então" → IA recusou e explicou que é presencial. ✅

## Cadastro / análise
Nome completo, CPF, CNH, comprovante de endereço, 3 contatos, link de rede social. Pra consulta de risco (SGRLock) a IA precisa de **nome + CPF + data de nascimento**, normalmente lidos da **foto da CNH**.

## Consulta / aprovação
- **NÃO** consulta Serasa/SPC.
- Consulta: ações criminais, lista de locadoras do Brasil, histórico de prejuízo a locadoras (= **SGRLock Banned List/BGCL**, ver [[07]]).
- Pode ter nome sujo; NÃO pode ter crime relevante nem estar em lista negra de locadoras.

## Tom de voz
Direto, humano, sem clichê de IA, **sem travessão**, frases curtas. Foco do entregador: dinheiro, urgência, nome sujo, medo de ficar parado.

## Telefone humano (dos scripts): +55 19 98903-6693

## Pendências de conteúdo
- Texto jurídico final da condição "a moto fica sua" (opcional).
