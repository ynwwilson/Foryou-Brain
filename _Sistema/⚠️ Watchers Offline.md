---
date: 2026-07-06 21:13:24
tags: [alerta, sistema]
---

# ⚠️ Watchers Offline

**Detectado em:** 2026-07-06 21:13:24

Os seguintes watchers estão sem heartbeat há mais de 120s:

- **Codex**
- **Antigravity**

## Como resolver

```powershell
pm2 list
pm2 restart all
```
