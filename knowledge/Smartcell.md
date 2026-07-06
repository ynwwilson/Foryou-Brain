---
tipo: knowledge
tags: [cliente, entregue, smartcell, e-commerce, case-publico]
atualizado: 2026-05-06
---

# Smartcell — Smartcell Premium Store

> **Nome do arquivo está desatualizado** (diz "em construção em Patos-PB" — na verdade é Patos-MG e foi entregue em 25/04/2026). Mantido por links existentes; conteúdo abaixo é a versão atual.

## Status
Entregue em 25/04/2026. Em produção: https://smartcellsite.com.br

## Cliente
Fellipe — Patos-MG

## Modelo comercial
20% do lucro de cada produto vendido. Sem cobrança de projeto. Manutenção e evolução incluídas no acordo de participação. Split de sócios entre José/Marco/Eduardo (soma 100%) implementado dentro do admin financeiro como regra de negócio.

## Stack final
Lovable + Lovable Cloud (Supabase) + Lovable AI Gateway (Gemini 2.5 Pro/Flash + GPT-5) + Mercado Pago + Asaas + ViaCEP + WhatsApp `wa.me` + PWA

## Escopo entregue
Loja completa branded + catálogo dinâmico (iPhone novos/seminovos/usados, Xiaomi, Mac, iPad, Watch, AirPods, Acessórios) + checkout próprio em 4 etapas + pagamentos PIX automáticos (Mercado Pago QR + polling 5s, Asaas) + recuperação de carrinho + IA gerando descrição e imagem de produto + 13 módulos no painel admin + PWA + LGPD compliance.

Detalhes completos em [[Projetos/Smartcell|Projetos/Smartcell]] e capacidades técnicas reaproveitáveis em [[Licoes tecnicas e-commerce Smartcell|Lições técnicas]].

## Autorização para uso comercial
Fellipe autorizou uso como case público — nome, marca, número (553438212212) e demo pública. Disponível para virar 4º asset de venda gravado, junto de Rodrigo (IA atendimento), Dayane (educação) e ForYou Code interno.

## Por que importa para a ForYou Code
- **Validação técnica:** stack roda checkout PIX automático em produção sem MegaAPI (alternativa pra cliente que não quer chatbot)
- **Validação comercial:** participação nos lucros como modelo viável — projeto sem fee, receita escalável
- **Validação de nicho:** e-commerce premium com seminovos (IMEI/bateria/checklist 30 itens) é um schema reaproveitável
- **Asset de venda:** material visual forte para demos e anúncios

## Links relacionados
- [[Projetos/Smartcell|Projetos/Smartcell — escopo completo]]
- [[Licoes tecnicas e-commerce Smartcell|Lições técnicas reaproveitáveis]]
- [[Catalogo de entregas ForYou Code|Catálogo de entregas]]
- [[atlas/Mapa de clientes|Mapa de clientes]]
- [[Como precificar projetos na ForYou Code|Precificação]]
