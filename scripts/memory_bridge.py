"""
memory_bridge.py — Ponte entre vault Obsidian e workspace OpenClaw
Implementa as 4 camadas: HOT / WARM / COLD / WORKSPACE

Uso:
  python memory_bridge.py hot               # carrega MOC + MEMORY.md
  python memory_bridge.py warm <tag>        # notas por tag
  python memory_bridge.py warm --days 3     # diarios recentes
  python memory_bridge.py cold "<query>"    # busca full-text no vault
  python memory_bridge.py stats             # estatisticas do vault
  python memory_bridge.py feedback <msg>    # salva feedback JSON
"""

import os
import sys
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

VAULT = Path(__file__).parent.parent
MEMORY_DIR = VAULT / "memory"
FEEDBACK_DIR = MEMORY_DIR / "feedback"

# --- HOT ---

def hot():
    """Carrega MOC + MEMORY.md (sempre no contexto)."""
    output = []

    moc_path = VAULT / "🧠 Meu Cerebro.md"
    if moc_path.exists():
        output.append("=== MOC ===")
        output.append(moc_path.read_text(encoding="utf-8"))

    mem_path = VAULT / "MEMORY.md"
    if mem_path.exists():
        output.append("\n=== MEMORY.md ===")
        output.append(mem_path.read_text(encoding="utf-8"))

    print("\n".join(output))

# --- WARM ---

def warm(args):
    """Carrega notas por tag ou diarios recentes."""
    if "--days" in args:
        idx = args.index("--days")
        days = int(args[idx + 1]) if idx + 1 < len(args) else 3
        _warm_recent(days)
    elif args:
        _warm_tag(args[0])
    else:
        _warm_recent(3)

def _warm_recent(days):
    today = datetime.now().date()
    output = []
    for i in range(days):
        date = today - timedelta(days=i)
        f = MEMORY_DIR / f"{date}.md"
        if f.exists():
            output.append(f"=== {date} ===")
            output.append(f.read_text(encoding="utf-8"))
    print("\n".join(output) if output else "Nenhum diario recente encontrado.")

def _warm_tag(tag):
    tag_clean = tag.lstrip("#")
    matches = []
    for md in VAULT.rglob("*.md"):
        if ".obsidian" in str(md):
            continue
        try:
            content = md.read_text(encoding="utf-8")
            if f"#{tag_clean}" in content or f"- {tag_clean}" in content:
                matches.append((md, content))
        except Exception:
            continue

    if not matches:
        print(f"Nenhuma nota com tag #{tag_clean}")
        return

    for path, content in matches[:5]:
        print(f"=== {path.name} ===")
        print(content[:2000])
        print()

# --- COLD ---

def cold(query):
    """Busca full-text no vault."""
    if not query:
        print("Uso: memory_bridge.py cold '<query>'")
        return

    query_lower = query.lower()
    results = []

    for md in VAULT.rglob("*.md"):
        if ".obsidian" in str(md):
            continue
        try:
            content = md.read_text(encoding="utf-8")
            if query_lower in content.lower():
                # Extrai trecho relevante
                idx = content.lower().find(query_lower)
                snippet = content[max(0, idx-100):idx+300].strip()
                results.append((md.relative_to(VAULT), snippet))
        except Exception:
            continue

    if not results:
        print(f"Nenhum resultado para '{query}'")
        return

    print(f"Encontrado em {len(results)} notas:\n")
    for path, snippet in results[:8]:
        print(f"--- {path} ---")
        print(snippet)
        print()

# --- STATS ---

def stats():
    """Estatisticas do vault."""
    notes = list(VAULT.rglob("*.md"))
    notes = [n for n in notes if ".obsidian" not in str(n)]

    total = len(notes)
    wikilinks = 0
    tags = set()
    orphans = 0
    note_names = {n.stem for n in notes}

    for note in notes:
        try:
            content = note.read_text(encoding="utf-8")
            links = re.findall(r'\[\[([^\]|#]+)', content)
            wikilinks += len(links)
            found_tags = re.findall(r'#(\w[\w-]*)', content)
            tags.update(found_tags)
            has_link = any(f"[[{note.stem}]]" in n.read_text(encoding="utf-8", errors="replace")
                          for n in notes if n != note)
            if not has_link and not links:
                orphans += 1
        except Exception:
            continue

    data = {
        "total_notes": total,
        "total_wikilinks": wikilinks,
        "unique_tags": len(tags),
        "orphan_notes": orphans,
        "tags": sorted(tags)[:20],
    }
    print(json.dumps(data, ensure_ascii=False, indent=2))

# --- FEEDBACK ---

def feedback(message):
    """Salva feedback estruturado em JSON."""
    FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    feedback_file = FEEDBACK_DIR / f"{today}.json"

    existing = []
    if feedback_file.exists():
        try:
            existing = json.loads(feedback_file.read_text(encoding="utf-8"))
        except Exception:
            existing = []

    entry = {
        "id": f"fb-{today}-{len(existing)+1:03d}",
        "timestamp": datetime.now().isoformat(),
        "type": "insight",
        "context": message,
        "importance": "medium",
        "applied": False
    }

    existing.append(entry)
    feedback_file.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Feedback salvo: {entry['id']}")

# --- MAIN ---

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return

    cmd = args[0]
    rest = args[1:]

    if cmd == "hot":
        hot()
    elif cmd == "warm":
        warm(rest)
    elif cmd == "cold":
        cold(" ".join(rest))
    elif cmd == "stats":
        stats()
    elif cmd == "feedback":
        feedback(" ".join(rest))
    else:
        print(f"Comando desconhecido: {cmd}")
        print(__doc__)

if __name__ == "__main__":
    main()
