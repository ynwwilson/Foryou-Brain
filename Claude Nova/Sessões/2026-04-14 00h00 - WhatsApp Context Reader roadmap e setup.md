# WhatsApp Context Reader — Sessão 2026-04-14

## Objetivo
Montar um sistema capaz de ler conversas completas do WhatsApp — incluindo texto, áudio, imagem e vídeo — e entregar contexto total ao Claude para análise, resumo e entendimento de qualquer conversa ou grupo.

---

## O que foi feito

### Pesquisa de capacidades (Claude Code)
- Levantamento completo das capacidades multimodais do Claude em abril/2026
- Claude processa texto e imagens nativamente; áudio e vídeo precisam de pipeline externo
- Descoberta do **WhatsApp MCP** (`lharries/whatsapp-mcp`) — MCP server em Go que conecta via WhatsApp Web multidevice API, sincroniza mensagens em SQLite local
- Levantamento do **Claude Cowork + Dispatch** (lançado março 2026) — computer use disponível
- Conclusão: imagens funcionam nativamente; áudio precisa Whisper; vídeo precisa ffmpeg + Whisper

### Roadmap criado
Arquivo salvo em: `C:/Users/ynwwi/Projects/whatsapp-context/ROADMAP.md`

**5 fases:**

| Fase | Descrição |
|---|---|
| 0 — Setup | mingw, ffmpeg, faster-whisper, build bridge, QR code |
| 1 — MVP | Texto + imagens via MCP funcionando |
| 2 — Áudio | `faster-whisper` model `tiny`, auto-transcreve .ogg, cache em SQLite |
| 3 — Vídeo leve | ffmpeg extrai 1 frame/30s + áudio → Whisper, resultado: frames + transcrição |
| 4 — Assembler | `get_full_context()` empacota conversa inteira cronológica, resolvendo todos os tipos de mídia |
| 5 — Serviço | bridge como Windows service (NSSM) |

### Arquitetura definida
```
whatsapp-bridge (Go) → SQLite local
    ↓
processor/audio.py (faster-whisper)
processor/video.py (ffmpeg + faster-whisper)
    ↓
whatsapp-mcp-server/main.py (Python MCP estendido)
    ↓
Claude Code — get_full_context()
```

**Novas tabelas SQLite:**
- `media_transcriptions` — cache de transcrições de áudio/vídeo
- `media_keyframes` — cache de frames extraídos de vídeos

### Ambiente do usuário verificado
- Go 1.26.1 ✅
- Python 3.12.8 ✅
- Node 24.14.1 ✅
- Chocolatey ✅
- gcc/mingw ❌ (precisa instalar)
- ffmpeg ❌ (precisa instalar)
- faster-whisper ❌ (precisa instalar)

---

## O que ficou pendente

### Setup manual (usuário)
```bash
# 1 — gcc
choco install mingw -y  # reiniciar terminal depois

# 2 — ffmpeg
choco install ffmpeg -y

# 3 — Python deps
pip install faster-whisper

# 4 — Build bridge
git clone https://github.com/lharries/whatsapp-mcp.git ~/Projects/whatsapp-mcp
cd ~/Projects/whatsapp-mcp/whatsapp-bridge
CGO_ENABLED=1 go build -o whatsapp-bridge.exe .

# 5 — Autenticar (precisa do celular para QR code)
./whatsapp-bridge.exe

# 6 — Registrar MCP
claude mcp add whatsapp -- python ~/Projects/whatsapp-mcp/whatsapp-mcp-server/main.py
```

### Implementação (Codex ou Claude Code)
- `processor/audio.py` — faster-whisper, `get_or_transcribe()`
- `processor/video.py` — ffmpeg keyframes + transcrição
- Schema SQL (2 tabelas novas)
- Extensão do `whatsapp-mcp-server/main.py` com transcrição automática e `get_full_context()`

### MCP Obsidian
- Estava retornando erro 40101 (Authorization required) durante esta sessão
- Fix identificado: falta `OBSIDIAN_API_KEY` no config do MCP em `~/.claude-nova/settings.json`

---

## Decisões técnicas
- **faster-whisper modelo `tiny`** — 39MB, CPU, 4x mais rápido que openai/whisper. Trocar para `base` se qualidade PT-BR insuficiente
- **1 frame a cada 30s** — vídeo de 3min → 6 imagens + transcrição. Leve e suficiente
- **Cache em SQLite** — processa uma vez, nunca reprocessa
- **1M tokens de contexto** do Opus 4.6 — cabe meses de conversa numa sessão

---

## Tempo estimado para conclusão
- Setup manual: ~12 min
- Implementação do código: ~15 min (paralelo com setup)
- Testes: ~10 min
- **Total: ~25 minutos** após início do setup

---

*Sessão: Claude Nova | Data: 2026-04-14*
