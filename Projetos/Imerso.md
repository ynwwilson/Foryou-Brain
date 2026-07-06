---
tipo: projeto
status: em desenvolvimento — MVP funcional
criado: 2026-05-13
stack: TanStack Start, Supabase, Cloudflare R2/Workers, Modal, PlayCanvas
repo: ynwwilson/imersohouses (privado)
---

# Imerso

> **entre antes de visitar.**

SaaS brasileiro que transforma scans 3D de imóveis (Gaussian Splatting) em **tours imersivos navegáveis compartilháveis pelo WhatsApp**. Foco em corretores e imobiliárias.

## Visão de produto

O corretor escaneia o imóvel pelo celular (app externo como Polycam/Scaniverse), sobe o arquivo `.ply` no Imerso, o sistema processa em ~2 minutos, gera um link público compartilhável, e o cliente abre o tour 3D direto no celular — **caminhando dentro do imóvel como num jogo, em primeira pessoa**, com tour cinematográfico automático opcional. Reduz visitas perdidas, qualifica leads antes da visita física.

**Referência do "WOW" do produto**: Reels do Denis Miyabara mostrando walkthrough cinematográfico de casa inteira em Gaussian Splat — câmera atravessa cômodos, sobe escadas, sai pro quintal, sem cortes.

## Por que existe

- Tours 360° (Matterport) são caros (~R$ 1.500-3.000 por imóvel com fotógrafo) e estáticos (teleporte entre fotos, não navegação livre)
- Gaussian Splatting entrega qualidade fotorrealística rodando 60 FPS no browser, mas até 2026 nenhum player no Brasil estava entregando isso com **workflow vertical pro corretor**
- Janela competitiva aberta: workflow brasileiro (PT-BR + PIX + WhatsApp + CRECI + integração corretor) ainda não foi tomada

## Modelo de negócio

- **Free**: 1 imóvel grátis pra testar
- **Avulso**: R$ 79 por imóvel (tour fica 6 meses online)
- **Plano Corretor**: R$ 149/mês, 5 imóveis ativos
- **Plano Imobiliária**: R$ 499/mês, 20 imóveis, multi-corretor
- Pagamento via PIX (Asaas)

Custo operacional por scan: ~R$ 0,30-0,50 (Modal CPU + R2 storage com zero egress). Margem ~99% no infra.

## Stack técnica

| Camada | Tech |
|---|---|
| Frontend | TanStack Start (Vite 7 + React 19 + SSR + Cloudflare Worker) |
| UI | Tailwind v4 + shadcn/ui (Radix) |
| Auth + DB | Supabase (Postgres + RLS + Auth) |
| Storage | Supabase Storage (buckets `imerso-uploads-raw`, `imerso-splats-final`, `imerso-capas`) |
| 3D Engine | `@playcanvas/react@0.11.3` + `playcanvas@2.18.1` |
| Processing | Modal.com (Python serverless, container com Node + `@playcanvas/splat-transform`) |
| Pagamento | Asaas PIX (Fase 9, ainda não plugado) |
| Email | Resend (Fase 10) |
| WhatsApp | wa.me links no MVP; Z-API/Evolution depois |
| Deploy | Cloudflare Workers Builds |
| Package manager | Bun |

## Arquitetura do pipeline real (Fase 4)

```
Browser do corretor
  ↓ 1. cria imóvel via form
  ↓ 2. clica "Subir scan", arrasta .ply
  ↓ 3. POST Modal /upload_url → recebe { scan_id, signed PUT URL }
  ↓ 4. PUT direto pro Supabase Storage (uploads-raw)
  ↓ 5. POST Modal /process → dispara worker async

Modal (Python container)
  ↓ baixa .ply do uploads-raw
  ↓ roda `splat-transform input.ply output.compressed.ply` (compressão pesada)
  ↓ upload pro splats-final (público CDN)
  ↓ atualiza scan.splat_url + scan.status='pronto'
  ↓ atualiza imovel.status='publicado'

Frontend
  ↓ polling do scan.status a cada 4s
  ↓ quando 'pronto': mostra "Tour pronto!"
  ↓ tour público em /r/[slug] abre splat real
```

**URLs Modal deployadas:**
- Upload: `https://ynwwilson--imerso-pipeline-upload-url.modal.run`
- Process: `https://ynwwilson--imerso-pipeline-process.modal.run`

## Modelo de dados (Supabase Postgres)

5 tabelas core, todas com RLS por `corretor_id = auth.uid()`:

- **corretor** — 1:1 com `auth.users`, trigger `handle_new_user` auto-cria no signup; auto-heal no client se faltar; default `imoveis_limite=100` (MVP)
- **imovel** — endereço flat em colunas (não JSONB) pra suportar filtros UF/cidade; `valor_centavos: bigint` (nunca float pra dinheiro); slug único com UUID v4 anti-colisão
- **scan** — histórico de scans por imóvel; `arquivo_raw_path`, `splat_url`, `tamanho_bytes`, `custo_gpu_centavos`, `progresso_pct`, `processado_em`
- **tour_view** — LGPD-friendly: armazena hash SHA256 do IP+UA, nunca IP cru; trigger `update_imovel_analytics` denormaliza views_total no imóvel
- **pagamento** — vinculado ao corretor + opcionalmente imóvel; mutações apenas via service_role (webhook Asaas)
- **tour_path** — waypoints JSONB pra Cinematic Tour automático; 1 path ativo por imóvel (unique index parcial)

## Funcionalidades já entregues (MVP funcional)

### Auth e onboarding
- Signup/login/logout/reset password (Supabase Auth)
- Onboarding modal de 3 passos no primeiro acesso (persiste em localStorage)
- Tutorial completo em `/tutorial` (4 etapas + 6 dicas + checklist)

### Dashboard do corretor
- Lista de imóveis com cards (thumb + status + views)
- Criar imóvel: form completo com CEP autocomplete via ViaCEP real, upload de capa via Supabase Storage, valor com máscara R$, validação por campo
- Editar imóvel: form pré-preenchido funcional
- Editar perfil: nome/telefone/CRECI persistido no DB
- Publicar/despublicar tour

### Pipeline de scan
- Upload real de `.ply`/`.compressed.ply`/`.splat`/`.ksplat` via drag-and-drop (até 2GB)
- Progress bar de upload + processing
- Polling de status a cada 4s
- Fallback "Simular processamento" com splat demo (caveira da PlayCanvas) pra testes sem subir arquivo

### Cinematic Tour System (Fase 4.5)
3 modos de viewer no `SplatViewer.tsx`:
- **Cinematic**: anima câmera via Catmull-Rom spline + slerp entre waypoints, smoothstep easing, pause/play
- **Fly**: navegação primeira pessoa (WASD + dual joystick mobile half-screen)
- **Orbit**: gira ao redor (default sem waypoints)

**Path Editor** em `/imoveis/$id/tour-path`: splat fullscreen, corretor caminha + clica "Adicionar waypoint", painel lateral com lista (label editável, slider duração, mover ↑↓, remover), Preview alterna pra cinematic, Salvar via mutation.

### Tour público (página viral)
- `/r/[slug]` com SSR + OG tags dinâmicas absolutas (preview rico no WhatsApp)
- Hero com foto + valor grande + ficha técnica em pills
- CTA gigante "Iniciar Tour 3D" abre modal com viewer
- Float WhatsApp persistente com mensagem pré-pronta contextualizada
- Tracking automático de view (LGPD via hash IP)

## Problemas conhecidos e débitos técnicos

### Navegação interior incompleta
O fly mode atual deixa câmera atravessar paredes. Faltam:
- Collision mesh automático a partir do splat
- Walk mode com altura humana fixa (1.6m) e velocidade de caminhada (1.4 m/s)
- Camera presets ("exploração livre", "andar pela sala", "tour guiado", "foco em planta")
- Detecção automática de chão/piso
- Teleporte entre cômodos via hotspots

Status: **pesquisando soluções open-source antes de implementar** (Deep Research em andamento).

### Deprecation warnings PlayCanvas
`@playcanvas/react@0.11.3` usa APIs deprecadas da `playcanvas@2.18.1` (CameraComponent#onPreCull/onPostRender etc). Funciona, mas console fica com 11 errors vermelhos. Resolver: downgrade engine pra `~2.11.x` ou aguardar `@playcanvas/react` atualizar.

### Outros débitos
- Faltam Cloudflare Queues entre upload e Modal (resiliência)
- Sem 4 artefatos por scan (delivery splat / poster / collision mesh / scene.json) — só 1 hoje
- Banco não está abstrato pra suportar SPZ (Niantic, 10x menor que PLY) — futuro
- `routeTree.gen.ts` precisa regenerar manualmente às vezes
- App nativo iOS com captura ARKit + LiDAR + RoomPlan guidance está pra Fase 3 do roadmap (~3 meses)

## Estado atual das fases (commits no repo `ynwwilson/imersohouses`)

✅ **Fase 0** — Recursos externos (GitHub, Supabase, Lovable, Modal)
✅ **Fase 1** — Bootstrap TanStack Start via Lovable
✅ **Fase 2** — Schema Postgres + RLS aplicado
✅ **Fase 3** — Auth flow real plugado
✅ **Fase 4** — Pipeline Modal + Supabase Storage (deployado e funcional)
⏳ **Fase 4.5** — Cinematic Tour System (entregue, falta walk mode com colisão)
✅ **Fase 6** — Fork/customização do viewer (SplatViewer próprio com `@playcanvas/react` direto)
✅ **Fase 7** — Página pública `/r/[slug]` plugada no DB
✅ **Fase 8** — Dashboard CRUD completo
⏳ **Fase 9** — Asaas PIX
⏳ **Fase 10** — Notificações Resend + WhatsApp
⏳ **Fase 11** — Deploy produção (domínio `imerso.com.br`)
⏳ **Fase 12** — Onboarding piloto com 3 corretores

## Resultado final esperado (vision 12-18 meses)

1. Corretor abre app Imerso no iPhone Pro
2. **Captura nativa com ARKit + LiDAR + AR overlay** (Apple RoomPlan pra guidance)
3. Score de qualidade da captura antes do upload
4. Pre-processamento on-device (só frames-chave + poses enviadas)
5. Server processa em 2 minutos via Modal + splat-transform
6. Tour pronto, push notification
7. 1 toque → manda no WhatsApp pro cliente
8. Cliente abre, navega em 1ª pessoa pelo imóvel
9. Float WhatsApp dentro do tour com mensagem contextualizada
10. Dashboard mostra analytics: views, tempo médio, dispositivo, último visitante
11. **V2**: AI staging (mobília virtual em imóvel vazio), agente IA de tour ("essa sala tem sol da manhã?"), auto-listing (descrição + ficha + preço sugerido)
12. **V3**: Integração ZapImóveis/VivaReal (embed tour no anúncio do portal)

## Decisões importantes tomadas

- **iOS-first**: app nativo só pra iPhone no MVP, Android depois
- **Single-app** TanStack Start (não monorepo); dashboard + tour público no mesmo Worker
- **PlayCanvas direto** (`@playcanvas/react`), não `@playcanvas/blocks` (que tá bugado v0.3.7)
- **Captura externa via Polycam/Scaniverse no MVP**; app nativo só na Fase 3
- **Supabase Storage** em vez de Cloudflare R2 inicialmente (zero setup novo; migra depois quando egress doer)
- **Endereço flat** em colunas (não JSONB) pra suportar filtros UF/cidade
- **Valor em centavos** (bigint) — nunca float pra dinheiro
- **LGPD**: tour_view armazena hash SHA256 de IP+UA, nunca IP cru
- **slug com UUID v4** anti-colisão (epoch + random)
- **Retry automático** de INSERT em caso de unique violation
- **traduzErroSupabase** centraliza tradução de erros PostgreSQL pra pt-BR

## Onde fica o que

- **Código**: `C:\Users\ynwwi\Projects\imersohouses\` (repo: `ynwwilson/imersohouses` privado)
- **Modal app**: `modal.com/apps/ynwwilson/main/deployed/imerso-pipeline`
- **Supabase**: `qrpousllojxmvgldqeil.supabase.co` (região `sa-east-1`)
- **Preview Lovable**: `imersohouses.lovable.app`
- **Conta de teste**: wilsonads.ia@gmail.com

## Próximo movimento

Aguardando resultado do **Deep Research v2** pra decidir entre:
1. Adotar lib open-source pronta com walk mode + collision (se existir)
2. Construir walk mode + collision do zero (vira moat)
3. Trocar Polycam por Scaniverse como recomendação principal pro corretor (free + on-device)

Após decidir, implementar walk mode antes de seguir pras Fases 9-11 (cobrança + deploy + piloto).

---

## Links relacionados

- [[ForYou Code]] — empresa que está construindo Imerso
- [[Pipeline Comercial 2026]]
- [[Smartcell]] — case similar de produto da ForYou
