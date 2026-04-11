---
title: "Terminal browser Hostinger quebra comandos longos"
type: licao
created: 2026-04-03
tags: [vps, hostinger, ssh, terminal, infraestrutura]
---

# Terminal browser Hostinger quebra comandos longos

## O problema
O terminal web da Hostinger insere quebras de linha físicas ao colar texto longo. Isso faz o bash interpretar cada fragmento como um comando separado — corrompendo heredocs, base64, comandos encadeados com `&&`.

## A solução definitiva
Habilitar SSH com chave ed25519 e gerenciar o VPS diretamente:

```bash
# Na máquina local — gera par de chaves
ssh-keygen -t ed25519 -f ~/.ssh/concretize_vps -N ""

# No terminal do Hostinger — cola a chave pública
mkdir -p ~/.ssh && echo "CHAVE_PUBLICA" >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys

# Conectar daqui
ssh -i ~/.ssh/concretize_vps root@IP_DO_VPS "comando"
```

## Bloqueios adicionais da Hostinger
- `PasswordAuthentication no` está em `/etc/ssh/sshd_config.d/60-cloudimg-settings.conf` (sobrescreve o config principal)
- PAM bloqueado por padrão — chave é mais confiável que senha

## Como aplicar
Sempre que for usar VPS da Hostinger: configure SSH por chave ANTES de tentar qualquer automação.
