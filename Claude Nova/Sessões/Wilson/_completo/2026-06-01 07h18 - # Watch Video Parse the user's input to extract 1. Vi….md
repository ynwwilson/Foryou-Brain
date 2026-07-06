---
date: 2026-06-01 07h18
fim: 2026-06-01 07:40:23
tool: claude-nova
title: "# Watch Video Parse the user's input to extract 1. Vi…"
session_id: 5582116b-dfcc-4884-a016-ef04ad88e588
tags: [claude-nova, sessão, completo]
---

# # Watch Video Parse the user's input to extract 1. Vi…

> **Ferramenta:** Claude Nova · **Início:** 2026-06-01 07h18 · **Fim:** 2026-06-01 07:40:23
> **Dir:** `C:\Users\ynwwi`

## Objetivo
# Watch Video  Parse the user's input to extract: 1. **Vi…

## Conversa

**Mestre:** <command-message>claude-video-vision:watch-video</command-message> <command-name>/claude-video-vision:watch-video</command-name>
> 07:18

---

**Mestre:** # Watch Video  Parse the user's input to extract: 1. **Video path** — the file path (required) 2. **Prompt** — any question or instruction about the video (optional) 3. **Flags** — `--fps <number>`, `--resolution <number>` (optional)  Then follow this workflow **in order — do NOT skip step 2**:  1. Call `video_info` on the path to verify it's a valid video and get duration.  2. **REQUIRED for videos > 30s:** Call `video_analyze` BEFORE `video_watch`. This is NOT optional.    Use filters: `scene_changes: true, silence: true, transcription: true` at minimum.    Add other filters based on the user's question (motion, blur, exposure, loudness, etc.).    The analysis tells you WHERE to look — use it to plan smart frame extraction.  3. Call `video_watch`:    - **Short videos (< 2 min):** Use `fps: "auto"` without `view_sample` — full coverage to avoid missing brief moments.    - **Long videos (> 2 min):** Use `segments` with variable FPS based on analysis data. Use `view_sample` to limit initial frames.  4. If the user asks for more detail on a specific moment, use `video_detail` to drill in with higher FPS/resolution on a 3-5 second window. Use `view_sample: 3` first, then request specific timestamps.  5. If the user provided a prompt/question, answer it based on the video content. 6. If no prompt was provided, give a comprehensive summary of what happens in the video.  If `video_watch` fails with a setup error, call `video_setup` first, then retry.
> 07:18

---

**Mestre:** <command-message>claude-video-vision:watch-video</command-message> <command-name>/claude-video-vision:watch-video</command-name> <command-args>"C:\Users\ynwwi\Downloads\dayane1.mp4" veja o video da dayane, do projeto salinha, metodo rainha da aprovacao, entenda o que ela ta falando, do que ela ta falando, transcreva, explique bem contexto de audio e visual e me fale o que ta acontecendo com tudo separado, transcrição, visual, o que acontece, termos tecnicos, etc</command-args>
> 07:19

---

**Mestre:** # Watch Video  Parse the user's input to extract: 1. **Video path** — the file path (required) 2. **Prompt** — any question or instruction about the video (optional) 3. **Flags** — `--fps <number>`, `--resolution <number>` (optional)  Then follow this workflow **in order — do NOT skip step 2**:  1. Call `video_info` on the path to verify it's a valid video and get duration.  2. **REQUIRED for videos > 30s:** Call `video_analyze` BEFORE `video_watch`. This is NOT optional.    Use filters: `scene_changes: true, silence: true, transcription: true` at minimum.    Add other filters based on the user's question (motion, blur, exposure, loudness, etc.).    The analysis tells you WHERE to look — use it to plan smart frame extraction.  3. Call `video_watch`:    - **Short videos (< 2 min):** Use `fps: "auto"` without `view_sample` — full coverage to avoid missing brief moments.    - **Long videos (> 2 min):** Use `segments` with variable FPS based on analysis data. Use `view_sample` to limit initial frames.  4. If the user asks for more detail on a specific moment, use `video_detail` to drill in with higher FPS/resolution on a 3-5 second window. Use `view_sample: 3` first, then request specific timestamps.  5. If the user provided a prompt/question, answer it based on the video content. 6. If no prompt was provided, give a comprehensive summary of what happens in the video.  If `video_watch` fails with a setup error, call `video_setup` first, then retry. ARGUMENTS: "C:\Users\ynwwi\Downloads\dayane1.mp4" veja o video da dayane, do projeto salinha, metodo rainha da aprovacao, entenda o que ela ta falando, do que ela ta falando, transcreva, explique bem contexto de audio e visual e me fale o que ta acontecendo com tudo separado, transcrição, visual, o que acontece, termos tecnicos, etc
> 07:19

---

**Mestre:** <command-message>claude-video-vision:watch-video</command-message> <command-name>/claude-video-vision:watch-video</command-name>
> 07:39

---

**Mestre:** # Watch Video  Parse the user's input to extract: 1. **Video path** — the file path (required) 2. **Prompt** — any question or instruction about the video (optional) 3. **Flags** — `--fps <number>`, `--resolution <number>` (optional)  Then follow this workflow **in order — do NOT skip step 2**:  1. Call `video_info` on the path to verify it's a valid video and get duration.  2. **REQUIRED for videos > 30s:** Call `video_analyze` BEFORE `video_watch`. This is NOT optional.    Use filters: `scene_changes: true, silence: true, transcription: true` at minimum.    Add other filters based on the user's question (motion, blur, exposure, loudness, etc.).    The analysis tells you WHERE to look — use it to plan smart frame extraction.  3. Call `video_watch`:    - **Short videos (< 2 min):** Use `fps: "auto"` without `view_sample` — full coverage to avoid missing brief moments.    - **Long videos (> 2 min):** Use `segments` with variable FPS based on analysis data. Use `view_sample` to limit initial frames.  4. If the user asks for more detail on a specific moment, use `video_detail` to drill in with higher FPS/resolution on a 3-5 second window. Use `view_sample: 3` first, then request specific timestamps.  5. If the user provided a prompt/question, answer it based on the video content. 6. If no prompt was provided, give a comprehensive summary of what happens in the video.  If `video_watch` fails with a setup error, call `video_setup` first, then retry.
> 07:39

---

**Mestre:** <command-message>claude-video-vision:watch-video</command-message> <command-name>/claude-video-vision:watch-video</command-name> <command-args>"C:\Users\ynwwi\Downloads\Você perde o código, a IA refaz. Você perde o banco de dados, você declara falência. @jonathan_k.mp4" transcreva esse video</command-args>
> 07:39

---

**Mestre:** # Watch Video  Parse the user's input to extract: 1. **Video path** — the file path (required) 2. **Prompt** — any question or instruction about the video (optional) 3. **Flags** — `--fps <number>`, `--resolution <number>` (optional)  Then follow this workflow **in order — do NOT skip step 2**:  1. Call `video_info` on the path to verify it's a valid video and get duration.  2. **REQUIRED for videos > 30s:** Call `video_analyze` BEFORE `video_watch`. This is NOT optional.    Use filters: `scene_changes: true, silence: true, transcription: true` at minimum.    Add other filters based on the user's question (motion, blur, exposure, loudness, etc.).    The analysis tells you WHERE to look — use it to plan smart frame extraction.  3. Call `video_watch`:    - **Short videos (< 2 min):** Use `fps: "auto"` without `view_sample` — full coverage to avoid missing brief moments.    - **Long videos (> 2 min):** Use `segments` with variable FPS based on analysis data. Use `view_sample` to limit initial frames.  4. If the user asks for more detail on a specific moment, use `video_detail` to drill in with higher FPS/resolution on a 3-5 second window. Use `view_sample: 3` first, then request specific timestamps.  5. If the user provided a prompt/question, answer it based on the video content. 6. If no prompt was provided, give a comprehensive summary of what happens in the video.  If `video_watch` fails with a setup error, call `video_setup` first, then retry. ARGUMENTS: "C:\Users\ynwwi\Downloads\Você perde o código, a IA refaz. Você perde o banco de dados, você declara falência. @jonathan_k.mp4" transcreva esse video
> 07:39

---

