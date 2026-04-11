---
title: "Chatwoot self-hosted requer pgvector e Evolution API tem config interna"
type: licao
created: 2026-04-03
tags: [chatwoot, evolution-api, docker, postgresql, infraestrutura]
---

# Chatwoot e Evolution API — gotchas de instalação

## Chatwoot latest requer pgvector
A imagem `chatwoot/chatwoot:latest` exige a extensão `vector` no PostgreSQL.
A imagem padrão `postgres:15` não tem. Usar sempre:
```yaml
image: pgvector/pgvector:pg15
```

## Evolution API — hostname hardcoded
A Evolution API espera o PostgreSQL no hostname `postgres` (hardcoded no schema Prisma).
Solução: adicionar alias de rede no docker-compose:
```yaml
chatwoot-db:
  networks:
    default:
      aliases:
        - postgres
```

## Evolution API — variáveis corretas
- Variável: `DATABASE_CONNECTION_URI` (não `DATABASE_URL`)
- Usuário padrão: `user`
- Senha padrão: `pass`
- Banco: `evolution`

Criar manualmente no Postgres antes de subir:
```sql
CREATE DATABASE evolution;
CREATE USER "user" WITH PASSWORD 'pass';
GRANT ALL PRIVILEGES ON DATABASE evolution TO "user";
GRANT ALL ON SCHEMA public TO "user";
```

## Evolution API — API key de autenticação
Configurar via: `AUTHENTICATION_API_KEY`

## Como aplicar
Usar esse docker-compose como base para qualquer novo cliente.
