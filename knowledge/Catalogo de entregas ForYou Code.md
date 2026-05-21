---
tipo: knowledge
tags:
  - foryoucode
  - catalogo
  - produto
  - entregas
  - capacidades
  - modulos
  - agentes-ia
  - integracoes
atualizado: '2026-05-21'
---

# Catálogo de Entregas — ForYou Code

> **Fonte oficial do que a ForYou Code entrega.** Todo material comercial, página do site, prompt de Claude que gera escopo e proposta para cliente devem referenciar esta nota. Atualizar aqui antes de qualquer outro documento.

> **Princípio guia:** *commodity regulada/fiscal/legada = integramos. Camada operacional = construímos.* Tudo que está aqui ou já foi entregue (validado), ou é construível com a stack atual em prazo razoável.

---

## 0. Posicionamento atualizado

> Fonte canônica: [[Posicionamento ForYou Code]].

A ForYouCode **não vende app, CRM ou automação como produto fechado**.

A ForYouCode constrói o sistema próprio que a empresa teria se pudesse transformar a operação real dela em tecnologia.

A régua é:
1. É legal?
2. É tecnicamente possível?
3. Melhora venda, controle, entrega, cobrança, atendimento, experiência ou decisão?

Se sim, a ForYouCode consegue desenhar, construir ou integrar.

O catálogo abaixo não deve ser lido como limite. Ele é uma biblioteca de capacidades já validadas ou viáveis. A venda começa pela operação do cliente, não pela lista de módulos.

---

## 1. Resumo executivo

A ForYou Code entrega **ecossistemas digitais white-label** em 5 camadas:

1. **Núcleo de aplicação** — app + painel + banco + deploy + autenticação. Todo cliente recebe.
2. **Módulos operacionais** — CRM, atendimento, BI, automações, financeiro, marketing, agendamento, e-commerce. Cliente escolhe.
3. **Agentes de IA** — vendedores, atendentes, qualificadores, retentores, analistas. Customizados por nicho.
4. **Features por nicho** — bibliotecas prontas pra educação, saúde, imobiliária, varejo B2B, e-commerce, construção.
5. **Automatismos entre sistemas** — orquestração entre o que o cliente já paga (ERP, banco, Meta Ads) e o que entregamos.

**O que NÃO entregamos:** commodity fiscal/regulada (ERP completo, folha, NF-e direto, sistema contábil). Integramos via API.

**Cases e produtos que validam o catálogo:**
- **Rainha da Aprovação / Dayane** (entregue 20/03/2026, em produção em metodorainhadaaprovacao.vercel.app): plataforma educacional multi-perfil com 4 áreas (aluno/professor/diretor/admin), banco de questões, simulado adaptativo, redação, X-Ray do aluno, retenção, contratos. Manutenção e aprimoramentos contínuos. Case público autorizado (não divulgar valor).
- **Concretize / Rodrigo** (em produção): IA de atendimento WhatsApp com visão, voz, mirroring, painel de takeover humano, dashboard de leads, integração Chatwoot.
- **Smartcell Premium Store / Fellipe** (entregue 25/04/2026, em produção em smartcellsite.com.br): e-commerce premium de eletrônicos com PIX automático, IA gerando descrição e imagem por cor, painel admin com 13 módulos, schema dedicado para seminovos (IMEI/bateria/checklist 30 itens), split de sócios no financeiro. Modelo: 20% participação nos lucros, sem fee de projeto. Case público autorizado.
- **ForYou Leads** (interno, em produção): máquina de prospecção com scraping, análise de perfil com Claude, mensagem personalizada, envio de DM com vídeo via AdsPower/Playwright, pipeline, ManyChat, métricas, A/B test, sentimento, ROI por hashtag e alertas Telegram.
- **Imerso** (produto próprio, MVP funcional): SaaS de tour 3D imobiliário com upload/processamento de scan, viewer navegável, página pública compartilhável por WhatsApp, analytics e painel do corretor.
- **Infinity Content** (interno): máquina de conteúdo que busca novidades em fontes atualizadas, usa web search quando precisa e gera dossiê com hook, roteiro, CTA, fonte e link real.

Esses exemplos provam a tese: a ForYouCode não está limitada a CRM, app ou automação. A empresa transforma operação específica em sistema proprietário.

---

## 1.1 As 4 dores reais do ICP (não é "gasto muito em SaaS")

> A economia de SaaS é prova quantitativa, não a doença. Quem fatura R$150k+/mês não está apertado pelos R$2.700/mês de mensalidade — está apertado pelo **caos que aqueles 12 SaaS criaram**. Toda comunicação comercial (site, anúncio, pitch, proposta) deve falar com essas 4 dores.

| # | Dor | Tradução prática | Sinal de compra (do ICP) |
|---|---|---|---|
| 1 | **Perda de controle** | Não sabe onde está cada lead, cada pedido, cada conversa | "Estou perdendo controle do processo" |
| 2 | **Fragmentação de dado** | CRM não fala com WhatsApp, que não fala com financeiro, que não fala com BI | "Tenho tudo em lugares diferentes" |
| 3 | **Sem marca própria no digital** | Cliente final usa ferramenta de terceiro com a cara do terceiro | "Quero um app com meu nome" |
| 4 | **Receita escapando** | Lead some, vendedor não registra, atendimento perde a janela | "Perco cliente por demora", "minha comunicação é bagunça" |

### A pergunta que o site/pitch deve provocar

**Antes (errado):** *"Quanto você gasta?"*
**Depois (certo):** *"Quanto você está deixando de ganhar enquanto opera fragmentado?"*

A primeira pergunta é commodity (qualquer concorrente faz). A segunda é o que sustenta R$30k–R$60k de ticket.

### Virada de narrativa em todo material

| Antes | Depois |
|---|---|
| "Substituímos seus SaaS" | "Orquestramos tudo — o que você já paga e o que a gente constrói" |
| "Economia de mensalidade" | "Eliminação de tarefa manual entre sistemas" |
| "Tem CRM, BI, atendimento" | "CRM que recebe lead direto do anúncio, atendimento que vira card no funil, BI que mostra CAC do dia em tempo real" |
| "Integração com ERP" | "Pedido fechado vira NF emitida sem ninguém clicar em nada" |
| "Você economiza R$X" | "Você para de operar entre ferramentas e começa a operar uma só" |

---

## 2. Stack técnica oficial

> Tudo que está abaixo é o que a equipe domina hoje. Qualquer entrega sai dessa caixa de ferramentas.

### Camada de aplicação
| Ferramenta | Papel | Quando usa |
|---|---|---|
| **Google Antigravity** | Motor principal de construção | Apps complexos, lógica, agentes, refatoração, testes E2E |
| **Lovable** | Preview + ajustes de UI | Frontend, componentes visuais, edições rápidas |
| **Claude Code** | Terminal agêntico | Automações, scripts, integrações, ajustes cirúrgicos |
| **Bridge Python** | Cola entre serviços | Conectar Claude Code a APIs externas |

### Camada de infraestrutura
| Ferramenta | Papel |
|---|---|
| **Vercel** | Deploy frontend + serverless functions |
| **Cloudflare** | CDN, DNS, Workers, Pages |
| **Supabase** | Postgres + auth + storage + realtime + edge functions |
| **Upstash Redis** | Cache, filas, deduplicação, rate limit |
| **pgvector** (Supabase) | Embeddings, busca semântica, memória de IA |

### Camada de comunicação
| Ferramenta | Papel |
|---|---|
| **MegaAPI** | WhatsApp Business API gerenciado |
| **Evolution API** (self-hosted) | WhatsApp alternativo quando precisa controle total |
| **Chatwoot** (self-hosted) | Inbox unificado omnichannel |
| **WhatsApp Cloud API** (Meta direto) | Quando volume justifica oficial |

### Camada de IA
| Ferramenta | Papel |
|---|---|
| **Anthropic Claude** | IA principal — texto + visão |
| **OpenAI GPT** | Fallback de texto |
| **OpenAI Whisper** | Transcrição de áudio |
| **Lovable AI Gateway** | Acesso unificado a Gemini 2.5 Pro/Flash + GPT-5 (validado em Smartcell para descrição e imagem de produto) |
| **Gemini Image** | Geração de imagem por cor (validado em Smartcell) |
| **Embeddings** (OpenAI ou Voyage) | Busca semântica, RAG |

### Camada operacional
| Ferramenta | Papel |
|---|---|
| **Autentique** | Contratos digitais |
| **AdsPower** | Gestão multi-conta Meta Ads |
| **Obsidian + GitHub** | Memória, briefings, documentação |

### Princípios técnicos não negociáveis
- **Sem n8n** — automação é código direto
- **Toda automação ganha frontend em Lovable** — usuário tem que ver e controlar
- **Mesmo repositório GitHub** para Antigravity, Lovable e Claude Code
- **Push no Git = atualiza Lovable automaticamente**
- **Banco de dados sempre no Supabase do cliente** — dado é dele, não nosso

---

## 3. Núcleo de aplicação (toda entrega inclui)

Tudo cliente recebe, sempre, em qualquer projeto. Sem exceção.

### Aplicação branded
- **App web responsivo + PWA** instalável no celular
- **Domínio próprio do cliente** (foryoumarca.com.br ou loja.cliente.com.br)
- **Marca do cliente em tudo** — logo, paleta, fonte, ícone do app
- **Multi-dispositivo** — funciona em desktop, tablet, mobile sem app store
- **Modo offline básico** quando faz sentido (PWA)

### Painel administrativo
- **Backoffice completo** com a marca do cliente
- **Multi-usuário** com níveis de acesso configuráveis
- **Dashboard inicial** customizado por papel
- **Busca global** em todos os módulos
- **Notificações em tempo real** dentro do painel

### Autenticação e segurança
- **Login por e-mail/senha**
- **Login social** (Google, Apple) opcional
- **Recuperação de senha** automática
- **2FA** (autenticação de dois fatores) opcional
- **Níveis de acesso** (admin / gerente / operador / cliente final / customizável)
- **Sessões com expiração** configurável
- **Logs de auditoria** — quem fez o quê, quando, de onde
- **RLS (Row Level Security)** no Supabase pra isolar dados por cliente/empresa

### Infraestrutura entregue
- **Deploy automático** via GitHub → Vercel
- **CDN e DNS** configurados no Cloudflare
- **Banco de dados** no Supabase (projeto do cliente)
- **SSL / HTTPS** automático
- **Backup automático diário** do banco
- **Monitoramento básico** (uptime, erros)
- **Ambiente de produção + staging** quando faz sentido

### Sistema de notificação
- **E-mail transacional** (Resend, SendGrid ou Supabase nativo)
- **Push notification** (web push)
- **WhatsApp transacional** (via MegaAPI)
- **SMS** (opcional, Twilio)
- **In-app** (notificação dentro do painel)
- **Templates configuráveis** sem precisar de dev

### Documentação operacional
- **Manual básico** pro cliente operar
- **Vídeos de onboarding** (até 3 vídeos curtos por contrato)
- **Glossário de funcionalidades** dentro do próprio painel
- **FAQ inicial** populado pelo time

---

## 4. Módulos operacionais (substituem SaaS de terceiro)

> Cada módulo é independente. Cliente escolhe o que precisa. Tudo conversa via banco único.

### 4.1 CRM
**Substitui:** Pipedrive, RD Station CRM, HubSpot, Kommo, Agendor.

- Pipeline visual estilo Kanban com drag-and-drop
- Múltiplos pipelines (vendas, parceria, recrutamento)
- Qualificação automática por scoring (BANT, custom)
- Tags e segmentação
- Atribuição automática ou manual por vendedor
- Histórico unificado por contato (e-mail + WhatsApp + ligação + nota)
- Tarefas e follow-ups com lembrete
- Métricas: taxa de conversão por etapa, tempo médio em cada fase, ticket médio
- Importação em massa (CSV)
- Exportação para Excel/CSV
- Integração nativa com WhatsApp (cada conversa vira card)

### 4.2 Atendimento omnichannel
**Substitui:** Zendesk, Intercom, Octadesk, Take Blip, ManyChat.

- Inbox unificado: WhatsApp + Instagram DM + Facebook + e-mail
- Chatwoot self-hosted ou interface própria
- Macros e respostas rápidas
- Distribuição automática por fila / setor
- Takeover humano com 1 clique (assume conversa da IA)
- Histórico completo na tela ao assumir
- Notas internas (sem ver pelo cliente)
- SLA configurável (tempo máximo de resposta)
- Tags por conversa
- Atribuição por departamento ou agente
- Métricas: tempo médio de resposta, CSAT, conversas por agente

### 4.3 BI / Dashboard executivo
**Substitui:** Metabase, Power BI, Looker, Klipfolio.

- Dashboards por papel (dono, gerente, vendedor, financeiro)
- Métricas em tempo real (atualização ao vivo via Supabase Realtime)
- Comparativos período × período
- Drill-down (clica no número e abre detalhe)
- Filtros dinâmicos (período, vendedor, produto, região)
- Export para Excel/PDF
- Relatórios agendados por e-mail (diário/semanal/mensal)
- Alertas por gatilho (métrica abaixo de X dispara aviso)
- Gráficos customizados (barras, linhas, funil, mapa de calor)
- Indicadores customizáveis pelo dono

### 4.4 Pagamentos
**Substitui (parcialmente):** Asaas, Vindi, Iugu, Stripe Billing.

- **Pix instantâneo** com QR code
- **Cartão** crédito e débito
- **Boleto** bancário
- **Recorrência** (assinatura mensal/anual)
- **Cobrança automática** com retry
- **Split de pagamento** (entre sócios, parceiros, indicadores)
- **Conciliação** automática com banco
- **Régua de cobrança** (lembrete → cobrança → suspensão)
- **Link de pagamento** rápido
- **Checkout transparente** (cliente não sai do app)
- **Antecipação de recebíveis** (via gateway)

> **Integração via:** MercadoPago, Stripe, Pagar.me, Asaas. Não construímos gateway próprio — integramos.

### 4.5 Financeiro leve
**Substitui (parcialmente):** Conta Azul básico, Granatum, Nibo.

- Contas a pagar / contas a receber
- Fluxo de caixa projetado
- Categorização automática
- Conciliação com extrato bancário (Open Finance)
- DRE simplificado
- Alertas de vencimento
- Previsão de receita por recorrência
- Inadimplência por cliente

> **Importante:** não substitui ERP fiscal completo (Omie, Conta Azul completo, Bling). Integra com eles. Cobertura: gestão financeira do dia a dia, não compliance fiscal.

### 4.6 Marketing / E-mail / Automação
**Substitui:** RD Station Marketing, Mailchimp, ActiveCampaign, ManyChat.

- Campanhas com segmentação (tags, comportamento, etapa do funil)
- Templates editáveis (drag-and-drop)
- Automações por gatilho:
  - Boas-vindas pós-cadastro
  - Aniversário do cliente
  - Carrinho abandonado
  - Inatividade (X dias sem comprar/usar)
  - Pós-compra / pós-atendimento
  - Régua de aquecimento (pre-venda)
- Tracking de abertura, clique, conversão
- A/B test de assunto e corpo
- Lista de remarketing exportável pro Meta Ads (sincronia automática)
- WhatsApp marketing (broadcast com cuidado anti-ban)
- Push marketing
- SMS marketing

### 4.7 Gestão de projetos / Tarefas
**Substitui:** Trello, Asana, Monday, ClickUp, Notion projects.

- Quadros tipo Kanban
- Atribuição com prazo
- Comentários e anexos
- Templates de processo
- Subtarefas
- Dependências (X só começa quando Y terminar)
- Time tracking opcional
- Relatório de produtividade
- Visualização lista / calendário / Gantt

### 4.8 Agendamento
**Substitui:** Calendly, Reservio, Tutorbird, Zoonik.

- Calendário público com link
- Bloqueio de horário (intervalo, almoço, folga)
- Confirmação automática
- Lembrete pré-agendamento (24h, 2h)
- Pagamento antecipado opcional
- Multi-profissional (cada um com agenda)
- Multi-serviço (cada serviço tem duração diferente)
- Lista de espera com encaixe automático
- Reagendamento self-service
- Sincronia com Google Calendar / Outlook

### 4.9 Portal do cliente final
**Substitui:** Aplicativo branded de fornecedor terceiro (geralmente caro e genérico).

- App/portal com a marca do cliente
- Acesso individual por usuário/aluno/paciente
- Histórico pessoal (compras, atendimentos, sessões)
- Suporte direto integrado ao WhatsApp
- Notificações personalizadas
- Documentos disponíveis (contratos, NFs, recibos)
- Programa de fidelidade / pontos
- Indicação com bonificação
- Sistema de avaliação (NPS)

### 4.10 Automações no-code interno (substitui Zapier)
**Substitui:** Zapier, Make, n8n, Pipedream.

- Editor visual de fluxos (drag-and-drop)
- Gatilhos (quando X acontece)
- Ações encadeadas
- Condicionais (se X então Y)
- Loops e iterações
- Webhooks de entrada e saída
- Conexão nativa com TODOS os módulos do ecossistema
- Logs de execução
- Histórico de erro com retry

> **Diferencial:** as automações da ForYou Code conhecem **internamente** os módulos do cliente. Zapier conecta APIs externas — o nosso conecta dados do próprio sistema, sem hop intermediário, sem custo por execução.

### 4.11 E-commerce (módulo dedicado — validado no Smartcell)
**Substitui:** Shopify, Tray, Nuvemshop, Loja Integrada.

**Validado em produção (Smartcell, 25/04/2026):**
- Catálogo dinâmico com filtros, sort, comparador, lightbox fullscreen
- Páginas dedicadas por categoria/modelo (ex: /iphone, /iphone-17, /seminovos, /mac)
- Schema de produto + variações (cor, capacidade, condição)
- **Schema dedicado para seminovos** — bateria %, IMEI, checklist 30 itens, foto da unidade real
- **Compartilhamento de imagem por modelo+cor** entre condições (novo/seminovo/usado/lacrado)
- Carrinho persistente em localStorage com merge por ID/cor/storage
- Checkout próprio em 4 etapas (Endereço → Entrega → Pagamento → Confirmação)
- **PIX automático** com Mercado Pago (QR + copia-e-cola + webhook + polling 5s)
- **PIX/Boleto Asaas** alternativo
- Frete por região com regra fixa (alternativa a integração com transportadora)
- Frete grátis automático acima de gatilho (>R$1.000 no Smartcell)
- Bloqueio de venda fora da área de atendimento
- Cupons (% / valor / frete grátis)
- Cupom de boas-vindas (BEMVINDO 5% no Smartcell)
- Welcome popup com cupom no primeiro acesso
- Urgency triggers: estoque baixo, timer 3h, viewers dinâmicos
- Recuperação de carrinho automática
- Notify-me (e-mail quando produto voltar ao estoque)
- Newsletter capture com Zod
- Reviews funcionais (estrelas, distribuição, persistência)
- Comparador de produtos (modal 2-3 produtos, diferenças destacadas)
- Favoritos persistentes (heart, contador)
- Busca global agrupada por categoria (debounce 300ms)
- Related products
- Finalização via WhatsApp `wa.me` com mensagem formatada (alternativa a checkout 100% automatizado, pra quem quer atendimento humano fechar)
- ViaCEP para endereço automático
- Gestão de pedidos com SC-XXXX (rastreio: timeline vertical, valida pedido+CPF)
- PWA com service worker, install banner, offline cache

**Disponível mas ainda não validado em produção:**
- Cartão crédito/débito direto
- Frete via Correios + Melhor Envio + transportadora (validado em outras lojas seria roadmap)
- Wishlist (separado de favoritos)
- Programa de pontos / cashback
- Integração com marketplace (Mercado Livre, Shopee)
- Pixel de Meta + Google + TikTok
- Cupom personalizado por cliente

### 4.12 Comunidade / Hub do usuário
**Substitui:** Circle, Mighty Networks, Discord (parcial).

- Fórum por tópico
- Posts com texto, foto, vídeo
- Comentários e reações
- Mensagem direta entre membros
- Grupos privados / públicos
- Eventos com inscrição
- Lives integradas (YouTube, Vimeo)
- Gamificação (badges, ranking, XP)

### 4.13 Aulas / Conteúdo / EAD (módulo opcional)
**Substitui:** Hotmart membros, Eduzz, Kiwify membros, Memberkit.

- Catálogo de aulas/cursos
- Player de vídeo com controle de progresso
- Materiais de apoio (PDF, exercícios)
- Comentários por aula
- Certificado automático
- Trilhas de aprendizado
- Acesso por tempo limitado ou vitalício
- Liberação progressiva de módulos

### 4.14 Helpdesk / tickets
- Sistema de chamado interno
- Categoria + prioridade + SLA
- Atribuição por equipe
- Histórico do chamado
- Base de conhecimento (FAQ próprio)
- Cliente acompanha status

### 4.15 Formulários
**Substitui:** Typeform, Jotform, Google Forms (com mais poder).

- Editor de formulário drag-and-drop
- Múltiplos tipos de campo
- Lógica condicional (mostra X só se Y respondeu Z)
- Captura de UTM e origem
- Resposta vai direto pro CRM como lead
- Resposta dispara automação
- Embed em qualquer site
- Multi-step (uma pergunta por tela)

### 4.16 Assinatura digital interna
- Geração de contrato com variáveis (nome, valor, prazo)
- Assinatura no próprio app (sem precisar Autentique se simples)
- Trilha de auditoria
- Geolocalização e IP no momento da assinatura
- Para contratos críticos: integração com Autentique

---

## 5. Catálogo de Agentes de IA

> Cada agente é uma IA com função específica + acesso aos dados do cliente. Vende como módulo, customiza por nicho. Toda IA tem painel de controle, histórico de decisões e botão de takeover humano.

### 5.1 Capacidades técnicas (em todo agente)
- **Texto** — conversa natural, contexto longo, mirroring de estilo
- **Visão** — analisa fotos enviadas pelo cliente (Anthropic Vision)
- **Voz** — transcreve áudios (OpenAI Whisper)
- **Catálogo visual** — envia fotos e vídeos nativos no WhatsApp
- **Memória semântica** — lembra do contato (pgvector + RAG)
- **Multi-canal** — mesma IA atende WhatsApp, Instagram, web, e-mail
- **Humanização** — fatiamento em balões, banimento de emojis, mirroring
- **Handoff humano** — qualquer humano que responder pelo WhatsApp desativa a IA automaticamente
- **Logging de objeções** — toda objeção é registrada e categorizada
- **Painel de raciocínio** — dono vê o que a IA pensou antes de responder

### 5.2 Agentes comerciais

| Agente | Função | Quando aciona | Stack |
|---|---|---|---|
| **SDR** | Primeiro contato, qualificação BANT, agenda call | Lead novo entra (anúncio, formulário, indicação) | Claude + WhatsApp + CRM |
| **Vendedor** | Conversa completa de venda, tira objeção, fecha pequeno ticket | Lead qualificado | Claude + catálogo + pagamento |
| **Recuperador de carrinho** | Aborda quem abandonou checkout/conversa | 24h sem resposta + intenção alta | Claude + automação |
| **Reativação** | Cliente inativo há X dias | Trigger por inatividade configurável | Claude + segmentação |
| **Upsell / Cross-sell** | Sugere produto complementar pós-venda | Após fechamento + janela de 7 dias | Claude + histórico de compra |
| **Indicador / Programa de afiliados** | Aborda satisfeitos pra indicar | Pós-NPS positivo | Claude + sistema de pontos |

### 5.3 Agentes de atendimento

| Agente | Função |
|---|---|
| **Suporte nível 1** | Resolve dúvida frequente sem humano (consulta base de conhecimento) |
| **Triagem** | Classifica conversa e roteia pro setor certo (vendas / suporte / financeiro) |
| **Status de pedido** | Consulta entrega, NF, prazo — integrado com transportadora e ERP |
| **Cobrança** | Aborda inadimplente com tom adequado, oferece negociação dentro de regra |
| **NPS / feedback** | Coleta avaliação pós-entrega + segmenta promotores e detratores |
| **Agente de FAQ** | Treina-se com a base de conhecimento do cliente, responde 80% das dúvidas |

### 5.4 Agentes operacionais

| Agente | Função |
|---|---|
| **Onboarding** | Conduz cliente novo pelo primeiro uso do produto/serviço |
| **Retenção** | Detecta sinais de churn (inatividade, queda de uso) e age |
| **Análise de objeções** | Mapeia padrão de "não" e reporta pro dono semanalmente |
| **Resumidor de call** | Transcreve e resume reunião com cliente |
| **Briefing automático** | Prepara contexto antes do humano entrar (lê histórico, pesquisa LinkedIn opcional) |
| **Recrutador de RH** | Triagem inicial de candidato, perguntas pré-entrevista, scoring |
| **Pré-vendas técnico** | Tira dúvida técnica complexa antes de vendedor entrar |

### 5.5 Agentes por nicho (customizações prontas)

#### Educação (escolas, cursos, EAD)
- **Tutor virtual** — explica exercício, tira dúvida sobre matéria
- **Corretor de redação** — corrige por critérios do ENEM/vestibular, sugere melhorias
- **Gerador de simulado adaptativo** — monta prova com base no histórico de erros do aluno
- **Motivador de estudo** — engajamento em horário programado
- **Plantão tira-dúvida 24/7**
- **Mentor de aprovação** — acompanha rotina e ajusta planejamento

#### Saúde (clínicas, consultórios)
- **Triagem de sintoma** — Manchester adaptado, encaminha caso urgente
- **Pré-anamnese** — coleta info antes da consulta
- **Lembrete de exame** — exame X vence em Y dias
- **Orientação pré/pós-procedimento**
- **Confirmação de consulta** com humanização
- **Programa de retorno** — paciente que não volta há X meses

#### Imobiliária
- **Matching de imóvel** — entende critério do comprador, sugere imóveis
- **Agendamento de visita** com corretor disponível
- **Qualificação de comprador** (renda, financiamento, prazo)
- **Documentação digital** — orienta passo a passo

#### Distribuidora B2B
- **Consulta de catálogo** — preço, disponibilidade, prazo
- **Montagem de pedido** pelo WhatsApp
- **Política de preço por cliente** (cada cliente tem sua tabela)
- **Reposição automática** — sugere reposição com base em frequência

#### Construção / Pré-moldados (case Concretize)
- **Orçamento estimado** com base em medidas
- **Status de obra** com foto
- **Comunicação obra ↔ cliente**
- **Vistoria com checklist**

#### E-commerce
- **Vendedor visual** — recomenda produto, manda foto, finaliza venda
- **Suporte pós-venda** — rastreio, troca, devolução
- **Recuperador de carrinho com tom premium**
- **Curadoria de presente** (datas comemorativas)

#### Studios recorrentes (academia, pilates, yoga)
- **Captador de aula experimental** — anúncio até check-in
- **Retenção de mensalista** — detecta queda de frequência
- **Reativador** — aluno cancelou, oferece volta com condição

#### Prestador de serviço B2B
- **Qualificador de proposta** — entende escopo antes de vendedor entrar
- **Acompanhamento de projeto**
- **Faturamento automático**

---

## 6. Capacidades técnicas avançadas (validadas em produção)

> Coisas que o time já implementou e dá pra reusar.

### Engenharia de e-commerce (case Smartcell)
- **PIX automático com polling** — frontend consulta status a cada 5s, atualiza UI quando webhook confirma
- **Edge functions para webhook de pagamento** — Mercado Pago e Asaas com helpers compartilhados
- **Fallback de modelo de IA** — `_shared/ai-fallback.ts` alterna entre Gemini e GPT quando provedor cai
- **Compartilhamento de imagem por modelo+cor** entre condições — economiza 4× cadastro
- **Schema dedicado de seminovos** — bateria %, IMEI, checklist 30 itens
- **Frete por região com regra fixa** — alternativa mais previsível que integração com transportadora pra loja regional
- **Checkout híbrido** — PIX automático no site + finalização via `wa.me` (atendimento humano fecha)
- **Split de sócios no admin** — regra de negócio para clientes em modelo de participação
- **PWA + localStorage agressivo** — favoritos, comparador, carrinho, tema rodam offline sem custo de backend
- **Urgency triggers** sutis baseados em dado real (estoque, timer programado, viewers dinâmicos)
- **FOUC prevention inline** para dark mode
- **Component CRUD reutilizado** entre tipos relacionados (produto vs seminovo)

### Engenharia de IA conversacional (case Concretize)
- **Deduplicação de mensagem por messageId** (Redis) — evita resposta duplicada
- **Rate limit por telefone** (Redis) — protege custo e UX
- **Fila por telefone** — mensagens em ordem
- **Lock por telefone** — IA não responde 2x ao mesmo tempo
- **Cluster de mensagens** (3s no Redis) — agrupa mensagens rápidas em uma resposta
- **Fallback Claude → OpenAI → handoff humano** — resiliência total
- **Mirroring** — IA espelha estilo (formal/informal/com emoji/sem) do contato
- **Fatiamento em balões** — resposta sai em mensagens curtas, não bloco gigante
- **Banimento de emoji** (configurável) — para nichos sérios
- **Catálogo visual** — IA envia foto e vídeo do produto nativamente no WhatsApp
- **Webhook resiliente** — sempre HTTP 200, retry inteligente
- **Multi-instância** — uma infra atende vários clientes white-label

### Engenharia de dados
- **RLS (Row Level Security)** — multi-tenant seguro no Supabase
- **Realtime subscriptions** — painel atualiza ao vivo
- **Edge Functions** — lógica perto do banco, sem servidor dedicado
- **pgvector** — busca semântica, RAG, embedding de conhecimento
- **Backup automático** + restore point-in-time
- **Migrations versionadas** — schema controlado por código

### Engenharia de integração
- **Webhook bidirecional** — recebe e dispara
- **Polling com retry** — quando webhook não é opção
- **Open Finance** (banco PJ) — extrato e conciliação
- **OAuth2** com providers externos
- **Bridge Python** — quando precisa de biblioteca específica

### Performance e escala
- **CDN do Cloudflare** — frontend rápido globalmente
- **Edge Functions na Vercel** — backend perto do usuário
- **Cache em Redis** — consulta frequente sem ir no banco
- **Lazy loading** + code splitting
- **PWA com cache offline**

### Segurança
- **Sanitização de input** em todo formulário
- **Rate limit** em APIs públicas
- **Token rotativo** em integrações
- **Logs sem expor credencial** (lição aprendida no Concretize)
- **Trim em variáveis de ambiente** (Vercel preserva whitespace)
- **Validação no backend** sempre (cliente é manipulável)

---

## 6.5 Matriz Nicho × Módulos × Agentes (resposta rápida pra "o que ofereço pra esse cliente?")

> Tabela de consulta rápida para vendedor/proposta. Quando o lead chegar com nicho X, esta matriz responde direto: módulos core a oferecer + agentes de IA recomendados + features específicas.

| Nicho | Módulos core | Agentes IA recomendados | Features específicas | Pacote típico | Case |
|---|---|---|---|---|---|
| **Educação** (escolas, cursinhos, preparatórios) | CRM, Atendimento, EAD, Portal cliente final, BI | Tutor virtual, Corretor de redação, Mentor de aprovação | Banco de questões, simulado adaptativo, X-Ray do aluno, painel multi-perfil (aluno/professor/diretor) | Ecossistema R$30-60k | Rainha da Aprovação |
| **Saúde** (clínicas, consultórios, estética, odonto) | CRM, Agendamento, Atendimento, Portal | Triagem, Pré-anamnese, Confirmação, Programa de retorno | Prontuário, anamnese customizável, fila com encaixe, LGPD compliance | Ecossistema R$25-50k | — |
| **Studios recorrentes** (academia, pilates, yoga) | Agendamento, Pagamento (recorrência), Portal, Marketing | Captador de aula experimental, Retentor de mensalista, Reativador | Cota mensal, lista de espera, check-in QR, evolução com foto | Ecossistema R$20-40k | — |
| **Imobiliária** | CRM, Atendimento, Portal | SDR, Matching de imóvel, Qualificador, Documentação | Catálogo, tour virtual, funil de visita, comissão por corretor | Ecossistema R$25-45k | — |
| **Distribuidora B2B / Atacado** | CRM, E-commerce, Atendimento, Financeiro | Consulta de catálogo, Montagem de pedido, Reposição automática | Política de preço por cliente, limite de crédito, representante com painel próprio | Ecossistema R$30-50k | — |
| **E-commerce varejo premium** | E-commerce, CRM, Marketing, Atendimento | Vendedor visual, Recuperador de carrinho, Curador de presente | PIX automático, schema seminovos, IA gera descrição/imagem, frete por região | Pacote E-commerce R$20-35k OU participação | Smartcell |
| **Construção / Pré-moldados** | CRM, Atendimento, Gestão de projetos | SDR, Orçamento estimado, Status de obra | Vistoria com checklist, comunicação obra↔cliente, aprovação de etapa | Pacote IA R$3-5k OU Ecossistema | Concretize |
| **Prestador de serviço B2B** | CRM, Projetos, Pagamento, Portal | Qualificador, SDR, Acompanhamento | Proposta gerada, time tracking, faturamento por hora/projeto | Ecossistema R$25-40k | — |
| **Restaurante / Delivery** | CRM, Atendimento, Pagamento, Marketing | Vendedor visual, Suporte pós-pedido | Cardápio QR, integração iFood, cardápio dinâmico (item esgotado) | Ecossistema R$20-35k | — |
| **Beleza / Salões / Estética** | Agendamento, CRM, Pagamento, Portal | Captador, Retentor, Indicação | Pacote de procedimento, antes/depois, comissão por profissional, gift card | Ecossistema R$15-30k | — |
| **Eventos / Casamento** | CRM, Pagamento, Comunidade | Organizador, Confirmação | Lista de convidado RSVP, lista de presente, galeria de foto | Pacote único | — |
| **Coworking / Espaços** | Agendamento, Pagamento, Portal | Receptivo, Cobrança | Reserva de sala, controle de acesso QR, pacote de hora | Pacote modular | — |

### Como usar
1. **Lead chega:** identificar nicho na primeira conversa
2. **Bater na matriz:** módulos core + agentes recomendados
3. **Customizar com features específicas** do nicho
4. **Sugerir pacote** mais próximo
5. **Mostrar case** mais alinhado (ou explicar que será o primeiro daquele nicho)

### Quando o nicho não está na matriz
Se o lead é de nicho não listado, voltar ao princípio: **commodity regulada = integramos. Operação = construímos.** Identificar 3-5 módulos core do que o cliente faz, agentes que façam sentido, e propor escopo customizado.

---

## 7. Features por nicho do ICP

### 7.1 Educação (Perfil A — caso Rainha da Aprovação validado)

**Painel do aluno:**
- Banco de questões (filtro por matéria, ano, dificuldade)
- Simulado adaptativo (questões com base no histórico)
- Caderno de erros automático (revisão dirigida)
- Flashcards com repetição espaçada (Anki-like)
- Planner de estudo com meta diária/semanal
- Correção de redação por IA (critérios ENEM/vestibular)
- Player de aula com progresso
- Material de apoio (PDF, audiobook)
- Comunicação direta com professor
- Gamificação (XP, ranking, conquistas)

**Painel do professor:**
- Painel de turma com lista de alunos
- Análise individual por aluno (X-Ray)
- Correção em massa de redação
- Banco de questões compartilhado
- Distribuição de tarefas
- Comunicação aluno ↔ professor
- Material em vídeo (upload e organização)

**Painel da diretora / dono da escola:**
- Dashboard executivo (matrícula, retenção, frequência)
- Análise de retenção por turma
- Gestão de contratos
- Financeiro (mensalidade, inadimplência)
- X-Ray do aluno completo (acadêmico + comportamental + financeiro)
- Comunicação em massa
- Gestão de professor

**Roadmap educacional:**
- Plano de aula gerado por IA
- Análise preditiva de aprovação
- Recomendação de conteúdo individualizada
- Comunidade de aluno

### 7.2 Saúde (clínicas, consultórios, estética, odonto)

- Agenda multi-profissional
- Prontuário eletrônico (estruturado por especialidade)
- Prescrição digital (via Memed integrado, opcional)
- Anamnese customizável por especialidade
- Fila de espera com encaixe automático
- Lembrete pré-consulta (humanizado)
- Confirmação automática
- Pós-consulta com orientação
- Programa de retorno
- Indicação com bonificação
- Pacote / plano de tratamento
- Histórico clínico do paciente (foto, evolução)
- Ficha técnica de procedimento
- Termo de consentimento digital
- LGPD compliance (paciente é dado sensível)

### 7.3 Studios recorrentes (academia, pilates, yoga, crossfit)

- Agendamento de aula com cota mensal
- Lista de espera por aula
- Check-in por QR Code
- Avaliação de evolução (medidas, fotos, peso)
- Plano alimentar / treino integrado
- Comunidade interna do aluno
- Mensalidade automática
- Comprovante de presença pra plano de saúde
- Integração com wearable (opcional)
- Aula online ao vivo (Zoom/Meet integrado)

### 7.4 Imobiliárias

- Catálogo de imóveis com fotos e vídeos
- Tour virtual (link 360°)
- Matching automático lead ↔ imóvel
- Agendamento de visita com corretor
- Funil de visita (interesse → visita → proposta → fechamento)
- Documentação digital (RG, CPF, comprovante de renda)
- Análise de crédito (parceria com bureaus)
- Gestão de proposta com contraproposta
- Comissão por corretor calculada automática
- Rede de parceiros (corretor de fora pode ver catálogo)
- Sincronia com portais (Zap, Viva Real — opcional)

### 7.5 Distribuidoras / Atacado B2B

- Catálogo com política de preço por cliente (cada cliente tem tabela)
- Pedido pelo WhatsApp
- Pedido pelo app/portal do cliente
- Limite de crédito por cliente
- Bloqueio automático por inadimplência
- Fechamento de pedido em massa
- Rota de entrega otimizada
- Gestão de devolução / troca
- Representante comercial com painel próprio (vê só os clientes dele)
- Integração com ERP (Bling, Omie, Tiny)
- Histórico de compra por cliente (sugestão de reposição)

### 7.6 E-commerce premium (case Smartcell validado)

**Entregue em 25/04/2026 — em produção em smartcellsite.com.br**

- Vitrine branded com SEO + JSON-LD + lazy loading + alt text
- Hero customizável (vídeo background, parallax, gradient title)
- Catálogo multi-categoria (iPhone, Mac, iPad, Watch, AirPods, Xiaomi, acessórios)
- Páginas dedicadas por modelo (/iphone-17, /seminovos, /mac, etc)
- Schema dedicado para seminovos (bateria %, IMEI, checklist 30 itens)
- Compartilhamento de imagem por modelo+cor entre condições
- Carrinho persistente em localStorage com merge inteligente
- Frete por região (regra fixa, sem transportadora) com bloqueio fora da área
- Frete grátis automático acima de gatilho
- PIX automático com Mercado Pago + Asaas (polling de status no front)
- Checkout em 4 etapas com ViaCEP
- Finalização via WhatsApp `wa.me` (atendimento humano fecha após PIX confirmado)
- Pedidos SC-XXXX, rastreio com timeline e validação
- Cupons + welcome popup com cupom de primeira compra
- Urgency triggers (estoque, timer, viewers)
- Recuperação de carrinho
- Notify-me para reposição
- Reviews, comparador, favoritos, busca global
- IA gerando descrição de produto (Lovable AI Gateway: Gemini/GPT)
- IA gerando imagens de produto por cor (Gemini Image)
- PWA com service worker, install banner
- LGPD compliance (cookie consent, privacidade, cookies, termos)
- Painel admin com 13 módulos (Dashboard, Produtos, Seminovos, Pedidos, CRM, Financeiro, Categorias, Banners, Galeria, Avaliações, Usuários, Notificações, Jobs IA, Configurações)
- **Split de sócios no admin financeiro** (regra de negócio quando o modelo é participação nos lucros)
- WhatsApp templates com variáveis dinâmicas para pós-venda

**Roadmap natural a partir do Smartcell:**
- Integração com transportadora real (Correios, Melhor Envio)
- Programa de pontos / fidelidade
- Chatbot vendedor IA conversacional (a IA atual gera produto, não conversa)
- E-mail transacional próprio
- GA / Pixel configurados

### 7.7 Construtoras / Pré-moldados (caso Concretize expandido)

- Orçamento online com calculadora
- Catálogo de produto com aplicação técnica
- Gestão de obra (cronograma, etapas)
- Vistoria com foto e checklist
- Comunicação obra ↔ cliente
- Aprovação de etapa (cliente assina digital)
- Pagamento por marco
- Gestão de equipe (quem está em qual obra)
- Compra de material com fornecedor
- Memorial descritivo digital

### 7.8 Prestador de serviço B2B

- Proposta gerada por IA com base em briefing
- Contrato + assinatura no fluxo
- Time tracking (hora trabalhada por cliente)
- Faturamento por hora ou projeto
- Painel do cliente acompanhar entrega
- Aprovação de etapa
- NPS pós-projeto
- Repositório de entregas (cliente acessa depois)

### 7.9 Restaurante / Delivery

- Cardápio digital com QR
- Pedido pelo WhatsApp (com IA)
- Pedido pelo app branded
- Integração com iFood (opcional)
- Gestão de mesa (presencial)
- Comanda digital
- Programa de fidelidade
- Cardápio dinâmico (item esgotado some automaticamente)
- Pesquisa de satisfação pós-refeição

### 7.10 Beleza / Estética / Salões

- Agenda multi-profissional
- Pacote de procedimento
- Histórico de cliente com foto antes/depois
- Programa de fidelidade
- Comissão por profissional
- Estoque de produto
- Indicação com bonificação
- Cartão presente (gift card)

### 7.11 Eventos / Casamento / Festas

- Lista de convidado com confirmação
- Lista de presente
- Galeria de foto
- Cronograma do evento
- Pagamento de fornecedor
- Convite digital com RSVP

### 7.12 Coworking / Espaços compartilhados

- Reserva de sala
- Controle de acesso (QR)
- Gestão de assinatura
- Comunicação entre membros
- Pacote de hora avulsa

---

## 8. Integrações (commodity — não construímos, conectamos)

> **Princípio:** o que é regulado, fiscal, legado ou commodity de mercado nunca substituímos. Integramos via API e orquestramos.

### 8.1 ERP / Fiscal (sempre integração)
| Sistema | O que integramos |
|---|---|
| **Omie** | Cliente, produto, NF, contas a pagar/receber |
| **Conta Azul** | Mesmo escopo |
| **Bling** | Mesmo escopo + e-commerce |
| **Tiny ERP** | Mesmo escopo, foco e-commerce |
| **Sankhya** | Médio porte, integração via API ou banco |
| **Totvs** | Grande porte, integração via REST/SOAP |
| **NF-e direto SEFAZ** | Quando cliente já tem certificado e quer emitir do nosso painel |

### 8.2 Banco PJ / Financeiro
- Itaú, Banco do Brasil, Inter, Bradesco, Santander
- Stark Bank (API-first)
- Cora, Conta Simples (digitais PJ)
- Open Finance (consulta extrato unificada)
- Conciliação automática

### 8.3 Pagamento (gateway)
- **Mercado Pago** — PIX dinâmico com QR + copia-e-cola + webhook + polling de status (validado em Smartcell)
- **Asaas** — PIX/Boleto + webhook (validado em Smartcell)
- Stripe
- Pagar.me (Stone)
- PagSeguro
- Iugu
- Vindi (recorrência específica)
- Pix direto via instituição

### 8.4 Logística / Transportadora
- Correios (etiqueta, rastreio)
- Melhor Envio (multi-transportadora)
- Loggi
- Jadlog
- Total Express
- Transportadora privada (via API custom)

### 8.5 Comunicação
- **WhatsApp:** MegaAPI, Evolution API, WhatsApp Cloud API (Meta oficial)
- **Instagram / Facebook:** Graph API
- **E-mail:** Resend, SendGrid, Mailgun, AWS SES
- **SMS:** Twilio, Zenvia, TotalVoice
- **Chat:** Chatwoot self-hosted

### 8.6 Marketing
- Meta Ads (Conversions API)
- Google Ads (Conversions API)
- TikTok Ads
- Pixel + GTM
- UTM tracking nativo

### 8.7 Workspace / Produtividade
- Google Workspace (Drive, Calendar, Sheets, Docs)
- Microsoft 365
- Zoom (link automático em call)
- Google Meet
- Loom (gravação)

### 8.8 Contrato / Assinatura
- Autentique (padrão)
- DocuSign (cliente exigente)
- D4Sign

### 8.9 Infoproduto / Curso (parceria, não concorrência)
- Hotmart (webhook de venda → CRM)
- Eduzz
- Kiwify
- Monetizze

### 8.10 Recurso humano / Folha
- Sólides (gestão de pessoas)
- Pontomais (ponto eletrônico)
- Folha de pagamento do contador (consulta)

### 8.11 Bureau / Crédito
- Serasa Experian (consulta CPF/CNPJ)
- Boa Vista
- Receita Federal (consulta CNPJ)
- Cep + endereço (ViaCEP)

### 8.12 IA / Modelo
- Anthropic Claude (principal)
- OpenAI GPT (fallback)
- OpenAI Whisper (áudio)
- Voyage / OpenAI Embeddings
- Replicate (modelo aberto)
- Gemini (Google) — quando faz sentido

---

## 9. Automatismos prontos (orquestração entre sistemas)

> **A integração é o produto.** Cada item abaixo é uma tarefa manual que **deixa de existir** depois que conectamos.

### 9.1 Marketing → Vendas
- Meta/Google Ads → CRM (lead entra etiquetado com campanha + custo)
- Lista de remarketing automática (cliente sai, abandono entra)
- Instagram DM → Inbox unificado
- Comentário em anúncio → IA aborda no DM
- Form do site → CRM + automação de boas-vindas

### 9.2 Comunicação → Registro
- WhatsApp → CRM (cada conversa vira card)
- Instagram DM → CRM
- E-mail recebido → ticket / lead com classificação
- Chamada telefônica (via Voip) → log no CRM

### 9.3 Agenda → Operação
- Google Calendar / Outlook ↔ Sistema (bidirecional)
- Zoom / Meet → link automático + gravação no CRM
- Lembrete automático (24h, 2h, 30 min antes)
- No-show detectado → automação de reativação

### 9.4 Venda → Pós-venda
- Autentique → Onboarding (contrato assinado dispara fluxo)
- Pagamento confirmado → Liberação + NF + boas-vindas
- Hotmart/Eduzz → CRM + segmentação automática
- Compra → Programa de pontos atualizado

### 9.5 Operação → Financeiro
- Pedido fechado → ERP (NF emitida automática)
- Pagamento recebido → Conciliação automática
- Inadimplência → Régua de cobrança
- Vencimento próximo → Lembrete personalizado

### 9.6 Dados → Decisão
- Métricas em tempo real no painel do dono
- Alerta proativo (CAC subiu, conversão caiu)
- Relatório semanal por e-mail
- IA detecta padrão e reporta

### 9.7 Atendimento → Inteligência
- Conversa → Análise de sentimento + objeção registrada
- Reclamação → Ticket + alerta + follow-up
- NPS detrator → Trigger de retenção
- Pergunta frequente → FAQ atualizado

### 9.8 Por que isso importa no posicionamento

**Integração sozinha é commodity** — qualquer um faz. **Integração que vira automatismo entre sistemas é o produto.**

A camada que vocês não constroem (ERP, NF-e, folha) é justamente a que ninguém quer construir: commodity regulada, quem entrega isso é Omie/Conta Azul/Bling com 20 anos de compliance. A narrativa muda de **"substituímos tudo"** para **"orquestramos tudo"**:

1. **Consolidação operacional** — CRM, atendimento, BI, automações, e-mail, projetos viram **um lugar só com a marca do cliente**
2. **Dados conectados** — o ERP continua sendo Omie, mas a API do Omie alimenta o painel ForYou Code, que cruza com WhatsApp, com lead, com financeiro. **A integração é o produto.**
3. **Camada de inteligência em cima** — IA só funciona com dados unificados. Quem tem 12 SaaS soltos não consegue ter IA decente. Vocês entregam o substrato.
4. **Ativo vs aluguel** — sistema no domínio do cliente, banco do cliente. Mesmo o que continua sendo SaaS de terceiro fica orquestrado pelo painel deles.

---

## 10. O que NÃO entregamos (delimitação contratual)

> **Importante explicitar pra evitar escopo infinito e proteger a relação.**

### Nunca construímos (commodity regulada)
- ERP fiscal completo (compliance brasileiro tem 20+ anos de lei — integramos)
- Folha de pagamento (mesma razão)
- Sistema contábil (mesmo)
- Emissão direta de NF-e (integramos com emissor)
- eSocial / SPED / DCTF (commodity fiscal)

### Não fazemos hoje (fora de escopo padrão)
- App mobile nativo iOS/Android (entregamos PWA — nativo é roadmap)
- Marketplace público multi-vendor com regulação (B2C agregador) — caso a caso
- Hardware / IoT (a não ser integração via API existente)
- Suporte 24/7 com plantão humano (oferecemos SLA, não plantão)
- Tradução para múltiplos idiomas (cobramos como customização)
- Adequação a normas internacionais (HIPAA US, GDPR fora do BR) — caso a caso

### Não somos
- Agência de marketing (atendemos se chegar, não prospectamos)
- Consultoria de processo (entregamos sistema, não auditoria)
- Suporte técnico de hardware
- Provedor de internet / hospedagem genérica (usamos Vercel/Cloudflare/Supabase)

---

## 11. Pacotes / Níveis de entrega

### Pacote IA de Atendimento — R$3.000–R$5.000 + manutenção

**Inclui:**
- Núcleo de aplicação (painel branded)
- Módulo CRM básico
- Módulo Atendimento omnichannel
- Agente de IA (1 customizado por nicho)
- Capacidades avançadas (visão, voz, mirroring)
- Painel de takeover humano
- Dashboard de leads e objeções
- Integração WhatsApp (MegaAPI ou Cloud API)
- Integração com Meta Ads (lead etiquetado)
- 3 meses de manutenção Essencial inclusos

**Tempo de entrega:** 2 a 3 semanas

**Case de referência:** Concretize / Rodrigo

### Pacote Ecossistema Completo — R$30.000–R$60.000 + manutenção

**Inclui:**
- Tudo do pacote IA de Atendimento
- App branded (web + PWA) com a marca do cliente
- 4 a 8 módulos operacionais (cliente escolhe na proposta)
- Portal do cliente final
- BI / Dashboard executivo
- Automações no-code interno
- Integração com ERP do cliente
- Bibliotecas de nicho aplicáveis
- Até 3 agentes de IA customizados
- 3 meses de manutenção Essencial inclusos

**Tempo de entrega:** 6 a 12 semanas (depende do escopo)

**Case de referência:** Rainha da Aprovação (educação)

### Pacote E-commerce Premium — R$20k-R$35k + manutenção OU participação nos lucros

**Inclui:**
- Núcleo + módulo E-commerce dedicado
- Catálogo dinâmico com filtros, comparador, busca global, favoritos
- Checkout próprio em 4 etapas com PIX automático (Mercado Pago + Asaas)
- Schema dedicado para seminovos (se aplicável)
- Recuperação de carrinho + welcome popup com cupom + urgency triggers
- IA gerando descrição e imagem de produto (Gemini + GPT com fallback)
- Painel admin completo (Dashboard, Produtos, Seminovos, Pedidos, CRM, Financeiro com KPIs e split de sócios, Banners, Galeria, Avaliações, Usuários, Notificações, Jobs IA)
- LGPD compliance + PWA
- ViaCEP + frete por região OU integração com transportadora
- Finalização via WhatsApp `wa.me` (alternativa a checkout 100% automatizado)
- 3 meses de manutenção Essencial inclusos

**Modelos comerciais possíveis:**
1. **Projeto fechado** R$20k-R$35k + manutenção (recomendado para quem ainda não tem volume)
2. **Participação nos lucros** % das vendas, sem fee de projeto (validado no Smartcell — 20%, sem mais cobrança, manutenção e evolução incluídas)

**Tempo de entrega:** 8-12 semanas

**Case de referência (validado em produção):** Smartcell Premium Store — entregue 25/04/2026, em produção em smartcellsite.com.br. Case público autorizado (nome, marca, número 553438212212).

### Pacote Customizado — orçamento sob escopo

Cliente que precisa de combinação específica fora dos pacotes acima. Mesma stack, mesmas capacidades, escopo dedicado.

---

## 12. Tickets e modelos de cobrança

| Modelo | Quando usa |
|---|---|
| **Projeto fechado** | Padrão — valor único pelo escopo |
| **Mensalidade de manutenção** | Sempre — 3 tiers (R$97 / R$197 / R$397) |
| **Marketing mensal** | Quando cliente quer Meta Ads gerenciado (R$1.000–R$1.500/mês) |
| **Participação nos lucros** | Cliente estratégico, escala alta — % das vendas (ex: Smartcell 20%) |
| **Sócio em equity** | Casos raríssimos, com forte alinhamento estratégico |

### Formas de pagamento
- Pix à vista (5% off)
- Cartão 3x sem juros
- Pix parcelado com contrato (1ª parcela ≥ demais — regra inegociável)
- Boleto parcelado em casos específicos

### Faturamento mínimo do cliente para fazer sentido
- IA de Atendimento: R$50k+/mês
- Ecossistema: R$100k+/mês
- E-commerce: depende da margem do nicho

---

## 13. Manutenção pós-entrega

### Tier Hospedagem — R$97/mês
- Hosting (Vercel + Cloudflare + Supabase)
- Backup automático
- Sem suporte ativo, sem alteração

### Tier Essencial — R$197/mês (recomendado)
- Tudo do Hospedagem
- Correção de bug
- Suporte por WhatsApp em horário comercial
- Atualização de dependências

### Tier Crescimento — R$397/mês
- Tudo do Essencial
- Melhorias mensais (até X horas)
- Relatório mensal
- Novos pequenos features

### Custo de infra que cliente paga (independente do tier)
- Supabase Pro: ~R$120/mês (até crescer)
- Vercel Pro: ~R$100/mês (geralmente Hobby resolve no início)
- MegaAPI: R$100–R$300/mês (depende do volume)
- Domínio: R$60/ano

> **Regra:** primeiros 3 meses de Essencial **inclusos** no projeto. Renovação a partir do 4º mês.

---

## 13.5 Fórmulas de ROI (para usar em proposta e site)

> Custo vs custo perde a venda. **Custo vs retorno** ganha. Toda proposta usa pelo menos uma fórmula abaixo.

### Fórmula 1 — Receita escapando (qualquer cliente com WhatsApp)

```
Leads/mês × Ticket médio × % perdido por demora/desorganização = R$/mês escapando
```

**Exemplo (anchor padrão para o site):**
- 50 leads/mês × R$1.500 ticket × 20% perdido = **R$15.000/mês escapando**
- × 12 = **R$180.000/ano**

**Aplicação:**
- 20% é estimativa conservadora (estudo: resposta em segundos converte 21x mais que em horas)
- Cliente que tem ticket maior ou volume maior → número explode rapidamente
- O número de receita escapando costuma ser MAIOR que a economia de SaaS

### Fórmula 2 — IA de Atendimento (break-even em meses)

```
Implementação: R$4k
Ganho mensal: 2-3 vendas recuperadas × ticket médio
Break-even: implementação ÷ ganho mensal
```

**Exemplo:** ticket R$500, 2 vendas/mês recuperadas = R$1.000/mês → break-even em **4 meses**. A partir do 5º mês, ganho líquido puro.

### Fórmula 3 — Ecossistema para negócio recorrente

```
Receita preservada = base de cliente recorrente × redução de churn × ticket mensal
```

**Exemplo (escola 200 alunos R$800/mês):**
- Receita recorrente: R$160.000/mês
- Churn estimado (10%/ano): 20 alunos perdidos = R$192k/ano em risco
- Plataforma reduz 30% do churn = 6 alunos retidos
- Receita preservada: R$4.800/mês = **R$57.600/ano**
- Investimento R$30k → break-even em **~6 meses**

### Fórmula 4 — Substituição de SaaS (bônus, não tese)

```
SaaS substituível atual − manutenção ForYou Code = economia mensal real
```

**Exemplo:**
- Hoje paga: ManyChat R$200 + CRM R$200 + Automação R$100 + E-mail mkt R$200 = **R$700/mês**
- Manutenção ForYou Code Essencial: R$197/mês
- Economia: **R$500/mês = R$6.000/ano** (bônus, sem contar receita recuperada)

### Pitch unificado

> "Você paga R$700 em ferramentas que não são suas, não têm sua marca, não falam entre si. A gente substitui essa camada por R$197 de manutenção. Mas a conta que importa é outra: você está deixando R$15k/mês escapar por causa do caos. O projeto se paga em 6 meses. Depois disso, você ganha o resto da vida."

---

## 13.6 Frases-pitch prontas (para site, anúncio, proposta)

> Catálogo de copy testada. Reusar literalmente quando fizer sentido.

### Headlines fortes

- "Você não tem um problema de custo. Tem um problema de controle."
- "Quantos sistemas estão controlando seu negócio em vez de você?"
- "E quanto da sua semana virou cola entre sistemas que não conversam?"
- "E quanto você está deixando na mesa enquanto tudo isso está fragmentado?"
- "O ecossistema não para no que a gente constrói. Continua trabalhando enquanto você dorme — entre seus sistemas atuais e os novos."

### Sub-headlines / sub-copy

- "Mais que economia — é deixar de orquestrar 12 ferramentas pra orquestrar uma."
- "Não é falta de produtividade — é falta de integração."
- "Lead que some, atendimento que demora, vendedor que esquece de registrar. O caos custa receita, não só mensalidade."
- "Conectamos o que você já paga (ERP, banco, Meta Ads) com o que a gente entrega (CRM, atendimento, BI). Cada um para de ser uma ilha — vira parte de um fluxo único, automático, com a sua marca."

### CTAs

- "Quero ver como funciona pro meu negócio"
- "Toda integração vira automação. Você para de operar entre ferramentas e começa a operar uma só."
- "Preenche um formulário rápido e em 48h a gente te manda o escopo do seu app — de graça."

### Pitches de produto

**IA de Atendimento (abertura natural):**
> "A gente pegou um cliente que tinha 40, 50 mensagens por dia no WhatsApp e não conseguia responder tudo a tempo. Ele perdia venda por demora. A gente construiu uma IA que responde, qualifica e manda pro funil certo — mas o diferencial real não é a IA em si. É o painel: o dono abre e vê cada lead pelo nome, as objeções que a pessoa levantou, o que a IA respondeu e o raciocínio por trás. Se quiser entrar na conversa, clica e assume com o histórico completo na tela. E no final do mês, todos os dados de atendimento alimentam o marketing — sabe quais objeções aparecem mais, qual perfil fecha mais, qual horário converte melhor. Não é bot. É inteligência de vendas."

**Ecossistema (dor de dependência):**
> "A maioria das empresas hoje é refém das ferramentas que usa. Paga CRM pra um, pagamento pra outro, app de cliente pra um terceiro — cada um com sua mensalidade, seus termos de uso que mudam, e nenhum com a cara do negócio. A gente faz diferente: constrói o ecossistema inteiro dentro do domínio do cliente, com o banco de dados dele, com a marca dele. App para os clientes finais, painel de gestão, CRM, automações de WhatsApp, sistema de pagamentos integrado — tudo num lugar só. Quando a gente entrega, o sistema é do cliente. Não tem mensalidade pra nós, não tem risco de suspensão, não tem ninguém aumentando preço. Ele tem um ativo, não um aluguel."

**Diferencial do processo (antes de falar preço):**
> "A gente não manda proposta em PDF e espera você imaginar como vai ficar. Antes de qualquer número, a gente constrói o protótipo do seu app — com a sua marca, no seu domínio — e te mostra funcionando. Você navega, vê os fluxos, pede ajuste. Só depois disso a gente fala de valor. Porque a gente não quer que você compre no escuro."

**Para "já tenho ferramenta":**
> "Entendo. Mas me faz uma pergunta: essa ferramenta te mostra as objeções que cada lead levantou? O raciocínio que o bot usou pra responder? Você consegue entrar na conversa e assumir com o histórico completo na tela? Se não — não é a mesma coisa. O que a gente entrega é controle, não só automação."

**Cold opener (DM / prospecção):**
> "Vi aqui que vocês têm um volume bom de leads chegando. A gente trabalha com um nicho específico: donos de negócio que não conseguem mais dar conta do atendimento manualmente, ou que precisam de um app com a marca deles no mercado. Não é revenda de ferramenta — a gente constrói. Faz sentido eu te mandar como funcionou pra outro cliente do seu setor?"

**Argumento de preço para IA:**
> "Você paga isso uma vez. Atendente de WhatsApp custa R$1.500-R$2.500/mês pra sempre — e sai de férias e esquece contexto. Em 2 meses você já pagou o equivalente."

**Para objeção de manutenção parecida com SaaS:**
> "Você paga R$X em ferramentas que não tem sua marca, que você não controla, e que podem mudar de preço amanhã. Mas a conta mais importante não é essa. É a seguinte: você tem 200 clientes pagando R$800/mês. Se você perde 10% por ano — 20 alunos — isso é R$192k de receita que some todo ano. A plataforma existe pra você parar de perder isso. Se ela retiver só 6 alunos a mais por ano, o projeto se paga em 6 meses. O resto é ativo. Você não está comprando software — está comprando a capacidade de reter o que já conquistou."

---

## 13.7 Estrutura recomendada da ChaosSection do site (foryoucodee.com.br)

> Documentação da seção do site que comunica as dores. Aqui pra qualquer mudança futura partir desta versão.

### Bloco 1 — Calculadora de SaaS (reenquadrada)

**Headline:** "Quantos sistemas estão controlando seu negócio em vez de você?"
**Sub:** "Marque o que sua empresa usa hoje. No final, você vai ver onde mora o caos — e o que dá pra consolidar."

**Tag por item:**
- **INTEGRAMOS** (cinza, plug): ERP, NF-e, folha, workspace, contabilidade, banco PJ, gateway de pagamento
- **SUBSTITUÍMOS** (verde, check): CRM, BI, atendimento, chatbot, e-mail mkt, Zapier, projetos, agendamento, helpdesk, formulários, financeiro leve, portal de cliente

**Painel sticky com 3 linhas:**
```
Você gasta hoje:                R$ X.XXX/mês
└─ Continua existindo:          R$ X.XXX/mês
└─ Substituído pela ForYou Code: R$ X.XXX/mês  (em destaque verde)
```

**Microcopy:** "Mais que economia — é deixar de orquestrar 12 ferramentas pra orquestrar uma."

### Bloco 2 — Calculadora de tempo (reenquadrada)

**Headline:** "E quanto da sua semana virou cola entre sistemas que não conversam?"
**Sub:** "Cada hora aqui não é hora de venda, gestão ou estratégia. É hora copiando dado de um lugar pro outro."
**Microcopy embaixo do output:** "Esse é o tempo que some operando fragmentado. Não é falta de produtividade — é falta de integração."

### Bloco 3 — Calculadora de receita escapando (NOVO — destaque maior)

**Headline:** "E quanto você está deixando na mesa enquanto tudo isso está fragmentado?"
**Sub:** "Lead que some, atendimento que demora, vendedor que esquece de registrar. O caos custa receita, não só mensalidade."

**3 inputs:**
1. Leads/mês (10–500, default 50)
2. Ticket médio R$ (100–50.000, default 1.500)
3. % perdido por demora/desorganização (5–40%, default 20%)

**Output:**
```
Receita escapando por mês:    R$ XX.XXX
Por ano:                      R$ XXX.XXX
```

**Microcopy verde:** "É isso que a integração + IA recupera. Não é economia de mensalidade — é venda que voltava a acontecer."

### Bloco 4 — Cards qualitativos (caos invisível)

Mantém como está.

### Bloco 5 — CTA de fechamento

**Headline:** "Você não tem um problema de custo. Tem um problema de controle."
**Sub:** "A gente conserta o controle. O custo cai como consequência. E a receita que estava escapando volta a entrar."
**Botão:** "Quero ver como funciona pro meu negócio" → formulário pré-briefing

---

## 14. Tempo de entrega (referência por tipo)

| Tipo | Tempo | Nota |
|---|---|---|
| IA de Atendimento simples (1 nicho) | 2–3 semanas | Validado: Concretize em ~3 semanas |
| Ecossistema básico (3–4 módulos) | 6–8 semanas | |
| Ecossistema complexo (educação tipo Dayane) | 8–12 semanas | Validado: Rainha da Aprovação |
| E-commerce premium | 8–12 semanas | |
| Customização forte (multi-perfil B2B com complexidade) | 12+ semanas | Caso a caso |

**Acelera se:** cliente entrega ativos rápido (logo, identidade), tem clareza de escopo, decide rápido.

**Atrasa se:** cliente muda escopo no meio (cobrar adendo), demora para validar entrega, requer integração com sistema legado mal documentado.

---

## 15. Glossário para o site (termos que importam)

| Termo | Definição curta para usar em copy |
|---|---|
| **Ecossistema digital** | App + painel + módulos + IA + integrações, tudo conectado, com sua marca |
| **White-label** | Sistema com a marca do cliente, no domínio dele, na infra dele |
| **Módulo** | Funcionalidade independente que o cliente escolhe (CRM, atendimento, BI...) |
| **Agente de IA** | IA com função específica e acesso aos dados, não chatbot genérico |
| **Painel de takeover** | Tela que mostra raciocínio da IA + botão pra humano assumir |
| **Automação interna** | Substituto do Zapier dentro do próprio sistema, sem custo por execução |
| **Integração** | Conexão com sistema do cliente (ERP, banco) que continua existindo |
| **Capacidade** | O que a IA consegue fazer (texto, visão, voz, mirroring) |
| **Onboarding** | Processo que conduz cliente novo pelo primeiro uso |
| **Núcleo** | O que toda entrega inclui sem opção (app + painel + auth + deploy) |

---

## 16. Como usar este catálogo

### No site (foryoucodee.com.br)
- Página "O que entregamos" — matriz de Módulos × Nicho
- Página por nicho (educação, saúde, e-commerce...) — features específicas + agente de IA + case
- Bloco "monte seu ecossistema" — checkbox dos módulos
- Bloco "agentes de IA" — catálogo visual
- ChaosSection — separar SaaS em "integramos" vs "substituímos"

### Na proposta para cliente
- Listar só módulos relevantes ao nicho dele
- Marcar features escolhidas com base no formulário/call
- Anexar 1 case do nicho mais próximo
- Indicar qual pacote (IA / Ecossistema / E-commerce) e ajustar valor

### No prompt do Claude (formulário pré-briefing)
- Carregar este catálogo como contexto
- Cruzar respostas do formulário com módulos disponíveis
- Gerar escopo personalizado em 48h

### Atualização
- **Toda entrega validada em produção** vira linha aqui
- **Toda dúvida recorrente de cliente** ("vocês fazem X?") vira linha
- **Toda decisão de "não fazemos isso"** vira linha na seção 10

---

## 17. Links relacionados

- [[ICP da ForYou Code|ICP]]
- [[Plano Comercial ForYou Code 2026|Plano Comercial 2026]]
- [[Como precificar projetos na ForYou Code|Precificação]]
- [[Processo de vendas da ForYou Code|Processo de vendas]]
- [[Processo de entrega de projetos na ForYou Code|Processo de entrega]]
- [[Onboarding de cliente novo na ForYou Code|Onboarding]]
- [[Guia de Clonagem IA de Atendimento|Manual de clonagem v3.1]]
- [[ForYou Code constroi o ecossistema digital que o cliente precisar dentro do proprio app dele|O que entregamos (resumo)]]
- [[ForYou Life - SaaS Gratuito ForYou Code|ForYou Life (lead magnet)]]
- [[atlas/Decisoes de stack da ForYou Code|Decisões de stack]]
