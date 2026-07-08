---
date: 2026-07-08 07:16:17
tags: [alerta, sistema]
---

# ⚠️ Watchers Offline

**Detectado em:** 2026-07-08 07:16:17

Os seguintes watchers estão sem heartbeat há mais de 120s:

- **Codex**
- **Antigravity**

## Como resolver

```powershell
pm2 list
pm2 restart all
```
