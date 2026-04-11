---
tipo: atlas
atualizado: 2026-03-25
---

# Arquitetura do Vault Stark

> Como este vault está organizado e por quê.

---

## Estrutura de pastas

```
Stark/
├── 00-home/
│   ├── index.md          → Dashboard central — começa aqui
│   └── top-of-mind.md    → Prioridades e foco atual
│
├── atlas/
│   ├── vault-information-arch.md   → Este arquivo
│   ├── Projetos ativos.md          → Mapa de todos os projetos e clientes
│   └── Decisoes de stack da ForYou Code.md  → Stack técnica definida
│
├── inbox/
│   └── queue.md          → Captura rápida — processar depois
│
├── knowledge/            → Fatos permanentes e estruturados
│   ├── [um arquivo por conceito]
│   └── ...
│
├── sessions/             → Log de sessões de trabalho (AAAA-MM-DD.md)
│
└── voice-notes/          → Notas de voz transcritas
```

---

## Fluxo de captura

```
Ideia / decisão / informação nova
    ↓
inbox/queue.md  (jogou rápido, sem pensar)
    ↓
Processa → vai para knowledge/, atlas/ ou sessions/
    ↓
inbox fica vazio
```

---

## Regras do vault

1. **Inbox é temporário** — nada fica lá mais de 48h
2. **Knowledge é permanente** — só entra o que é verdade duradoura
3. **Sessions são cronológicas** — uma por sessão de trabalho, nome = data
4. **Atlas é mapa** — liga conceitos, não armazena detalhes
5. **index.md é o ponto de entrada** — sempre atualizado com estado real

---

## Conexão com o Jarvis (Claude Code)

O vault é a **Camada 2** do sistema Jarvis.
- Camada 1: CLAUDE.md + autoMemory em `~/.claude/memory/`
- Camada 2: Este vault — conhecimento estruturado e navegável
- Camada 3 (pendente): brain-ingest para processar vídeo e áudio

Claude Code acessa este vault via MCPs (a instalar: smart-connections, qmd).
