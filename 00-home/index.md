---
tipo: home
atualizado: 2026-03-25
---

# Stark — Cérebro do Mestre

> Vault pessoal de Mestre · Co-fundador da ForYou Code · Sistema Jarvis

---

## Estado do Jarvis

- [x] CLAUDE.md criado
- [x] Memória automática ativada
- [x] Vault Stark configurado
- [ ] MCPs instalados (smart-connections, qmd)
- [ ] brain-ingest rodado nas primeiras fontes
- [ ] Primeiro agente Telegram funcional
- [ ] VPS configurado (Hetzner ou Oracle Cloud)

---

## Clientes ativos

```dataview
TABLE status AS "Status", file.link AS "Cliente"
FROM "knowledge"
WHERE contains(tags, "cliente") AND contains(tags, "ativo")
SORT file.name ASC
```

---

## Em construção

```dataview
TABLE file.link AS "Projeto"
FROM "knowledge"
WHERE contains(tags, "em-construcao")
SORT file.name ASC
```

---

## Últimas sessões

```dataview
TABLE data AS "Data", foco AS "Foco"
FROM "sessions"
WHERE tipo = "sessao"
SORT data DESC
LIMIT 5
```

---

## Notas atualizadas recentemente

```dataview
TABLE file.mtime AS "Atualizado"
FROM "knowledge" OR "atlas"
SORT file.mtime DESC
LIMIT 8
```

---

## Navegação do vault

| Seção | Para que serve |
|---|---|
| [[atlas/vault-information-arch\|Arquitetura do vault]] | Como o vault está organizado |
| [[atlas/Mapa de clientes\|Mapa de clientes]] | Todos os clientes com status e receita |
| [[atlas/Mapa do sistema de conteudo\|Sistema de conteúdo]] | Personas, funil, canais |
| [[atlas/Decisoes de stack da ForYou Code\|Decisões de stack]] | Stack técnica definida |
| [[inbox/queue\|Inbox]] | Capturar antes de organizar |
| [[00-home/top-of-mind\|Top of Mind]] | O que está quente agora |

---

## Canvas visuais

- [[atlas/Ecossistema ForYou Code|Ecossistema ForYou Code]]
- [[atlas/Arquitetura do Jarvis|Arquitetura do Jarvis]]
- [[atlas/Funil TOF-MOF-BOF|Funil TOF / MOF / BOF]]
