# Secretária IA — feature-âncora da plataforma

> Doc dedicado. Vinculado a `Plataforma Imobiliária Patos de Minas.md`.
> Ideia do Mestre (2026-06-29), elevada e detalhada aqui.

---

## 1. Conceito (a versão 100%)

Cada corretor / imobiliária ganha uma **secretária pessoal de IA, só dele**, que tem **poder total sobre a conta dele na plataforma** e é comandada por **voz ou texto, em linguagem natural** (manda um áudio no WhatsApp/app e pronto).

**O salto de visão:** a secretária **não é um recurso lateral — ela é a interface principal do produto** para o corretor. Ele praticamente **não mexe em painel**: ele *fala* e ela executa. O dashboard vira backup, não o caminho principal.

> Pitch: *"Você não anuncia imóvel. Você tem uma secretária que cuida de tudo — é só falar com ela."*

Exemplo do Mestre:
> Corretor: "Vendi o ap da rua Artur Magalhães, nº 500."
> Secretária: "Fechado. Vou marcar como vendido nas suas vendas, atualizar seus números e tirar do ar. Confirma?"
> Corretor: "Confirma."
> Secretária: "Pronto. Esse foi seu 3º fechamento no mês 👏"

---

## 2. Por que isso é o CORAÇÃO do produto (não enfeite)

Ataca de uma vez os pontos que o conselho disse que matam portal imobiliário:

1. **Mantém o dado fresco sozinho.** O maior assassino de portal é catálogo desatualizado (corretor não mexe no painel). Mas mandar um áudio? Manda. Vendeu → fala → sai do ar na hora. **O hub se mantém vivo sem esforço.**
2. **Entrega a atribuição** (o coração que faltava). "Vendi o X" → registra a venda → vira prova de valor e gancho de renovação. Do jeito mais natural que existe: o cara só fala.
3. **Sobe o quanto ele paga e derruba o churn.** Deixa de ser "site de anúncio" e vira **"minha secretária"**. Ninguém cancela secretária. Responde direto o risco aberto (*"corretor paga tendo imobpatos grátis?"* → paga, porque o imobpatos nunca terá isso).
4. **Diferencial que ninguém na praça tem** — nem imobpatos (morto), nem ZAP/OLX. Reposiciona a marca de "portal" para "assistente de vendas do corretor".
5. **Stickiness diária.** Ele fala com ela todo dia → hábito → retenção.

---

## 3. Poder total — o que ela faz (tudo que o corretor faria no painel)

A secretária tem acesso ao **mesmo conjunto de ações** que o corretor teria clicando no painel — só que por linguagem natural. "Poder total" = ela é uma camada de linguagem por cima de **toda a API da conta dele**.

**Imóveis**
- Cadastrar por voz (ela pergunta o que falta: fotos, valor, bairro...).
- Editar preço, descrição, status.
- Marcar **vendido / alugado / reservado** → sai do hub ativo, entra no contador do perfil.
- Reativar, duplicar, destacar (se plano permitir).

**Leads / clientes**
- "Quem me chamou hoje?" → lista os contatos.
- Desbloquear lead (nome + telefone).
- Mudar status do lead (contatei / visitou / proposta / fechou).
- "Me lembra de ligar pro João amanhã 9h" → cria lembrete/follow-up.

**Perfil**
- Atualizar bio, foto, área de atuação.
- "Como tá meu perfil esse mês?" → contadores e estatísticas faladas.

**Consultas e relatórios falados**
- "Como foi minha semana?" · "Qual imóvel teve mais contato?" · "Quantas visitas marquei?"

**Agenda**
- Marcar visita, ver agenda do dia, lembrar de compromissos.

**Busca para o cliente dele**
- "Tenho um cliente querendo casa 3 quartos até 400 mil no centro, o que tem?" → ela busca **no hub inteiro** (inclusive imóveis de parceiros) e devolve as opções pra ele repassar.

**Proativa (fase 2)**
- "Seu anúncio X tá há 60 dias sem atualizar, quer renovar?"
- "Você tem 3 leads sem resposta há 2 dias."
- Resumo diário automático: "bom dia, ontem você recebeu 4 contatos e tem 1 visita hoje às 15h."

**Marketing (fase 2+)**
- Gera legenda/post do imóvel pro Instagram dele.

---

## 4. "Poder total" COM segurança (inegociável)

Poder total sem trava = desastre (IA remove o imóvel errado). Regras:

- **Isolamento por dono.** Cada secretária só age na **conta do próprio corretor**. Nunca edita/remove imóvel de outro. Autenticação pelo número/login do dono.
- **Confirmação em ação destrutiva ou irreversível** (remover, marcar vendido, mudar preço relevante, desbloquear lead pago): ela repete o que vai fazer e pede **"confirma?"** antes.
- **Desambiguação, nunca chute.** "Você tem 2 imóveis na rua Artur Magalhães — o 500 ou o 230?" Se não tem certeza, pergunta.
- **Log de auditoria de tudo** que ela fez + **desfazer** ("desfaz a última").
- **Limites duros:** não faz pagamento, não cancela plano, não muda dado financeiro sem confirmação explícita e dupla.

---

## 5. Como funciona (arquitetura, alto nível — pro Wilson)

1. **Canal:** MVP = gravar áudio / digitar **dentro do app** (zero dependência). Fase 2 = **WhatsApp** (Cloud API) — reabre custo/aprovação Meta, por isso fica pra depois.
2. **Áudio → texto:** transcrição pt-BR (Whisper ou API de STT).
3. **Cérebro:** LLM com **function-calling / tool use** (Claude, alinhado ao stack). O modelo decide qual ação chamar.
4. **Tools = ações da conta.** Cada ação do painel (criar imóvel, marcar vendido, listar leads, criar lembrete...) é exposta como uma função que a IA pode chamar. **É isso que dá o "poder total"** — mesmo conjunto de ações do corretor, via linguagem.
5. **Contexto/memória por corretor:** estado da conta + histórico recente; **busca no catálogo dele** pra resolver "o ap da rua X" → id do imóvel.
6. **Guardrails:** confirmação + escopo restrito à conta + log + desfazer.

> Resumo técnico: a secretária é uma **camada conversacional sobre a API do produto**. Construa a API/ações primeiro (o MVP já faz isso); a secretária pluga por cima.

---

## 6. Faseamento (não furar o lançamento)

- **MVP (2-3 semanas):** SEM secretária. Mas o banco/ações já desenhados pra ela plugar depois.
- **v0 — primeiro pós-lançamento / gancho do Pro:** atualizar status por voz (vendido/alugado → sai do hub, com confirmação) · consultar contatos · cadastro rápido (rascunho). Tudo in-app.
- **v1:** leads completos (status, follow-up, lembrete) · agenda · busca pro cliente · edição de imóvel por voz.
- **v2 — secretária completa:** proativa (resumos, alertas, sugestões) · WhatsApp · geração de conteúdo/post · apoio a parceria entre corretores.

---

## 7. Monetização

A secretária é **o gancho nº1 do plano Pro**.
- **Free:** aparece no hub, sem secretária (ou só consulta básica).
- **Pro (~R$199/mês):** leads desbloqueados **+ secretária com poder total**.
→ Justifica o R$199 fácil: ele não paga por anúncio, paga por uma secretária que trabalha por ele 24h.

---

## 8. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| IA executa ação errada (remove imóvel errado) | Confirmação obrigatória + desambiguação + desfazer + log |
| Alucinação de dado | Sempre busca no catálogo real do corretor antes de agir; nunca inventa id |
| Custo de token por uso | Baixo (poucos áudios/dia por corretor); só no Pro |
| Dependência de WhatsApp (custo/Meta) | Começar in-app; WhatsApp só na v2 |
| Corretor não confiar na IA | Começar pelo simples (status/consulta), confirmação visível, ganhar confiança antes de dar mais poder |

---

## 9. Ideia extra: dar nome/persona à secretária

Uma secretária com **nome e personalidade** ("fala com a [Nome]") aumenta o sentimento de "ela é minha". Reforça marca e hábito. Nome a definir junto com a marca da plataforma.

---

## 10. Veredito

É **o maior diferencial do projeto** e o que melhor resolve os riscos do conselho (dado fresco + atribuição + WTP + churn). **Mantém-se como feature-âncora premium**, construída logo após o MVP — não dentro das 2-3 semanas, mas com o banco já preparado pra ela desde o dia 1.
