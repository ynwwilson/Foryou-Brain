---
tags: comercial plano-do-dia semana-1
data: 2026-04-13
semana: Semana 1 — Fundação
relacionado: "[[knowledge/Plano Comercial ForYou Code 2026]]"
pipeline: "[[Projetos/Pipeline Comercial 2026]]"
---

# Plano do Dia — Segunda-feira, 13/04/2026
## Semana 1 — Fundação · ForYou Code

> Dia 1 oficial do plano comercial. Ponto de partida: praticamente zero infraestrutura pronta.
> Foco total em criar base — contas, site, Meta Ads estruturado, primeiros prospects.

---

## Resumo por pessoa

| Pessoa | Foco do dia |
|--------|-------------|
| **José** | Meta Ads (contas + configuração) · Site + formulário (início da construção) |
| **Marco** | Contas nas plataformas de freela · LinkedIn otimizado |
| **Eduardo** | Contas nas plataformas de freela · LinkedIn otimizado · Início da pesquisa de 30 prospects |

---

## Contexto


> *"Pessoal, hoje a gente começa de verdade. Eduardo e Marco, vocês criam as contas nas plataformas de freela — eu já deixei tudo escrito, até o texto pra colar. Amanhã a gente grava os 3 demos. Eu fico com as contas de anúncio no Meta Ads e já começo a construir o site com o formulário. Review na sexta."*

---

## JOSÉ

### 1. Meta — do zero: aquecer e configurar

> Ponto de partida: zero. Não é criar campanha hoje — é estruturar tudo antes de gastar R$1.

- [ ] Criar/acessar o **Meta Business Manager** (business.facebook.com)
- [ ] Criar a **Página do Facebook** da ForYou Code
  - Nome: ForYou Code
  - Categoria: Software / Empresa de Tecnologia
  - Foto: logo
  - Bio: mesma descrição curta usada nas plataformas de freela
- [ ] Vincular Instagram @foryoucodee à Página no Business Manager
- [ ] Vincular perfis dos sócios (@wilsonads.ia, @yngomesmarco) como ativos de anúncio
- [ ] Criar a **conta de anúncios** dentro do Business Manager
  - Moeda: BRL · Fuso: Brasília
- [ ] Adicionar **forma de pagamento** na conta de anúncios
- [ ] Criar e instalar o **Pixel** → vincular à conta de anúncios
  - Testar disparo com Meta Pixel Helper
- [ ] **Aquecer a conta:** não rodar anúncio hoje
  - Deixar a página com pelo menos 3 posts antes de qualquer anúncio
  - Interagir com a página nos primeiros dias para construir sinal

> Campanhas, públicos e criativos só na semana 4. Hoje é fundação.

---

### 2. Site + Formulário — começar a construir hoje

**Stack:** Antigravity ou Lovable → deploy no Vercel

---

#### A promessa central — deixar explícita em TODO lugar

> **"Preenche o formulário e em 48h você recebe no WhatsApp uma prévia real do seu app — com a sua marca, as suas cores e as funcionalidades do seu negócio."**

Não é escopo. Não é PDF. É uma **prévia navegável** — telas do app com o nome do negócio dele, as cores dele, os módulos que fazem sentido pro caso dele. Ele vê o produto antes de comprar. Isso é o diferencial que nenhum concorrente oferece.

**Por que isso converte muito mais:**
- "Escopo em 48h" → abstrato, parece documento
- "Prévia do seu app em 48h" → concreto, visual, desejável
- Quem recebe uma prévia com o próprio nome/marca já comprou emocionalmente antes da call

---

#### Estrutura da página (one-pager)

```
[HEADLINE]
Em 48h você vê como seria o app do seu negócio.
Com a sua marca. De graça.

[SUBHEADLINE]
Preenche um formulário rápido e a gente monta
uma prévia real — telas, módulos, fluxos —
tudo contextualizado pro seu negócio.
Você vê antes de decidir qualquer coisa.

[PROVA SOCIAL — 2 cases em cards]
→ Escola com 200 alunos: app do aluno + painel da professora
   + dashboard da diretora. Em produção hoje.
→ Empresa com 40 leads/dia: IA de atendimento + painel
   de controle em tempo real. Em produção hoje.

[CTA ÚNICO — botão grande]
"Quero ver a prévia do meu app →"

[ABAIXO DO BOTÃO — microcopy]
Leva 4 minutos. Sem compromisso. Sem custo.
```

---

#### Formulário — completo para gerar prévia real

> O formulário precisa ser suficientemente detalhado para que Claude consiga montar uma prévia com identidade visual e funcionalidades específicas — não um template genérico.

**P1 — Nome do seu negócio**
*(campo aberto — ex: "Escola Evolução", "Clínica Bem Estar")*

**P2 — Qual é o seu segmento?**
- Escola / Cursinho / Plataforma educacional
- Clínica / Consultório / Centro de saúde
- Studio (pilates, academia, dança, artes marciais)
- Distribuidora / Empresa B2B
- E-commerce com marca própria
- Prestador de serviço com muitos clientes
- Outro: *(campo aberto)*

**P3 — Quem vai usar o app?**
*(múltipla escolha)*
- Meus clientes / alunos / pacientes
- Minha equipe interna
- Ambos

**P4 — Quais são as 3 principais coisas que o app precisa fazer?**
*(campo aberto — ex: "Agendamento online, comunicação com alunos, emissão de boleto")*
Placeholder: *Seja específico — quanto mais detalhe, mais fiel fica a prévia*

**P5 — Qual é o seu maior problema operacional hoje?**
*(campo aberto — ex: "Perco leads por demora no WhatsApp", "Minha equipe usa 4 ferramentas diferentes que não se integram")*

**P6 — Quais ferramentas você paga hoje?**
*(campo aberto — ex: "Hotmart R$300/mês, Calendly, planilha do Google")*
Placeholder: *Liste tudo que paga, mesmo que pareça básico*

**P7 — Tem alguma referência visual? Cor da sua marca?**
*(campo aberto + upload opcional de logo)*
- Cor principal: *(ex: "azul escuro", "#1A2E4A")*
- Logo: *(upload — opcional)*
- Referência de app que gosta: *(ex: "gosto do estilo do Nubank")*

**P8 — Quantos clientes, alunos ou pacientes ativos você tem hoje?**
- Menos de 50
- 50 a 200
- 200 a 500
- Mais de 500

**P9 — Faturamento mensal aproximado**
- Até R$50 mil
- R$50 mil a R$150 mil
- R$150 mil a R$500 mil
- Acima de R$500 mil

**P10 — Nome completo + WhatsApp**
*(campos obrigatórios)*

---

**Mensagem pós-envio:**
> *"Perfeito, [nome]! A gente já viu o que você preencheu. Em até 48h você recebe no WhatsApp uma prévia real do seu app — com as cores do [nome do negócio], os módulos que fazem sentido pro seu caso e as telas principais navegáveis. Não é template, não é PDF genérico. É feito pro seu negócio."*

---

#### O que muda nos anúncios com essa promessa

O CTA de todos os criativos passa a ser:

> *"Preenche um formulário de 4 minutos e em 48h você recebe a prévia do seu app — com a sua marca, de graça."*

Nunca mais "escopo" — sempre **"prévia do seu app"**.

---

**Regras do site:**
- ❌ Sem preço listado
- ❌ Sem chat ao vivo — tudo vai pra WhatsApp
- ❌ Sem múltiplas páginas — one-pager converte melhor
- ✅ Link usado nas plataformas de freela assim que estiver no ar
- ✅ A palavra "prévia" aparece no mínimo 3 vezes na página

---

## MARCO

### Plataformas de freela — criar contas

**Perfil padrão (usar em todas):**
- Nome: `ForYou Code`
- Foto: logo da ForYou Code
- Site: Instagram @foryoucodee (até o site ficar pronto)
- Taxa hora: R$350
- Localização: Patos de Minas, MG (atende todo o Brasil — online)

---

#### Workana — workana.com
- [ ] Criar conta como freelancer/agência
- [ ] Título: ver abaixo
- [ ] Colar descrição (ver abaixo)
- [ ] Adicionar habilidades
- [ ] Adicionar 2 projetos no portfólio
- [ ] Salvar buscas: `app personalizado` · `sistema de gestão` · `automação whatsapp` · `CRM personalizado` · `plataforma digital`
- [ ] Ativar notificações por e-mail para cada busca

#### 99Freelas — 99freelas.com.br
- [ ] Criar conta como prestador
- [ ] Mesmo título e descrição da Workana
- [ ] Ativar alertas nas categorias: Desenvolvimento Web · Aplicativos Mobile · Automação e Scripts

#### Freelancer.com
- [ ] Username: `foryoucode`
- [ ] Adaptar descrição para inglês (mesma estrutura — prova primeiro)
- [ ] Salvar buscas: `whatsapp automation brazil` · `custom app brazil` · `crm development`

#### LinkedIn — perfis dos sócios
- [ ] José — Headline: `ForYou Code · App pra escola com 200 alunos + IA pra 40 leads/dia. Em produção.`
- [ ] Marco — Headline: `ForYou Code · Sistemas e IA de atendimento pra donos de negócio`
- [ ] Eduardo — Headline: `ForYou Code · Apps e automações sob medida`
- [ ] Ativar seção "Serviços" em todos: Desenvolvimento de Aplicativos · Automação WhatsApp · CRM · IA para Negócios
- [ ] Salvar busca por: `desenvolvimento app` · `automação whatsapp` · `sistema crm`

---

### COPY — Tudo pronto para colar

> **Regra que guiou a reescrita:** nenhuma frase que não seja prova concreta ou descrição do problema real do cliente. Zero claims. Zero tentativa de soar diferente dizendo que é diferente.

---

**TÍTULO (Workana, 99Freelas)**

```
Entregamos: plataforma pra escola com 200 alunos e IA de atendimento pra empresa com 40 leads/dia no WhatsApp. Os dois em produção.
```

---

**DESCRIÇÃO (Workana, 99Freelas)**

```
Há alguns meses a gente entregou uma plataforma pra uma escola aqui em Minas Gerais.

O aluno entra pelo app: simulados, banco de questões, caderno de erros, planner. A professora tem painel com desempenho individual de cada aluno. A diretora abre o dashboard e vê retenção, contratos, quem está em risco de cancelar — antes que o aluno cancele. Tudo com a marca da escola, no domínio dela. Nenhuma plataforma de terceiro no meio.

Antes disso, construímos a IA de atendimento de uma empresa que recebia 40 mensagens por dia no WhatsApp e perdia venda por demora. A IA responde. Mas o que mudou de verdade foi o seguinte: o dono abre um painel e vê cada conversa pelo nome do lead — o que a pessoa perguntou, a objeção que levantou, o que a IA respondeu e por quê. Entra na conversa quando quer, com tudo na tela. No final do mês, sabe qual objeção aparece mais, qual horário converte melhor, qual perfil fecha mais.

Se você quer ver um desses sistemas funcionando antes de decidir qualquer coisa — me chama. 10 minutos.
```

---

**PORTFÓLIO — Projeto 1**

Título:
```
Escola com 200 alunos, 3 ferramentas que não se falavam, zero app próprio. Resolvemos.
```

Descrição:
```
A escola pagava pra três sistemas diferentes que não conversavam entre si. Aluno sem acesso próprio. Professora sem visibilidade de desempenho. Diretora sem dado nenhum sobre retenção.

Construímos a plataforma inteira. O aluno entra pelo app e tem banco de questões, simulados adaptativos, caderno de erros e planner de estudos. A professora tem painel de turmas, histórico de cada aluno, análise de desempenho individual. A diretora abre o dashboard e vê retenção por período, contratos ativos, alunos em risco de cancelamento em tempo real.

Tudo com a marca da escola. No domínio deles. Nenhuma mensalidade pra plataforma de terceiro. Em produção hoje.
```

---

**PORTFÓLIO — Projeto 2**

Título:
```
40 mensagens por dia no WhatsApp. Perdia venda todo dia sem saber quantas. Mudamos isso.
```

Descrição:
```
O dono sabia que perdia venda por demora na resposta. Não sabia quantas. Não sabia quem era cada lead. Não sabia o que as pessoas perguntavam, o que travava o fechamento, qual objeção aparecia mais.

Construímos a IA de atendimento. Ela responde em segundos, qualifica e encaminha. Mas o que mudou de verdade foi o painel: o dono abre e vê cada conversa pelo nome do lead. Vê o que a pessoa perguntou, a objeção que levantou, o raciocínio que a IA usou pra responder. Entra na conversa com um clique quando quiser — com o histórico completo na tela, nada se perde.

No final do mês: quais objeções aparecem mais, quais horários convertem melhor, qual perfil de lead fecha mais. Dado que antes não existia.
```

---

**RESPOSTA QUANDO APARECER PROJETO RELEVANTE**

```
Oi [nome], vi seu projeto aqui.

Já entregamos exatamente isso — pra [escola com 200 alunos / empresa com 40 leads/dia no WhatsApp / clínica]. Tá no ar hoje, posso te mandar o link pra você navegar agora.

10 minutos de call e você vê tudo funcionando. Tem hoje ou amanhã?
```

*(sem "não vou te mandar proposta por texto" — soa arrogante. Só vai direto ao que importa.)*

---

**DESCRIÇÃO CURTA (GetNinjas, Trampos, campos com limite de caracteres)**

```
Entregamos dois sistemas em produção: plataforma educacional pra escola com 200 alunos e IA de atendimento pra empresa com 40 leads/dia no WhatsApp. Se o seu projeto parece com um desses, a gente provavelmente já sabe o que fazer. Me chama pra ver funcionando.
```

---

## EDUARDO

### Plataformas de freela — criar contas

#### GetNinjas — getninjas.com.br
- [ ] Criar conta como profissional
- [ ] Categoria: Tecnologia da Informação → Desenvolvimento de Software
- [ ] Raio de atendimento: Todo o Brasil (online)
- [ ] Descrição: *(usar a descrição curta da seção COPY acima)*
- [ ] Serviços: Desenvolvimento de Aplicativos · Automação WhatsApp · CRM Personalizado · IA para Negócios

#### Trampos.co
- [ ] Criar conta como profissional/empresa
- [ ] Título e descrição: *(usar a descrição curta da seção COPY acima)*
- [ ] Monitorar projetos de produto digital

#### LinkedIn — Eduardo
- [ ] Headline: `ForYou Code · Apps e automações sob medida`
- [ ] Ativar seção Serviços: Desenvolvimento de Aplicativos · Automação WhatsApp · CRM · IA para Negócios
- [ ] Salvar buscas relevantes

---

### Pesquisa de 30 prospects — Instagram (iniciar hoje)

**Onde buscar:**

| Busca | Foco |
|-------|------|
| `escola de inglês Patos de Minas` | Escola com base de alunos mensalistas |
| `cursinho vestibular Patos de Minas` | Volume alto, processo manual |
| `clínica odontológica Patos de Minas` | Múltiplos profissionais, agenda cheia |
| `studio pilates Patos de Minas` | Recorrência, clientes mensalistas |
| `clínica estética Patos de Minas` | Agendamento + comunicação caótica |
| `escola de música Patos de Minas` | Alunos mensalistas, sem sistema próprio |
| `distribuidora Patos de Minas` | B2B com time comercial |
| `academia Patos de Minas` | Academias independentes (não franquias) |
| `escola Uberlândia` | Expandir para Triângulo Mineiro |
| `clínica Uberlândia` | Segunda cidade prioritária da região |

**Sinais de que entra na lista:**
- Bio com endereço físico
- Posts frequentes sobre atendimento, turmas, agenda
- Stories ativos — dono presente no digital
- Link na bio para ferramentas genéricas (Linktree, Google Forms, Calendly avulso)
- Comentários de clientes reais

**Sinais de descartar:**
- Franquia grande (não decide)
- Menos de 500 seguidores com pouca atividade
- Perfil parado há meses

**Tabela para preencher e mandar pro José:**

| Nome do negócio | Nicho | Cidade | @Instagram | Sinais observados | Produto indicado |
|----------------|-------|--------|-----------|------------------|-----------------|
| | | | | | |

> Produto indicado: **IA** (negócio com volume de WhatsApp) ou **Ecossistema** (escola, clínica, studio com recorrência)

---

## Meta do dia

- [ ] Todas as contas de freela criadas e preenchidas (Marco + Eduardo)
- [ ] LinkedIn otimizado de todos
- [ ] Meta Ads configurado (José)
- [ ] Site com estrutura base no ar (José)
- [ ] Pelo menos 10 prospects na tabela (Eduardo)

---

## Amanhã — Terça 14/04

Dia dos demos. Gravar os 3 assets:
- Asset 1: painel do Rodrigo (2–3 min)
- Asset 2: app da Dayane (2–3 min)
- Asset 3: app ForYou Code interno (2–3 min)
- Eduardo: edição básica dos 3
