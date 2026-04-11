---
tipo: knowledge
tags: [foryoucode, entrega, processo, operacional]
atualizado: 2026-03-25
---

# Processo de entrega de projetos na ForYou Code

## Stack de entrega
Lovable (frontend/builder) + Supabase (banco) + Vercel (deploy) + Cloudflare (CDN/DNS)

## Etapas do projeto

### 1. Contrato
- Assinar via Autentique antes de começar qualquer coisa
- Incluir cláusula de omissões customizada (protege contra escopo infinito)

### 2. Levantamento de escopo
- Listar todas as funcionalidades acordadas
- Definir o que está IN e o que está OUT do contrato
- Alinhar prazo de entrega

### 3. Construção
- Montar o app no Lovable
- Conectar ao Supabase (auth, banco, storage)
- Desenvolver módulos: CRM, pagamentos, WhatsApp API, agentes de IA conforme escopo

### 4. Testes
- Validar cada módulo antes de apresentar
- Testar fluxos completos do ponto de vista do usuário final do cliente

### 5. Entrega e handoff
- Apresentar o sistema funcionando ao cliente
- Passar acesso (Vercel, Supabase, domínio)
- Documentar o básico para o cliente operar

### 6. Pós-entrega
- Suporte incluído conforme contrato
- Oportunidade de vender mensalidade ou próximo módulo

## Regra de ouro
Nenhuma funcionalidade extra é feita sem novo contrato ou adendo assinado.
O que não está no contrato, não está no escopo.
