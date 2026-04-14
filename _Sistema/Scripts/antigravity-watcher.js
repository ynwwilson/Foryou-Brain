#!/usr/bin/env node
/**
 * antigravity-watcher.js
 * Monitora ~/.gemini/antigravity/brain/ e salva sessões no vault Obsidian.
 * Gerenciado pelo pm2. Heartbeat a cada 30s.
 */

'use strict';

const fs       = require('fs');
const path     = require('path');
const os       = require('os');
const chokidar = require(path.join(__dirname, 'node_modules', 'chokidar'));

// ── Config ────────────────────────────────────────────────────────────────────

const CONFIG_PATH  = path.join(os.homedir(), '.session-saver', 'config.json');
const CACHE_DIR    = path.join(os.homedir(), '.session-saver', 'cache');
const HB_PATH      = path.join(os.homedir(), '.session-saver', 'heartbeat-antigravity.json');
const PROCESSED_DB = path.join(os.homedir(), '.session-saver', 'antigravity-processed.json');

function loadConfig() {
  try {
    return JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
  } catch (_) {
    return {
      vaultPath: 'C:/Users/ynwwi/Projects/claude-novo/stark/Stark',
      antigravityBrainPath: 'C:/Users/ynwwi/.gemini/antigravity/brain',
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

function atomicWrite(destPath, content) {
  const tmpPath = `${destPath}.tmp.${process.pid}.${Date.now()}`;
  fs.writeFileSync(tmpPath, content, 'utf8');
  fs.renameSync(tmpPath, destPath);
}

function writeHeartbeat() {
  try {
    fs.mkdirSync(path.dirname(HB_PATH), { recursive: true });
    atomicWrite(HB_PATH, JSON.stringify({ ts: Date.now(), pid: process.pid, watcher: 'antigravity' }));
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

// ── Parse walkthrough.md ──────────────────────────────────────────────────────

function extractTitle(walkthroughContent) {
  const match = walkthroughContent.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : null;
}

function readTaskMd(taskPath) {
  try {
    return fs.readFileSync(taskPath, 'utf8').trim();
  } catch (_) {
    return null;
  }
}

// ── Build note for complete session ──────────────────────────────────────────

function buildCompleteNote(taskId, brainDir, cfg) {
  const walkthroughPath = path.join(brainDir, 'walkthrough.md');
  const taskPath        = path.join(brainDir, 'task.md');
  const implPath        = path.join(brainDir, 'implementation_plan.md');

  const walkthroughContent = fs.readFileSync(walkthroughPath, 'utf8');
  const taskContent        = readTaskMd(taskPath);

  // Start time: use task.md birthtime (when task was created)
  let startTime;
  try {
    startTime = fs.statSync(taskPath).birthtime;
  } catch (_) {
    try {
      startTime = fs.statSync(walkthroughPath).birthtime;
    } catch (_) {
      startTime = new Date();
    }
  }

  const rawTitle = extractTitle(walkthroughContent);
  const title    = rawTitle
    ? sanitizeFilename(rawTitle)
    : `Sessão ${formatDatetime(startTime)}`;

  const sessionDatetime = formatDatetime(startTime);
  const nowStr          = formatTimestamp(new Date());

  const frontmatter = [
    '---',
    `date: ${sessionDatetime}`,
    `tool: antigravity`,
    `title: "${title.replace(/"/g, "'")}"`,
    `task_id: ${taskId}`,
    `tags: [antigravity, sessão]`,
    '---'
  ].join('\n');

  let body = `# ${title}\n\n`;
  body += `> **Ferramenta:** Antigravity · **Início:** ${sessionDatetime} · **Último save:** ${nowStr}\n\n`;

  if (taskContent) {
    body += `## Tarefas\n\n${taskContent}\n\n`;
  }

  // Implementation plan (optional)
  if (fs.existsSync(implPath)) {
    try {
      const impl = fs.readFileSync(implPath, 'utf8').trim();
      if (impl) body += `## Plano de Implementação\n\n${impl}\n\n`;
    } catch (_) {}
  }

  body += `## Walkthrough\n\n`;
  // Skip the H1 title (already used), include rest
  const walkthroughBody = walkthroughContent.replace(/^#\s+.+\n/, '').trim();
  body += `${walkthroughBody}\n`;

  return { title, sessionDatetime, content: `${frontmatter}\n\n${body}` };
}

// ── Build note for incomplete session (only task.md) ─────────────────────────

function buildIncompleteNote(taskId, brainDir, cfg) {
  const taskPath  = path.join(brainDir, 'task.md');
  const taskContent = readTaskMd(taskPath);

  let startTime;
  try {
    startTime = fs.statSync(taskPath).birthtime;
  } catch (_) {
    startTime = new Date();
  }

  const sessionDatetime = formatDatetime(startTime);
  const nowStr          = formatTimestamp(new Date());
  const title           = `⏳ Sessão em andamento ${sessionDatetime}`;

  const frontmatter = [
    '---',
    `date: ${sessionDatetime}`,
    `tool: antigravity`,
    `title: "${title.replace(/"/g, "'")}"`,
    `task_id: ${taskId}`,
    `status: incomplete`,
    `tags: [antigravity, sessão, incompleta]`,
    '---'
  ].join('\n');

  let body = `# ${title}\n\n`;
  body += `> **Ferramenta:** Antigravity · **Status:** Em andamento · **Detectado:** ${nowStr}\n\n`;
  body += `> Esta nota será atualizada automaticamente quando a sessão for concluída.\n\n`;

  if (taskContent) {
    body += `## Tarefas\n\n${taskContent}\n`;
  }

  return { title, sessionDatetime, content: `${frontmatter}\n\n${body}` };
}

// ── Save session note ─────────────────────────────────────────────────────────

function saveAntигравitySession(taskId, brainDir, cfg) {
  const author = cfg.author || 'Wilson';
  const sessionsDir = path.join(cfg.vaultPath, 'Antigravity', 'Sessões', author);
  fs.mkdirSync(sessionsDir, { recursive: true });
  fs.mkdirSync(CACHE_DIR, { recursive: true });

  const walkthroughPath = path.join(brainDir, 'walkthrough.md');
  const isComplete = fs.existsSync(walkthroughPath);

  let result;
  try {
    if (isComplete) {
      result = buildCompleteNote(taskId, brainDir, cfg);
    } else {
      result = buildIncompleteNote(taskId, brainDir, cfg);
    }
  } catch (err) {
    logError('build', `${taskId}: ${err.message}`);
    return;
  }

  // Cache key per taskId
  const cacheFile = path.join(CACHE_DIR, `antigravity_${taskId}.json`);
  let notePath;
  try {
    const cache = JSON.parse(fs.readFileSync(cacheFile, 'utf8'));
    notePath = cache.notePath;
    if (!fs.existsSync(notePath)) notePath = null;
  } catch (_) { notePath = null; }

  if (!notePath) {
    const prefix   = isComplete ? '' : '⏳ ';
    const filename = `${result.sessionDatetime} - ${result.title}.md`;
    notePath       = path.join(sessionsDir, filename);
  }

  atomicWrite(notePath, result.content);
  atomicWrite(cacheFile, JSON.stringify({ notePath, title: result.title, complete: isComplete }));

  const db = loadProcessed();
  db[taskId] = { processedAt: Date.now(), notePath, complete: isComplete };
  saveProcessed(db);
}

// ── Debounce ──────────────────────────────────────────────────────────────────

const debounceTimers = new Map();

function debouncedSave(taskId, brainDir, cfg, delay = 2000) {
  if (debounceTimers.has(taskId)) clearTimeout(debounceTimers.get(taskId));
  const timer = setTimeout(() => {
    debounceTimers.delete(taskId);
    try {
      saveAntигравitySession(taskId, brainDir, cfg);
    } catch (err) {
      logError('save', `${taskId}: ${err.message}`);
    }
  }, delay);
  debounceTimers.set(taskId, timer);
}

// ── Error log ─────────────────────────────────────────────────────────────────

function logError(context, msg) {
  try {
    const cfg = loadConfig();
    const errDir  = path.join(cfg.vaultPath, '_Sistema');
    fs.mkdirSync(errDir, { recursive: true });
    const errPath = path.join(errDir, 'antigravity-watcher-errors.md');
    const line    = `\n- ${formatTimestamp(new Date())} [${context}] ${msg}`;
    fs.appendFileSync(errPath, line, 'utf8');
  } catch (_) {}
}

// ── Extract taskId from file path ─────────────────────────────────────────────

function getTaskIdFromPath(filePath, brainBase) {
  const rel = path.relative(brainBase, filePath);
  const parts = rel.split(path.sep);
  return parts[0] || null;
}

// ── Catch-up scan (last 24h) ──────────────────────────────────────────────────

function catchUpScan(cfg) {
  const days   = cfg.catchUpDays || 7;
  const cutoff = Date.now() - days * 24 * 60 * 60 * 1000;
  const db       = loadProcessed();
  const brainBase = cfg.antigravityBrainPath;

  if (!fs.existsSync(brainBase)) return;

  let taskDirs;
  try { taskDirs = fs.readdirSync(brainBase, { withFileTypes: true }); } catch (_) { return; }

  for (const entry of taskDirs) {
    if (!entry.isDirectory()) continue;
    const taskId  = entry.name;
    const brainDir = path.join(brainBase, taskId);

    const taskPath = path.join(brainDir, 'task.md');
    if (!fs.existsSync(taskPath)) continue;

    try {
      const stat = fs.statSync(taskPath);
      if (stat.mtimeMs < cutoff && !(db[taskId])) continue;
      // If already processed as complete, skip
      if (db[taskId]?.complete) continue;
      saveAntигравitySession(taskId, brainDir, cfg);
    } catch (_) {}
  }
}

// ── Main ──────────────────────────────────────────────────────────────────────

function main() {
  const cfg = loadConfig();

  fs.mkdirSync(CACHE_DIR, { recursive: true });
  fs.mkdirSync(path.join(cfg.vaultPath, 'Antigravity', 'Sessões', cfg.author || 'Wilson'), { recursive: true });

  const brainBase = cfg.antigravityBrainPath;
  if (!fs.existsSync(brainBase)) {
    fs.mkdirSync(brainBase, { recursive: true });
  }

  // Catch-up on startup
  try { catchUpScan(cfg); } catch (err) { logError('catchup', err.message); }

  // Heartbeat
  writeHeartbeat();
  setInterval(writeHeartbeat, 30000);

  const watcher = chokidar.watch(brainBase, {
    persistent: true,
    ignoreInitial: true,
    depth: 3,
    awaitWriteFinish: {
      stabilityThreshold: 500,
      pollInterval: 100
    }
  });

  function handleChange(filePath) {
    const name = path.basename(filePath);
    if (name !== 'walkthrough.md' && name !== 'task.md' && name !== 'implementation_plan.md') return;

    const taskId  = getTaskIdFromPath(filePath, brainBase);
    if (!taskId) return;
    const brainDir = path.join(brainBase, taskId);

    debouncedSave(taskId, brainDir, cfg);
  }

  watcher.on('add',    handleChange);
  watcher.on('change', handleChange);
  watcher.on('error',  err => logError('watcher', err.message));

  process.on('SIGTERM', () => { watcher.close(); process.exit(0); });
  process.on('SIGINT',  () => { watcher.close(); process.exit(0); });

  console.log(`[antigravity-watcher] Watching: ${brainBase}`);
}

main();
