---
date: 2026-05-04 23h15
fim: 2026-05-04 23:56:01
tool: claude-nova
title: "confirma o setup do video vision"
session_id: 79f08a13-a23f-454a-b798-0d4987df07f8
tags: [claude-nova, sessão]
---

# confirma o setup do video vision

> **Ferramenta:** Claude Nova · **Início:** 2026-05-04 23h15 · **Fim:** 2026-05-04 23:56:01
> **Dir:** `C:\Users\ynwwi`

## Objetivo
só fechar e abrir, e como uso esse plugin da melhor forma?

## Conversa

**Mestre:** confirma o setup do video vision
> 23:15

---

**Mestre:** só fechar e abrir, e como uso esse plugin da melhor forma?
> 23:29

**Claude Nova:** Sim — fecha e abre o Claude Code (não basta `/reload-plugins`, tem que matar o processo todo pra herdar o PATH novo). Depois rode `video_setup` de novo só pra confirmar "OK". ## Como usar bem **As 4 tools do plugin (do mais leve pro mais pesado):** | Tool | Quando usar | Custo | |---|---|---| | `video_info` | "que vídeo é esse?" — duração, resolução, codec | grátis (só ffprobe) | | `video_watch` | uso padrão — ver + transcrever | médio (frames + áudio) | | `video_analyze` | pergunta específica sobre o vídeo | médio | | `video_detail` | precisa de alta fidelidade visual (ex: ler texto na tela, contar objetos) | alto (mais frames) | **Fluxo recomendado:** 1. **Sempre comece com `video_info`** se o vídeo tem mais de ~2 min — pra eu saber se vale extrair tudo ou recortar um trecho. 2. **`video…
> 23:29

---

**Mestre:** sim
> 23:30

---

**Mestre:** você consegue ver o que o ta acontecendo na nota "Roadmap Site ForYou Code — v1"?
> 23:53

---

**Mestre:** e voce sabe o que tava acontecendo? consegue escrever os prompts?
> 23:55

---

