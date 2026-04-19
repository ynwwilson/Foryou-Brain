---
date: 2026-04-19 01:33:46
tags: [alerta, sistema]
---

# ⚠️ Watchers Offline

**Detectado em:** 2026-04-19 01:33:46

Os seguintes watchers estão sem heartbeat há mais de 120s:

- **Codex**
- **Antigravity**

## Como resolver

```powershell
pm2 list
pm2 restart all
```
