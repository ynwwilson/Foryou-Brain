# 14 — Mapa de Conexões

> Voltar ao [[AG Estofados — Índice]]
>
> Tudo que o Claude (eu) consigo orquestrar sozinho — organizado por **3 portas de conexão**. Referência viva pra Mestre, Marco, Eduardo.

## Porta 1 — MCPs (Model Context Protocol)

Conexão nativa. Chamo função, recebo dado. Plug & play.

### MCPs já conectados pelo Mestre

| MCP | Status | Função |
|---|---|---|
| **context-mode** | ✅ Ativo | Sandboxing, indexação, redução de contexto |
| **Desktop Commander** (claude.ai) | ✅ Ativo | Filesystem Windows |
| **Google Drive, Gmail, Calendar** (claude.ai) | ✅ Ativo | Workspace ForYou |
| **Slack, Box, Zapier** (claude.ai) | ✅ Ativo | Comunicação e storage |
| **Vercel** (claude.ai) | ✅ Ativo | Tooling Vercel oficial |
| **Composio** | ✅ Ativo | 1000+ apps (Gmail, Slack, GitHub, Insta, Meta Ads, WhatsApp, etc.) |
| **Context7** | ✅ Ativo | Docs sempre atualizadas (GSAP, Lovable, etc.) |

### MCPs a conectar pra AG Estofados

| MCP | URL / pacote | Pra quê |
|---|---|---|
| **Lovable** | `https://mcp.lovable.dev` (OAuth) | Controle do projeto Lovable |
| **Supabase** ou **Neon Tools** | Oficial | Schema, queries, edge functions |
| **Vercel** (custom) | `https://mcp.vercel.com` | Deploy, env vars, preview |
| **Cloudflare** | Oficial Cloudflare | DNS, Workers, R2, Stream, KV |
| **GitHub** | `github/github-mcp-server` | Repos, PRs, Actions |
| **Sentry** | Oficial | Erros em produção |
| **PostHog** | Oficial | Analytics + replay + flags |
| **Playwright** (skill) | `lackeyjb/playwright-skill` | QA visual real |
| **Firecrawl / Exa / Tavily** | Oficial | Research e scrape |
| **Replicate** | Oficial | Modelos open hospedados |
| **Hugging Face** | Oficial | Modelos especializados |
| **ElevenLabs** | Oficial | Voz IA (quando ativar) |
| **HeyGen / D-ID** | Não-oficial | Avatares falantes (quando ativar) |
| **Notion** | Oficial | Documentação compartilhada |
| **Linear** | Oficial | Tarefas e bugs |
| **Browserbase** | Oficial | Browser na nuvem |
| **Stripe** | Oficial | Pagamento (futuro) |
| **Figma Dev Mode** | Oficial | Design tokens (futuro) |

## Porta 2 — APIs via código

Qualquer HTTPS do mundo. Eu escrevo `fetch()`. Mestre me dá a key (em `.env`).

### APIs essenciais pra AG

| API | Pra que serve no AG | Status |
|---|---|---|
| **Gemini API** (Google AI Studio) | Veo 3, Imagen 4, Nano Banana via código | ⚠️ Falta key |
| **OpenAI API** | Sora 2, GPT-Image-1, GPT-4o Vision | ⚠️ Falta key |
| **Anthropic API** | Claude em edge (atendimento, blog, classificação) | ✅ Tem |
| **ElevenLabs** | Voz IA, narração | ⚠️ Quando ativar |
| **Replicate** | Flux Pro, Stable Video, Whisper, RemBG, Real-ESRGAN | Opcional |
| **Resend** | E-mail transacional | ⚠️ Falta key |
| **Cloudflare** | R2, Stream, Workers, KV, DNS | ✅ Tem |
| **Vercel** | Deploy programático | ✅ Tem |
| **GitHub** | Git ops, Actions | ✅ Tem |
| **Mapbox / Google Maps** | Mapa premium /sobre | Opcional |
| **WhatsApp Cloud API** | Atendimento (Fase 3) | Futuro |
| **Instagram Graph API** | Site auto-Insta (#9 pipeline) | Futuro |
| **Sentry / PostHog** | Observabilidade | Criar |

### APIs avançadas (quando escalar)

| API | Caso de uso |
|---|---|
| **Algolia / Meilisearch / Typesense** | Busca instantânea no catálogo (após 30+ peças) |
| **Pinecone / Qdrant / Weaviate** | Vector DB pra RAG (atendimento IA) |
| **Mercado Pago / Asaas / Stripe** | Pagamento Brasil |
| **OpenRouter** | Acesso unificado a 200 modelos LLM |
| **Modal / Beam** | GPU on-demand pra fine-tune |
| **fal.ai** | Modelos rápidos pra real-time (Flux Schnell 200ms) |

## Porta 3 — Browser real (humano automático)

Quando não tem API, eu opero o site como humano. Login, click, upload, screenshot.

| Skill / Tool | Pra quê |
|---|---|
| **dev-browser** | Navegação programada, screenshots, evaluate JS |
| **gstack / webapp-testing** | Playwright real, gravação de sessão |
| **Browserbase + Stagehand** | Browser na nuvem com IA dirigindo cliques |
| **Manus Computer** (futuro ForYou) | Tarefas Meta visuais (Instagram, Ads) |
| **ChatGPT Atlas / Operator** | Operador autônomo (se Mestre tiver Pro) |

## Composio — atalho pra ecossistema inteiro

[Composio](https://composio.dev) já está ativo na conta do Mestre. Dá acesso OAuth a **1000+ apps** sem precisar conectar 1 por 1:

| App via Composio | Caso no AG |
|---|---|
| Gmail | Notificação de lead, agenda |
| Slack | Notificação interna ForYou |
| GitHub | Code ops (alternativa ao GitHub MCP direto) |
| Instagram | Pegar posts pra pipeline #9 |
| Meta Ads | Criar anúncios sozinho (com autorização) |
| WhatsApp Business | Atendimento (Fase 3) |
| HubSpot / Pipedrive | CRM (se entrar) |
| Calendly / Cal.com | Agendamento de visita à loja |
| Notion | Wiki compartilhada |

## Limites do que faço sozinho

Pra confiança plena, listei onde eu paro sem o Mestre:

| Não faço sozinho | Por quê |
|---|---|
| Comprar com cartão do Mestre | Mestre vira chave; eu rodo com ela |
| Postar no Instagram da AG | CLAUDE.md exige tripla confirmação |
| Enviar mensagem real ao cliente | Mesma regra |
| Criar campanha paga | Tripla confirmação |
| Apagar dado em produção | Confirmação obrigatória |
| Login interativo (CAPTCHA, 2FA) | Mestre loga 1x, eu opero com sessão |

Tudo o resto roda solo depois da chave virada.

## Composio (apps já configurados pelo Mestre)

> Verificar lista completa na conta do Mestre. Provavelmente já tem Gmail, Slack, GitHub, Insta, Meta Ads.

## Padrão de armazenamento de chaves

```
C:\Users\ynwwi\Projetos\foryoucode.env       ← chaves comuns da ForYou
C:\Users\ynwwi\Projetos\ag-estofados\.env    ← chaves específicas do projeto AG
```

Cada projeto tem seu `.env`. Chaves reutilizáveis (GitHub, Vercel, Cloudflare, Anthropic) ficam no `foryoucode.env` e são referenciadas em todos.

✅ Feito (2026-05-22): arquivos `.txt` renomeados pra `.env` real; `.gitignore` global em `C:\Users\ynwwi\.gitignore_global` + `.gitignore` em `Projetos\`.

## Como o fluxo de trabalho fica

```
Mestre fala: "quero hero com vídeo cinematográfico de mãos costurando"
            ↓
Claude (eu) entende:
  ├─ Veo 3 via Gemini API (Porta 2)
  ├─ Topaz Video AI via license (Porta 2)
  ├─ Cloudflare Stream upload via API (Porta 1)
  ├─ Lovable update via MCP (Porta 1)
  ├─ GitHub commit via MCP (Porta 1)
  └─ Vercel deploy via MCP (Porta 1)

Tudo orquestrado sozinho. Mestre só vê o preview pronto.
```
