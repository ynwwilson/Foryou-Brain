---
tags: [projeto/webhub, cliente/webseg, cliente/webcar, demo, ativo]
created: 2026-05-06
status: planejamento
---

# Demo Web Car — WebHub

> Plataforma operacional unificada **Webseg + WebCar** (corretora + loja de carros, grupo Web em Patos de Minas/MG).
> Demo grátis pra apresentar pro cliente. Modelo comercial: **pagamento único**, sem mensalidade da agência.

## 📁 Arquivos no disco
- Schema/Seed/Claim: `C:\Users\ynwwi\Projects\webhub-demo\01-supabase\`
- Prompts Lovable: `C:\Users\ynwwi\Projects\webhub-demo\02-lovable-prompts\`
- Esta nota é a versão consolidada autocontida — tudo o que você precisa colar.

---

## ⏱ SEQUÊNCIA DE EXECUÇÃO (siga em ordem)

### 1️⃣ Criar projeto Supabase
1. [supabase.com](https://supabase.com) → New project
2. Nome `webhub-demo` · região South America (São Paulo) · senha do banco anote
3. Aguarda 1-2 min provisionar
4. **Project Settings → API** copia:
   - `Project URL`
   - `anon public` key

### 2️⃣ Rodar SQL Schema
- Abre **SQL Editor** → New query
- Cola o bloco da seção **🗄️ SQL 1 — SCHEMA** desta nota
- Run
- Validar: cria 16 tabelas (vê em **Table Editor**)

### 3️⃣ Rodar SQL Seed
- New query
- Cola o bloco **🗄️ SQL 2 — SEED**
- Run
- Validar: 30 clientes em `profiles`, 20 em `vehicles`, 25 em `policies`

### 4️⃣ Criar 4 users de demo
- **Authentication → Users → Add user** (4x), marca **Auto-confirm** em cada
- `cliente@webhub.demo` / `demo123`
- `corretor@webhub.demo` / `demo123`
- `vendedor@webhub.demo` / `demo123`
- `admin@webhub.demo` / `demo123`

### 5️⃣ Rodar SQL Demo Claim
- New query
- Cola o bloco **🗄️ SQL 3 — DEMO CLAIM**
- Run
- Validar: roles dos 4 users atualizados; dados de João Pereira transferidos pro cliente@webhub.demo

### 6️⃣ Criar projeto Lovable
- [lovable.dev](https://lovable.dev) → New project
- Cola o conteúdo de **🤖 PROMPT 1 — FOUNDATION** desta nota
- Quando Lovable pedir env vars do Supabase, cola URL e anon key
- Aguarda build (3-8 min)
- Testa login com `admin@webhub.demo` / `demo123`

### 7️⃣ Colar Prompt 2 — Cliente
- No chat do Lovable cola **🤖 PROMPT 2 — CLIENTE**
- Aguarda
- Testa: login `cliente@webhub.demo` mostra apólices reais

### 8️⃣ Colar Prompt 3 — Corretor
- Cola **🤖 PROMPT 3 — CORRETOR**
- Testa: login `corretor@webhub.demo` mostra Kanban com 18+ leads

### 9️⃣ Colar Prompt 4 — WebCar
- Cola **🤖 PROMPT 4 — WEBCAR**
- Testa: login `vendedor@webhub.demo` mostra estoque + pipeline com 12 vendas

### 🔟 Colar Prompt 5 — Admin
- Cola **🤖 PROMPT 5 — ADMIN**
- Testa: login `admin@webhub.demo` mostra dashboards consolidados

### 1️⃣1️⃣ Colar Prompt 6 — Cross-sell + Polish
- Cola **🤖 PROMPT 6 — CROSS-SELL + POLISH**
- Edge Functions Claude precisam de `ANTHROPIC_API_KEY` em **Project Settings → Edge Functions → Secrets**
- Pega chave em [console.anthropic.com](https://console.anthropic.com)
- Modelo: `claude-sonnet-4-6`
- Teste killer: 3 abas (admin/corretor/cliente), aperta "Simular venda" no admin → vê tudo atualizando ao vivo

### 1️⃣2️⃣ Demo final
- Pega URL pública do Lovable
- Grava vídeo de 3min: 4 logins → simulador cross-sell no admin
- Manda pra Webseg sem compromisso

---

## 🔑 Logins de Demo

| Role | Email | Senha | O que verá |
|---|---|---|---|
| Cliente | cliente@webhub.demo | demo123 | João Pereira — apólice Porto, sinistro em análise, Drive Score 87 |
| Corretor | corretor@webhub.demo | demo123 | Camila Andrade — CRM 18 leads, 25 apólices, comissões |
| Vendedor | vendedor@webhub.demo | demo123 | Diego Vendas — 20 carros estoque, 12 vendas pipeline |
| Admin | admin@webhub.demo | demo123 | Wilson — dashboards consolidados + simulador cross-sell |

---

## 💰 Modelo Comercial

- **Pagamento único** sem mensalidade da agência: R$ 25-50k
- **Infra mensal repassada** (cliente paga direto):
  - Supabase Pro: ~$25/mês
  - Claude API: $50-200/mês
  - WhatsApp Cloud API: $0,05-0,15/conversa
  - Hosting: gratuito ou ~$20/mês
- Total infra: R$ 500-1.500/mês

---

## ⚠️ Limitações conhecidas (do demo)

- Cotações são simuladas via função local — em produção plugar Segfy/Quiver
- OCR de CNH/CRLV é mock — em prod plugar Google Vision
- Pagamentos mockados — em prod plugar Asaas/Stripe
- WhatsApp não envia de verdade — em prod plugar WhatsApp Cloud API
- Drive Score é fake — em prod ler sensores celular ou OBD2

---

## 🚧 Checklist final antes de mostrar

- [ ] 4 logins funcionam
- [ ] Cliente vê apólices, abre sinistro com IA
- [ ] Corretor arrasta leads no Kanban
- [ ] Vendedor vê pipeline de vendas
- [ ] Admin vê dashboards
- [ ] Simulador cross-sell funciona ao vivo (3 abas abertas)
- [ ] Claude responde no copiloto e sinistro
- [ ] Mobile não quebra
- [ ] Dark mode funciona

---

## 🗄️ SQL 1 — SCHEMA
````sql
-- =====================================================================
-- WEBHUB DEMO â€” Schema completo Supabase
-- Cole isso no SQL Editor do Supabase e rode tudo de uma vez
-- =====================================================================

create extension if not exists "uuid-ossp";
create extension if not exists "pgcrypto";

-- =====================================================================
-- 1. PROFILES (usuÃ¡rios: cliente, corretor, vendedor, admin)
-- =====================================================================
create table if not exists public.profiles (
  id uuid primary key default uuid_generate_v4(),
  email text unique,
  full_name text not null,
  phone text,
  cpf text,
  role text not null default 'cliente' check (role in ('cliente','corretor','vendedor','admin')),
  avatar_url text,
  data_nascimento date,
  cep text,
  endereco text,
  cidade text,
  estado text,
  meta jsonb default '{}'::jsonb,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- =====================================================================
-- 2. VEHICLES (estoque WebCar)
-- =====================================================================
create table if not exists public.vehicles (
  id uuid primary key default uuid_generate_v4(),
  marca text not null,
  modelo text not null,
  versao text,
  ano_modelo int not null,
  ano_fabricacao int not null,
  cor text,
  km int default 0,
  combustivel text,
  cambio text,
  placa text,
  chassi text,
  renavam text,
  preco_venda numeric(12,2) not null,
  preco_avaliacao numeric(12,2),
  status text not null default 'disponivel' check (status in ('disponivel','reservado','vendido','em_avaliacao')),
  fotos text[] default array[]::text[],
  descricao text,
  destaque boolean default false,
  is_seminovo boolean default true,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- =====================================================================
-- 3. CLIENT_VEHICLES (carros dos segurados)
-- =====================================================================
create table if not exists public.client_vehicles (
  id uuid primary key default uuid_generate_v4(),
  client_id uuid not null references public.profiles(id) on delete cascade,
  marca text not null,
  modelo text not null,
  versao text,
  ano_modelo int,
  placa text,
  chassi text,
  km_atual int,
  cor text,
  data_aquisicao date,
  origem text default 'externo' check (origem in ('webcar','externo')),
  vehicle_id uuid references public.vehicles(id),
  proximo_ipva date,
  proximo_licenciamento date,
  proxima_revisao date,
  created_at timestamptz default now()
);

-- =====================================================================
-- 4. LEADS (Webseg + WebCar unificados)
-- =====================================================================
create table if not exists public.leads (
  id uuid primary key default uuid_generate_v4(),
  full_name text not null,
  phone text,
  email text,
  cpf text,
  origem text not null check (origem in ('instagram','site','walk_in','indicacao','webcar','google_ads','meta_ads','whatsapp','telefone')),
  produto_interesse text not null check (produto_interesse in ('auto','moto','residencial','vida','viagem','agro','empresarial','carro_novo','carro_usado','financiamento')),
  vehicle_interest_id uuid references public.vehicles(id),
  observacoes text,
  status text not null default 'novo' check (status in ('novo','contato','cotacao_enviada','em_negociacao','fechado','perdido')),
  responsavel_id uuid references public.profiles(id),
  client_id uuid references public.profiles(id),
  motivo_perda text,
  ai_summary text,
  ai_score int default 50,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- =====================================================================
-- 5. QUOTES (cotaÃ§Ãµes)
-- =====================================================================
create table if not exists public.quotes (
  id uuid primary key default uuid_generate_v4(),
  lead_id uuid references public.leads(id),
  client_id uuid references public.profiles(id),
  vehicle_data jsonb not null default '{}'::jsonb,
  driver_data jsonb not null default '{}'::jsonb,
  coberturas jsonb,
  resultados jsonb,
  cotacao_escolhida jsonb,
  status text not null default 'rascunho' check (status in ('rascunho','enviada','aceita','rejeitada','expirada')),
  valor_total numeric(12,2),
  parcelas int default 12,
  ai_recommendation text,
  origem_cross_sell boolean default false,
  car_sale_id uuid,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- =====================================================================
-- 6. POLICIES (apÃ³lices)
-- =====================================================================
create table if not exists public.policies (
  id uuid primary key default uuid_generate_v4(),
  client_id uuid not null references public.profiles(id) on delete cascade,
  client_vehicle_id uuid references public.client_vehicles(id),
  numero_apolice text not null,
  seguradora text not null,
  produto text not null check (produto in ('auto','moto','residencial','vida','viagem','agro','empresarial')),
  valor_premio numeric(12,2) not null,
  valor_franquia numeric(12,2),
  vigencia_inicio date not null,
  vigencia_fim date not null,
  status text not null default 'ativa' check (status in ('ativa','cancelada','vencida','em_renovacao','suspensa')),
  coberturas jsonb,
  comissao_percentual numeric(5,2) default 15,
  comissao_valor numeric(12,2),
  pdf_url text,
  responsavel_id uuid references public.profiles(id),
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- =====================================================================
-- 7. CLAIMS (sinistros)
-- =====================================================================
create table if not exists public.claims (
  id uuid primary key default uuid_generate_v4(),
  policy_id uuid not null references public.policies(id),
  client_id uuid not null references public.profiles(id),
  numero_sinistro text,
  tipo text not null check (tipo in ('colisao','roubo','furto','natureza','terceiro','incendio','vidros','panico')),
  data_ocorrencia timestamptz not null default now(),
  local_ocorrencia text,
  geolocalizacao jsonb,
  descricao text,
  ai_dossier text,
  ai_fraud_score int default 10,
  fotos text[] default array[]::text[],
  documentos text[] default array[]::text[],
  status text not null default 'aberto' check (status in ('aberto','em_analise','vistoria','aprovado','pago','recusado','encerrado')),
  oficina text,
  valor_estimado numeric(12,2),
  valor_aprovado numeric(12,2),
  timeline jsonb default '[]'::jsonb,
  responsavel_id uuid references public.profiles(id),
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- =====================================================================
-- 8. CAR_SALES (vendas WebCar)
-- =====================================================================
create table if not exists public.car_sales (
  id uuid primary key default uuid_generate_v4(),
  vehicle_id uuid not null references public.vehicles(id),
  client_id uuid references public.profiles(id),
  client_lead_id uuid references public.leads(id),
  client_full_name text not null,
  client_cpf text,
  client_phone text,
  client_email text,
  vendedor_id uuid references public.profiles(id),

  preco_negociado numeric(12,2),
  carro_troca jsonb,
  forma_pagamento text check (forma_pagamento in ('avista','financiado','misto','consorcio')),
  entrada numeric(12,2),

  financeira text,
  parcelas int,
  valor_parcela numeric(12,2),
  taxa_juros numeric(5,2),
  status_credito text default 'nao_iniciado' check (status_credito in ('nao_iniciado','enviado','em_analise','aprovado','rejeitado','aprovado_condicional')),

  documentos jsonb default '{}'::jsonb,

  contrato_url text,
  assinatura_status text default 'pendente' check (assinatura_status in ('pendente','enviado','assinado_cliente','assinado_loja','concluido')),

  etapa_atual text not null default 'lead' check (etapa_atual in ('lead','test_drive','proposta','credito','contrato','entrega','concluida','perdida')),

  data_entrega date,
  proxima_revisao date,
  garantia_meses int default 3,

  comissao_vendedor numeric(12,2),
  cross_sell_quote_id uuid,
  observacoes text,

  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

alter table public.quotes
  drop constraint if exists fk_quote_car_sale,
  add constraint fk_quote_car_sale foreign key (car_sale_id) references public.car_sales(id);

-- =====================================================================
-- 9. DOCUMENTS (cofre digital)
-- =====================================================================
create table if not exists public.documents (
  id uuid primary key default uuid_generate_v4(),
  client_id uuid not null references public.profiles(id),
  tipo text not null,
  nome text not null,
  url text not null,
  ocr_data jsonb,
  validade date,
  uploaded_by uuid references public.profiles(id),
  related_type text,
  related_id uuid,
  created_at timestamptz default now()
);

-- =====================================================================
-- 10. PAYMENTS
-- =====================================================================
create table if not exists public.payments (
  id uuid primary key default uuid_generate_v4(),
  client_id uuid not null references public.profiles(id),
  policy_id uuid references public.policies(id),
  car_sale_id uuid references public.car_sales(id),
  tipo text not null check (tipo in ('parcela_seguro','entrada_carro','parcela_carro','sinistro_pago','renovacao','indicacao_cashback')),
  valor numeric(12,2) not null,
  metodo text check (metodo in ('cartao','boleto','pix','debito_automatico','transferencia')),
  status text not null default 'pendente' check (status in ('pendente','pago','atrasado','falhou','estornado')),
  vencimento date,
  data_pagamento timestamptz,
  parcela_atual int,
  parcela_total int,
  link_boleto text,
  qr_pix text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- =====================================================================
-- 11. ACTIVITIES (timeline cross-system)
-- =====================================================================
create table if not exists public.activities (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references public.profiles(id),
  related_type text,
  related_id uuid,
  tipo text not null,
  titulo text not null,
  descricao text,
  data jsonb,
  created_at timestamptz default now()
);

-- =====================================================================
-- 12. MESSAGES (WhatsApp mock)
-- =====================================================================
create table if not exists public.messages (
  id uuid primary key default uuid_generate_v4(),
  client_id uuid references public.profiles(id),
  lead_id uuid references public.leads(id),
  conversation_id uuid not null,
  from_role text not null check (from_role in ('cliente','corretor','vendedor','sistema','ai')),
  from_user_id uuid references public.profiles(id),
  conteudo text not null,
  tipo text default 'texto' check (tipo in ('texto','imagem','audio','arquivo','template')),
  url_anexo text,
  ai_generated boolean default false,
  ai_sentiment text,
  lida boolean default false,
  created_at timestamptz default now()
);

-- =====================================================================
-- 13. COMMISSIONS
-- =====================================================================
create table if not exists public.commissions (
  id uuid primary key default uuid_generate_v4(),
  policy_id uuid references public.policies(id),
  car_sale_id uuid references public.car_sales(id),
  beneficiario_id uuid not null references public.profiles(id),
  tipo text not null check (tipo in ('seguro_inicial','seguro_renovacao','venda_carro','indicacao')),
  valor numeric(12,2) not null,
  percentual numeric(5,2),
  status text not null default 'prevista' check (status in ('prevista','aprovada','paga','cancelada')),
  data_prevista date,
  data_pagamento date,
  observacao text,
  created_at timestamptz default now()
);

-- =====================================================================
-- 14. NOTIFICATIONS
-- =====================================================================
create table if not exists public.notifications (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid not null references public.profiles(id),
  titulo text not null,
  mensagem text,
  tipo text check (tipo in ('renovacao','sinistro','pagamento','documento','cross_sell','ia','venda','lead')),
  url_acao text,
  prioridade text default 'normal' check (prioridade in ('baixa','normal','alta','critica')),
  lida boolean default false,
  created_at timestamptz default now()
);

-- =====================================================================
-- 15. INDICATIONS (programa de indicaÃ§Ã£o simples)
-- =====================================================================
create table if not exists public.indications (
  id uuid primary key default uuid_generate_v4(),
  indicador_id uuid not null references public.profiles(id),
  indicado_nome text not null,
  indicado_telefone text,
  indicado_email text,
  produto text,
  status text default 'pendente' check (status in ('pendente','convertido','perdido')),
  cashback_valor numeric(12,2),
  cashback_status text default 'pendente' check (cashback_status in ('pendente','liberado','pago')),
  lead_gerado_id uuid references public.leads(id),
  policy_gerada_id uuid references public.policies(id),
  created_at timestamptz default now()
);

-- =====================================================================
-- 16. DRIVE_SCORES (telemetria)
-- =====================================================================
create table if not exists public.drive_scores (
  id uuid primary key default uuid_generate_v4(),
  client_id uuid not null references public.profiles(id),
  client_vehicle_id uuid references public.client_vehicles(id),
  periodo text not null,
  score int not null,
  km_total numeric,
  freadas_bruscas int,
  aceleracoes_bruscas int,
  velocidade_max numeric,
  horario_madrugada_pct numeric,
  desconto_percentual numeric,
  created_at timestamptz default now()
);

-- =====================================================================
-- INDEXES
-- =====================================================================
create index if not exists idx_leads_status on public.leads(status);
create index if not exists idx_leads_responsavel on public.leads(responsavel_id);
create index if not exists idx_leads_origem on public.leads(origem);
create index if not exists idx_policies_client on public.policies(client_id);
create index if not exists idx_policies_status on public.policies(status);
create index if not exists idx_policies_vencimento on public.policies(vigencia_fim);
create index if not exists idx_claims_status on public.claims(status);
create index if not exists idx_claims_client on public.claims(client_id);
create index if not exists idx_car_sales_etapa on public.car_sales(etapa_atual);
create index if not exists idx_car_sales_vendedor on public.car_sales(vendedor_id);
create index if not exists idx_payments_status on public.payments(status);
create index if not exists idx_payments_vencimento on public.payments(vencimento);
create index if not exists idx_messages_conversation on public.messages(conversation_id);
create index if not exists idx_notifications_user_lida on public.notifications(user_id, lida);

-- =====================================================================
-- TRIGGERS â€” updated_at
-- =====================================================================
create or replace function public.update_updated_at()
returns trigger as $$
begin new.updated_at = now(); return new; end;
$$ language plpgsql;

drop trigger if exists trg_profiles_updated on public.profiles;
create trigger trg_profiles_updated before update on public.profiles for each row execute function public.update_updated_at();
drop trigger if exists trg_vehicles_updated on public.vehicles;
create trigger trg_vehicles_updated before update on public.vehicles for each row execute function public.update_updated_at();
drop trigger if exists trg_leads_updated on public.leads;
create trigger trg_leads_updated before update on public.leads for each row execute function public.update_updated_at();
drop trigger if exists trg_quotes_updated on public.quotes;
create trigger trg_quotes_updated before update on public.quotes for each row execute function public.update_updated_at();
drop trigger if exists trg_policies_updated on public.policies;
create trigger trg_policies_updated before update on public.policies for each row execute function public.update_updated_at();
drop trigger if exists trg_claims_updated on public.claims;
create trigger trg_claims_updated before update on public.claims for each row execute function public.update_updated_at();
drop trigger if exists trg_car_sales_updated on public.car_sales;
create trigger trg_car_sales_updated before update on public.car_sales for each row execute function public.update_updated_at();
drop trigger if exists trg_payments_updated on public.payments;
create trigger trg_payments_updated before update on public.payments for each row execute function public.update_updated_at();

-- =====================================================================
-- TRIGGER â€” handle_new_user (cria profile automÃ¡tico ao signup)
-- =====================================================================
create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, email, full_name, role)
  values (
    new.id,
    new.email,
    coalesce(new.raw_user_meta_data->>'full_name', split_part(new.email,'@',1)),
    coalesce(new.raw_user_meta_data->>'role', 'cliente')
  )
  on conflict (id) do nothing;
  return new;
end;
$$ language plpgsql security definer;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute function public.handle_new_user();

-- =====================================================================
-- HELPER FUNCTIONS (uso em RLS)
-- =====================================================================
create or replace function public.user_role() returns text as $$
  select role from public.profiles where id = auth.uid();
$$ language sql security definer stable;

create or replace function public.is_staff() returns boolean as $$
  select coalesce((select role in ('corretor','vendedor','admin') from public.profiles where id = auth.uid()), false);
$$ language sql security definer stable;

create or replace function public.is_admin() returns boolean as $$
  select coalesce((select role = 'admin' from public.profiles where id = auth.uid()), false);
$$ language sql security definer stable;

-- =====================================================================
-- RLS â€” ENABLE
-- =====================================================================
alter table public.profiles enable row level security;
alter table public.vehicles enable row level security;
alter table public.client_vehicles enable row level security;
alter table public.leads enable row level security;
alter table public.quotes enable row level security;
alter table public.policies enable row level security;
alter table public.claims enable row level security;
alter table public.car_sales enable row level security;
alter table public.documents enable row level security;
alter table public.payments enable row level security;
alter table public.activities enable row level security;
alter table public.messages enable row level security;
alter table public.commissions enable row level security;
alter table public.notifications enable row level security;
alter table public.indications enable row level security;
alter table public.drive_scores enable row level security;

-- =====================================================================
-- RLS â€” POLICIES
-- =====================================================================
drop policy if exists "profiles_read" on public.profiles;
create policy "profiles_read" on public.profiles for select using (auth.uid() = id or public.is_staff());
drop policy if exists "profiles_update_self" on public.profiles;
create policy "profiles_update_self" on public.profiles for update using (auth.uid() = id or public.is_admin());

drop policy if exists "vehicles_read" on public.vehicles;
create policy "vehicles_read" on public.vehicles for select using (true);
drop policy if exists "vehicles_staff" on public.vehicles;
create policy "vehicles_staff" on public.vehicles for all using (public.is_staff());

drop policy if exists "client_vehicles_access" on public.client_vehicles;
create policy "client_vehicles_access" on public.client_vehicles for all using (auth.uid() = client_id or public.is_staff());

drop policy if exists "leads_staff" on public.leads;
create policy "leads_staff" on public.leads for all using (public.is_staff());

drop policy if exists "quotes_read" on public.quotes;
create policy "quotes_read" on public.quotes for select using (auth.uid() = client_id or public.is_staff());
drop policy if exists "quotes_staff_write" on public.quotes;
create policy "quotes_staff_write" on public.quotes for all using (public.is_staff());

drop policy if exists "policies_read" on public.policies;
create policy "policies_read" on public.policies for select using (auth.uid() = client_id or public.is_staff());
drop policy if exists "policies_staff_write" on public.policies;
create policy "policies_staff_write" on public.policies for all using (public.is_staff());

drop policy if exists "claims_read" on public.claims;
create policy "claims_read" on public.claims for select using (auth.uid() = client_id or public.is_staff());
drop policy if exists "claims_create" on public.claims;
create policy "claims_create" on public.claims for insert with check (auth.uid() = client_id or public.is_staff());
drop policy if exists "claims_update" on public.claims;
create policy "claims_update" on public.claims for update using (public.is_staff());

drop policy if exists "car_sales_staff" on public.car_sales;
create policy "car_sales_staff" on public.car_sales for all using (public.is_staff());
drop policy if exists "car_sales_client_read" on public.car_sales;
create policy "car_sales_client_read" on public.car_sales for select using (auth.uid() = client_id);

drop policy if exists "documents_access" on public.documents;
create policy "documents_access" on public.documents for all using (auth.uid() = client_id or public.is_staff());

drop policy if exists "payments_read" on public.payments;
create policy "payments_read" on public.payments for select using (auth.uid() = client_id or public.is_staff());
drop policy if exists "payments_staff_write" on public.payments;
create policy "payments_staff_write" on public.payments for all using (public.is_staff());

drop policy if exists "activities_staff" on public.activities;
create policy "activities_staff" on public.activities for all using (public.is_staff());
drop policy if exists "activities_self_read" on public.activities;
create policy "activities_self_read" on public.activities for select using (user_id = auth.uid());

drop policy if exists "messages_access" on public.messages;
create policy "messages_access" on public.messages for all using (auth.uid() = client_id or public.is_staff());

drop policy if exists "commissions_staff" on public.commissions;
create policy "commissions_staff" on public.commissions for all using (public.is_staff());

drop policy if exists "notifications_self" on public.notifications;
create policy "notifications_self" on public.notifications for all using (auth.uid() = user_id or public.is_admin());

drop policy if exists "indications_access" on public.indications;
create policy "indications_access" on public.indications for all using (auth.uid() = indicador_id or public.is_staff());

drop policy if exists "drive_read" on public.drive_scores;
create policy "drive_read" on public.drive_scores for select using (auth.uid() = client_id or public.is_staff());
drop policy if exists "drive_write" on public.drive_scores;
create policy "drive_write" on public.drive_scores for all using (public.is_staff());

-- =====================================================================
-- REALTIME â€” habilitar pra cross-sell live
-- =====================================================================
alter publication supabase_realtime add table public.leads;
alter publication supabase_realtime add table public.quotes;
alter publication supabase_realtime add table public.notifications;
alter publication supabase_realtime add table public.car_sales;
alter publication supabase_realtime add table public.activities;
alter publication supabase_realtime add table public.messages;

-- DONE!

````

---

## 🗄️ SQL 2 — SEED
````sql
-- =====================================================================
-- WEBHUB DEMO â€” SEED DATA
-- Rode DEPOIS do 01-schema.sql.
-- Esse seed cria 30 clientes fictÃ­cios + 20 carros + leads + apÃ³lices + sinistros + vendas.
-- Os dados ficam visÃ­veis pros perfis staff (corretor/vendedor/admin) no demo.
-- =====================================================================

-- LIMPAR dados anteriores (cuidado: zera tudo do demo)
truncate public.activities, public.messages, public.notifications,
  public.commissions, public.indications, public.drive_scores,
  public.payments, public.documents, public.claims, public.policies,
  public.quotes, public.car_sales, public.leads, public.client_vehicles,
  public.vehicles, public.profiles cascade;

-- =====================================================================
-- 1. PROFILES â€” 30 clientes fictÃ­cios + corretores/vendedores fictÃ­cios
-- =====================================================================
insert into public.profiles (id, full_name, email, phone, cpf, role, data_nascimento, cep, endereco, cidade, estado) values
  -- Corretores fictÃ­cios (pra atribuir leads/apÃ³lices)
  ('11111111-1111-1111-1111-111111111111','Camila Andrade (Corretora)','camila@webseg.demo','34999110011','111.222.333-44','corretor','1990-03-15','38700-000','PraÃ§a Alexina CÃ¢ndida, 100','Patos de Minas','MG'),
  ('22222222-2222-2222-2222-222222222222','Bruno Lima (Corretor)','bruno@webseg.demo','34999220022','222.333.444-55','corretor','1988-07-22','38700-000','PraÃ§a Alexina CÃ¢ndida, 100','Patos de Minas','MG'),
  -- Vendedores fictÃ­cios WebCar
  ('33333333-3333-3333-3333-333333333333','Diego Vendas (WebCar)','diego.vendas@webcar.demo','34999330033','333.444.555-66','vendedor','1985-11-08','38700-000','PraÃ§a Alexina CÃ¢ndida, 100','Patos de Minas','MG'),
  ('44444444-4444-4444-4444-444444444444','Rafael Vendas (WebCar)','rafael.vendas@webcar.demo','34999440044','444.555.666-77','vendedor','1992-02-19','38700-000','PraÃ§a Alexina CÃ¢ndida, 100','Patos de Minas','MG'),
  -- 30 Clientes
  ('a1000001-0000-0000-0000-000000000001','JoÃ£o Pereira Silva','joao.pereira@gmail.com','34988110001','555.111.222-33','cliente','1985-04-12','38700-001','Rua das Flores, 123','Patos de Minas','MG'),
  ('a1000002-0000-0000-0000-000000000002','Maria Aparecida Costa','maria.costa@gmail.com','34988110002','555.222.333-44','cliente','1978-09-23','38700-002','Av. JK, 456','Patos de Minas','MG'),
  ('a1000003-0000-0000-0000-000000000003','Carlos Eduardo Santos','carlos.santos@hotmail.com','34988110003','555.333.444-55','cliente','1990-06-15','38700-003','Rua dos Andradas, 789','Patos de Minas','MG'),
  ('a1000004-0000-0000-0000-000000000004','Ana Beatriz Oliveira','ana.oliveira@gmail.com','34988110004','555.444.555-66','cliente','1995-11-30','38700-004','Rua Major Gote, 321','Patos de Minas','MG'),
  ('a1000005-0000-0000-0000-000000000005','Pedro Henrique Almeida','pedro.almeida@gmail.com','34988110005','555.555.666-77','cliente','1982-02-08','38700-005','Av. Brasil, 1500','Patos de Minas','MG'),
  ('a1000006-0000-0000-0000-000000000006','Juliana Ferreira','juliana.ferreira@yahoo.com','34988110006','555.666.777-88','cliente','1992-07-19','38700-006','Rua GoiÃ¡s, 234','Patos de Minas','MG'),
  ('a1000007-0000-0000-0000-000000000007','Marcos Vinicius Rodrigues','marcos.rodrigues@gmail.com','34988110007','555.777.888-99','cliente','1987-12-04','38700-007','Rua SÃ£o Paulo, 567','Patos de Minas','MG'),
  ('a1000008-0000-0000-0000-000000000008','Patricia Gomes','patricia.gomes@gmail.com','34988110008','555.888.999-00','cliente','1989-03-25','38700-008','Av. FÃ¡tima Porto, 89','Patos de Minas','MG'),
  ('a1000009-0000-0000-0000-000000000009','Roberto Carlos Lima','roberto.lima@hotmail.com','34988110009','555.999.000-11','cliente','1975-08-17','38700-009','Rua Belo Horizonte, 432','Patos de Minas','MG'),
  ('a1000010-0000-0000-0000-000000000010','Fernanda Souza','fernanda.souza@gmail.com','34988110010','555.000.111-22','cliente','1993-05-02','38700-010','Rua Minas Gerais, 765','Patos de Minas','MG'),
  ('a1000011-0000-0000-0000-000000000011','Gustavo Henrique Martins','gustavo.martins@gmail.com','34988110011','556.111.222-33','cliente','1986-10-14','38700-011','Av. Getulio Vargas, 200','Patos de Minas','MG'),
  ('a1000012-0000-0000-0000-000000000012','Larissa Cristina Dias','larissa.dias@gmail.com','34988110012','556.222.333-44','cliente','1991-01-28','38700-012','Rua Coromandel, 150','Patos de Minas','MG'),
  ('a1000013-0000-0000-0000-000000000013','Ricardo Augusto Souza','ricardo.souza@gmail.com','34988110013','556.333.444-55','cliente','1980-04-09','38700-013','Rua Lagoa Grande, 88','Patos de Minas','MG'),
  ('a1000014-0000-0000-0000-000000000014','Camila Fernandes Borges','camila.borges@gmail.com','34988110014','556.444.555-66','cliente','1994-08-21','38700-014','Av. ParanaÃ­ba, 1234','Patos de Minas','MG'),
  ('a1000015-0000-0000-0000-000000000015','Lucas Mateus Alves','lucas.alves@gmail.com','34988110015','556.555.666-77','cliente','1988-11-11','38700-015','Rua EspÃ­rito Santo, 99','Patos de Minas','MG'),
  ('a1000016-0000-0000-0000-000000000016','Beatriz Helena Pacheco','beatriz.pacheco@gmail.com','34988110016','556.666.777-88','cliente','1996-02-14','38700-016','Rua Carmo do ParanaÃ­ba, 555','Patos de Minas','MG'),
  ('a1000017-0000-0000-0000-000000000017','Daniel Rocha Pereira','daniel.rocha@gmail.com','34988110017','556.777.888-99','cliente','1983-07-07','38700-017','Av. MarabÃ¡, 321','Patos de Minas','MG'),
  ('a1000018-0000-0000-0000-000000000018','Vanessa Mendes Carvalho','vanessa.carvalho@gmail.com','34988110018','556.888.999-00','cliente','1990-09-30','38700-018','Rua Uberaba, 678','Patos de Minas','MG'),
  ('a1000019-0000-0000-0000-000000000019','Felipe Augusto Castro','felipe.castro@gmail.com','34988110019','556.999.000-11','cliente','1985-12-22','38700-019','Av. Getulio Vargas, 1500','Patos de Minas','MG'),
  ('a1000020-0000-0000-0000-000000000020','Sabrina Teixeira','sabrina.teixeira@gmail.com','34988110020','556.000.111-22','cliente','1992-04-05','38700-020','Rua Patos, 200','Patos de Minas','MG'),
  ('a1000021-0000-0000-0000-000000000021','Rodrigo Mello Faria','rodrigo.faria@gmail.com','34988110021','557.111.222-33','cliente','1979-06-18','38700-021','Rua AraxÃ¡, 78','Patos de Minas','MG'),
  ('a1000022-0000-0000-0000-000000000022','Michele Aparecida Reis','michele.reis@gmail.com','34988110022','557.222.333-44','cliente','1987-03-29','38700-022','Av. JK, 2000','Patos de Minas','MG'),
  ('a1000023-0000-0000-0000-000000000023','Tiago Pereira Nunes','tiago.nunes@gmail.com','34988110023','557.333.444-55','cliente','1991-10-13','38700-023','Rua Ouro Preto, 444','Patos de Minas','MG'),
  ('a1000024-0000-0000-0000-000000000024','Aline Sampaio Vieira','aline.vieira@gmail.com','34988110024','557.444.555-66','cliente','1989-05-26','38700-024','Rua Tiradentes, 89','Patos de Minas','MG'),
  ('a1000025-0000-0000-0000-000000000025','Eduardo Henrique Pinto','eduardo.pinto@gmail.com','34988110025','557.555.666-77','cliente','1984-08-04','38700-025','Av. Brasil, 999','Patos de Minas','MG'),
  ('a1000026-0000-0000-0000-000000000026','Priscila Moreira','priscila.moreira@gmail.com','34988110026','557.666.777-88','cliente','1993-01-17','38700-026','Rua BambuÃ­, 33','Patos de Minas','MG'),
  ('a1000027-0000-0000-0000-000000000027','Wanderson Costa','wanderson.costa@gmail.com','34988110027','557.777.888-99','cliente','1981-11-09','38700-027','Av. ParanaÃ­ba, 600','Patos de Minas','MG'),
  ('a1000028-0000-0000-0000-000000000028','Karla Vasconcelos','karla.vasconcelos@gmail.com','34988110028','557.888.999-00','cliente','1995-07-23','38700-028','Rua Itamar Franco, 432','Patos de Minas','MG'),
  ('a1000029-0000-0000-0000-000000000029','Henrique OtÃ¡vio Lopes','henrique.lopes@gmail.com','34988110029','557.999.000-11','cliente','1986-04-16','38700-029','Av. Getulio Vargas, 750','Patos de Minas','MG'),
  ('a1000030-0000-0000-0000-000000000030','Tatiane Oliveira Cruz','tatiane.cruz@gmail.com','34988110030','557.000.111-22','cliente','1990-12-31','38700-030','Rua Buritizeiros, 65','Patos de Minas','MG');

-- =====================================================================
-- 2. VEHICLES â€” 20 carros no estoque WebCar
-- =====================================================================
insert into public.vehicles (id, marca, modelo, versao, ano_modelo, ano_fabricacao, cor, km, combustivel, cambio, placa, preco_venda, status, fotos, descricao, destaque, is_seminovo) values
  ('b0000001-0000-0000-0000-000000000001','Honda','Civic','EXL 2.0 CVT',2024,2024,'Prata',8500,'Flex','CVT','RWE2A11',162900,'disponivel',ARRAY['https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?w=800'],'Civic EXL 2024 impecÃ¡vel, Ãºnico dono, todas revisÃµes em concessionÃ¡ria.',true,true),
  ('b0000002-0000-0000-0000-000000000002','Toyota','Corolla','XEi 2.0',2023,2023,'Branco',22000,'Flex','CVT','RXY3C22',149900,'disponivel',ARRAY['https://images.unsplash.com/photo-1623869675781-80aa31012c78?w=800'],'Corolla XEi 2023, top de linha, multimÃ­dia, banco de couro.',true,true),
  ('b0000003-0000-0000-0000-000000000003','Volkswagen','T-Cross','Highline 200 TSI',2024,2023,'Cinza',15000,'Flex','Aut.','RZA7B33',152000,'disponivel',ARRAY['https://images.unsplash.com/photo-1606220838315-056192d5e927?w=800'],'T-Cross Highline 2024, teto solar, cockpit digital.',false,true),
  ('b0000004-0000-0000-0000-000000000004','Jeep','Compass','Limited T270',2023,2023,'Preto',31000,'Flex','Aut.','RAZ4D44',179900,'disponivel',ARRAY['https://images.unsplash.com/photo-1589638298538-bd80d92b21d6?w=800'],'Compass Limited 2023, completÃ­ssimo, 7 lugares opcional.',false,true),
  ('b0000005-0000-0000-0000-000000000005','Hyundai','HB20','Comfort Plus 1.0',2024,2024,'Vermelho',0,'Flex','Manual','RBC8E55',89900,'disponivel',ARRAY['https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=800'],'HB20 zero km, central multimÃ­dia, ar digital.',false,false),
  ('b0000006-0000-0000-0000-000000000006','Chevrolet','Onix Plus','LTZ 1.0 Turbo',2023,2023,'Prata',28000,'Flex','Aut.','RCA9F66',92500,'disponivel',ARRAY['https://images.unsplash.com/photo-1494976388531-d1058494cdd8?w=800'],'Onix Plus LTZ 2023, sedan completo.',false,true),
  ('b0000007-0000-0000-0000-000000000007','Nissan','Kicks','Exclusive',2023,2023,'Branco',24500,'Flex','CVT','RDX5G77',128000,'disponivel',ARRAY['https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800'],'Kicks Exclusive top de linha 2023.',false,true),
  ('b0000008-0000-0000-0000-000000000008','BYD','Seal','Premium AWD',2024,2024,'Azul',5000,'ElÃ©trico','Aut.','REL2H88',329900,'disponivel',ARRAY['https://images.unsplash.com/photo-1617788138017-80ad40651399?w=800'],'BYD Seal elÃ©trico top, autonomia 580km, 530cv.',true,false),
  ('b0000009-0000-0000-0000-000000000009','Fiat','Pulse','Impetus Turbo',2023,2023,'Cinza',19000,'Flex','CVT','RFP3I99',119900,'disponivel',ARRAY['https://images.unsplash.com/photo-1606664922998-f180dd5b6e6c?w=800'],'Fiat Pulse Impetus 2023, ADAS completo.',false,true),
  ('b0000010-0000-0000-0000-000000000010','Renault','Kwid','Outsider 1.0',2024,2024,'Verde',0,'Flex','Manual','RGW4J10',76900,'disponivel',ARRAY['https://images.unsplash.com/photo-1494905998402-395d579af36f?w=800'],'Kwid Outsider zero km.',false,false),
  ('b0000011-0000-0000-0000-000000000011','Ford','Ranger','XLT 3.2 4x4',2022,2022,'Preto',58000,'Diesel','Aut.','RHR5K11',229900,'disponivel',ARRAY['https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800'],'Ranger XLT 4x4 diesel, top de linha.',true,true),
  ('b0000012-0000-0000-0000-000000000012','Toyota','Hilux','SRX 2.8 4x4',2023,2023,'Prata',42000,'Diesel','Aut.','RIH6L22',319900,'disponivel',ARRAY['https://images.unsplash.com/photo-1571987502227-9231b837d92a?w=800'],'Hilux SRX 4x4 2023, top.',false,true),
  ('b0000013-0000-0000-0000-000000000013','Volkswagen','Polo','Highline 200 TSI',2024,2023,'Branco',12500,'Flex','Aut.','RJP7M33',102900,'disponivel',ARRAY['https://images.unsplash.com/photo-1592194996308-7b43878e84a6?w=800'],'Polo Highline 2024, completo.',false,true),
  ('b0000014-0000-0000-0000-000000000014','Hyundai','Creta','Limited 1.0 Turbo',2023,2023,'Cinza',26000,'Flex','Aut.','RKC8N44',141900,'disponivel',ARRAY['https://images.unsplash.com/photo-1614026480209-cdf68fbc8050?w=800'],'Creta Limited 2023, SUV completo.',false,true),
  ('b0000015-0000-0000-0000-000000000015','Honda','HR-V','Touring CVT',2023,2023,'Prata',35000,'Flex','CVT','RLV9O55',157900,'disponivel',ARRAY['https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?w=800'],'HR-V Touring 2023.',false,true),
  ('b0000016-0000-0000-0000-000000000016','Chevrolet','Tracker','Premier Turbo',2023,2023,'Vermelho',31000,'Flex','Aut.','RMT0P66',132900,'disponivel',ARRAY['https://images.unsplash.com/photo-1542362567-b07e54358753?w=800'],'Tracker Premier 2023.',false,true),
  ('b0000017-0000-0000-0000-000000000017','Fiat','Toro','Volcano 2.0 4x4',2023,2023,'Preto',38000,'Diesel','Aut.','RNT1Q77',189900,'disponivel',ARRAY['https://images.unsplash.com/photo-1612825173281-9a193378527e?w=800'],'Toro Volcano 4x4 diesel.',false,true),
  ('b0000018-0000-0000-0000-000000000018','Renault','Duster','Iconic 1.3 Turbo',2024,2023,'Branco',18000,'Flex','CVT','ROD2R88',128900,'disponivel',ARRAY['https://images.unsplash.com/photo-1606613566900-6d8b7e8e15a3?w=800'],'Duster Iconic 2024.',false,true),
  ('b0000019-0000-0000-0000-000000000019','Honda','City','Touring CVT',2024,2024,'Cinza',9500,'Flex','CVT','RPC3S99',128500,'disponivel',ARRAY['https://images.unsplash.com/photo-1606016159991-dfe4f2746ad5?w=800'],'City Touring 2024 sedan.',false,true),
  ('b0000020-0000-0000-0000-000000000020','BMW','320i','M Sport',2022,2022,'Preto',45000,'Gasolina','Aut.','RBM4T20',299900,'disponivel',ARRAY['https://images.unsplash.com/photo-1555215695-3004980ad54e?w=800'],'BMW 320i M Sport 2022, impecÃ¡vel.',true,true);

-- =====================================================================
-- 3. CLIENT_VEHICLES â€” carros vinculados aos segurados
-- =====================================================================
insert into public.client_vehicles (id, client_id, marca, modelo, versao, ano_modelo, placa, km_atual, cor, data_aquisicao, origem, proximo_ipva, proximo_licenciamento, proxima_revisao) values
  ('c0000001-0000-0000-0000-000000000001','a1000001-0000-0000-0000-000000000001','Honda','Civic','EXL',2022,'PMG1A22',45000,'Prata','2022-08-15','externo','2026-07-15','2026-08-31','2026-08-15'),
  ('c0000002-0000-0000-0000-000000000002','a1000002-0000-0000-0000-000000000002','Toyota','Corolla','XEi',2021,'PMG2B33',62000,'Branco','2021-05-10','externo','2026-05-10','2026-06-30','2026-09-10'),
  ('c0000003-0000-0000-0000-000000000003','a1000003-0000-0000-0000-000000000003','Fiat','Argo','Drive',2023,'PMG3C44',28000,'Vermelho','2023-02-20','webcar','2026-08-20','2026-08-31','2026-08-20'),
  ('c0000004-0000-0000-0000-000000000004','a1000004-0000-0000-0000-000000000004','Hyundai','HB20','Comfort',2022,'PMG4D55',39000,'Prata','2022-11-05','externo','2026-09-05','2026-08-31','2026-11-05'),
  ('c0000005-0000-0000-0000-000000000005','a1000005-0000-0000-0000-000000000005','Volkswagen','T-Cross','Highline',2023,'PMG5E66',32000,'Cinza','2023-03-12','webcar','2026-08-12','2026-08-31','2026-09-12'),
  ('c0000006-0000-0000-0000-000000000006','a1000006-0000-0000-0000-000000000006','Jeep','Renegade','Sport',2020,'PMG6F77',78000,'Verde','2020-09-08','externo','2026-06-08','2026-08-31','2026-09-08'),
  ('c0000007-0000-0000-0000-000000000007','a1000007-0000-0000-0000-000000000007','Honda','HR-V','EXL',2024,'PMG7G88',12000,'Preto','2024-01-20','webcar','2026-07-20','2026-08-31','2026-07-20'),
  ('c0000008-0000-0000-0000-000000000008','a1000008-0000-0000-0000-000000000008','Chevrolet','Onix','LT',2021,'PMG8H99',58000,'Branco','2021-07-25','externo','2026-08-25','2026-08-31','2026-07-25'),
  ('c0000009-0000-0000-0000-000000000009','a1000009-0000-0000-0000-000000000009','Toyota','Hilux','SRX',2022,'PMG9I00',55000,'Prata','2022-10-15','externo','2026-09-15','2026-08-31','2026-10-15'),
  ('c0000010-0000-0000-0000-000000000010','a1000010-0000-0000-0000-000000000010','Renault','Kwid','Zen',2023,'PMG0J11',22000,'Cinza','2023-04-18','webcar','2026-08-18','2026-08-31','2026-10-18'),
  ('c0000011-0000-0000-0000-000000000011','a1000011-0000-0000-0000-000000000011','Honda','City','EX',2023,'PMG1K22',18000,'Preto','2023-06-22','webcar','2026-08-22','2026-08-31','2026-09-22'),
  ('c0000012-0000-0000-0000-000000000012','a1000012-0000-0000-0000-000000000012','Fiat','Pulse','Drive',2024,'PMG2L33',8000,'Branco','2024-02-10','webcar','2026-07-10','2026-08-31','2026-08-10'),
  ('c0000013-0000-0000-0000-000000000013','a1000013-0000-0000-0000-000000000013','Volkswagen','Nivus','Highline',2022,'PMG3M44',42000,'Cinza','2022-12-05','externo','2026-08-05','2026-08-31','2026-12-05'),
  ('c0000014-0000-0000-0000-000000000014','a1000014-0000-0000-0000-000000000014','Hyundai','Creta','Limited',2023,'PMG4N55',26000,'Vermelho','2023-08-30','webcar','2026-09-30','2026-08-31','2026-08-30'),
  ('c0000015-0000-0000-0000-000000000015','a1000015-0000-0000-0000-000000000015','Toyota','Yaris','XL',2021,'PMG5O66',71000,'Prata','2021-04-14','externo','2026-09-14','2026-08-31','2026-10-14'),
  ('c0000016-0000-0000-0000-000000000016','a1000016-0000-0000-0000-000000000016','Honda','Civic','Touring',2024,'PMG6P77',5000,'Cinza','2024-03-25','webcar','2026-08-25','2026-08-31','2026-09-25'),
  ('c0000017-0000-0000-0000-000000000017','a1000017-0000-0000-0000-000000000017','Chevrolet','Tracker','Premier',2022,'PMG7Q88',45000,'Branco','2022-07-08','webcar','2026-09-08','2026-08-31','2026-08-08'),
  ('c0000018-0000-0000-0000-000000000018','a1000018-0000-0000-0000-000000000018','Renault','Duster','Iconic',2023,'PMG8R99',24000,'Preto','2023-05-19','webcar','2026-08-19','2026-08-31','2026-09-19'),
  ('c0000019-0000-0000-0000-000000000019','a1000019-0000-0000-0000-000000000019','Nissan','Kicks','Exclusive',2022,'PMG9S00',38000,'Verde','2022-08-02','externo','2026-08-02','2026-08-31','2026-08-02'),
  ('c0000020-0000-0000-0000-000000000020','a1000020-0000-0000-0000-000000000020','Honda','Fit','EX',2020,'PMG0T11',88000,'Branco','2020-11-12','externo','2026-09-12','2026-08-31','2026-11-12');

-- =====================================================================
-- 4. POLICIES â€” 25 apÃ³lices ativas (com vencimentos espaÃ§ados)
-- =====================================================================
insert into public.policies (client_id, client_vehicle_id, numero_apolice, seguradora, produto, valor_premio, valor_franquia, vigencia_inicio, vigencia_fim, status, coberturas, comissao_percentual, comissao_valor, responsavel_id) values
  ('a1000001-0000-0000-0000-000000000001','c0000001-0000-0000-0000-000000000001','APL-2025-0001','Porto Seguro','auto',3450.00,3500.00,'2025-08-15','2026-08-15','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":150000,"app":true,"carro_reserva":15}',15,517.50,'11111111-1111-1111-1111-111111111111'),
  ('a1000002-0000-0000-0000-000000000002','c0000002-0000-0000-0000-000000000002','APL-2025-0002','Bradesco Seguros','auto',2890.00,2800.00,'2025-09-10','2026-09-10','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":100000,"app":true,"carro_reserva":7}',12,346.80,'22222222-2222-2222-2222-222222222222'),
  ('a1000003-0000-0000-0000-000000000003','c0000003-0000-0000-0000-000000000003','APL-2025-0003','Allianz','auto',2150.00,2500.00,'2025-10-20','2026-10-20','ativa','{"colisao":true,"roubo":true,"terceiros":50000,"app":true}',15,322.50,'11111111-1111-1111-1111-111111111111'),
  ('a1000004-0000-0000-0000-000000000004','c0000004-0000-0000-0000-000000000004','APL-2025-0004','SulAmerica','auto',2380.00,2700.00,'2025-11-05','2026-11-05','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":100000,"app":true}',13,309.40,'22222222-2222-2222-2222-222222222222'),
  ('a1000005-0000-0000-0000-000000000005','c0000005-0000-0000-0000-000000000005','APL-2025-0005','Porto Seguro','auto',3100.00,3200.00,'2025-12-15','2026-12-15','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":200000,"app":true,"carro_reserva":15}',15,465.00,'11111111-1111-1111-1111-111111111111'),
  ('a1000006-0000-0000-0000-000000000006','c0000006-0000-0000-0000-000000000006','APL-2026-0006','Tokio Marine','auto',2750.00,3000.00,'2026-01-08','2027-01-08','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":100000,"app":true}',14,385.00,'22222222-2222-2222-2222-222222222222'),
  ('a1000007-0000-0000-0000-000000000007','c0000007-0000-0000-0000-000000000007','APL-2026-0007','HDI','auto',3590.00,4000.00,'2026-01-20','2027-01-20','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":150000,"app":true,"carro_reserva":15}',15,538.50,'11111111-1111-1111-1111-111111111111'),
  ('a1000008-0000-0000-0000-000000000008','c0000008-0000-0000-0000-000000000008','APL-2026-0008','Mapfre','auto',2120.00,2500.00,'2026-02-25','2027-02-25','ativa','{"colisao":true,"roubo":true,"terceiros":50000,"app":true}',12,254.40,'22222222-2222-2222-2222-222222222222'),
  ('a1000009-0000-0000-0000-000000000009','c0000009-0000-0000-0000-000000000009','APL-2026-0009','Porto Seguro','auto',4250.00,5000.00,'2026-03-15','2027-03-15','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":300000,"app":true,"carro_reserva":30}',15,637.50,'11111111-1111-1111-1111-111111111111'),
  ('a1000010-0000-0000-0000-000000000010','c0000010-0000-0000-0000-000000000010','APL-2026-0010','Bradesco Seguros','auto',1890.00,2000.00,'2026-04-18','2027-04-18','ativa','{"colisao":true,"roubo":true,"terceiros":50000,"app":true}',12,226.80,'22222222-2222-2222-2222-222222222222'),
  ('a1000011-0000-0000-0000-000000000011','c0000011-0000-0000-0000-000000000011','APL-2025-0011','Allianz','auto',2890.00,2800.00,'2025-06-22','2026-06-22','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":100000,"app":true}',13,375.70,'11111111-1111-1111-1111-111111111111'),
  ('a1000012-0000-0000-0000-000000000012','c0000012-0000-0000-0000-000000000012','APL-2025-0012','Porto Seguro','auto',2450.00,2500.00,'2025-07-10','2026-07-10','em_renovacao','{"colisao":true,"roubo":true,"terceiros":100000,"app":true}',15,367.50,'11111111-1111-1111-1111-111111111111'),
  ('a1000013-0000-0000-0000-000000000013','c0000013-0000-0000-0000-000000000013','APL-2025-0013','SulAmerica','auto',2950.00,3000.00,'2025-09-05','2026-09-05','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":150000,"app":true,"carro_reserva":15}',13,383.50,'22222222-2222-2222-2222-222222222222'),
  ('a1000014-0000-0000-0000-000000000014','c0000014-0000-0000-0000-000000000014','APL-2025-0014','Porto Seguro','auto',3290.00,3500.00,'2025-10-30','2026-10-30','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":200000,"app":true,"carro_reserva":15}',15,493.50,'11111111-1111-1111-1111-111111111111'),
  ('a1000015-0000-0000-0000-000000000015','c0000015-0000-0000-0000-000000000015','APL-2025-0015','Bradesco Seguros','auto',1750.00,1800.00,'2025-08-25','2026-08-25','em_renovacao','{"colisao":true,"roubo":true,"terceiros":50000,"app":true}',12,210.00,'22222222-2222-2222-2222-222222222222'),
  ('a1000016-0000-0000-0000-000000000016','c0000016-0000-0000-0000-000000000016','APL-2026-0016','Porto Seguro','auto',3850.00,4000.00,'2026-04-25','2027-04-25','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":250000,"app":true,"carro_reserva":30}',15,577.50,'11111111-1111-1111-1111-111111111111'),
  ('a1000017-0000-0000-0000-000000000017','c0000017-0000-0000-0000-000000000017','APL-2025-0017','Tokio Marine','auto',2390.00,2500.00,'2025-08-08','2026-08-08','em_renovacao','{"colisao":true,"roubo":true,"terceiros":100000,"app":true}',14,334.60,'22222222-2222-2222-2222-222222222222'),
  ('a1000018-0000-0000-0000-000000000018','c0000018-0000-0000-0000-000000000018','APL-2025-0018','HDI','auto',2890.00,3000.00,'2025-09-19','2026-09-19','ativa','{"colisao":true,"roubo":true,"natureza":true,"terceiros":150000,"app":true}',15,433.50,'11111111-1111-1111-1111-111111111111'),
  ('a1000019-0000-0000-0000-000000000019','c0000019-0000-0000-0000-000000000019','APL-2025-0019','Mapfre','auto',2150.00,2500.00,'2025-09-02','2026-09-02','ativa','{"colisao":true,"roubo":true,"terceiros":50000,"app":true}',12,258.00,'22222222-2222-2222-2222-222222222222'),
  ('a1000020-0000-0000-0000-000000000020','c0000020-0000-0000-0000-000000000020','APL-2025-0020','Bradesco Seguros','auto',1450.00,1500.00,'2025-12-12','2026-12-12','ativa','{"colisao":true,"roubo":true,"terceiros":50000,"app":true}',12,174.00,'22222222-2222-2222-2222-222222222222'),
  -- ApÃ³lices residenciais e vida pra mostrar multi-produto
  ('a1000001-0000-0000-0000-000000000001',null,'APL-RES-0001','Porto Seguro','residencial',1200.00,500.00,'2025-08-15','2026-08-15','ativa','{"incendio":true,"roubo":true,"natureza":true,"eletrico":true}',20,240.00,'11111111-1111-1111-1111-111111111111'),
  ('a1000005-0000-0000-0000-000000000005',null,'APL-VIDA-0005','SulAmerica','vida',890.00,null,'2025-12-15','2026-12-15','ativa','{"morte":300000,"invalidez":300000,"doencas_graves":150000}',25,222.50,'11111111-1111-1111-1111-111111111111'),
  ('a1000009-0000-0000-0000-000000000009',null,'APL-RES-0009','Bradesco','residencial',1650.00,750.00,'2026-03-15','2027-03-15','ativa','{"incendio":true,"roubo":true,"natureza":true}',20,330.00,'22222222-2222-2222-2222-222222222222'),
  ('a1000016-0000-0000-0000-000000000016',null,'APL-VIDA-0016','Porto Seguro','vida',1290.00,null,'2026-04-25','2027-04-25','ativa','{"morte":500000,"invalidez":500000}',25,322.50,'11111111-1111-1111-1111-111111111111'),
  ('a1000021-0000-0000-0000-000000000021',null,'APL-EMP-0021','Porto Seguro','empresarial',4500.00,3000.00,'2025-09-01','2026-09-01','ativa','{"incendio":true,"roubo":true,"responsabilidade_civil":500000,"interrupcao":100000}',18,810.00,'11111111-1111-1111-1111-111111111111');

-- =====================================================================
-- 5. CLAIMS â€” sinistros em vÃ¡rios estados
-- =====================================================================
insert into public.claims (policy_id, client_id, numero_sinistro, tipo, data_ocorrencia, local_ocorrencia, geolocalizacao, descricao, status, oficina, valor_estimado, valor_aprovado, timeline, responsavel_id, ai_fraud_score) values
  ((select id from public.policies where numero_apolice='APL-2025-0001'),'a1000001-0000-0000-0000-000000000001','SIN-2026-0001','colisao','2026-04-12 14:30:00','Av. JK com Av. Brasil, Patos de Minas/MG','{"lat":-18.5783,"lng":-46.5141}','ColisÃ£o traseira em semÃ¡foro. Outro veÃ­culo bateu na traseira.','em_analise','Auto Center Premium',8500.00,null,'[{"data":"2026-04-12 15:00","evento":"Sinistro aberto pelo app","autor":"Cliente"},{"data":"2026-04-12 15:05","evento":"IA gerou dossiÃª preliminar","autor":"WebHub IA"},{"data":"2026-04-13 09:00","evento":"DocumentaÃ§Ã£o enviada Ã  Porto Seguro","autor":"Camila Andrade"},{"data":"2026-04-15 11:30","evento":"Vistoria agendada","autor":"Porto Seguro"},{"data":"2026-04-18 14:00","evento":"Vistoria realizada","autor":"Vistoriador Porto"}]'::jsonb,'11111111-1111-1111-1111-111111111111',8),
  ((select id from public.policies where numero_apolice='APL-2025-0003'),'a1000003-0000-0000-0000-000000000003','SIN-2026-0002','vidros','2026-04-25 09:15:00','Rua Major Gote, Patos de Minas/MG','{"lat":-18.5810,"lng":-46.5180}','Para-brisa trincado por pedra na BR-365.','aprovado','Carglass Patos',1200.00,1200.00,'[{"data":"2026-04-25 09:30","evento":"Sinistro aberto","autor":"Cliente"},{"data":"2026-04-25 11:00","evento":"AprovaÃ§Ã£o automÃ¡tica","autor":"Allianz"},{"data":"2026-04-26 14:00","evento":"Reparo agendado Carglass","autor":"Sistema"}]'::jsonb,'11111111-1111-1111-1111-111111111111',5),
  ((select id from public.policies where numero_apolice='APL-2025-0007'),'a1000007-0000-0000-0000-000000000007','SIN-2026-0003','colisao','2026-05-01 18:45:00','Av. ParanaÃ­ba, Patos de Minas/MG','{"lat":-18.5760,"lng":-46.5100}','Cliente bateu lateralmente em poste tentando estacionar.','aberto','Funilaria Web',12500.00,null,'[{"data":"2026-05-01 19:00","evento":"Sinistro aberto via botÃ£o de pÃ¢nico","autor":"Cliente"},{"data":"2026-05-01 19:02","evento":"IA fez triagem inicial e gerou dossiÃª","autor":"WebHub IA"},{"data":"2026-05-02 08:00","evento":"Aguardando vistoria","autor":"HDI"}]'::jsonb,'11111111-1111-1111-1111-111111111111',12),
  ((select id from public.policies where numero_apolice='APL-2025-0013'),'a1000013-0000-0000-0000-000000000013','SIN-2026-0004','roubo','2026-04-20 02:30:00','Rua Lagoa Grande, Patos de Minas/MG','{"lat":-18.5840,"lng":-46.5220}','VeÃ­culo subtraÃ­do na rua durante a madrugada. B.O. registrado.','em_analise','-',null,null,'[{"data":"2026-04-20 03:00","evento":"Sinistro aberto","autor":"Cliente"},{"data":"2026-04-20 08:00","evento":"B.O. anexado","autor":"Cliente"},{"data":"2026-04-21 10:00","evento":"AnÃ¡lise iniciada","autor":"SulAmerica"},{"data":"2026-04-25 14:00","evento":"Aguardando 30 dias para indenizaÃ§Ã£o","autor":"SulAmerica"}]'::jsonb,'22222222-2222-2222-2222-222222222222',15),
  ((select id from public.policies where numero_apolice='APL-2026-0009'),'a1000009-0000-0000-0000-000000000009','SIN-2026-0005','natureza','2026-03-28 16:00:00','BR-365 Km 234','{"lat":-18.5900,"lng":-46.5300}','Granizo em viagem. MÃºltiplos amassados na lataria.','pago','Auto Center Premium',7800.00,7800.00,'[{"data":"2026-03-28 16:30","evento":"Sinistro aberto","autor":"Cliente"},{"data":"2026-03-30 09:00","evento":"Vistoria realizada","autor":"Porto Seguro"},{"data":"2026-04-05 14:00","evento":"Aprovado","autor":"Porto Seguro"},{"data":"2026-04-15 10:00","evento":"Reparo concluÃ­do","autor":"Auto Center Premium"},{"data":"2026-04-20 11:00","evento":"Sinistro pago e encerrado","autor":"Sistema"}]'::jsonb,'11111111-1111-1111-1111-111111111111',6);

-- =====================================================================
-- 6. CAR_SALES â€” 12 vendas WebCar em vÃ¡rios estÃ¡gios
-- =====================================================================
insert into public.car_sales (vehicle_id, client_id, client_full_name, client_cpf, client_phone, client_email, vendedor_id, preco_negociado, forma_pagamento, entrada, financeira, parcelas, valor_parcela, taxa_juros, status_credito, etapa_atual, observacoes) values
  ('b0000001-0000-0000-0000-000000000001','a1000016-0000-0000-0000-000000000016','Beatriz Helena Pacheco','556.666.777-88','34988110016','beatriz.pacheco@gmail.com','33333333-3333-3333-3333-333333333333',158000,'financiado',40000,'AymorÃ©',48,3450.00,1.49,'aprovado','contrato','Cliente jÃ¡ fechou. Aguardando assinatura.'),
  ('b0000002-0000-0000-0000-000000000002','a1000007-0000-0000-0000-000000000007','Marcos Vinicius Rodrigues','555.777.888-99','34988110007','marcos.rodrigues@gmail.com','44444444-4444-4444-4444-444444444444',145000,'financiado',35000,'BV Financeira',60,2890.00,1.59,'aprovado','entrega','Entrega marcada pra prÃ³xima quinta.'),
  ('b0000003-0000-0000-0000-000000000003','a1000003-0000-0000-0000-000000000003','Carlos Eduardo Santos','555.333.444-55','34988110003','carlos.santos@hotmail.com','33333333-3333-3333-3333-333333333333',148000,'misto',60000,'ItaÃº',36,3120.00,1.39,'em_analise','credito','CrÃ©dito enviado, aguardando retorno do banco.'),
  ('b0000004-0000-0000-0000-000000000004',null,'Helena Carvalho Silva','444.123.456-78','34988111111','helena@gmail.com','44444444-4444-4444-4444-444444444444',175000,'financiado',45000,'Santander',48,3690.00,1.55,'enviado','credito','Cliente nova, primeiro contato via Instagram.'),
  ('b0000005-0000-0000-0000-000000000005',null,'Luiz OtÃ¡vio Mendes','333.222.111-09','34988122222','luiz.mendes@gmail.com','33333333-3333-3333-3333-333333333333',88500,null,null,null,null,null,null,'nao_iniciado','test_drive','Cliente fez test drive, gostou. Vai pensar.'),
  ('b0000006-0000-0000-0000-000000000006',null,'Camila Aparecida Souza','222.333.444-55','34988133333','camila.souza@gmail.com','44444444-4444-4444-4444-444444444444',91000,'financiado',25000,null,null,null,null,'nao_iniciado','proposta','Proposta enviada, aguardando decisÃ£o.'),
  ('b0000008-0000-0000-0000-000000000008',null,'Augusto Pereira Costa','111.444.555-66','34988144444','augusto.costa@gmail.com','33333333-3333-3333-3333-333333333333',325000,'avista',325000,null,null,null,null,'nao_iniciado','lead','Cliente VIP, tem interesse no Seal elÃ©trico.'),
  ('b0000009-0000-0000-0000-000000000009',null,'Renata Vieira Lopes','999.888.777-66','34988155555','renata.vieira@gmail.com','44444444-4444-4444-4444-444444444444',118000,'financiado',30000,'AymorÃ©',48,2280.00,1.45,'aprovado','contrato','Pulse Impetus aprovado, em geraÃ§Ã£o de contrato.'),
  ('b0000011-0000-0000-0000-000000000011','a1000019-0000-0000-0000-000000000019','Felipe Augusto Castro','556.999.000-11','34988110019','felipe.castro@gmail.com','33333333-3333-3333-3333-333333333333',225000,'financiado',60000,'BV Financeira',60,3950.00,1.65,'aprovado','concluida','Venda concluÃ­da, entrega feita.'),
  ('b0000014-0000-0000-0000-000000000014',null,'Marina Ribeiro Coutinho','888.777.666-55','34988166666','marina.r@gmail.com','44444444-4444-4444-4444-444444444444',138000,'financiado',38000,null,null,null,null,'nao_iniciado','proposta','Cliente quer ver o Creta vs Tracker.'),
  ('b0000015-0000-0000-0000-000000000015',null,'Eduardo Henrique Reis','777.666.555-44','34988177777','eduardo.r@gmail.com','33333333-3333-3333-3333-333333333333',155000,'misto',55000,'ItaÃº',36,3290.00,1.42,'aprovado','contrato','HR-V aprovado, gerar contrato.'),
  ('b0000019-0000-0000-0000-000000000019',null,'Patricia Santos Lima','666.555.444-33','34988188888','patricia.l@gmail.com','44444444-4444-4444-4444-444444444444',125000,'financiado',30000,'Santander',48,2580.00,1.49,'em_analise','credito','City Touring, crÃ©dito em anÃ¡lise no Santander.');

-- =====================================================================
-- 7. LEADS â€” 40 leads em vÃ¡rios estados
-- =====================================================================
insert into public.leads (full_name, phone, email, cpf, origem, produto_interesse, vehicle_interest_id, observacoes, status, responsavel_id, ai_score) values
  -- Leads novos (do dia)
  ('Mariana Pereira Souza','34999000001','mariana.s@gmail.com',null,'instagram','auto',null,'Quero cotar seguro auto. Civic 2024.','novo','11111111-1111-1111-1111-111111111111',75),
  ('Ricardo Mello Mendes','34999000002','ricardo.m@gmail.com',null,'site','auto',null,'CotaÃ§Ã£o para Toyota Corolla 2023.','novo','22222222-2222-2222-2222-222222222222',68),
  ('Beatriz Castro','34999000003',null,null,'whatsapp','residencial',null,'Quero seguro pra casa nova.','novo','11111111-1111-1111-1111-111111111111',55),
  ('Henrique Lopes','34999000004','henrique.l@gmail.com',null,'instagram','carro_novo','b0000003-0000-0000-0000-000000000003','Tenho interesse no T-Cross.','novo','33333333-3333-3333-3333-333333333333',82),
  ('Vanessa Almeida','34999000005','vanessa.a@gmail.com',null,'walk_in','carro_usado','b0000007-0000-0000-0000-000000000007','Veio na loja olhar o Kicks.','novo','44444444-4444-4444-4444-444444444444',71),
  -- Leads em contato
  ('Pedro Augusto Silva','34999000006','pedro.a.silva@gmail.com',null,'google_ads','auto',null,'Pediu cotaÃ§Ã£o online.','contato','11111111-1111-1111-1111-111111111111',65),
  ('LetÃ­cia Carvalho','34999000007','leticia.c@gmail.com',null,'meta_ads','auto',null,'AnÃºncio Instagram.','contato','22222222-2222-2222-2222-222222222222',58),
  ('Fabiano Reis','34999000008',null,null,'indicacao','auto',null,'Indicado pela Maria Costa.','contato','11111111-1111-1111-1111-111111111111',88),
  ('Carolina Moura','34999000009','carolina.m@gmail.com',null,'site','vida',null,'Seguro de vida familiar.','contato','22222222-2222-2222-2222-222222222222',62),
  -- CotaÃ§Ã£o enviada
  ('Eduardo Lima','34999000010','eduardo.l@gmail.com',null,'instagram','auto',null,'Civic 2022.','cotacao_enviada','11111111-1111-1111-1111-111111111111',72),
  ('Sandra Vieira','34999000011','sandra.v@gmail.com',null,'site','residencial',null,'Apartamento centro.','cotacao_enviada','22222222-2222-2222-2222-222222222222',68),
  ('Roberto Nunes','34999000012','roberto.n@gmail.com',null,'walk_in','carro_novo','b0000004-0000-0000-0000-000000000004','Compass Limited, fechando proposta.','cotacao_enviada','33333333-3333-3333-3333-333333333333',91),
  -- Em negociaÃ§Ã£o
  ('Patricia Mendes Castro','34999000013','patricia.mc@gmail.com',null,'webcar','auto',null,'Comprou Pulse, quer seguro.','em_negociacao','11111111-1111-1111-1111-111111111111',95),
  ('Lucas Henrique Pinto','34999000014','lucas.h@gmail.com',null,'webcar','auto',null,'Comprou HR-V, quer seguro.','em_negociacao','22222222-2222-2222-2222-222222222222',92),
  -- Fechados
  ('Tiago Borges Souza','34999000015','tiago.b@gmail.com',null,'indicacao','auto',null,'Fechou apÃ³lice Porto.','fechado','11111111-1111-1111-1111-111111111111',98),
  ('Renata Cristina Alves','34999000016','renata.c@gmail.com',null,'site','auto',null,'Fechou Bradesco.','fechado','22222222-2222-2222-2222-222222222222',95),
  -- Perdidos
  ('Marcelo Augusto','34999000017','marcelo.a@gmail.com',null,'google_ads','auto',null,'Achou outro mais barato.','perdido','11111111-1111-1111-1111-111111111111',30),
  ('Juliana Pacheco','34999000018','juliana.p@gmail.com',null,'instagram','auto',null,'Decidiu nÃ£o fazer agora.','perdido','22222222-2222-2222-2222-222222222222',25);

-- =====================================================================
-- 8. PAYMENTS â€” parcelas e cobranÃ§as
-- =====================================================================
insert into public.payments (client_id, policy_id, tipo, valor, metodo, status, vencimento, data_pagamento, parcela_atual, parcela_total) values
  ('a1000001-0000-0000-0000-000000000001',(select id from public.policies where numero_apolice='APL-2025-0001'),'parcela_seguro',287.50,'cartao','pago','2026-04-15','2026-04-15',8,12),
  ('a1000001-0000-0000-0000-000000000001',(select id from public.policies where numero_apolice='APL-2025-0001'),'parcela_seguro',287.50,'cartao','pendente','2026-05-15',null,9,12),
  ('a1000002-0000-0000-0000-000000000002',(select id from public.policies where numero_apolice='APL-2025-0002'),'parcela_seguro',240.83,'boleto','pago','2026-04-10','2026-04-09',7,12),
  ('a1000002-0000-0000-0000-000000000002',(select id from public.policies where numero_apolice='APL-2025-0002'),'parcela_seguro',240.83,'boleto','atrasado','2026-05-10',null,8,12),
  ('a1000005-0000-0000-0000-000000000005',(select id from public.policies where numero_apolice='APL-2025-0005'),'parcela_seguro',258.33,'pix','pago','2026-04-15','2026-04-14',5,12),
  ('a1000005-0000-0000-0000-000000000005',(select id from public.policies where numero_apolice='APL-2025-0005'),'parcela_seguro',258.33,'pix','pendente','2026-05-15',null,6,12),
  ('a1000007-0000-0000-0000-000000000007',(select id from public.policies where numero_apolice='APL-2026-0007'),'parcela_seguro',299.17,'cartao','pago','2026-04-20','2026-04-19',4,12),
  ('a1000007-0000-0000-0000-000000000007',(select id from public.policies where numero_apolice='APL-2026-0007'),'parcela_seguro',299.17,'cartao','pendente','2026-05-20',null,5,12),
  ('a1000009-0000-0000-0000-000000000009',(select id from public.policies where numero_apolice='APL-2026-0009'),'parcela_seguro',354.17,'debito_automatico','pago','2026-04-15','2026-04-15',2,12),
  ('a1000016-0000-0000-0000-000000000016',(select id from public.policies where numero_apolice='APL-2026-0016'),'parcela_seguro',320.83,'cartao','pago','2026-04-25','2026-04-25',1,12);

-- =====================================================================
-- 9. COMMISSIONS â€” comissÃµes previstas e pagas
-- =====================================================================
insert into public.commissions (policy_id, beneficiario_id, tipo, valor, percentual, status, data_prevista, data_pagamento) values
  ((select id from public.policies where numero_apolice='APL-2025-0001'),'11111111-1111-1111-1111-111111111111','seguro_inicial',517.50,15,'paga','2025-09-15','2025-09-30'),
  ((select id from public.policies where numero_apolice='APL-2025-0002'),'22222222-2222-2222-2222-222222222222','seguro_inicial',346.80,12,'paga','2025-10-10','2025-10-31'),
  ((select id from public.policies where numero_apolice='APL-2025-0005'),'11111111-1111-1111-1111-111111111111','seguro_inicial',465.00,15,'paga','2026-01-15','2026-01-31'),
  ((select id from public.policies where numero_apolice='APL-2026-0007'),'11111111-1111-1111-1111-111111111111','seguro_inicial',538.50,15,'paga','2026-02-20','2026-02-28'),
  ((select id from public.policies where numero_apolice='APL-2026-0009'),'11111111-1111-1111-1111-111111111111','seguro_inicial',637.50,15,'paga','2026-04-15','2026-04-30'),
  ((select id from public.policies where numero_apolice='APL-2026-0016'),'11111111-1111-1111-1111-111111111111','seguro_inicial',577.50,15,'prevista','2026-05-25',null),
  ((select id from public.policies where numero_apolice='APL-RES-0001'),'11111111-1111-1111-1111-111111111111','seguro_inicial',240.00,20,'paga','2025-09-15','2025-09-30'),
  ((select id from public.policies where numero_apolice='APL-VIDA-0005'),'11111111-1111-1111-1111-111111111111','seguro_inicial',222.50,25,'paga','2026-01-15','2026-01-31');

insert into public.commissions (car_sale_id, beneficiario_id, tipo, valor, percentual, status, data_prevista, data_pagamento)
select id, vendedor_id, 'venda_carro', preco_negociado * 0.025, 2.5, 'paga', '2026-03-15', '2026-03-31'
from public.car_sales where etapa_atual = 'concluida';

-- =====================================================================
-- 10. NOTIFICATIONS â€” notificaÃ§Ãµes pra cada perfil
-- =====================================================================
insert into public.notifications (user_id, titulo, mensagem, tipo, prioridade, lida) values
  ('11111111-1111-1111-1111-111111111111','3 renovaÃ§Ãµes nos prÃ³ximos 30 dias','ApÃ³lices APL-2025-0001, 0011, 0014 vencem em breve','renovacao','alta',false),
  ('11111111-1111-1111-1111-111111111111','Novo lead: Mariana Pereira','Quer cotar Civic 2024 â€” origem Instagram','lead','normal',false),
  ('11111111-1111-1111-1111-111111111111','ðŸ”¥ Cross-sell WebCar','Beatriz comprou Civic. CotaÃ§Ã£o automÃ¡tica gerada.','cross_sell','alta',false),
  ('22222222-2222-2222-2222-222222222222','2 sinistros aguardando aÃ§Ã£o','Sinistros 0001 e 0004 precisam de retorno','sinistro','alta',false),
  ('22222222-2222-2222-2222-222222222222','Pagamento em atraso','Maria Costa - 5 dias atrasado','pagamento','normal',false),
  ('33333333-3333-3333-3333-333333333333','CrÃ©dito aprovado','Beatriz - financiamento AymorÃ© aprovado','venda','alta',false),
  ('33333333-3333-3333-3333-333333333333','Test drive agendado','Luiz OtÃ¡vio amanhÃ£ 14h','venda','normal',false),
  ('44444444-4444-4444-4444-444444444444','Entrega marcada','Marcos Vinicius - quinta-feira 10h','venda','alta',false);

-- =====================================================================
-- 11. ACTIVITIES â€” timeline de eventos
-- =====================================================================
insert into public.activities (user_id, related_type, related_id, tipo, titulo, descricao) values
  ('11111111-1111-1111-1111-111111111111','lead',(select id from public.leads where full_name='Mariana Pereira Souza' limit 1),'criou','Lead criado via Instagram','Mariana entrou pelo DM'),
  ('11111111-1111-1111-1111-111111111111','lead',(select id from public.leads where full_name='Pedro Augusto Silva' limit 1),'enviou_msg','Mensagem enviada','CotaÃ§Ã£o enviada via WhatsApp'),
  ('11111111-1111-1111-1111-111111111111','policy',(select id from public.policies where numero_apolice='APL-2026-0016'),'criou','ApÃ³lice fechada','Beatriz - Honda Civic 2024 - Porto Seguro'),
  ('33333333-3333-3333-3333-333333333333','car_sale',(select id from public.car_sales where client_full_name='Beatriz Helena Pacheco' limit 1),'criou','Venda fechada WebCar','Civic EXL 2024 financiado AymorÃ©'),
  ('33333333-3333-3333-3333-333333333333','car_sale',(select id from public.car_sales where client_full_name='Beatriz Helena Pacheco' limit 1),'cross_sell','Cross-sell automÃ¡tico Webseg','CotaÃ§Ã£o de seguro gerada automaticamente'),
  ('22222222-2222-2222-2222-222222222222','claim',(select id from public.claims where numero_sinistro='SIN-2026-0004'),'atualizou','Sinistro em anÃ¡lise','Aguardando 30 dias para indenizaÃ§Ã£o de roubo'),
  ('11111111-1111-1111-1111-111111111111','claim',(select id from public.claims where numero_sinistro='SIN-2026-0005'),'atualizou','Sinistro pago','R$ 7.800 transferido cliente Roberto Carlos');

-- =====================================================================
-- 12. MESSAGES â€” conversas WhatsApp mock
-- =====================================================================
insert into public.messages (client_id, conversation_id, from_role, from_user_id, conteudo, tipo) values
  ('a1000001-0000-0000-0000-000000000001','aaaa1111-0000-0000-0000-000000000001','cliente',null,'Bom dia! Preciso fazer a renovaÃ§Ã£o do meu Civic.','texto'),
  ('a1000001-0000-0000-0000-000000000001','aaaa1111-0000-0000-0000-000000000001','corretor','11111111-1111-1111-1111-111111111111','Bom dia JoÃ£o! Vou cotar agora pra vocÃª. Algum detalhe mudou desde o ano passado? KM, endereÃ§o?','texto'),
  ('a1000001-0000-0000-0000-000000000001','aaaa1111-0000-0000-0000-000000000001','cliente',null,'NÃ£o, tudo igual. Apenas mais 12.000 km rodados.','texto'),
  ('a1000001-0000-0000-0000-000000000001','aaaa1111-0000-0000-0000-000000000001','corretor','11111111-1111-1111-1111-111111111111','Perfeito. Em 1h te mando 5 cotaÃ§Ãµes pra escolher.','texto'),
  ('a1000007-0000-0000-0000-000000000007','aaaa2222-0000-0000-0000-000000000002','cliente',null,'Bati o carro agora! O que faÃ§o?','texto'),
  ('a1000007-0000-0000-0000-000000000007','aaaa2222-0000-0000-0000-000000000002','ai',null,'Marcos, primeiro: vocÃª estÃ¡ bem? Toque ''SIM'' se ninguÃ©m se machucou. JÃ¡ estou abrindo o sinistro pra vocÃª.','texto'),
  ('a1000007-0000-0000-0000-000000000007','aaaa2222-0000-0000-0000-000000000002','cliente',null,'SIM, todo mundo bem.','texto'),
  ('a1000007-0000-0000-0000-000000000007','aaaa2222-0000-0000-0000-000000000002','ai',null,'Ã“timo. Agora abra a cÃ¢mera no app e siga os passos. Vou te guiar foto a foto. A Camila jÃ¡ foi notificada.','texto');

-- =====================================================================
-- 13. INDICATIONS â€” programa de indicaÃ§Ã£o simples
-- =====================================================================
insert into public.indications (indicador_id, indicado_nome, indicado_telefone, produto, status, cashback_valor, cashback_status) values
  ('a1000001-0000-0000-0000-000000000001','Carlos Vizinho','34988999001','auto','convertido',150.00,'liberado'),
  ('a1000005-0000-0000-0000-000000000005','Cunhada Marina','34988999002','residencial','pendente',null,'pendente'),
  ('a1000009-0000-0000-0000-000000000009','SÃ³cio JosÃ©','34988999003','empresarial','convertido',300.00,'pago');

-- =====================================================================
-- 14. DRIVE_SCORES â€” pontuaÃ§Ã£o telemetria Ãºltimos meses
-- =====================================================================
insert into public.drive_scores (client_id, client_vehicle_id, periodo, score, km_total, freadas_bruscas, aceleracoes_bruscas, velocidade_max, horario_madrugada_pct, desconto_percentual) values
  ('a1000001-0000-0000-0000-000000000001','c0000001-0000-0000-0000-000000000001','2026-04',87,1250,3,5,118,2,8),
  ('a1000001-0000-0000-0000-000000000001','c0000001-0000-0000-0000-000000000001','2026-03',82,1180,5,8,125,5,6),
  ('a1000001-0000-0000-0000-000000000001','c0000001-0000-0000-0000-000000000001','2026-02',79,1320,7,10,130,8,5),
  ('a1000005-0000-0000-0000-000000000005','c0000005-0000-0000-0000-000000000005','2026-04',92,980,2,3,110,1,12),
  ('a1000007-0000-0000-0000-000000000007','c0000007-0000-0000-0000-000000000007','2026-04',75,1450,8,12,135,10,4);

-- =====================================================================
-- 15. DOCUMENTS â€” alguns documentos no cofre
-- =====================================================================
insert into public.documents (client_id, tipo, nome, url, validade) values
  ('a1000001-0000-0000-0000-000000000001','cnh','CNH JoÃ£o Pereira.pdf','https://storage.demo/cnh-joao.pdf','2028-04-12'),
  ('a1000001-0000-0000-0000-000000000001','crlv','CRLV Civic 2022.pdf','https://storage.demo/crlv-civic.pdf','2026-12-31'),
  ('a1000001-0000-0000-0000-000000000001','apolice','ApÃ³lice Porto Seguro 2025-2026.pdf','https://storage.demo/apolice-001.pdf','2026-08-15'),
  ('a1000005-0000-0000-0000-000000000005','cnh','CNH Pedro Almeida.pdf','https://storage.demo/cnh-pedro.pdf','2027-02-08'),
  ('a1000005-0000-0000-0000-000000000005','crlv','CRLV T-Cross 2023.pdf','https://storage.demo/crlv-tcross.pdf','2026-12-31');

-- DONE â€” seed completo

````

---

## 🗄️ SQL 3 — DEMO CLAIM
````sql
-- =====================================================================
-- WEBHUB DEMO â€” DEMO ACCOUNT CLAIM
-- Rode DEPOIS de criar os 4 usuÃ¡rios de demo no Supabase Auth UI:
--
--   1. cliente@webhub.demo  â†’ senha: demo123
--   2. corretor@webhub.demo â†’ senha: demo123
--   3. vendedor@webhub.demo â†’ senha: demo123
--   4. admin@webhub.demo    â†’ senha: demo123
--
-- Como criar:
--   Supabase Dashboard â†’ Authentication â†’ Users â†’ Add User â†’ Create new user
--   (desmarque "Send email invite", marque "Auto-confirm user")
--
-- Esse SQL atualiza os roles e dÃ¡ ao "cliente@webhub.demo" um perfil rico em dados
-- (toda a base do JoÃ£o Pereira Silva passa pra ele).
-- =====================================================================

-- 1. Atualiza role dos 3 perfis staff
update public.profiles set
  role = 'corretor',
  full_name = 'Camila Andrade',
  phone = '34999110011',
  cpf = '111.222.333-44',
  cidade = 'Patos de Minas',
  estado = 'MG'
where email = 'corretor@webhub.demo';

update public.profiles set
  role = 'vendedor',
  full_name = 'Diego Vendas',
  phone = '34999330033',
  cpf = '333.444.555-66',
  cidade = 'Patos de Minas',
  estado = 'MG'
where email = 'vendedor@webhub.demo';

update public.profiles set
  role = 'admin',
  full_name = 'Wilson (Dono)',
  phone = '34999990000',
  cpf = '999.888.777-66',
  cidade = 'Patos de Minas',
  estado = 'MG'
where email = 'admin@webhub.demo';

-- 2. Pegamos o UUID real do auth user "cliente@webhub.demo"
--    e re-apontamos todos os dados do "JoÃ£o Pereira Silva" pra ele
do $$
declare
  v_demo_client_id uuid;
  v_old_client_id uuid := 'a1000001-0000-0000-0000-000000000001';
begin
  select id into v_demo_client_id from public.profiles where email = 'cliente@webhub.demo';

  if v_demo_client_id is null then
    raise exception 'Crie o usuÃ¡rio cliente@webhub.demo no Supabase Auth primeiro!';
  end if;

  -- Atualiza o profile do demo client com dados ricos
  update public.profiles set
    full_name = 'JoÃ£o Pereira Silva',
    phone = '34988110001',
    cpf = '555.111.222-33',
    role = 'cliente',
    data_nascimento = '1985-04-12',
    cep = '38700-001',
    endereco = 'Rua das Flores, 123',
    cidade = 'Patos de Minas',
    estado = 'MG'
  where id = v_demo_client_id;

  -- Re-aponta dados do JoÃ£o Silva fictÃ­cio pro novo demo client
  update public.client_vehicles set client_id = v_demo_client_id where client_id = v_old_client_id;
  update public.policies set client_id = v_demo_client_id where client_id = v_old_client_id;
  update public.claims set client_id = v_demo_client_id where client_id = v_old_client_id;
  update public.payments set client_id = v_demo_client_id where client_id = v_old_client_id;
  update public.documents set client_id = v_demo_client_id where client_id = v_old_client_id;
  update public.messages set client_id = v_demo_client_id where client_id = v_old_client_id;
  update public.indications set indicador_id = v_demo_client_id where indicador_id = v_old_client_id;
  update public.drive_scores set client_id = v_demo_client_id where client_id = v_old_client_id;
  update public.car_sales set client_id = v_demo_client_id where client_id = v_old_client_id;
  update public.leads set client_id = v_demo_client_id where client_id = v_old_client_id;

  -- Apaga o profile fictÃ­cio antigo (jÃ¡ foi transferido)
  delete from public.profiles where id = v_old_client_id;

  -- Cria notificaÃ§Ãµes pro cliente
  insert into public.notifications (user_id, titulo, mensagem, tipo, prioridade, lida) values
    (v_demo_client_id,'Sua apÃ³lice vence em 90 dias','RenovaÃ§Ã£o Porto Seguro disponÃ­vel com desconto Drive Score','renovacao','normal',false),
    (v_demo_client_id,'Sinistro em anÃ¡lise','SIN-2026-0001 - vistoria realizada, aguardando retorno','sinistro','alta',false),
    (v_demo_client_id,'Pagamento prÃ³ximo','Parcela 9/12 vence em 15/05 - R$ 287,50','pagamento','normal',false),
    (v_demo_client_id,'IndicaÃ§Ã£o aprovada','VocÃª ganhou R$ 150 de cashback! Carlos Vizinho fechou apÃ³lice.','ia','normal',false);

  raise notice 'Demo client % configurado com sucesso!', v_demo_client_id;
end $$;

-- 3. Atualiza responsavel_id de leads/policies/etc pro corretor real
do $$
declare
  v_corretor_id uuid;
  v_old_corretor_id uuid := '11111111-1111-1111-1111-111111111111';
begin
  select id into v_corretor_id from public.profiles where email = 'corretor@webhub.demo';
  if v_corretor_id is not null then
    update public.leads set responsavel_id = v_corretor_id where responsavel_id = v_old_corretor_id;
    update public.policies set responsavel_id = v_corretor_id where responsavel_id = v_old_corretor_id;
    update public.claims set responsavel_id = v_corretor_id where responsavel_id = v_old_corretor_id;
    update public.commissions set beneficiario_id = v_corretor_id where beneficiario_id = v_old_corretor_id;
    update public.notifications set user_id = v_corretor_id where user_id = v_old_corretor_id;
    update public.activities set user_id = v_corretor_id where user_id = v_old_corretor_id;
    update public.messages set from_user_id = v_corretor_id where from_user_id = v_old_corretor_id;
  end if;
end $$;

do $$
declare
  v_vendedor_id uuid;
  v_old_vendedor_id uuid := '33333333-3333-3333-3333-333333333333';
begin
  select id into v_vendedor_id from public.profiles where email = 'vendedor@webhub.demo';
  if v_vendedor_id is not null then
    update public.car_sales set vendedor_id = v_vendedor_id where vendedor_id = v_old_vendedor_id;
    update public.leads set responsavel_id = v_vendedor_id where responsavel_id = v_old_vendedor_id;
    update public.commissions set beneficiario_id = v_vendedor_id where beneficiario_id = v_old_vendedor_id;
    update public.notifications set user_id = v_vendedor_id where user_id = v_old_vendedor_id;
    update public.activities set user_id = v_vendedor_id where user_id = v_old_vendedor_id;
  end if;
end $$;

-- DONE!
-- Agora os 4 logins funcionam com dados ricos:
--   cliente@webhub.demo  â†’ vÃª suas apÃ³lices, sinistros, pagamentos
--   corretor@webhub.demo â†’ vÃª CRM completo, comissÃµes
--   vendedor@webhub.demo â†’ vÃª pipeline WebCar, vendas
--   admin@webhub.demo    â†’ vÃª tudo, dashboards consolidados

````

---

## 🤖 PROMPT 1 — FOUNDATION

# PROMPT 1 â€” FOUNDATION (cole no Lovable como primeiro prompt do projeto novo)

---

Crie um app web chamado **WebHub** â€” plataforma operacional unificada de uma corretora de seguros (Webseg) e uma loja de carros (WebCar) localizadas em Patos de Minas/MG, mesma marca do grupo "Web". O app tem 4 portais distintos baseados em role: **cliente, corretor, vendedor, admin**.

## Stack obrigatÃ³ria
- React + TypeScript + Vite
- Tailwind CSS
- shadcn/ui (todos os componentes que precisar)
- React Router DOM v6
- Supabase (auth + database + realtime)
- lucide-react para Ã­cones
- recharts para grÃ¡ficos
- date-fns + locale pt-BR para datas
- sonner para toasts

## Identidade visual

**Tema:** profissional, denso, executivo. Nada de gamificaÃ§Ã£o ou estÃ©tica infantil.

**Cores (configure no `tailwind.config.ts` e `index.css`):**
- Primary (Webseg azul): `#1e3a8a` (azul navy escuro) com tons 50-950
- Accent (WebCar dourado): `#f59e0b` (amber 500) com variaÃ§Ãµes
- Background: `#f8fafc` (slate-50) | dark: `#0f172a` (slate-900)
- Foreground: `#0f172a` | dark: `#f1f5f9`
- Sucesso: `#16a34a` | Erro: `#dc2626` | Aviso: `#f59e0b`
- Borders: `#e2e8f0` | dark: `#1e293b`

**Tipografia:** Inter (sans) â€” importar de Google Fonts no `index.html`.

**Componentes:** densos, com sombras sutis, cantos arredondados (`rounded-lg`), sem cores berrantes. PadrÃ£o "fintech moderna" tipo Nubank/QuintoAndar/Linear.

## Estrutura de pastas
```
src/
  lib/
    supabase.ts          // client supabase
    utils.ts             // cn helper, formatters BRL/data
    types.ts             // tipos compartilhados (Profile, Vehicle, Lead, Policy, etc â€” espelhar tabelas Supabase)
  hooks/
    useAuth.ts           // hook de auth + profile
    useRealtime.ts       // realtime subscriptions
  components/
    layout/
      AppShell.tsx       // sidebar + header + outlet
      Sidebar.tsx        // navegaÃ§Ã£o por role
      Header.tsx         // breadcrumb + notif + user menu
    ui/                  // shadcn (button, card, dialog, table, badge, input, select, tabs, sheet, dropdown-menu, avatar, toast, progress, separator, skeleton)
    shared/
      KpiCard.tsx        // card de KPI grande para dashboards
      StatusBadge.tsx    // badge colorido por status (lead/policy/claim/sale)
      EmptyState.tsx
      DataTable.tsx      // tabela genÃ©rica com filtros e busca
  pages/
    Auth.tsx             // login + signup combinado
    NotFound.tsx
    cliente/
      Dashboard.tsx
      Apolices.tsx
      Sinistros.tsx
      Garagem.tsx
      Documentos.tsx
      Pagamentos.tsx
      Cotador.tsx
      Indicacao.tsx
    corretor/
      Dashboard.tsx
      Leads.tsx           // kanban
      Clientes.tsx
      Sinistros.tsx
      Comissoes.tsx
      WhatsApp.tsx
      Cotador.tsx
    webcar/
      Dashboard.tsx
      Estoque.tsx
      Vendas.tsx          // pipeline kanban
      VendaDetalhe.tsx
      Clientes.tsx
    admin/
      Dashboard.tsx       // KPIs consolidados
      Funil.tsx           // funil WebCar â†’ Webseg
      Performance.tsx
      CrossSell.tsx       // botÃ£o simular venda
  App.tsx                 // routes com guards por role
  main.tsx
```

## Supabase

**VariÃ¡veis de ambiente** (`.env`):
```
VITE_SUPABASE_URL=
VITE_SUPABASE_ANON_KEY=
```

Cliente Supabase em `src/lib/supabase.ts`:
```ts
import { createClient } from '@supabase/supabase-js'
export const supabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_ANON_KEY,
  { auth: { persistSession: true, autoRefreshToken: true } }
)
```

**Tabelas jÃ¡ existem no Supabase** (nÃ£o criar de novo):
`profiles, vehicles, client_vehicles, leads, quotes, policies, claims, car_sales, documents, payments, activities, messages, commissions, notifications, indications, drive_scores`.

Espelhe os tipos TypeScript em `src/lib/types.ts` baseado nos campos das tabelas (vocÃª verÃ¡ no schema do Supabase).

## Auth + roles

`useAuth.ts` deve:
1. Pegar a sessÃ£o do Supabase
2. Buscar o profile (`select * from profiles where id = user.id`)
3. Expor: `{ user, profile, role, loading, signIn, signUp, signOut }`
4. Ouvir `onAuthStateChange`

**Rotas com guard:**
```
/                  â†’ redireciona pelo role
/login             â†’ Auth
/cliente/*         â†’ role=cliente
/corretor/*        â†’ role=corretor
/webcar/*          â†’ role=vendedor
/admin/*           â†’ role=admin
/admin/*           â†’ admin pode acessar qualquer rota tambÃ©m
```

Se profile.role nÃ£o bate com a rota â†’ 403.

## Sidebar (por role)

**Cliente:**
- InÃ­cio (Dashboard)
- ApÃ³lices
- Sinistros
- Garagem
- Documentos
- Pagamentos
- Cotar Seguro
- Indicar e Ganhar

**Corretor:**
- InÃ­cio
- Leads
- Clientes
- Sinistros
- Cotador
- WhatsApp
- ComissÃµes

**Vendedor (WebCar):**
- InÃ­cio
- Estoque
- Vendas (pipeline)
- Clientes

**Admin:**
- VisÃ£o Geral
- Funil Unificado
- Performance Equipe
- Cross-sell
- + tudo dos outros portais (admin tem acesso total)

Cada item com Ã­cone do lucide. Highlight do item ativo. Logo "WebHub" em cima da sidebar (texto estilizado: `Web` em navy + `Hub` em amber, font-bold).

## Header

- Breadcrumb Ã  esquerda
- Sino de notificaÃ§Ãµes (popover lendo `notifications` do Supabase realtime)
- Avatar + nome + dropdown (Meu perfil / Sair)

## PÃ¡gina de Auth

Card centralizado com tabs **Entrar / Criar conta**.

**Login:** email + senha + botÃ£o "Entrar". ApÃ³s login, redireciona pelo role.

**Cadastro:** nome completo + email + senha + role (select: cliente/corretor/vendedor/admin â€” NORMALMENTE sÃ³ cliente, mas no demo permitimos os 4 pra facilitar testes).

**RodapÃ©:** "Logins de demo" com 4 botÃµes prÃ©-preenchidos:
- ðŸ‘¤ Cliente (cliente@webhub.demo / demo123)
- ðŸ¤ Corretor (corretor@webhub.demo / demo123)
- ðŸš— Vendedor (vendedor@webhub.demo / demo123)
- ðŸ‘‘ Admin (admin@webhub.demo / demo123)

Clicar em qualquer botÃ£o preenche os campos e faz login.

## Dashboards iniciais (skeletons que populamos depois)

Cada dashboard de role mostra um header com saudaÃ§Ã£o ("Bom dia, [nome]") + 3-4 KpiCards genÃ©ricos com loading skeleton + uma seÃ§Ã£o "PrÃ³ximas aÃ§Ãµes". NÃ£o precisa estar funcional ainda â€” sÃ³ estrutura.

## Helpers em `src/lib/utils.ts`

```ts
export const cn = (...inputs: any[]) => /* clsx + tailwind-merge */
export const formatBRL = (n: number) => n.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })
export const formatDate = (d: string | Date) => /* dd/MM/yyyy com date-fns */
export const formatDateTime = (d: string | Date) => /* dd/MM/yyyy HH:mm */
export const timeAgo = (d: string | Date) => /* "hÃ¡ 3 horas" pt-BR */
export const getStatusColor = (status: string, type: 'lead'|'policy'|'claim'|'sale') => /* mapa de cores */
export const getInitials = (name: string) => /* "JoÃ£o Silva" â†’ "JS" */
```

## StatusBadge mapeamento

```
LEAD: novo=blue, contato=indigo, cotacao_enviada=violet, em_negociacao=amber, fechado=green, perdido=red
POLICY: ativa=green, em_renovacao=amber, vencida=red, cancelada=slate, suspensa=orange
CLAIM: aberto=red, em_analise=amber, vistoria=blue, aprovado=green, pago=emerald, recusado=slate
SALE: lead=blue, test_drive=indigo, proposta=violet, credito=amber, contrato=cyan, entrega=teal, concluida=green, perdida=red
```

## NotificaÃ§Ãµes realtime

Hook `useRealtime` subscreve `notifications` filtrado por `user_id = auth.uid()`. Toast + atualiza badge no sino. Som nÃ£o â€” sÃ³ visual.

## EntregÃ¡veis desse prompt

1. Projeto rodando com `npm run dev` 
2. Login funcional com os 4 logins de demo
3. ApÃ³s login, cada role cai no seu dashboard skeleton
4. Sidebar correta por role
5. Header com sino de notificaÃ§Ãµes lendo do Supabase
6. Dark mode toggle no header (opcional mas faÃ§a)
7. Tudo responsivo (mobile sidebar vira sheet)

NÃ£o implemente ainda os portais individuais a fundo â€” sÃ³ estrutura. PrÃ³ximos prompts vÃ£o preencher cada portal.

**Importante:** TODA a estilizaÃ§Ã£o deve ser tema **profissional executivo**, sem emojis enfeitando UI (emojis sÃ³ nos botÃµes de demo do login).


---

## 🤖 PROMPT 2 — CLIENTE

# PROMPT 2 â€” PORTAL CLIENTE (cole no Lovable depois do prompt 1)

---

Implemente o **Portal Cliente** completo do WebHub. O cliente logado vÃª apenas seus prÃ³prios dados (RLS jÃ¡ cuida disso). Use os dados reais do Supabase, sem mock.

## 1. `/cliente` â€” Dashboard

Layout em grid:

**Topo:** SaudaÃ§Ã£o dinÃ¢mica ("Bom dia/tarde/noite, JoÃ£o").

**Linha 1 â€” 4 KPIs grandes:**
- ApÃ³lices ativas (count de `policies` com status='ativa')
- PrÃ³xima parcela (prÃ³ximo payment com status='pendente' â€” mostrar valor + data)
- Drive Score atual (Ãºltimo drive_score do mÃªs corrente â€” mostrar nÃºmero grande + delta vs mÃªs anterior)
- Cashback acumulado (soma de `indications.cashback_valor` com status='liberado' ou 'pago')

**Linha 2 â€” 2 colunas:**
- **Esquerda (2/3):** Card "Suas apÃ³lices ativas" â€” lista compacta com: produto, seguradora, vigÃªncia, valor mensal, badge status. Click â†’ abre detalhe da apÃ³lice.
- **Direita (1/3):** Card "PrÃ³ximas aÃ§Ãµes" â€” lista vertical:
  - RenovaÃ§Ã£o em X dias
  - Sinistro aberto (se tiver)
  - Documento expirando
  - Pagamento prÃ³ximo

**Linha 3:** Card "Sua garagem" â€” carrosselzinho horizontal com 1 card por carro: foto placeholder, modelo, ano, placa, prÃ³ximo IPVA/licenciamento. Click â†’ /cliente/garagem.

**Linha 4:** Card "Atividade recente" â€” timeline com Ãºltimos 5 eventos do cliente (apÃ³lice criada, sinistro atualizado, pagamento, etc â€” buscar de `activities` filtrado).

## 2. `/cliente/apolices` â€” ApÃ³lices

**Listagem:** cards verticais, 1 por apÃ³lice. Cada card mostra:
- Header: produto + seguradora + status badge
- NÃºmero da apÃ³lice
- VigÃªncia (inÃ­cio â†’ fim) com barra de progresso visual mostrando "X% do perÃ­odo usado"
- Valor mensal + parcela atual/total
- Coberturas em badges horizontais (ColisÃ£o, Roubo, Natureza, Terceiros R$ XXX, App, Carro reserva 15d)
- BotÃµes: "Ver detalhes" / "Carteirinha digital" / "Renovar 1-clique"

**BotÃ£o "Carteirinha digital"** abre dialog grande com layout de carteira:
- Fundo gradient navy â†’ amber
- Logo WebHub + seguradora
- Nome do cliente
- Modelo + placa do veÃ­culo
- NÃºmero da apÃ³lice
- VigÃªncia
- QR code (gerar com biblioteca tipo `qrcode` apontando pra URL fictÃ­cia)
- BotÃ£o "Adicionar ao Apple/Google Wallet" (placeholder, mostrar toast "Em breve")
- BotÃ£o "Compartilhar apÃ³lice" (gera link copiÃ¡vel)

**BotÃ£o "Renovar 1-clique"** abre dialog "Vamos renovar sua apÃ³lice" com:
- Resumo da apÃ³lice atual
- "Recotando para vocÃª nas seguradoras..." (loading 2s, depois mostra 4 cotaÃ§Ãµes fake comparativas: Porto, Bradesco, Allianz, SulAmerica com preÃ§os diferentes)
- Cliente escolhe â†’ toast "CotaÃ§Ã£o selecionada, corretor em contato em atÃ© 1h"

## 3. `/cliente/sinistros` â€” Sinistros

**Header:** BotÃ£o grande vermelho "ðŸš¨ Abrir sinistro agora" (sticky no topo)

**Lista de sinistros** (`claims` do cliente): cards com tipo, data, status badge, valor estimado. Click â†’ detalhe.

**Detalhe do sinistro:** dialog/sheet lateral com:
- Header: tipo + nÃºmero + status
- Local + data + descriÃ§Ã£o
- Mini-mapa (placeholder com lat/lng visÃ­vel)
- Galeria de fotos (`fotos` array)
- **Timeline visual** â€” vertical, cada evento do `timeline` jsonb com data, evento, autor, Ã­cone colorido pelo tipo
- Card "Status atual" com prÃ³xima aÃ§Ã£o esperada
- Documentos anexados
- Chat com regulador (botÃ£o "Enviar mensagem" â€” fake)

**BotÃ£o de pÃ¢nico** (sticky) abre o **Sinistro IA Wizard** (modal full-screen):

### Passo 1 â€” Triagem
"VocÃª estÃ¡ bem? AlguÃ©m se machucou?"
- BotÃ£o grande "âœ“ Estou bem, sem feridos"
- BotÃ£o "ðŸš¨ Tem feridos â€” chamar ambulÃ¢ncia" (mostra nÃºmero 192 + abre WhatsApp pra corretor)

### Passo 2 â€” LocalizaÃ§Ã£o
"Vamos pegar sua localizaÃ§Ã£o"
- BotÃ£o "Permitir localizaÃ§Ã£o" â†’ mostra lat/lng com nome da cidade
- Campo "Local exato" (auto-preenchido pelo geocoding fake)

### Passo 3 â€” Tipo
Cards grandes pra escolher: ColisÃ£o / Roubo / Furto / Natureza / Vidros / Outro

### Passo 4 â€” Fotos guiadas
"Tira essas fotos uma de cada vez"
- Lista checklist:
  - ðŸ“· Frente do seu carro
  - ðŸ“· Lateral esquerda
  - ðŸ“· Lateral direita
  - ðŸ“· Traseira
  - ðŸ“· Dano principal (close)
  - ðŸ“· VeÃ­culo do outro (se terceiro)
  - ðŸ“· Placa do outro veÃ­culo
  - ðŸ“· CNH do outro condutor
  - ðŸ“· Local da ocorrÃªncia amplo
- Cada item tem botÃ£o "Tirar foto" (mock â€” usa input file ou placeholder)
- Conforme tira, fica âœ“ verde

### Passo 5 â€” Voz/DescriÃ§Ã£o
"Me conta o que aconteceu (texto ou Ã¡udio)"
- Textarea grande
- BotÃ£o de gravar voz (mock â€” sÃ³ simula, depois preenche um texto fake)

### Passo 6 â€” IA gerou seu dossiÃª
Mostra um "dossiÃª" gerado: tÃ­tulo, descriÃ§Ã£o estruturada, data/hora, local, partes envolvidas, recomendaÃ§Ã£o de oficina prÃ³xima.
**Importante:** Esse dossiÃª deve ser gerado chamando o Claude. Adicione integraÃ§Ã£o via Supabase Edge Function ou diretamente via fetch para a Anthropic API se jÃ¡ tiver chave; caso contrÃ¡rio, retorne um dossiÃª hardcoded realista.

### Passo 7 â€” ConfirmaÃ§Ã£o
"Sinistro aberto. Camila Andrade foi notificada e entrarÃ¡ em contato em atÃ© 30 minutos. VocÃª receberÃ¡ atualizaÃ§Ãµes no app."
- BotÃ£o "Acompanhar" â†’ leva pra detalhe do sinistro recÃ©m-criado

Ao concluir o wizard: `INSERT into claims` + `INSERT into activities` + `INSERT into notifications` (pra todos corretores) + redireciona pro detalhe.

## 4. `/cliente/garagem` â€” Garagem digital

**Lista** (`client_vehicles` do cliente): card grande por veÃ­culo:
- Foto (placeholder ou gerar com IA depois)
- Modelo + ano + versÃ£o
- Placa + cor + KM atual
- **3 cards horizontais embutidos:**
  - PrÃ³ximo IPVA (data + dias restantes)
  - PrÃ³ximo licenciamento (data + status)
  - PrÃ³xima revisÃ£o (data + KM previsto)
- HistÃ³rico (timeline pequena): "Comprou em XX/XX", "RevisÃ£o XX KM", "Sinistro XX"
- BotÃ£o "Ver apÃ³lice deste carro"
- BotÃ£o grande dourado **"Trocar de carro?"** â†’ leva pra `/cliente/garagem/trocar` (pÃ¡gina com estoque WebCar â€” vem do prompt webcar)

## 5. `/cliente/documentos` â€” Cofre

**Tabs:** Pessoais / VeÃ­culos / ApÃ³lices / Sinistros

Cada tab mostra grid de cards, 1 por documento. Cada card: Ã­cone do tipo, nome, validade, status (vÃ¡lido / expira em X dias / expirado).

BotÃ£o "Adicionar documento" abre dialog com select de tipo + upload (mock que insere row em `documents` com URL fake).

## 6. `/cliente/pagamentos` â€” Pagamentos

**Resumo no topo:**
- Total pago no ano
- PrÃ³ximo vencimento
- Atrasados (se tiver)

**Lista** (`payments` do cliente, ordem desc por vencimento): cada linha mostra:
- Tipo (parcela seguro / entrada carro / etc)
- Valor + parcela X/Y
- Vencimento
- Status badge
- MÃ©todo (Ã­cone)
- BotÃµes contextuais:
  - Se pendente: "Pagar agora" â†’ dialog com opÃ§Ãµes PIX / boleto / cartÃ£o (mock)
  - Se atrasado: "Renegociar" â†’ toast "Corretor avisado, vai te chamar"
  - Se pago: "Ver comprovante" â†’ dialog com comprovante fake

**Card lateral:** "Antecipe parcelas com 5% off" â€” botÃ£o pra dialog que mostra cÃ¡lculo.

## 7. `/cliente/cotador` â€” Cotador inteligente (cliente self-service)

Wizard de 5 passos:

### Passo 1 â€” Que tipo?
Cards grandes: Auto | Moto | Residencial | Vida | Viagem

### Passo 2 â€” VeÃ­culo (se auto)
- Campo placa (auto-completar via FIPE fake)
- Marca / Modelo / Ano (preenchidos auto se digitar placa)
- KM/ano

### Passo 3 â€” Perfil
- Idade
- CEP
- Garagem (sim/nÃ£o)
- Uso (passeio / trabalho / app)
- Outros condutores

### Passo 4 â€” Coberturas
- Sliders pra LMI (R$ 50k / 100k / 200k / 500k)
- Franquia (reduzida / normal / dobrada)
- Carro reserva (sim/nÃ£o, dias)
- AssistÃªncia 24h

### Passo 5 â€” Resultado IA
"Comparando 6 seguradoras..."
Mostra 6 cards (Porto, Bradesco, Allianz, SulAmerica, Tokio, HDI) com:
- Valor mensal (varia 5-25% entre eles)
- Coberturas
- Tempo de mercado
- AvaliaÃ§Ã£o NPS (estrelas)
- BotÃ£o "Falar com corretor sobre essa"

BotÃ£o escolher â†’ cria `quote` no Supabase + cria `lead` se nÃ£o tem cliente_id + abre WhatsApp em nova aba com mensagem prÃ©-formatada.

**Importante:** os preÃ§os devem ser calculados por uma funÃ§Ã£o simples baseada em idade, ano do veÃ­culo, CEP â€” nÃ£o totalmente random. Faz parecer real.

## 8. `/cliente/indicacao` â€” Indicar e ganhar

**Topo:** Card grande
- Total ganho (soma cashback)
- IndicaÃ§Ãµes convertidas / total
- Link Ãºnico: `https://webhub.demo/i/{user_id_curto}` (botÃ£o copiar)

**Form:** "Indique alguÃ©m"
- Nome
- Telefone
- Email (opcional)
- Produto
- BotÃ£o "Indicar agora" â†’ `INSERT indications`

**HistÃ³rico:** lista das indicaÃ§Ãµes do cliente com status.

**Sem badges, sem missÃµes, sem ranking â€” sÃ³ cashback direto, profissional.**

## Detalhes finais

- Tudo deve usar dados reais do Supabase via `useEffect` + `supabase.from(...).select()`.
- Loading states com skeleton.
- Empty states bonitos quando nÃ£o tem dado.
- Feedback de aÃ§Ãµes com `sonner` toast.
- Tudo responsivo.


---

## 🤖 PROMPT 3 — CORRETOR

# PROMPT 3 â€” PORTAL CORRETOR (Webseg)

---

Implemente o **Portal Corretor** completo. Use dados reais do Supabase. Visual: profissional, denso, executivo â€” pense Linear / Pipedrive / HubSpot.

## 1. `/corretor` â€” Dashboard

**Topo:** SaudaÃ§Ã£o + filtro de perÃ­odo (Hoje / Esta semana / Este mÃªs).

**Linha 1 â€” 5 KPIs:**
- Leads no funil (count `leads` not in fechado/perdido)
- CotaÃ§Ãµes enviadas (count `quotes` status='enviada')
- ApÃ³lices fechadas no mÃªs (count `policies` created this month)
- ComissÃ£o prevista (soma `commissions` status='prevista' do mÃªs)
- ComissÃ£o paga (soma `commissions` status='paga' do mÃªs)

**Linha 2:**
- **Card "RenovaÃ§Ãµes prÃ³ximas 30 dias"** â€” lista (cliente, apÃ³lice, vencimento, valor) com botÃ£o "Renovar"
- **Card "Sinistros aguardando aÃ§Ã£o"** â€” lista de claims status in ('aberto','em_analise','vistoria') ordenado por mais antigos

**Linha 3:**
- **GrÃ¡fico "Funil do mÃªs"** â€” barras horizontais: Novo / Contato / CotaÃ§Ã£o / NegociaÃ§Ã£o / Fechado / Perdido
- **GrÃ¡fico "Origem dos leads"** â€” pizza: Instagram, site, indicaÃ§Ã£o, walk-in, ads, etc

**Linha 4 â€” IA Copiloto card:**
Card destacado "ðŸ¤– Sua IA copiloto" com:
- "3 leads esfriaram, devo reabordar?" â†’ botÃ£o "Sim, criar mensagens"
- "Maria Costa pagou parcela em atraso â€” sugiro mensagem de relacionamento"
- "VocÃª tem 47% de conversÃ£o em leads de Instagram esse mÃªs"

## 2. `/corretor/leads` â€” CRM Kanban

**Topo:** filtros (responsÃ¡vel, origem, produto) + busca + botÃ£o "+ Novo lead".

**Kanban horizontal** com 6 colunas (status do lead):
- Novo
- Contato
- CotaÃ§Ã£o enviada
- Em negociaÃ§Ã£o
- Fechado
- Perdido

Cada card no kanban mostra:
- Nome cliente
- Origem (badge colorido + Ã­cone Instagram/Site/etc)
- Produto interesse
- Telefone
- Valor estimado (se tiver quote)
- AI Score (badge: verde >80, amarelo 50-80, vermelho <50)
- Tempo no estÃ¡gio (timeAgo)
- Avatar do responsÃ¡vel

**Drag-and-drop** entre colunas (use `@dnd-kit/core` ou `react-beautiful-dnd`) â†’ atualiza `leads.status` no Supabase.

**Click no card** â†’ abre `LeadDetail` em sheet lateral:
- Header: nome + status + score + aÃ§Ãµes (mover de stage, atribuir)
- Tabs:
  - **HistÃ³rico:** timeline de activities + messages
  - **CotaÃ§Ãµes:** lista de quotes com status
  - **Notas:** textarea + lista de notas
  - **Tarefas:** mini lista de tarefas pra esse lead
- **Painel direito (sticky):**
  - BotÃµes: "Enviar WhatsApp", "Ligar", "Enviar cotaÃ§Ã£o", "Marcar como fechado"
  - **ðŸ¤– IA Copiloto:**
    - BotÃ£o "Resumir cliente" â†’ chama IA, retorna 3 bullets sobre o cliente
    - BotÃ£o "Sugerir prÃ³xima aÃ§Ã£o" â†’ IA analisa o estÃ¡gio e sugere
    - BotÃ£o "Gerar mensagem" â†’ IA gera msg personalizada pro WhatsApp
    - BotÃ£o "Tratar objeÃ§Ã£o" â†’ input "qual objeÃ§Ã£o?" + IA dÃ¡ argumentos

## 3. `/corretor/clientes` â€” Lista de clientes

**DataTable** com:
- Nome / CPF / Telefone
- ApÃ³lices ativas (count)
- LTV (soma comissÃµes totais)
- Health Score (0-100, calculado: 100 - 30 se atraso pagamento - 20 se sinistro recente - 50 se cancelou no passado)
- Ãšltimo contato (timeAgo)
- BotÃ£o "Ver ficha"

**Ficha do cliente** (`/corretor/clientes/:id`):
- Header com avatar + dados + score
- Tabs:
  - **VisÃ£o geral:** resumo, prÃ³ximas aÃ§Ãµes, valor de carteira
  - **ApÃ³lices:** todas as policies (ativas e histÃ³ricas)
  - **Sinistros:** todos os claims
  - **Pagamentos:** histÃ³rico financeiro com status
  - **Mensagens:** thread WhatsApp completa
  - **Documentos:** cofre do cliente
  - **Atividades:** activities timeline completa
  - **ðŸ¤– IA:** "Resumo do relacionamento" gerado por IA quando clicar

## 4. `/corretor/sinistros` â€” Sinistros management

**Topo:** filtros (status, tipo, mÃªs) + busca.

**View padrÃ£o: Kanban** por status (Aberto / Em anÃ¡lise / Vistoria / Aprovado / Pago / Recusado).

Cada card: cliente + tipo + data + valor estimado + dias em stage.

**Toggle pra view Lista (DataTable)** com mais info.

**Click no sinistro** â†’ detalhe (mesma estrutura do detalhe do cliente, mas focada).

**BotÃµes de aÃ§Ã£o rÃ¡pida:**
- "Atualizar status"
- "Adicionar evento timeline"
- "Marcar como pago"
- "Avaliar fraude com IA" â†’ IA retorna score 0-100 e justificativa

## 5. `/corretor/cotador` â€” Cotador interno

Wizard mais robusto que o do cliente:

### Cliente
- Buscar cliente existente OU criar novo
- Preenche/confirma dados

### VeÃ­culo
- Buscar por placa (FIPE fake)
- Confirmar dados

### Perfil de risco
- Mais campos: condutor principal, condutores adicionais, garagem residÃªncia, garagem trabalho, percurso, KM/ano

### Coberturas detalhadas
- LMI customizÃ¡vel
- Franquia
- Coberturas opcionais (vidros, farÃ³is, retrovisor, carro reserva, assistÃªncia viagem)

### CotaÃ§Ã£o multi-seguradora
**6 seguradoras** com resultado em cards:
- Cada um com: valor, vigÃªncia, coberturas, condiÃ§Ãµes especiais
- BotÃ£o "Selecionar" 

ApÃ³s selecionar:
- Salva quote
- BotÃµes: "Enviar pro cliente via WhatsApp" / "Enviar pdf por email" / "Fechar agora"

## 6. `/corretor/whatsapp` â€” WhatsApp central

Layout estilo WhatsApp Web:
- **Esquerda (1/3):** lista de conversas (clientes + leads). Busca, filtros (nÃ£o lidos, lead, cliente).
- **Direita (2/3):** thread da conversa selecionada.

**Thread:**
- Bolhas de mensagem (esquerda do cliente, direita do corretor)
- Mensagens da IA com badge "ðŸ¤– IA" e fundo levemente diferente
- Mensagens automÃ¡ticas do sistema com badge "Sistema"
- Ãudios mockados (player + transcriÃ§Ã£o automÃ¡tica)

**Footer da thread:**
- Input + botÃ£o enviar
- BotÃ£o "ðŸ“Ž" anexar
- BotÃ£o "ðŸŽ¤" Ã¡udio
- BotÃ£o "ðŸ¤– Sugerir resposta IA" â†’ IA gera resposta baseada no contexto
- BotÃ£o "ðŸ“‹ Templates" â†’ lista de templates aprovados (renovaÃ§Ã£o, cobranÃ§a, oferta cross-sell, etc)

**Ao enviar:** insere em `messages`, atualiza activity, mostra na thread.

## 7. `/corretor/comissoes` â€” Painel de comissÃ£o

**Topo:** 4 KPIs:
- ComissÃ£o recebida no ano
- Prevista pra receber (prÃ³ximos 90 dias)
- Recorrente mensal (mÃ©dia)
- Ticket mÃ©dio por apÃ³lice

**GrÃ¡fico:** linha do tempo das comissÃµes mensais (Ãºltimos 12 meses).

**Tabs:**
- **ApÃ³lices:** tabela com policy + valor + status comissÃ£o
- **Vendas:** tabela com car_sale + comissÃ£o da venda
- **ConciliaÃ§Ã£o:** botÃ£o "Importar extrato seguradora" (upload CSV mock) â†’ mostra diff (esperado vs recebido)

## 8. UX detalhes

- NotificaÃ§Ãµes realtime (subscribe a `notifications`, `leads`, `claims`).
- Atalhos: `Ctrl+K` abre command palette pra buscar cliente/lead.
- Tooltips em aÃ§Ãµes.
- ConfirmaÃ§Ã£o em aÃ§Ãµes destrutivas.
- Loading skeletons sempre.
- Empty states com CTA.


---

## 🤖 PROMPT 4 — WEBCAR

# PROMPT 4 â€” PORTAL WEBCAR (loja de carros)

---

Implemente o **Portal Vendedor / WebCar** completo. EstÃ©tica: dourado/ambar como cor secundÃ¡ria mais presente (loja de carro). Profissional, denso. Pense em Carmax / Webmotors interno.

## 1. `/webcar` â€” Dashboard

**Topo:** SaudaÃ§Ã£o + filtro de perÃ­odo.

**Linha 1 â€” 5 KPIs:**
- Carros disponÃ­veis no estoque
- Vendas no mÃªs (count car_sales status='concluida')
- Faturamento do mÃªs (soma preco_negociado)
- Pipeline ativo (count car_sales not in concluida/perdida)
- ComissÃ£o prevista (soma comissÃµes venda do mÃªs)

**Linha 2:**
- **Card "Vendas em fechamento esta semana"** â€” lista
- **Card "Test drives agendados"** â€” lista (campos do `observacoes` ou criar pequena tabela `appointments` se quiser)

**Linha 3:**
- **GrÃ¡fico funil de vendas** â€” barras: lead / test drive / proposta / crÃ©dito / contrato / entrega / concluÃ­da
- **GrÃ¡fico estoque por categoria** â€” pizza por marca ou faixa de preÃ§o

## 2. `/webcar/estoque` â€” Estoque de veÃ­culos

**Topo:** filtros (marca, modelo, ano, faixa de preÃ§o, status, destaque) + busca + botÃ£o "+ Adicionar veÃ­culo".

**View Grid:** cards 3-4 colunas. Cada card:
- Foto principal (primeira do array `fotos`)
- Marca + modelo + versÃ£o
- Ano modelo / fabricaÃ§Ã£o
- KM
- Cor + combustÃ­vel + cÃ¢mbio (badges)
- PreÃ§o de venda (destacado, formato BRL)
- Status badge
- Quick actions:
  - "Ver detalhes"
  - "Reservar"
  - "Iniciar venda"
  - Toggle destaque (estrela)

**View Lista (toggle):** DataTable com mais campos.

**Detalhe do veÃ­culo** (`/webcar/estoque/:id`):
- Galeria de fotos (carrossel)
- Specs completos
- PreÃ§o + histÃ³rico de ajustes
- Status atual
- BotÃ£o "Iniciar venda" â†’ cria `car_sale` em `etapa_atual='lead'` e leva pra `/webcar/vendas/:saleId`

**Adicionar veÃ­culo (dialog):**
- Form completo com upload de fotos (mock â€” usar URLs Unsplash)
- Calculadora de margem (preÃ§o pago vs preÃ§o venda)

## 3. `/webcar/vendas` â€” Pipeline de vendas

**Kanban com 7 colunas** (etapas):
- Lead
- Test Drive
- Proposta
- CrÃ©dito
- Contrato
- Entrega
- ConcluÃ­da
(coluna "Perdida" colapsÃ¡vel no fim)

Cada card no kanban:
- Foto miniatura do carro
- Cliente
- Modelo do carro
- Valor negociado
- Vendedor (avatar)
- Tempo em stage
- Badge de status crÃ©dito (se aplicÃ¡vel)
- Ãcone de assinatura (se em contrato)

Drag-and-drop entre colunas â†’ atualiza `etapa_atual`.

**Click no card** â†’ navega pra `/webcar/vendas/:id` (pÃ¡gina detalhada).

## 4. `/webcar/vendas/:id` â€” Detalhe da venda

PÃ¡gina principal â€” layout em abas controladas por `etapa_atual`. Cada aba Ã© um passo do processo.

### Aba 1 â€” Cliente

**Esquerda (form):**
- Buscar cliente existente OU criar novo lead/profile
- CPF (com mÃ¡scara + validaÃ§Ã£o)
- CNH (upload + OCR mock que extrai dados)
- Comprovante de renda (upload)
- Comprovante de residÃªncia (upload)
- Estado civil, profissÃ£o, renda mensal

**Direita:**
- Card "VeÃ­culo selecionado" com foto + specs + preÃ§o
- BotÃ£o "Trocar veÃ­culo" â†’ volta pro estoque

### Aba 2 â€” Test drive

- Form: data + horÃ¡rio + condutor (CNH validada)
- Termo digital de responsabilidade (gerar PDF mock + assinatura digital com canvas)
- BotÃ£o "Confirmar test drive" â†’ muda etapa pra 'test_drive'

### Aba 3 â€” Proposta

- PreÃ§o de tabela vs preÃ§o negociado
- **AvaliaÃ§Ã£o de carro usado (trade-in):**
  - BotÃ£o "Adicionar carro de troca"
  - Form: marca / modelo / ano / KM / placa
  - Auto-busca FIPE (mock retornando valor de tabela)
  - Campo "Valor avaliado" + observaÃ§Ãµes de vistoria
  - Salva em `carro_troca` jsonb
- Forma de pagamento: Ã  vista / financiado / misto / consÃ³rcio
- Entrada (slider e campo)
- **Calculadora de financiamento:**
  - Parcelas (12-72)
  - Taxa de juros (input)
  - Mostra valor da parcela calculado
- BotÃ£o "Enviar proposta" â†’ atualiza preÃ§o, gera PDF de proposta com IA + envia WhatsApp
- BotÃ£o "Aceitar proposta" â†’ muda etapa pra 'credito'

### Aba 4 â€” AnÃ¡lise de crÃ©dito

- Selecionar financeira (dropdown: AymorÃ©, BV, ItaÃº, Santander, Bradesco, Pan)
- Form de envio (dados puxados do cliente automaticamente)
- BotÃ£o "Enviar anÃ¡lise"
- ApÃ³s enviar: status mock muda pra 'em_analise', depois 'aprovado' (com botÃ£o de "Simular retorno" pra demo)
- Quando aprovado: mostra condiÃ§Ãµes (taxa, parcelas, valor parcela aprovado)
- BotÃ£o "Aceitar condiÃ§Ãµes" â†’ muda etapa pra 'contrato'

**Importante:** Use IA pra gerar o "parecer de crÃ©dito" â€” chama Claude com os dados do cliente e retorna anÃ¡lise em texto.

### Aba 5 â€” Contrato

- **GeraÃ§Ã£o automÃ¡tica:** botÃ£o "Gerar contrato com IA" â†’ Claude gera contrato de compra e venda completo em texto (clÃ¡usulas, valores, partes, garantia, etc)
- Preview do contrato em formato A4
- BotÃ£o "Editar contrato" abre rich text editor
- **Assinatura digital:**
  - BotÃ£o "Enviar pra assinatura" â†’ mock que abre dialog "ZapSign integrado"
  - Status: pendente â†’ enviado â†’ assinado cliente â†’ assinado loja â†’ concluÃ­do
  - Cada step com timestamp
- Quando assinatura completa: muda etapa pra 'entrega'

### Aba 6 â€” Entrega

**Checklist de entrega:**
- âœ“ Vistoria final feita
- âœ“ Lacre instalado
- âœ“ Manuais entregues
- âœ“ Chave reserva
- âœ“ Documentos transferidos
- âœ“ Tanque cheio (cortesia)
- âœ“ Carro lavado e detalhado
- âœ“ Foto da entrega (cliente + vendedor + carro)

Termo de entrega (gerar + assinar).

**ðŸ”¥ SEÃ‡ÃƒO CROSS-SELL WEBSEG (DESTAQUE):**

Card destacado dourado com bordas:
> "NÃ£o esqueÃ§a do seguro deste carro!"

Mostra:
- BotÃ£o grande "Cotar seguro pra este cliente AGORA"
- Quando clica: gera automaticamente uma `quote` no Supabase com:
  - `client_id` = cliente da venda
  - `vehicle_data` = dados do carro vendido
  - `driver_data` = dados do cliente (idade, CEP, etc)
  - `origem_cross_sell` = true
  - `car_sale_id` = id da venda
- ApÃ³s gerar: redireciona pro cotador interno com tudo preenchido OU mostra cotaÃ§Ãµes simuladas direto
- Salva atividade "Cross-sell gerado" + cria notification pro corretor responsÃ¡vel + envia WhatsApp pro cliente (mock)

BotÃ£o "Concluir venda" â†’ muda etapa pra 'concluida' + cria `commission` pro vendedor + cria `activity` + notification.

### Aba 7 â€” PÃ³s-venda

- Data da entrega
- PrÃ³xima revisÃ£o (auto-calculada: data + 6 meses)
- Status garantia
- BotÃ£o "Agendar primeira revisÃ£o"
- HistÃ³rico de contato pÃ³s-venda

## 5. `/webcar/clientes` â€” Clientes WebCar

Listagem dos clientes que compraram (vinculados a `car_sales` ou que viraram leads).

DataTable com:
- Nome / CPF / telefone
- Carro comprado
- Data da venda
- Valor
- Vendedor
- Status seguro (tem apÃ³lice na Webseg? â†’ badge "âœ“ Webseg" / "âš  Sem seguro")
- BotÃ£o "Ver ficha"

Ficha do cliente: similar Ã  do corretor mas com foco em vendas.

## 6. UX

- NotificaÃ§Ãµes realtime.
- Quick search global.
- Mostrar foto/avatar do veÃ­culo em todas as referÃªncias (consistÃªncia visual forte).
- Cores: dourado/ambar mais presente que o azul (loja de carro).


---

## 🤖 PROMPT 5 — ADMIN

# PROMPT 5 â€” PORTAL ADMIN (dono / executivo)

---

Implemente o **Portal Admin**. Esse Ã© o painel do dono â€” visÃ£o consolidada das duas operaÃ§Ãµes (Webseg + WebCar). Visual: dashboard executivo, denso de nÃºmeros, grÃ¡ficos profissionais.

O admin tambÃ©m consegue acessar TODAS as outras rotas (cliente, corretor, webcar) â€” adicione um seletor "Visualizar como" no header pra alternar.

## 1. `/admin` â€” VisÃ£o Geral

**Topo:** Filtro de perÃ­odo global (Hoje / 7d / 30d / 90d / Ano / Custom).

**Linha 1 â€” 6 KPIs grandes (3 Webseg + 3 WebCar):**

Grupo Webseg (cor azul):
- ApÃ³lices ativas (count)
- MRR de comissÃ£o (soma comissÃ£o recorrente / 12 das apÃ³lices ativas)
- Sinistros abertos

Grupo WebCar (cor dourada):
- Carros vendidos no mÃªs
- Faturamento WebCar do mÃªs
- Pipeline ativo

Cada KPI mostra: valor grande + delta vs perÃ­odo anterior (verde/vermelho com seta) + sparkline pequeno.

**Linha 2:**
- **GrÃ¡fico "Receita consolidada"** (linha temporal) â€” duas sÃ©ries: ComissÃ£o Webseg + Margem WebCar (estimada como 5% do preÃ§o).
- **GrÃ¡fico "Funil unificado"** (waterfall ou bar): Visitante site â†’ Lead â†’ CotaÃ§Ã£o â†’ Venda WebCar â†’ ApÃ³lice Webseg â†’ RenovaÃ§Ã£o. Mostra conversÃ£o entre etapas.

**Linha 3 â€” 3 cards:**
- **Top corretores do mÃªs:** lista com avatar + nome + comissÃ£o + apÃ³lices fechadas
- **Top vendedores do mÃªs:** mesma lÃ³gica
- **Carros mais lucrativos:** veÃ­culos com maior margem mÃ©dia

**Linha 4:**
- **Heatmap de atividade:** dias da semana Ã— horas, mostra quando o pessoal mais movimenta o sistema
- **Mapa de leads por bairro de Patos de Minas** (mock â€” usar cards por CEP)

## 2. `/admin/funil` â€” Funil Unificado WebCar â†’ Webseg

PÃ¡gina dedicada ao **insight estrela**: cross-sell.

**Hero card no topo:**
- "X% das vendas WebCar viraram seguro Webseg este mÃªs"
- ComparaÃ§Ã£o: antes do WebHub (estimativa baixa) vs agora
- Receita extra gerada por cross-sell

**Funil visual (Sankey diagram com recharts ou bibliotec dedicada):**
- Visitas WebCar (site + Instagram + walk-in)
- â†’ Leads no CRM
- â†’ Test drives agendados
- â†’ Propostas enviadas
- â†’ CrÃ©dito aprovado
- â†’ Vendas fechadas
- â†’ CotaÃ§Ã£o Webseg gerada (auto)
- â†’ CotaÃ§Ã£o aceita
- â†’ ApÃ³lice fechada
- â†’ RenovaÃ§Ã£o 1 ano depois

Cada etapa: % de conversÃ£o, tempo mÃ©dio, gargalos destacados.

**AnÃ¡lise de oportunidades:**
- "12 carros vendidos sem seguro no Webseg" (lista com botÃ£o "Reabordar")
- "5 apÃ³lices Webseg vencendo, donos podem trocar de carro" (lista com botÃ£o "Oferta WebCar")

**Cohort:** quem comprou carro nos Ãºltimos 12 meses, % que renovou seguro, % que comprou outro carro depois.

## 3. `/admin/performance` â€” Performance da equipe

**Tabs:** Corretores / Vendedores

### Corretores
DataTable com:
- Nome
- Leads no funil (count)
- CotaÃ§Ãµes enviadas
- ConversÃ£o (%)
- ApÃ³lices fechadas no mÃªs
- ComissÃ£o gerada
- Ticket mÃ©dio
- Tempo mÃ©dio de resposta
- Health score da carteira (mÃ©dia dos clientes)
- NPS (mock)

Click no corretor â†’ drill-down individual: grÃ¡ficos pessoais, metas vs realizado, histÃ³rico.

### Vendedores
Similar:
- Carros vendidos
- Faturamento gerado
- Margem mÃ©dia
- Tempo mÃ©dio de venda (lead â†’ entrega)
- Pipeline ativo
- Cross-sell rate (% de vendas que geraram cotaÃ§Ã£o Webseg)
- ComissÃ£o

## 4. `/admin/cross-sell` â€” **PÃGINA DA DEMO KILLER**

**Essa Ã© a pÃ¡gina que vai impressionar.** Tem que ser dramÃ¡tica.

**Hero:**
- TÃ­tulo: "Cross-sell automÃ¡tico WebCar â†’ Webseg"
- SubtÃ­tulo: "Veja como uma venda de carro vira automaticamente uma cotaÃ§Ã£o de seguro em segundos"

**SeÃ§Ã£o 1 â€” EstatÃ­sticas live:**
- Cross-sells gerados hoje
- Taxa de conversÃ£o dos cross-sells (vs leads frios)
- Receita gerada por cross-sell no mÃªs

**SeÃ§Ã£o 2 â€” ConfiguraÃ§Ã£o da automaÃ§Ã£o:**
Card visual mostrando o fluxo (use cards conectados por setas):
```
[Venda fechada WebCar]
        â†“
[Trigger automÃ¡tico]
        â†“
[CotaÃ§Ã£o gerada Webseg com dados prÃ©-preenchidos]
        â†“
[NotificaÃ§Ã£o WhatsApp pro cliente em <30s]
        â†“
[Lead aparece no CRM do corretor responsÃ¡vel]
        â†“
[Atividade registrada]
```

Cada step com toggle on/off (visualmente â€” nÃ£o precisa funcionar) + tempo estimado.

**SeÃ§Ã£o 3 â€” ðŸ”¥ SIMULADOR LIVE (a estrela):**

Card grande destacado com gradiente navy â†’ amber:

> ## "Simule uma venda agora e veja a mÃ¡gica"

Form:
- Selecione um carro do estoque (dropdown com fotos)
- Selecione um cliente fictÃ­cio (dropdown) OU "criar novo"
- BotÃ£o GIGANTE: **"ðŸš€ SIMULAR VENDA WEBCAR"**

Quando aperta:

### Step 1 (1 segundo)
Toast verde: "âœ“ Venda WebCar registrada"
Mostra card animado entrando com os dados da venda (carro + cliente + valor).

### Step 2 (2 segundos depois)
Toast roxo: "ðŸ¤– IA analisando perfil do cliente..."
AnimaÃ§Ã£o de loading. Mostra texto sendo gerado com efeito typing.

### Step 3 (1 segundo depois)
Toast amber: "ðŸ“Š CotaÃ§Ã£o multi-seguradora gerada"
Aparece card mostrando 4 seguradoras com preÃ§os calculados.

### Step 4 (1 segundo depois)
Toast azul: "ðŸ’¬ WhatsApp enviado pro cliente"
Mostra mock visual de uma tela de WhatsApp com a mensagem chegando (com avatar do cliente, mensagem completa, Ã¡udio do cliente respondendo, etc â€” pode ser animado).

### Step 5 (1 segundo depois)
Toast verde grande: "âœ“ Lead Webseg criado e atribuÃ­do Ã  Camila Andrade"
Aparece card com o novo lead no CRM e indicador "NotificaÃ§Ã£o enviada".

### Resultado final
Painel "âœ“ ConcluÃ­do em 5 segundos" com resumo:
- Venda registrada: R$ X
- CotaÃ§Ã£o gerada: R$ Y mensais
- Lead atribuÃ­do: Camila Andrade
- ComissÃ£o prevista: R$ Z
- **ConversÃ£o prevista 3-5x maior que lead frio**

BotÃ£o: "Ver venda no portal WebCar" / "Ver lead no portal Corretor" / "Ver cotaÃ§Ã£o no portal Cliente".

**Tudo isso deve gravar de verdade no Supabase**: insert em car_sales, insert em quotes, insert em leads, inserts em activities, inserts em notifications. Use realtime para que se outra tela estiver aberta, ela atualize automaticamente.

## 5. `/admin/relatorios` (bonus se der tempo)

- RelatÃ³rios prÃ©-prontos: Receita por mÃªs, ComissÃµes por seguradora, Vendas por marca, Sinistralidade
- BotÃ£o exportar CSV / PDF

## 6. UI / UX

- Layout extremamente denso e profissional, tipo Linear / Vercel dashboards.
- Use `recharts` pra todos os grÃ¡ficos.
- Pra Sankey use `react-sankey` ou similar (se nÃ£o der, faz com barras horizontais conectadas).
- Cores consistentes: Webseg=navy, WebCar=amber, eventos cross-sell=violet.
- AnimaÃ§Ãµes sutis nas transiÃ§Ãµes do simulador (use `framer-motion` se possÃ­vel).
- O simulador de cross-sell Ã© a HÃ‰RO da demo â€” capricha, faz acontecer.


---

## 🤖 PROMPT 6 — CROSS-SELL + POLISH

# PROMPT 6 â€” CROSS-SELL LIVE + IA + POLISH FINAL

---

## Objetivo

Conectar tudo, fazer a automaÃ§Ã£o do cross-sell funcionar de verdade entre os portais (com realtime) e adicionar IA real onde fizer sentido. Polir a interface antes de mostrar pra cliente.

---

## 1. Edge Function â€” Cross-sell automÃ¡tico

Crie uma **Supabase Edge Function** chamada `trigger-cross-sell`:

```ts
// Recebe: { car_sale_id }
// Faz:
// 1. Busca car_sale + vehicle data
// 2. Cria quote no Webseg com:
//    - vehicle_data: { marca, modelo, ano, placa, preco }
//    - driver_data: { nome, cpf, idade calculada do data_nascimento, cep }
//    - origem_cross_sell: true
//    - car_sale_id
//    - resultados: array com 4 cotaÃ§Ãµes simuladas (Porto, Bradesco, Allianz, SulAmerica)
// 3. Cria lead se cliente novo
// 4. Cria notification pra todos corretores ativos
// 5. Cria notification pro cliente
// 6. Cria activities apropriadas
// 7. Cria mensagem mock no messages (WhatsApp simulado)
// 8. Atualiza car_sale com cross_sell_quote_id
// Retorna: { quote_id, lead_id, notifications_sent }
```

Chame essa function:
- Quando vendedor clica "Cotar seguro pra este cliente" no `/webcar/vendas/:id`
- Quando admin aperta "Simular venda" no `/admin/cross-sell`
- Quando uma `car_sale` muda etapa pra 'concluida' (idealmente trigger do Postgres, mas pode ser do front mesmo)

## 2. CÃ¡lculo de cotaÃ§Ã£o simulado (sem IA, funÃ§Ã£o pura)

```ts
function calcularCotacaoFake(vehicle, driver) {
  const basePrice = vehicle.preco_venda * 0.018  // ~1.8% do valor por ano
  const ageFactor = driver.idade < 25 ? 1.5 : driver.idade > 60 ? 1.2 : 1.0
  const yearFactor = vehicle.ano_modelo >= 2023 ? 1.1 : 1.0
  const cepRisk = 1.0  // pode randomizar
  
  const seguradoras = [
    { nome: 'Porto Seguro', mult: 1.0, nps: 4.6 },
    { nome: 'Bradesco', mult: 0.92, nps: 4.4 },
    { nome: 'Allianz', mult: 0.88, nps: 4.5 },
    { nome: 'SulAmerica', mult: 1.05, nps: 4.7 },
    { nome: 'Tokio Marine', mult: 0.95, nps: 4.3 },
    { nome: 'HDI', mult: 1.10, nps: 4.5 }
  ]
  
  return seguradoras.map(s => ({
    seguradora: s.nome,
    valor_anual: Math.round(basePrice * ageFactor * yearFactor * s.mult),
    valor_mensal: Math.round((basePrice * ageFactor * yearFactor * s.mult) / 12),
    franquia: Math.round(vehicle.preco_venda * 0.03),
    coberturas: { colisao: true, roubo: true, natureza: true, terceiros: 100000, app: true, carro_reserva: 15 },
    nps: s.nps,
    parcelas_max: 12
  }))
}
```

Use essa function em todos os cotadores (cliente, corretor, cross-sell).

## 3. IA real com Claude

Crie outra **Edge Function** chamada `ai-helper` que recebe:
```ts
{ action: 'summarize_client' | 'next_action' | 'generate_message' | 'objection_handling' | 'claim_dossier' | 'generate_contract' | 'fraud_score' | 'recommend_coverage', context: any }
```

Use a chave `ANTHROPIC_API_KEY` no Supabase secrets. Modelo: `claude-sonnet-4-6`.

**Prompts por aÃ§Ã£o:**

### `summarize_client`
System: "VocÃª Ã© um copiloto de corretor de seguros. Resuma o cliente em 3 bullets curtos pra preparar uma ligaÃ§Ã£o."
Context: nome, idade, apÃ³lices, sinistros, Ãºltimo contato, ticket
Output: 3 bullets

### `next_action`
System: "VocÃª Ã© estrategista de retenÃ§Ã£o em corretora. Sugira a prÃ³xima aÃ§Ã£o pra esse cliente."
Output: 1 aÃ§Ã£o concreta + justificativa em 2 linhas

### `generate_message`
System: "VocÃª Ã© especialista em WhatsApp pra corretores. Gere msg curta, em pt-BR, tom amigÃ¡vel e profissional, sem emoji."
Context: cliente, motivo, situaÃ§Ã£o
Output: 2-4 linhas pronto pra enviar

### `objection_handling`
System: "VocÃª Ã© treinador de vendas em seguros. DÃª 3 argumentos pra contornar a objeÃ§Ã£o."
Context: objeÃ§Ã£o do cliente, contexto
Output: 3 argumentos

### `claim_dossier`
System: "VocÃª Ã© regulador de sinistros. Estruture um dossiÃª profissional com as info dadas."
Context: tipo, local, data, descriÃ§Ã£o cliente, fotos disponÃ­veis
Output: dossiÃª em markdown com seÃ§Ãµes: Resumo, Partes envolvidas, SequÃªncia dos eventos, DocumentaÃ§Ã£o, RecomendaÃ§Ã£o

### `generate_contract`
System: "VocÃª Ã© advogado especialista em compra/venda automotiva. Gere contrato em pt-BR completo."
Context: vendedor, comprador, veÃ­culo, valor, condiÃ§Ãµes
Output: contrato completo em markdown

### `fraud_score`
System: "VocÃª Ã© analista anti-fraude. Avalie o sinistro e dÃª score 0-100 + 3 pontos de atenÃ§Ã£o."
Context: cliente, sinistro, histÃ³rico
Output: { score: number, alertas: string[], decisao_recomendada: string }

### `recommend_coverage`
System: "VocÃª Ã© consultor de seguros. Recomende coberturas ideais pra esse perfil."
Context: cliente, veÃ­culo, uso, condutores
Output: { lmi: number, franquia: 'reduzida'|'normal'|'dobrada', extras: string[], justificativa: string }

**No frontend:** crie hook `useAI()` que chama essa edge function e retorna loading + result.

Em cada lugar que mencionei "IA copiloto" ou "IA gera" nos prompts anteriores â†’ conecte com esse hook.

## 4. Realtime cross-portal

Subscribe nos seguintes canais por portal:

**Cliente:**
- `notifications` filtrado por user_id â†’ toast + atualiza badge
- `claims` prÃ³prios â†’ atualiza timeline
- `policies` prÃ³prias â†’ reage a renovaÃ§Ãµes

**Corretor:**
- `leads` (todos) â†’ atualiza kanban em tempo real
- `claims` â†’ atualiza painel
- `notifications` prÃ³prias
- `messages` (todas) â†’ atualiza WhatsApp central

**Vendedor:**
- `car_sales` â†’ atualiza pipeline
- `notifications` prÃ³prias

**Admin:**
- TUDO acima + `quotes` (pra ver cross-sells acontecendo)
- KPIs devem atualizar conforme dados mudam

## 5. WhatsApp simulado realista

Crie um componente `<WhatsAppMock>` que:
- Mostra UI estilo WhatsApp (verde primary, balÃµes cinza/verde, header com avatar)
- Quando uma `messages` Ã© inserida pro cliente, anima ela entrando na thread
- Tem som "ploft" sutil de notificaÃ§Ã£o (opcional)
- No portal cliente, mostra como notificaÃ§Ã£o push fake quando cross-sell acontece: card flutuante "ðŸ“± VocÃª recebeu uma nova mensagem da Webseg"

## 6. Polish visual

- Todos os carregamentos com `<Skeleton>` (shadcn) â€” nada de spinner branco
- Empty states com ilustraÃ§Ã£o SVG inline + CTA
- MicroanimaÃ§Ãµes com `framer-motion` em:
  - Cards entrando (fade + slide up)
  - Drag drop kanban (jÃ¡ vem com a lib)
  - Modal de sinistro IA (steps com slide horizontal)
  - Demo cross-sell (steps com slide e particles)
- Sons removidos exceto alerta crÃ­tico
- Dark mode polido (testar todas as telas em dark)
- Mobile responsivo (sidebar vira sheet, kanbans viram lista vertical scrollable)

## 7. Deploy

- Deploy via Lovable (ele expÃµe URL pÃºblica automÃ¡tica)
- Anotar URL final
- Testar todos 4 logins
- Testar fluxo completo: login admin â†’ simular venda â†’ ver chegando em real-time no portal cliente (em outra aba) e portal corretor (em outra aba)

## 8. PÃ¡gina `/landing` opcional

Antes do login, pÃ¡gina Ãºnica vendendo o WebHub:
- Hero: "WebHub â€” operaÃ§Ã£o digital completa do grupo Web"
- Pillar 1: WebCar digital
- Pillar 2: Webseg digital
- Pillar 3: Cross-sell automÃ¡tico
- VÃ­deo de 30s da demo
- BotÃ£o "Acessar plataforma" â†’ /login

---

## EntregÃ¡veis finais desse prompt

1. âœ… Edge Function `trigger-cross-sell` rodando no Supabase
2. âœ… Edge Function `ai-helper` rodando com Claude
3. âœ… Realtime sincronizando todos os portais
4. âœ… Demo cross-sell no admin **funcionando ao vivo**
5. âœ… IA conectada em pelo menos 5 pontos (sinistro, copiloto cliente, mensagem, contrato, fraude)
6. âœ… WhatsApp mock realista
7. âœ… Polish visual em todos os portais
8. âœ… Deploy pÃºblico no Lovable

**ApÃ³s esse prompt, a demo estÃ¡ pronta pra mostrar pro cliente.** O fluxo killer: abre 3 abas (admin / corretor / cliente), aperta "Simular venda" no admin, vÃª tudo se atualizando ao vivo.


