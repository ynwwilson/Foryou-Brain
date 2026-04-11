---
tipo: knowledge
tags: [produto, saas, gratuito, pulso, foryoucode]
atualizado: 2026-04-10
---

# ~~Pulso~~ → ForYou Life

> **Nome atualizado para ForYou Life.** Esta nota está desatualizada.
> Ver nota atual: [[knowledge/ForYou Life - SaaS Gratuito ForYou Code|ForYou Life — nota completa]]

---

## O que é

Não é tracker de hábitos. Não é agenda comum. É o lugar onde o empresário enxerga — com clareza — se está sendo produtivo ou só ocupado, o que está travando o negócio, e o que precisa mudar.

**Diferencial:** a maioria dos apps mostra dado. O Pulso interpreta, compara, alerta e fala o que está acontecendo — sem o empresário precisar perguntar.

---

## Problema que resolve

O empresário trabalha 12h/dia e não sabe se está avançando. Não tem registro de nada. Não mede conversão de reunião. Não sabe qual dia da semana performa melhor. Repete os mesmos erros porque nunca parou pra analisar. Tudo depende da memória dele.

---

## Funcionalidades

### Agenda inteligente + tarefas
Empresário adiciona reuniões, compromissos e tarefas. O app usa isso como fonte de dados — não é só calendário, é inteligência.

### Check-in automático pós-evento
Quando o horário de um evento passa, o app pergunta:

| Tipo de evento | Pergunta | O que auto-preenche |
|---|---|---|
| Reunião de proposta | Fechou? Quanto? | Faturamento, conversão, pipeline |
| Call de qualificação | Avançou? Próximo passo? | Status do lead, próxima tarefa |
| Reunião de equipe | O que foi decidido? Tem tarefa nova? | Tasks criadas automaticamente |
| Entrevista | Vai contratar? | Registro do processo seletivo |
| Evento pessoal (academia, consulta, jantar, etc.) | Pergunta leve e casual, resposta em 1 toque | Energia/humor do dia |

**Eventos pessoais — tom completamente diferente.** Não é formulário, é um amigo perguntando:

- Academia concluída → *"E aí irmão, como foi o treino?"* → **[ Ruim ] [ Normal ] [ Bom ]**
- Consulta médica → *"Tudo certo com a consulta?"* → **[ Sim ] [ Mais ou menos ] [ Não muito ]**
- Jantar/evento social → *"Curtiu?"* → **[ Muito ] [ Foi ok ] [ Preferia ter ficado em casa ]**

Um toque. Sem texto. Sem obrigação. Se o empresário ignorar, app não insiste.

Esses dados alimentam o gráfico de energia — o app cruza com produtividade:
> *"Você é 34% mais produtivo nos dias em que treinou. Essa semana você não treinou nenhum dia."*

Empresário responde em linguagem natural — *"fechei por R$12k, foi bem"* — app preenche tudo sozinho.

### Planejamento diário (2 min)
- **Manhã:** prioridade real do dia + o que vai delegar + bloqueio atual
- **Noite:** o que cumpriu + o que não fez + motivo

### Revisão semanal guiada (10 min)
Perguntas estruturadas sobre a semana. IA gera o "norte" da semana seguinte com base nas respostas.

---

## Dashboard e métricas

| Métrica | O que mede |
|---|---|
| Produtividade % | Tarefas planejadas vs concluídas |
| SLA pessoal % | Compromissos assumidos vs cumpridos no prazo |
| Eficácia % | Prioridades importantes vs realmente executadas |
| Consistência % | Dias com planejamento matinal completo |
| Conversão de reunião | Reuniões fechadas vs total, por dia/horário |
| Faturamento vs meta | Progresso + projeção pelo ritmo atual |
| Gráfico de energia | Humor/energia declarado cruzado com produtividade |

---

## A inteligência proativa

O app não espera o empresário abrir — ele chega com insights:

> *"Semana passada seu faturamento caiu 31% vs a anterior. Isso coincidiu com 4 dias sem planejamento matinal e você registrou 'travado em contratação' 3 vezes. Nas últimas 2 vezes que isso aconteceu, o que recuperou foi focar em prospecção nos primeiros 2 dias."*

> *"Você fecha 71% das reuniões antes do meio-dia. Depois das 17h, fecha 18%. Você tem 2 reuniões de proposta essa semana marcadas pras 18h."*

> *"Você mencionou o mesmo bloqueio há 3 semanas. Isso virou gargalo — não é tarefa, é decisão pendente."*

> *"Com base no seu ritmo atual, você vai atingir 58% da meta do mês. Você ainda tem 12 dias."*

**Estudos contextuais** — quando detecta padrão, surfaça pesquisa relevante:
> *"Seu SLA pessoal está em 42%. Pesquisa com 2.400 CEOs mostrou que líderes acima de 75% têm equipes 2x mais engajadas — o time espelha o comportamento do dono."*

---

## Custo operacional (Claude Haiku)

IA roda 1x por semana por usuário (~2.000 tokens):

| Usuários | Custo/mês |
|---|---|
| 1.000 | ~R$50 |
| 5.000 | ~R$250 |
| 20.000 | ~R$1.000 |

Check-ins pós-evento: ~500 tokens cada. Empresário tem ~3 eventos/dia = R$0,05/usuário/mês adicional.

**Total realista com 5.000 usuários ativos: ~R$400–500/mês.**

---

## Por que não conflita com os produtos da ForYou Code

ForYou Code vende sistemas para o **negócio** do cliente (apps, automações, CRM). O Pulso é ferramenta para a **rotina pessoal** do dono. Camadas diferentes — um complementa o outro.

---

## A ponte para os produtos pagos

Depois de meses de uso, o Pulso conhece os padrões do empresário. Quando o mesmo gargalo aparece repetido:

> *"Esse problema apareceu 8 vezes nos últimos 90 dias nos seus registros. A gente tem uma solução construída exatamente pra isso — quer ver?"*

Não é venda forçada. É dado real do empresário apontando para o produto certo.

---

## Como entra no processo comercial

- Seguiu qualquer perfil → 1 mês grátis via ManyChat
- Preencheu formulário de escopo gratuito (Meta Ads) → acesso junto com o escopo
- Virou cliente de app ou automação → acesso permanente incluso no contrato

---

## Stack

| Camada | Tecnologia |
|---|---|
| Interface | Lovable |
| Banco de dados | Supabase |
| Deploy | Vercel |
| IA (análise semanal + check-ins) | Claude Haiku |
| Push notifications | Supabase Edge Functions |

---

## MVP — o que construir primeiro

1. Agenda simples + adição de tarefas
2. Check-in automático pós-reunião (pergunta + auto-preenche faturamento)
3. Planejamento matinal (3 campos)
4. Dashboard básico: produtividade %, SLA %, meta do mês
5. Análise semanal com Haiku

**Fase 2:** padrões e alertas proativos, estudos contextuais, comparações históricas, gráfico de energia.

---

## Links
- [[knowledge/Plano Comercial ForYou Code 2026|Plano Comercial — seção 20]]
- [[knowledge/ICP da ForYou Code|ICP da ForYou Code]]
