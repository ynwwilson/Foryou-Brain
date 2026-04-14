#!/usr/bin/env node
/**
 * session-saver.js
 * Hook: Stop + PostToolUse
 * Salva cada sessão do Claude (conta 1 ou Nova) em nota individual no vault Obsidian.
 * Uma nota por sessão: Claude 1/Sessões/YYYY-MM-DD HHhMM - {título}.md
 */

'use strict';

const fs   = require('fs');
const path = require('path');
const os   = require('os');

// ── Config ────────────────────────────────────────────────────────────────────

const CONFIG_PATH = path.join(os.homedir(), '.session-saver', 'config.json');
const CACHE_DIR   = path.join(os.homedir(), '.session-saver', 'cache');
const HB_CODEX    = path.join(os.homedir(), '.session-saver', 'heartbeat-codex.json');
const HB_ANTGRAV  = path.join(os.homedir(), '.session-saver', 'heartbeat-antigravity.json');

function loadConfig() {
  try {
    return JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
  } catch (_) {
    return {
      vaultPath: 'C:/Users/ynwwi/Projects/claude-novo/stark/Stark',
      tools: {
        claude1:       { folder: 'Claude 1',    name: 'Claude'       },
        'claude-nova': { folder: 'Claude Nova', name: 'Claude Nova'  }
      },
      maxTextLength: 400,
      maxExchanges:  6,
      heartbeatMaxAge: 120000
    };
  }
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function pad(n) { return String(n).padStart(2, '0'); }

function formatDatetime(d) {
  return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())} ` +
         `${pad(d.getHours())}h${pad(d.getMinutes())}`;
}

function formatTimestamp(d) {
  return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())} ` +
         `${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
}

function sanitizeFilename(str) {
  return str
    .replace(/[<>:"/\\|?*\x00-\x1f]/g, '')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, 60);
}

function trunc(text, max) {
  const t = (text || '').replace(/\n+/g, ' ').trim();
  return t.length <= max ? t : t.slice(0, max) + '…';
}

function extractText(content) {
  if (!content) return '';
  if (typeof content === 'string') return content.trim();
  if (Array.isArray(content)) {
    return content
      .filter(c => c && c.type === 'text')
      .map(c => (c.text || '').trim())
      .join('\n')
      .trim();
  }
  return '';
}

function extractTools(content) {
  if (!Array.isArray(content)) return [];
  return content.filter(c => c && c.type === 'tool_use').map(c => c.name);
}

function hasRealText(content) {
  if (!content) return false;
  if (typeof content === 'string') {
    const t = content.trim();
    return t.length > 0 && !t.startsWith('<local-command-caveat>');
  }
  if (Array.isArray(content)) {
    return content.some(x => {
      if (!x || x.type !== 'text') return false;
      const t = (x.text || '').trim();
      return t.length > 0 && !t.startsWith('<local-command-caveat>');
    });
  }
  return false;
}

// ── Account detection ─────────────────────────────────────────────────────────

function detectAccount(transcriptPath) {
  if (!transcriptPath) return 'claude1';
  const p = transcriptPath.replace(/\\/g, '/');
  if (p.includes('/.claude-nova/') || p.includes('\\.claude-nova\\')) return 'claude-nova';
  return 'claude1';
}

// ── Cache (byte-position + note path per session) ─────────────────────────────

function getCachePath(sessionId) {
  return path.join(CACHE_DIR, `${sessionId}.json`);
}

function readCache(sessionId) {
  try {
    return JSON.parse(fs.readFileSync(getCachePath(sessionId), 'utf8'));
  } catch (_) {
    return { bytePos: 0, notePath: null, title: null };
  }
}

function writeCache(sessionId, data) {
  try {
    fs.mkdirSync(CACHE_DIR, { recursive: true });
    atomicWrite(getCachePath(sessionId), JSON.stringify(data));
  } catch (_) {}
}

// ── Atomic write ──────────────────────────────────────────────────────────────

function atomicWrite(destPath, content) {
  const tmpPath = `${destPath}.tmp.${process.pid}.${Date.now()}`;
  fs.writeFileSync(tmpPath, content, 'utf8');
  fs.renameSync(tmpPath, destPath);
}

// ── JSONL parsing (new lines only) ────────────────────────────────────────────

function parseNewLines(transcriptPath, fromByte) {
  if (!fs.existsSync(transcriptPath)) return { entries: [], newBytePos: fromByte };

  const stat = fs.statSync(transcriptPath);
  if (stat.size <= fromByte) return { entries: [], newBytePos: fromByte };

  const fd = fs.openSync(transcriptPath, 'r');
  const buf = Buffer.alloc(stat.size - fromByte);
  const bytesRead = fs.readSync(fd, buf, 0, buf.length, fromByte);
  fs.closeSync(fd);

  const chunk = buf.slice(0, bytesRead).toString('utf8');
  const entries = [];

  for (const line of chunk.split('\n')) {
    const trimmed = line.trim();
    if (!trimmed) continue;
    // Strip BOM if present
    const clean = trimmed.replace(/^\uFEFF/, '');
    try {
      entries.push(JSON.parse(clean));
    } catch (_) {}
  }

  return { entries, newBytePos: fromByte + bytesRead };
}

// ── Build full pairs from transcript ─────────────────────────────────────────

function buildPairs(transcriptPath, cfg) {
  if (!fs.existsSync(transcriptPath)) return { pairs: [], firstUserMsg: '', startTs: null };

  let raw;
  try {
    raw = fs.readFileSync(transcriptPath, 'utf8').replace(/^\uFEFF/, '');
  } catch (_) { return { pairs: [], firstUserMsg: '', startTs: null }; }

  const entries = raw.trim().split('\n').map(l => {
    try { return JSON.parse(l.trim()); } catch (_) { return null; }
  }).filter(Boolean);

  const allOrdered = entries.filter(e =>
    (e.type === 'user' || e.type === 'assistant') && e.message?.content
  );

  const pairs = [];
  for (let i = 0; i < allOrdered.length; i++) {
    const e = allOrdered[i];
    if (e.type !== 'user') continue;
    if (!hasRealText(e.message.content)) continue;

    let a = null;
    for (let j = i + 1; j < allOrdered.length; j++) {
      if (allOrdered[j].type === 'assistant') { a = allOrdered[j]; break; }
    }

    const uText  = trunc(extractText(e.message.content), cfg.maxTextLength || 400);
    const uTime  = e.timestamp
      ? new Date(e.timestamp).toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })
      : '';
    const aText  = a ? trunc(extractText(a.message.content), cfg.maxTextLength || 400) : '';
    const aTime  = a?.timestamp
      ? new Date(a.timestamp).toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })
      : '';
    const tools  = a ? extractTools(a.message.content) : [];
    pairs.push({ time: uTime, user: uText, assistant: aText, aTime, tools });
  }

  const firstUserEntry = allOrdered.find(e => e.type === 'user' && hasRealText(e.message?.content));
  const startTs        = firstUserEntry?.timestamp ? new Date(firstUserEntry.timestamp) : null;

  // Título: mensagem mais longa das 3 primeiras reais
  const firstThreeUsers = allOrdered
    .filter(e => e.type === 'user' && hasRealText(e.message?.content))
    .slice(0, 3);
  const bestEntry = firstThreeUsers.reduce((best, e) => {
    const t = extractText(e.message.content);
    return t.length > extractText(best.message.content).length ? e : best;
  }, firstThreeUsers[0] || firstUserEntry);
  const firstUserMsg = bestEntry ? trunc(extractText(bestEntry.message.content), 60) : '';

  return { pairs, firstUserMsg, startTs };
}

// ── Build note content ────────────────────────────────────────────────────────

function buildNoteContent(sessionId, transcriptPath, cwd, cfg, accountKey, sessionTitle, sessionDatetime, startTs) {
  const { pairs, firstUserMsg } = buildPairs(transcriptPath, cfg);
  const toolName = cfg.tools[accountKey]?.name || 'Claude';
  const maxEx    = cfg.maxExchanges || 6;
  const recent   = pairs.slice(-(maxEx));
  const nowStr   = formatTimestamp(new Date());

  const frontmatter = [
    '---',
    `date: ${sessionDatetime}`,
    `fim: ${nowStr}`,
    `tool: ${accountKey}`,
    `title: "${sessionTitle.replace(/"/g, "'")}"`,
    `session_id: ${sessionId}`,
    `tags: [${accountKey}, sessão]`,
    '---'
  ].join('\n');

  let body = `# ${sessionTitle}\n\n`;
  body += `> **Ferramenta:** ${toolName} · **Início:** ${sessionDatetime} · **Fim:** ${nowStr}\n`;
  if (cwd) body += `> **Dir:** \`${cwd}\`\n`;
  body += '\n';

  if (firstUserMsg) {
    body += `## Objetivo\n${firstUserMsg}\n\n`;
  }

  if (recent.length > 0) {
    body += `## Conversa\n\n`;
    for (const p of recent) {
      body += `**Mestre:** ${p.user}\n`;
      if (p.time) body += `> ${p.time}\n`;
      body += '\n';
      if (p.tools.length > 0) {
        body += `*Ferramentas: ${p.tools.join(', ')}*\n\n`;
      }
      if (p.assistant) {
        body += `**${toolName}:** ${p.assistant}\n`;
        if (p.aTime) body += `> ${p.aTime}\n`;
        body += '\n';
      }
      body += '---\n\n';
    }
  }

  return `${frontmatter}\n\n${body}`;
}

// ── Ensure sessions folder ────────────────────────────────────────────────────

function ensureSessionsDir(cfg, accountKey) {
  const folder     = cfg.tools[accountKey]?.folder || 'Claude 1';
  const sessionsDir = path.join(cfg.vaultPath, folder, 'Sessões');
  fs.mkdirSync(sessionsDir, { recursive: true });
  return sessionsDir;
}

// ── Get or create note path for this session ──────────────────────────────────

function resolveNotePath(sessionsDir, sessionId, firstUserMsg, startTs) {
  const cache = readCache(sessionId);
  if (cache.notePath && fs.existsSync(cache.notePath)) {
    return { notePath: cache.notePath, title: cache.title, isNew: false };
  }

  const dt    = startTs || new Date();
  const dtStr = formatDatetime(dt);
  const rawTitle = firstUserMsg && firstUserMsg.length >= 5
    ? sanitizeFilename(firstUserMsg)
    : `Sessão ${dtStr}`;
  const title    = rawTitle || `Sessão ${dtStr}`;
  const filename = `${dtStr} - ${title}.md`;
  const notePath = path.join(sessionsDir, filename);

  return { notePath, title, isNew: true };
}

// ── Heartbeat check ───────────────────────────────────────────────────────────

function checkHeartbeats(cfg) {
  const maxAge  = cfg.heartbeatMaxAge || 120000;
  const now     = Date.now();
  const stale   = [];

  for (const [label, hbPath] of [['Codex', HB_CODEX], ['Antigravity', HB_ANTGRAV]]) {
    try {
      const hb = JSON.parse(fs.readFileSync(hbPath, 'utf8'));
      if (now - hb.ts > maxAge) stale.push(label);
    } catch (_) {
      // heartbeat file missing — watcher nunca iniciou ou morreu sem criar arquivo
      // Não alertar se o arquivo simplesmente não existe ainda (primeiro uso)
    }
  }

  if (stale.length === 0) return;

  const alertDir  = path.join(cfg.vaultPath, '_Sistema');
  fs.mkdirSync(alertDir, { recursive: true });
  const alertPath = path.join(alertDir, '⚠️ Watchers Offline.md');
  const content   = [
    '---',
    `date: ${formatTimestamp(new Date())}`,
    'tags: [alerta, sistema]',
    '---',
    '',
    `# ⚠️ Watchers Offline`,
    '',
    `**Detectado em:** ${formatTimestamp(new Date())}`,
    '',
    `Os seguintes watchers estão sem heartbeat há mais de ${maxAge/1000}s:`,
    '',
    ...stale.map(s => `- **${s}**`),
    '',
    '## Como resolver',
    '',
    '```powershell',
    'pm2 list',
    'pm2 restart all',
    '```',
    ''
  ].join('\n');

  atomicWrite(alertPath, content);
}

// ── Main ──────────────────────────────────────────────────────────────────────

function main() {
  let data = '';
  process.stdin.on('data', chunk => { data += chunk; });
  process.stdin.on('end', () => {
    // Timeout de segurança: nunca travar a sessão
    const timeout = setTimeout(() => process.exit(0), 8000);

    try {
      const hookData      = JSON.parse(data || '{}');
      const transcriptPath = hookData.transcript_path;
      const sessionId     = hookData.session_id || 'unknown';
      const cwd           = hookData.cwd || '';

      if (!transcriptPath) { clearTimeout(timeout); return; }

      const cfg        = loadConfig();
      const accountKey = detectAccount(transcriptPath);
      const sessionsDir = ensureSessionsDir(cfg, accountKey);

      // Primeira passagem completa para obter título/timestamp de início
      const { pairs, firstUserMsg, startTs } = buildPairs(transcriptPath, cfg);
      if (pairs.length === 0 && !firstUserMsg) { clearTimeout(timeout); return; }

      const { notePath, title, isNew } = resolveNotePath(sessionsDir, sessionId, firstUserMsg, startTs);
      const sessionDatetime = formatDatetime(startTs || new Date());
      const content = buildNoteContent(sessionId, transcriptPath, cwd, cfg, accountKey, title, sessionDatetime, startTs);

      atomicWrite(notePath, content);

      // Atualizar cache com byte position atual
      const stat = fs.statSync(transcriptPath);
      writeCache(sessionId, { bytePos: stat.size, notePath, title });

      // Verificar heartbeat dos watchers
      checkHeartbeats(cfg);

    } catch (_) {
      // Falha silenciosa — nunca interromper a sessão
    } finally {
      clearTimeout(timeout);
    }
  });
}

main();
