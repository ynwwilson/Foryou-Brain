---
type: frontend-docs
project: Totus Cenografia IA
tags: [frontend, nextjs, painel, totus]
---

# Frontend Painel (Next.js 14)

URL produção: https://totus-cenografia-ia.vercel.app

## Stack

- Next.js 14.2.5 (App Router)
- React 18.3.1
- TypeScript 5.4
- Tailwind CSS 3.4 (paleta Totus: preto + verde neon + Poppins)
- shadcn-style components (própria, sem dependência completa)
- React Query 5 (polling 4s)
- Sonner (toasts)
- Recharts 2.12 (gráficos dashboard)
- Lucide icons
- Axios (httpclient)

## Estrutura

`C:\Users\ynwwi\Projects\totus-cenografia-ia\src\`

```
src/
├── app/                         ← Next.js App Router
│   ├── layout.tsx               ← Root layout (AuthProvider + Providers)
│   ├── globals.css              ← Paleta Totus (preto + neon + Poppins)
│   ├── page.tsx                 ← Dashboard
│   ├── login/page.tsx           ← Login JWT
│   ├── inbox/page.tsx           ← Atendimento (conversas)
│   ├── leads/
│   │   ├── page.tsx             ← Pipeline 3 colunas (Cold/Warm/Hot)
│   │   └── [id]/page.tsx        ← Profile lead (4 tabs)
│   ├── catalog/page.tsx         ← Produtos CRUD com upload de imagem
│   ├── approvals/page.tsx       ← Fila de aprovação
│   ├── brain/page.tsx           ← Editor 10 seções da IA
│   ├── publication/page.tsx     ← Versionamento + rollback
│   ├── objections/page.tsx      ← 7 objeções padrão Totus
│   ├── settings/page.tsx        ← Toggle global + business hours
│   └── status/page.tsx          ← Health checks visual
├── components/
│   ├── AppSidebar.tsx           ← Sidebar com 10 itens + toggle IA
│   ├── LayoutShell.tsx          ← Guard de autenticação
│   └── Providers.tsx            ← QueryClient + AuthProvider + Toaster
├── contexts/
│   └── AuthContext.tsx          ← JWT via localStorage
└── lib/
    ├── api.ts                   ← Axios + tipos + funções de API
    └── queries.ts               ← React Query hooks com polling
```

## Páginas (11)

### 1. `/login`
- Email + senha + JWT
- Redireciona pra `/` ao sucesso

### 2. `/` (Dashboard)
- KPIs: leads totais, hot, conversas hoje vs ontem, tempo economizado
- 2 gráficos Recharts: pipeline horizontal + tendência 7 dias
- Cards: sentimento, aprovações, fluxo comercial
- Auto-refresh 10s

### 3. `/inbox` (Atendimento)
- Lista de conversas com filtros
- Click → chat completo com histórico
- Pause IA naquela conversa
- Enviar mensagem manual

### 4. `/leads` (Pipeline)
- 3 colunas: Cold (azul) / Warm (amarelo) / Hot (vermelho)
- Cards mostram nome, empresa, evento, metragem, padrão preferido
- Click → /leads/[id]

### 5. `/leads/[id]` (Profile)
- 4 tabs:
  - **Memória**: campos estruturados (cidade, metragem, orçamento, etc.)
  - **Conversas**: histórico completo
  - **Objeções**: log de objeções mencionadas
  - **Follow-ups**: histórico de aprovações

### 6. `/catalog` (Padrões/Produtos)
- Grid de 9 padrões Totus (4, 6, 8 marcados como REFERÊNCIA)
- Botão "Novo Padrão" → modal CRUD
- Upload de imagem (base64, max 2MB)
- Campos: nome, padrão_number, descrição, preço/m², args de venda, contexto IA, ativo

### 7. `/approvals` (Aprovações)
- Lista de follow_ups com status=pending
- Filtros: todas / financeiras / críticas
- Cards mostram: cliente perguntou + IA quer responder + keywords detectadas
- Botões Approve & Send / Reject (com motivo)

### 8. `/brain` (Cérebro da IA)
- Sidebar com 10 seções (Identity, Tone, Sales Rules, Qualification, Handoff, Sensitive, Image, Lead Memory, Links, Guardrails)
- Cada seção tem campos editáveis
- Badges de impacto (CRITICAL, HIGH, MEDIUM, LOW)
- "Salvar Rascunho" → grava em `ai_brain_drafts`
- Botão "Publicar" → vai pra /publication

### 9. `/publication`
- 2 cards: Versão em produção / Rascunho atual
- Indicador "Modificado" se rascunho difere da prod
- Textarea: sumário da mudança
- Botão "Publicar Versão" cria nova v
- Histórico com botão "Restaurar" por versão (rollback)

### 10. `/objections`
- 7 objeções padrão hardcoded (vindas do manual da Totus)
- Cards mostrando "CLIENTE DIZ" + "IA RESPONDE"
- (Estática — vem do Manual Mestre)

### 11. `/status`
- 5 cards de health check em tempo real
- Atualiza a cada 30s
- Mostra: Neon, Anthropic, Redis, Chatwoot, WhatsApp
- Documenta como plugar Meta API

### 12. `/settings`
- Toggle global da IA (com confirmação)
- Business hours (start/end/dias da semana)
- Off-hours message editável
- Lista de infraestrutura (read-only)
- Links externos (Vercel/Neon/Anthropic)

## React Query polling

```typescript
// src/lib/queries.ts
const POLL_INTERVAL = 4000

export const useLeadsSummary = () => useQuery({
  queryKey: ['leads-summary'],
  queryFn: getLeadsSummary,
  refetchInterval: POLL_INTERVAL,
  refetchOnWindowFocus: true,
})

// Aprovações com 4s atualiza badge no sidebar dinamicamente
export const useFollowUps = (status = 'pending') => useQuery({
  queryKey: ['follow-ups', status],
  queryFn: () => listFollowUps(status),
  refetchInterval: POLL_INTERVAL,
})
```

## Paleta de cores (do site Totus)

```css
/* src/app/globals.css */
:root {
  --background: 0 0% 0%;       /* preto puro */
  --foreground: 0 0% 100%;     /* branco */
  --primary: 84 100% 50%;      /* VERDE NEON */
  --primary-foreground: 0 0% 0%;
  --card: 0 0% 5%;             /* cinza escuro */
  --border: 0 0% 15%;
  --destructive: 0 84% 60%;
  --warning: 45 93% 47%;
  --success: 142 70% 45%;
  --info: 210 100% 56%;
}

body {
  font-family: 'Poppins', system-ui, sans-serif;
}
```

## Auth flow

1. `/login` → POST `/api/auth/login` → JWT salvo em `localStorage.totus_token`
2. `AuthProvider` (no `Providers.tsx`) carrega user via `GET /api/auth/me`
3. `LayoutShell` redireciona pra `/login` se não autenticado
4. `axios interceptor` em `api.ts` injeta `Authorization: Bearer <token>` em todas as requisições
5. Em 401 do servidor, limpa token + redireciona pra `/login`

## Como rodar local

```powershell
cd C:\Users\ynwwi\Projects\totus-cenografia-ia
npm install
npm run dev
# http://localhost:3000
```

Variável: `NEXT_PUBLIC_API_URL` (default = `/api`, mas se rodar local pode setar pra `https://totus-cenografia-ia.vercel.app/api` para usar o backend de prod).
