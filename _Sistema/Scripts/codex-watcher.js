#!/usr/bin/env node
/**
 * codex-watcher.js
 * Monitora ~/.codex/sessions/ (rollout-*.jsonl) e salva sessões no vault Obsidian.
 * Gerenciado pelo pm2. Heartbeat a cada 30s.
 */

'use strict';

const fs      = require('fs');
const path    = require('path');
const os      = require('os');
const chokidar = require(path.join(__dirname, 'node_modules', 'chokidar'));

// ── Config ────────────────────────────────────────────────────────────────────

const CONFIG_PATH  = path.join(os.homedir(), '.session-saver', 'config.json');
const CACHE_DIR    = path.join(os.homedir(), '.session-saver', 'cache');
const HB_PATH      = path.join(os.homedir(), '.session-saver', 'heartbeat-codex.json');
const PROCESSED_DB = path.join(os.homedir(), '.session-saver', 'codex-processed.json');

function loadConfig() {
  try {
    return JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
  } catch (_) {
    return {
      vaultPath: 'C:/Users/ynwwi/Projects/claude-novo/stark/Stark',
      codexSessionsPath: 'C:/Users/ynwwi/.codex/sessions',
      maxTextLength: 400,
      maxExchanges: 6
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

function atomicWrite(destPath, content) {
  const tmpPath = `${destPath}.tmp.${process.pid}.${Date.now()}`;
  fs.writeFileSync(tmpPath, content, 'utf8');
  fs.renameSync(tmpPath, destPath);
}

function writeHeartbeat() {
  try {
    fs.mkdirSync(path.dirname(HB_PATH), { recursive: true });
    atomicWrite(HB_PATH, JSON.stringify({ ts: Date.now(), pid: process.pid, watcher: 'codex' }));
  } catch (_) {}
}

// ── Processed sessions DB ─────────────────────────────────────────────────────

function loadProcessed() {
  try {
    return JSON.parse(fs.readFileSync(PROCESSED_DB, 'utf8'));
  } catch (_) {
    return {};
  }
}

function saveProcessed(db) {
  try {
    atomicWrite(PROCESSED_DB, JSON.stringify(db, null, 2));
  } catch (_) {}
}

// ── Parse Codex rollout JSONL ─────────────────────────────────────────────────

function parseRollout(filePath) {
  let raw;
  try {
    raw = fs.readFileSync(filePath, 'utf8').replace(/^\uFEFF/, '');
  } catch (_) { return null; }

  const lines = raw.trim().split('\n').filter(Boolean);
  const pairs = [];
  let sessionMeta = null;
  let pendingUserMsg = null;

  for (const line of lines) {
    let entry;
    try { entry = JSON.parse(line); } catch (_) { continue; }

    if (entry.type === 'session_meta') {
      sessionMeta = entry.payload;
      continue;
    }

    // User message
    if (entry.type === 'event_msg' && entry.payload?.type === 'user_message') {
      const msg = entry.payload.message || '';
      if (msg.trim()) {
        pendingUserMsg = { text: msg.trim(), ts: entry.timestamp };
      }
      continue;
    }

    // Assistant response
    if (entry.type === 'response_item' && entry.payload?.role === 'assistant') {
      const content = entry.payload.content || [];
      const text = content
        .filter(c => c.type === 'output_text')
        .map(c => c.text || '')
        .join('\n')
        .trim();

      if (text && pendingUserMsg) {
        pairs.push({
          userText: pendingUserMsg.text,
          userTs: pendingUserMsg.ts,
          assistantText: text
        });
        pendingUserMsg = null;
      }
      continue;
    }
  }

  return { sessionMeta, pairs };
}

// ── Build Obsidian note ───────────────────────────────────────────────────────

function buildCodexNote(filePath, cfg) {
  const parsed = parseRollout(filePath);
  if (!parsed || parsed.pairs.length === 0) return null;

  const { sessionMeta, pairs } = parsed;
  const maxText = cfg.maxTextLength || 400;
  const maxEx   = cfg.maxExchanges  || 6;

  // Session start time: use file birthtime (when session started)
  let startTime;
  try {
    startTime = fs.statSync(filePath).birthtime;
  } catch (_) {
    startTime = new Date();
  }

  const firstUserMsg = trunc(pairs[0]?.userText || '', 60);
  const rawTitle     = firstUserMsg.length >= 5
    ? sanitizeFilename(firstUserMsg)
    : `Sessão ${formatDatetime(startTime)}`;
  const title        = rawTitle || `Sessão ${formatDatetime(startTime)}`;
  const sessionDatetime = formatDatetime(startTime);
  const nowStr       = formatTimestamp(new Date());

  const cwd = sessionMeta?.cwd || '';
  const model = sessionMeta?.model_provider || 'openai';

  const frontmatter = [
    '---',
    `date: ${sessionDatetime}`,
    `tool: codex`,
    `title: "${title.replace(/"/g, "'")}"`,
    `model: ${model}`,
    `tags: [codex, sessão]`,
    '---'
  ].join('\n');

  let body = `# ${title}\n\n`;
  body += `> **Ferramenta:** Codex · **Início:** ${sessionDatetime} · **Último save:** ${nowStr}\n`;
  if (cwd) body += `> **Dir:** \`${cwd}\`\n`;
  body += '\n';

  if (firstUserMsg) {
    body += `## Objetivo\n${firstUserMsg}\n\n`;
  }

  const recent = pairs.slice(-(maxEx));
  if (recent.length > 0) {
    body += `## Conversa\n\n`;
    for (const p of recent) {
      const time = p.userTs
        ? new Date(p.userTs).toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })
        : '';
      body += `**Mestre:** ${trunc(p.userText, maxText)}\n`;
      if (time) body += `> ${time}\n`;
      body += '\n';
      body += `**Codex:** ${trunc(p.assistantText, maxText)}\n\n`;
      body += '---\n\n';
    }
  }

  return { title, sessionDatetime, content: `${frontmatter}\n\n${body}`, startTime };
}

// ── Save session note ─────────────────────────────────────────────────────────

function saveCodexSession(filePath, cfg) {
  const author = cfg.author || 'Wilson';
  const sessionsDir = path.join(cfg.vaultPath, 'Codex', 'Sessões', author);
  fs.mkdirSync(sessionsDir, { recursive: true });
  fs.mkdirSync(CACHE_DIR, { recursive: true });

  const result = buildCodexNote(filePath, cfg);
  if (!result) return;

  // Use file path as cache key
  const cacheKey = filePath.replace(/[^a-z0-9]/gi, '_').slice(-80);
  const cacheFile = path.join(CACHE_DIR, `codex_${cacheKey}.json`);

  let notePath;
  try {
    const cache = JSON.parse(fs.readFileSync(cacheFile, 'utf8'));
    notePath = cache.notePath;
    if (!fs.existsSync(notePath)) notePath = null;
  } catch (_) { notePath = null; }

  if (!notePath) {
    const filename = `${result.sessionDatetime} - ${result.title}.md`;
    notePath = path.join(sessionsDir, filename);
  }

  atomicWrite(notePath, result.content);
  atomicWrite(cacheFile, JSON.stringify({ notePath, title: result.title }));

  // Mark as processed
  const db = loadProcessed();
  db[filePath] = { processedAt: Date.now(), notePath };
  saveProcessed(db);
}

// ── Debounce ──────────────────────────────────────────────────────────────────

const debounceTimers = new Map();

function debouncedSave(filePath, cfg, delay = 2000) {
  if (debounceTimers.has(filePath)) {
    clearTimeout(debounceTimers.get(filePath));
  }
  const timer = setTimeout(() => {
    debounceTimers.delete(filePath);
    try {
      saveCodexSession(filePath, cfg);
    } catch (err) {
      logError('save error', err.message);
    }
  }, delay);
  debounceTimers.set(filePath, timer);
}

// ── Error log ─────────────────────────────────────────────────────────────────

function logError(context, msg) {
  try {
    const cfg = loadConfig();
    const errDir  = path.join(cfg.vaultPath, '_Sistema');
    fs.mkdirSync(errDir, { recursive: true });
    const errPath = path.join(errDir, 'codex-watcher-errors.md');
    const line    = `\n- ${formatTimestamp(new Date())} [${context}] ${msg}`;
    fs.appendFileSync(errPath, line, 'utf8');
  } catch (_) {}
}

// ── Catch-up scan (last 24h) ──────────────────────────────────────────────────

function catchUpScan(cfg) {
  const days   = cfg.catchUpDays || 7;
  const cutoff = Date.now() - days * 24 * 60 * 60 * 1000;
  const db         = loadProcessed();
  const sessionsBase = cfg.codexSessionsPath;

  if (!fs.existsSync(sessionsBase)) return;

  function scanDir(dir) {
    let entries;
    try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch (_) { return; }
    for (const e of entries) {
      const full = path.join(dir, e.name);
      if (e.isDirectory()) { scanDir(full); continue; }
      if (!e.name.match(/^rollout-.*\.jsonl$/)) continue;
      try {
        const stat = fs.statSync(full);
        if (stat.mtimeMs < cutoff) continue;
        if (db[full] && db[full].processedAt > stat.mtimeMs) continue;
        saveCodexSession(full, cfg);
      } catch (_) {}
    }
  }

  scanDir(sessionsBase);
}

// ── Main ──────────────────────────────────────────────────────────────────────

function main() {
  const cfg = loadConfig();

  // Ensure dirs
  fs.mkdirSync(CACHE_DIR, { recursive: true });
  fs.mkdirSync(path.join(cfg.vaultPath, 'Codex', 'Sessões', cfg.author || 'Wilson'), { recursive: true });

  // Catch-up on startup
  try { catchUpScan(cfg); } catch (err) { logError('catchup', err.message); }

  // Heartbeat
  writeHeartbeat();
  setInterval(writeHeartbeat, 30000);

  // Watch sessions and archived_sessions
  const watchPaths = [
    path.join(cfg.codexSessionsPath),
  ].filter(p => fs.existsSync(p));

  if (watchPaths.length === 0) {
    logError('startup', `Codex sessions path not found: ${cfg.codexSessionsPath}`);
    return;
  }

  const watcher = chokidar.watch(watchPaths, {
    persistent: true,
    ignoreInitial: true,
    depth: 10,
    awaitWriteFinish: {
      stabilityThreshold: 500,
      pollInterval: 100
    }
  });

  watcher.on('add',    filePath => {
    if (/rollout-.*\.jsonl$/.test(filePath)) debouncedSave(filePath, cfg);
  });
  watcher.on('change', filePath => {
    if (/rollout-.*\.jsonl$/.test(filePath)) debouncedSave(filePath, cfg);
  });
  watcher.on('error',  err => logError('watcher', err.message));

  process.on('SIGTERM', () => {
    watcher.close();
    process.exit(0);
  });
  process.on('SIGINT', () => {
    watcher.close();
    process.exit(0);
  });

  console.log(`[codex-watcher] Watching: ${watchPaths.join(', ')}`);
}

main();
