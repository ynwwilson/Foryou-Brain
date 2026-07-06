---
date: 2026-06-10 17h43
tool: codex
title: "sabe a kommo CRM"
model: openai
tags: [codex, sessão]
---

# sabe a kommo CRM

> **Ferramenta:** Codex · **Início:** 2026-06-10 17h43 · **Último save:** 2026-06-10 18:13:08
> **Dir:** `C:\Users\ynwwi`

## Objetivo
sabe a kommo CRM?

## Conversa

**Mestre:** sabe a kommo CRM?
> 17:43

**Codex:** Vou carregar o mínimo de contexto global exigido e já respondo direto.

---

**Mestre:** O QUE ELES FAZ EM RELAÇÃO AO WHATSAPP, TUDO QUE FAZEM
> 17:45

**Codex:** Vou usar uma checagem rápida em fontes oficiais da Kommo, porque recursos de WhatsApp em CRM mudam com frequência e vale evitar chute.

---

**Mestre:** E COMO ELES CONECTAM AO WHATSAPP DO CLIENTE DELES?
> 17:47

**Codex:** Vou confirmar no guia oficial de setup da Kommo, porque aqui os detalhes importam: número novo, número já em uso, WABA/Facebook Business e coexistência mudam o caminho.

---

**Mestre:** ENTÃO A PESSOA NÃO PODE USAR A KOMMO E O WHATSAPP AO MESMO TEMPO CERTO?
> 17:48

**Codex:** Não exatamente. **Hoje pode sim usar Kommo e WhatsApp ao mesmo tempo**, mas depende do tipo de WhatsApp. **Se for WhatsApp Business App:**   Pode usar os dois juntos com o recurso chamado **WhatsApp Coexistence**. A pessoa continua respondendo pelo app no celular e também usa a Kommo para CRM, automação e atendimento. As conversas 1:1 sincronizam entre os dois. **Se for WhatsApp pessoal/normal:**   Aí não é o caminho certo. Para API oficial/Kommo, o número precisa virar WhatsApp Business/Cloud API. Normalmente o número pessoal precisa ser removido do WhatsApp comum antes de conectar. **Se conectar sem coexistência:**   Aí o número fica operando pela API/Kommo, e a pessoa não usa aquele mesmo número no app normal como antes. Limitações da coexistência: - grupos não sincronizam; - listas de …

---

**Mestre:** Então se o cliente quiser usar kommo e whatsapp bussines no mesmo número ela pode tranquilamente?
> 17:49

**Codex:** Sim. **Se for WhatsApp Business App, pode usar Kommo e WhatsApp Business no mesmo número** usando o recurso de **coexistência**. Funciona assim: - cliente continua usando o app WhatsApp Business no celular; - a Kommo conecta o mesmo número pela Cloud API; - conversas 1:1 sincronizam nos dois lados; - a Kommo usa esse número para CRM, bot, automação, templates e atendimento em equipe. Mas não é “sem nenhuma limitação”: - grupos não sincronizam; - chamadas de voz/vídeo não são atendidas pela Kommo; - listas de transmissão do app não funcionam como antes, deve usar broadcast da Kommo; - algumas funções do app podem ficar limitadas; - se o número estiver ligado ao Meta Inbox, pode precisar remover antes. Resumo: **para atendimento e vendas no mesmo número, sim, dá para usar tranquilamente.** S…

---

**Mestre:** tem certeza que a meta ainda tem a função de coexistensia, como fazem?
> 17:49

**Codex:** Vou checar direto na documentação oficial da Meta e na base da Kommo agora, porque “coexistência” é recurso que pode mudar por país, conta e elegibilidade.

---

**Mestre:** meu cliente quer sair da kommo e quer que eu crie algo igual para ele, ja tenho meta for developers, qual nivel de acesso devo ter pra conseguir habilitar coexistencia e fazer isso pra ele
> 17:54

**Codex:** Vou verificar isso nas docs atuais da Meta, porque a resposta muda bastante se você vai conectar só o número desse cliente ou virar provedor/onboarding para vários clientes.

---

**Mestre:** continue, cancelei sem querer
> 17:59

**Codex:** Sim. Continuando: Para criar algo tipo Kommo para o cliente, o acesso depende do modelo. **Se for só para esse cliente:**   O caminho mais simples é usar o **Meta Business do próprio cliente** e criar/conectar a WABA/número dele. Nesse caso você atua como desenvolvedor direto do cliente. A própria Meta diz que, como “direct developer”, normalmente não precisa de **Advanced Access** nem App Review para acessar ativos próprios. **Se você quer usar seu app para conectar o WhatsApp de clientes externos:**   Aí você precisa de **Advanced Access** aprovado no App Review para: - `whatsapp_business_management` - `whatsapp_business_messaging` Segundo a doc da Meta, para Cloud API no Embedded Signup v4, esses são os dois escopos principais exigidos com Advanced Access para acessar/gerenciar WABAs e …

---

**Mestre:** entao consigo ter coexistencia? nao entendi, me resuma
> 18:08

**Codex:** Sim, **você pode conseguir coexistência**, mas ela depende da Meta liberar para o número do cliente. Resumo simples: **Você consegue se:** - o número do cliente usa **WhatsApp Business App**, não WhatsApp pessoal; - o país/número é elegível; - o cliente tem ou cria um **Meta Business Portfolio**; - você conecta pelo fluxo oficial da Meta/Embedded Signup; - no onboarding aparece a opção de conectar o **WhatsApp Business App existente**; - o cliente escaneia o QR Code no app WhatsApp Business. **Você não consegue se:** - for WhatsApp pessoal comum; - a Meta não mostrar a opção de coexistência para aquele número; - o número/país/conta não for elegível; - você tentar fazer por WhatsApp Web/gambiarra. **Sobre acesso:**   Para um cliente só, usando o Business dele, você provavelmente consegue te…

---

**Mestre:** mas e se bao tiver opcao de coexistencia
> 18:12

**Codex:** Se **não aparecer a opção de coexistência**, você tem 3 caminhos: 1. **Usar só a API/CRM**    O cliente sai do WhatsApp Business App naquele número e passa a atender pelo seu sistema.      Ele não usa mais o app do celular do mesmo jeito. 2. **Manter o WhatsApp Business App e não ter automação oficial**    Ele continua no app, mas você não consegue fazer CRM/automação oficial completa pela Cloud API no mesmo número. 3. **Usar outro número**    Mantém o número atual no WhatsApp Business App e conecta um segundo número na API/CRM. O que você pode tentar antes de desistir: - confirmar que é **WhatsApp Business App**, não WhatsApp normal; - atualizar o app WhatsApp Business; - garantir que o cliente tem **Meta Business Portfolio**; - remover o número de **Meta Inbox**, se estiver conectado lá;…

---

