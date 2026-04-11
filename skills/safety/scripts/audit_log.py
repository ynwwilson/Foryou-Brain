"""
audit_log.py — Registro de auditoria do sistema Jarvis

Uso:
  python audit_log.py log --action TYPE --target TARGET --result RESULT [--confirmed BOOL] [--details TEXT]
  python audit_log.py tail [--n N]
  python audit_log.py search --action TYPE
"""

import sys
import json
import argparse
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path(__file__).parent.parent.parent.parent
AUDIT_FILE = VAULT / "memory" / "audit.log"


def log_entry(action: str, target: str, result: str, confirmed: bool = False, details: str = ""):
    AUDIT_FILE.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "target": target,
        "result": result,
        "confirmed": confirmed,
        "details": details,
    }

    with open(AUDIT_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"[audit] {entry['ts']} | {action} | {target} | {result}")


def tail(n: int = 20):
    if not AUDIT_FILE.exists():
        print("Nenhum log encontrado.")
        return

    lines = AUDIT_FILE.read_text(encoding="utf-8").strip().splitlines()
    recent = lines[-n:]
    for line in recent:
        try:
            e = json.loads(line)
            confirmed_str = "CONFIRMADO" if e.get("confirmed") else "auto"
            print(f"{e['ts'][:19]}  [{confirmed_str}]  {e['action']}  →  {e['target']}  [{e['result']}]")
            if e.get("details"):
                print(f"  ↳ {e['details']}")
        except Exception:
            print(line)


def search(action: str):
    if not AUDIT_FILE.exists():
        print("Nenhum log encontrado.")
        return

    lines = AUDIT_FILE.read_text(encoding="utf-8").strip().splitlines()
    matches = [l for l in lines if action.lower() in l.lower()]
    print(f"{len(matches)} entradas encontradas para '{action}':\n")
    for line in matches[-20:]:
        try:
            e = json.loads(line)
            print(f"  {e['ts'][:19]}  {e['action']}  {e['target']}  [{e['result']}]")
        except Exception:
            print(f"  {line}")


def main():
    parser = argparse.ArgumentParser(description="Audit log do Jarvis")
    subparsers = parser.add_subparsers(dest="cmd")

    p_log = subparsers.add_parser("log")
    p_log.add_argument("--action", required=True)
    p_log.add_argument("--target", default="")
    p_log.add_argument("--result", default="success")
    p_log.add_argument("--confirmed", default="false")
    p_log.add_argument("--details", default="")

    p_tail = subparsers.add_parser("tail")
    p_tail.add_argument("--n", type=int, default=20)

    p_search = subparsers.add_parser("search")
    p_search.add_argument("--action", required=True)

    args = parser.parse_args()

    if args.cmd == "log":
        confirmed = args.confirmed.lower() in ("true", "1", "yes")
        log_entry(args.action, args.target, args.result, confirmed, args.details)
    elif args.cmd == "tail":
        tail(args.n)
    elif args.cmd == "search":
        search(args.action)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
