---
tipo: knowledge
tags: [foryoucode, e-commerce, smartcell, licoes, padroes, reaproveitamento]
atualizado: 2026-05-06
---

# Lições Técnicas — Smartcell Premium Store

> Padrões e decisões de implementação descobertos durante a entrega do Smartcell (entregue em 25/04/2026). Reaproveitar nos próximos projetos de e-commerce, especialmente nichos com seminovos, loja regional ou modelo de participação nos lucros.

---

## 1. Seminovos exigem schema próprio

Não cabem no schema de "produto comum". Campos obrigatórios:
- Condição (novo / seminovo / usado / lacrado)
- Bateria % (para iPhone/dispositivos com bateria)
- IMEI (rastreabilidade individual)
- Checklist de avaliação (30 itens no Smartcell — tela, botões, câmeras, conector, áudio, sensores)
- Foto da unidade real (não foto de catálogo)

**Aplicação:** qualquer cliente do nicho seminovos/usados (eletrônico, automotivo, instrumentos musicais) precisa desse schema dedicado.

## 2. Compartilhamento de imagem por modelo+cor entre condições

Em vez de cadastrar foto pra cada SKU (modelo × condição × cor), cadastra-se a foto **por modelo+cor**, e todas as condições (novo/seminovo/usado/lacrado) reusam a mesma imagem. Economiza 4× o trabalho de cadastro e mantém consistência visual.

**Aplicação:** padrão sempre que houver variação de condição sobre o mesmo modelo físico.

## 3. Frete por região > integração com transportadora (loja regional)

Para loja regional (atende um estado ou agrupamento de cidades), regra fixa de frete por região é melhor que integração Correios/Melhor Envio:
- Mais previsível pro cliente
- Mais barato pra operação (sem fee por consulta)
- Permite frete grátis acima de X (gatilho de conversão)
- Implementação: ViaCEP confirma endereço, sistema calcula por cidade/região, bloqueia se fora da área

**Implementação Smartcell:** Patos R$9 / Triângulo Mineiro R$40 / Resto MG R$40 / Grátis >R$1.000 / Bloqueia fora de MG.

**Aplicação:** lojas regionais com zona de entrega bem delimitada. Para nacional, sim usar Melhor Envio.

## 4. Checkout híbrido — PIX automático + WhatsApp final

Combinação que dá o melhor dos dois mundos:
- **PIX automático** no site (Mercado Pago QR + polling 5s) → conversão imediata, sem fricção
- **Finalização via `wa.me`** (mensagem formatada com pedido, valor, endereço) → atendimento humano fecha, tira dúvida, ganha relacionamento

Não precisa de MegaAPI nesse modelo — só link `wa.me`. Para cliente que quer atendimento humano + venda automatizada, esse padrão substitui chatbot conversacional sem perder venda.

**Aplicação:** e-commerce de ticket médio/alto onde atendimento agrega (eletrônicos, joias, móveis premium, móveis sob medida).

## 5. Split de lucro entre sócios como regra de negócio

Quando o modelo é participação nos lucros, **a regra de split entra no admin financeiro como recurso explícito**, não em planilha externa:
- Painel mostra Receita × Custo × Lucro líquido por produto
- Soma 100% entre sócios (Smartcell: José + Marco + Eduardo)
- Cada um vê seu split em tempo real
- Top 10 produtos mais lucrativos

**Aplicação:** todo cliente em modelo de participação. Vira diferencial — cliente vê transparência financeira, sócios da ForYou Code também.

## 6. PWA + localStorage agressivo > backend para features secundárias

Features que não exigem dado central (favoritos, comparador, carrinho, histórico de visualização, preferência de tema, dados de cadastro) ficam em localStorage:
- UX instantânea (sem latência de rede)
- Custo zero de backend
- Funciona offline (PWA)
- Sincronização opcional quando user logar

**Aplicação:** sempre que a feature for "personalização do cliente" e não dado transacional. Para pedido, pagamento, estoque — sempre backend.

## 7. Fallback de modelo de IA é obrigatório

Em qualquer feature de IA em produção, ter fallback configurado:
- Modelo principal (ex: Gemini 2.5 Pro)
- Fallback (ex: GPT-5)
- Helper compartilhado (`_shared/ai-fallback.ts` no Smartcell)

Razão: provedor cai, quota estoura, latência sobe. Sem fallback, feature de IA quebra para o usuário final.

**Aplicação:** todo agente de IA, toda edge function que chama LLM, em todo projeto.

## 8. Edge Functions Supabase para webhook de pagamento

Padrão validado:
- `criar-pix-mercadopago` (gera QR, salva pendente)
- `webhook-mercadopago` (recebe confirmação, atualiza status)
- `consultar-status-pix` (polling do frontend a cada 5s)
- Mesmo padrão para Asaas

Vantagens: lógica perto do banco, sem servidor dedicado, escala automática, custo proporcional ao uso.

**Aplicação:** todo cliente que aceitar PIX. Padrão reaproveitável.

## 9. Urgency triggers como motor de conversão

Conjunto de gatilhos visuais sutis (não agressivos):
- "Última unidade" / "Estoque baixo"
- Timer de 3h em oferta
- "X pessoas vendo agora" (8–24 dinâmico)
- Welcome popup 3s com cupom de primeira compra

**Aplicação:** e-commerce com volume baixo/médio precisa criar senso de urgência sem mentir. Os números são reais (estoque) ou plausíveis (viewers).

## 10. Schema mobile-first em tabelas admin

Tabelas do painel admin precisam funcionar em mobile (sócio acessa do celular):
- `overflow-x-auto` em todas as tabelas
- Hidden columns em mobile (mostra só essencial)
- ConfirmDialog em ações destrutivas (delete, cancelar)
- Drag-and-drop ordering em listas (categoria, banner)

**Aplicação:** todo painel admin, sempre. Cliente vai abrir no celular, garantido.

## 11. Compartilhamento de componente entre rotas

`ProductForm` (formulário de produto) é reutilizado em:
- Novo produto
- Editar produto
- Novo seminovo (com extensão de schema)
- Editar variação

Componente recebe props de modo + schema variável. Evita duplicação e mantém UI consistente.

**Aplicação:** todo CRUD com tipos relacionados (produto vs seminovo, cliente PF vs PJ, projeto vs subprojeto).

## 12. FOUC prevention inline para dark mode

Quando suporta dark mode, script inline no `<head>` antes do React montar:
```html
<script>
  const theme = localStorage.getItem('theme');
  if (theme === 'dark') document.documentElement.classList.add('dark');
</script>
```
Evita flash de tela branca antes do JS aplicar o tema.

**Aplicação:** todo projeto com dark mode opcional.

---

## Padrões reaproveitáveis (resumo)

| Padrão | Quando aplicar |
|---|---|
| Schema seminovo | Cliente do nicho seminovos/usados |
| Imagem por modelo+cor | Produto com variação de condição |
| Frete por região | Loja regional bem delimitada |
| PIX automático + `wa.me` final | E-commerce ticket médio/alto |
| Split de sócios no admin | Cliente em participação nos lucros |
| localStorage para personalização | Favorito, carrinho, comparador, tema |
| Fallback de modelo IA | Toda feature de IA em produção |
| Edge functions para webhook | Pagamento, evento externo |
| Urgency triggers | E-commerce com volume baixo/médio |
| Tabelas admin mobile-first | Todo painel administrativo |
| Componente CRUD reutilizado | Tipos relacionados (produto/variação) |
| FOUC prevention inline | Dark mode opcional |

## Links relacionados
- [[Projetos/Smartcell|Smartcell — projeto completo]]
- [[Catalogo de entregas ForYou Code|Catálogo de entregas]]
- [[Processo de entrega de projetos na ForYou Code|Processo de entrega]]
