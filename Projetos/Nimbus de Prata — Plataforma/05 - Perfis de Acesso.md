---
tipo: doc-projeto
projeto: Nimbus de Prata
doc: 05 — Perfis de Acesso
data: 2026-06-26
---

# 05 — Perfis de Acesso

[[Nimbus de Prata — Índice|← Índice]]

> A Nimbus **não vende só direto para cliente final**. Veterinários e vendedores têm papel comercial importante. A plataforma considera **4 perfis** com permissões distintas.

## 1. Cliente final
Área **simples** (não precisa de dashboard de gestão). Acessa:
Compras · pedidos · pagamentos · reservas · propostas · favoritos · agendamentos · documentos autorizados · informações comerciais · atendimento com vendedor/veterinário responsável.

## 2. Veterinário parceiro
Painel próprio para trabalhar com produtos e clientes vinculados a ele. Pode:
- Ver catálogo autorizado
- Consultar informações técnicas
- Compartilhar páginas de animais e produtos
- Cadastrar clientes
- Registrar leads
- Acompanhar negociações e vendas próprias
- Ver agenda · registrar atividades
- Ver comissões · acompanhar pagamentos vinculados
- Usar a plataforma como ferramenta de apresentação profissional

> **Isolamento:** veterinário **não vê dados privados de outros profissionais** sem permissão.

## 3. Vendedor
Recursos semelhantes, voltados a vendas. Pode:
Cadastrar leads · registrar clientes · acompanhar pipeline · propostas · reservas · pedidos · ver vendas próprias · metas · comissões · ranking · registrar contatos e visitas · acompanhar agenda · compartilhar produtos.

## 4. Administrador
Controle **completo**. Gerencia:
Conteúdo do site · hero · textos · fotos · vídeos · animais · cavalos · embriões · sêmen · touros · doadoras · prenhezes · estoque · preços · disponibilidade · documentos · dados técnicos · genealogias · CRM · leads · usuários · veterinários · vendedores · clientes · pedidos · pagamentos · reservas · agenda · cupons · promoções · campanhas · SEO · QR Codes · relatórios · comissões · rankings.

### Notas de implementação (rascunho — validar)
- RBAC (role-based access control) com **escopo por dono**: vet/vendedor só enxergam seus próprios leads/clientes/vendas → row-level security (ex.: RLS no Supabase) é caminho natural.
- Comissões: precisa de regra (% por perfil? por categoria? por item?). **Perguntar ao cliente.**
- Cliente final autenticado vê só o que é dele + documentos liberados explicitamente.
- "Catálogo autorizado" para vet sugere que nem todo item é visível a todo profissional → flag de visibilidade por item/perfil.
