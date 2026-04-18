---
date: 2026-04-18 13:51:42
tags: [alerta, sistema]
---

# ⚠️ Watchers Offline

**Detectado em:** 2026-04-18 13:51:42

Os seguintes watchers estão sem heartbeat há mais de 120s:

- **Codex**
- **Antigravity**

## Como resolver

```powershell
pm2 list
pm2 restart all
```
