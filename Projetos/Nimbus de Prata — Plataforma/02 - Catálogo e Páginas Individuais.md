---
tipo: doc-projeto
projeto: Nimbus de Prata
doc: 02 — Catálogo e Páginas Individuais
data: 2026-06-26
---

# 02 — Catálogo e Páginas Individuais

[[Nimbus de Prata — Índice|← Índice]]

## O catálogo (parte central da experiência)

Apresenta de forma organizada todos os itens comercializáveis + itens institucionais que demonstram a força genética. Cada categoria com **área própria, filtros, busca, fotos e informações relevantes**. O visitante encontra o que procura **sem depender de conversa inicial no WhatsApp**.

### Categorias possíveis
Animais à venda · Cavalos à venda · Embriões · Sêmen · Touros · Doadoras · Prenhezes · Receptoras · Produtos genéticos · Animais de destaque · Animais históricos · Linhagens · Resultados · Itens sob consulta.

## Página individual = centro da experiência

> Não é ficha simples (uma foto + um preço). É **apresentação comercial premium, técnica e confiável**. Cada item tem identidade digital própria. Um veterinário, vendedor ou cliente abre a página e entende o valor **sem pedir tudo manualmente**. Aumenta confiança, reduz dúvidas, facilita a decisão.

### Campos possíveis (variam por categoria)

**Identificação:** nome · código · registro · raça · sexo · idade · data de nascimento · peso · pelagem · altura · categoria.

**Comercial:** disponibilidade · status comercial · preço · condições comerciais.

**Mídia e documentos:** fotos · vídeos · documentos · certificados · exames · laudos.

**Técnico/produtivo:** histórico · qualidades · características · dados técnicos · dados produtivos · informações reprodutivas.

**Genealogia:** pai · mãe · avós · linhagem · cruzamentos · descendentes.

**Relacionados:** produtos relacionados · itens semelhantes · embriões/sêmen/doadoras relacionados.

**Ações e share:** botões de compra, reserva, agendamento e contato · QR Code · link de compartilhamento.

### Notas de implementação (rascunho — validar)
- Modelo de dados precisa ser **flexível por categoria** (cavalo ≠ sêmen ≠ embrião). Campos opcionais + grupos condicionais.
- Genealogia é relacional (pai/mãe/avós/descendentes apontam para outros registros do próprio catálogo quando existirem) → habilita árvore navegável.
- QR Code por item: útil para feiras/leilões/etiquetas físicas levando à página digital.
- "Itens semelhantes/relacionados" = motor de recomendação simples por raça/linhagem/categoria.
