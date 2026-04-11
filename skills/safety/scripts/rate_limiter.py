"""
rate_limiter.py — Controle de rate limiting do sistema Jarvis

Uso:
  python rate_limiter.py check --action exec_shell     # verifica se pode executar
  python rate_limiter.py record --action exec_shell    # registra uma execução
  python rate_limiter.py status                        # mostra contadores atuais
  python rate_limiter.py reset --action exec_shell     # zera contador (emergência)

Retornos do check:
  OK             — pode executar
  LIMIT_REACHED  — aguardar próximo período
"""

import sys
import json
import argparse
from datetime import datetime, timezone
from pathlib import Path

VAULT = Path(__file__).parent.parent.parent.parent
STATE_FILE = VAULT / "memory" / "rate_limiter_state.json"

# Limites: (max_count, period_seconds)
LIMITS = {
    "api_call":       (5,  60),       # 5 por minuto
    "subagent_spawn": (1,  1800),     # 1 por 30 min
    "cron_execution": (3,  3600),     # 3 por hora
    "file_write":     (10, 3600),     # 10 por hora
    "message_send":   (20, 3600),     # 20 por hora
    "exec_shell":     (15, 3600),     # 15 por hora
}


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}


def save_state(state: dict):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def now_ts() -> float:
    return datetime.now(timezone.utc).timestamp()


def check(action: str) -> str:
    if action not in LIMITS:
        print(f"OK (ação '{action}' não tem limite definido)")
        return "OK"

    max_count, period = LIMITS[action]
    state = load_state()
    entry = state.get(action, {"count": 0, "window_start": now_ts()})

    elapsed = now_ts() - entry["window_start"]

    # Resetar janela se passou o período
    if elapsed >= period:
        entry = {"count": 0, "window_start": now_ts()}
        state[action] = entry
        save_state(state)

    if entry["count"] >= max_count:
        remaining = int(period - elapsed)
        print(f"LIMIT_REACHED (aguardar ~{remaining}s | {entry['count']}/{max_count} em {period}s)")
        return "LIMIT_REACHED"

    print(f"OK ({entry['count']}/{max_count} em {period}s)")
    return "OK"


def record(action: str):
    state = load_state()

    if action not in LIMITS:
        print(f"[rate] '{action}' registrado (sem limite definido)")
        return

    max_count, period = LIMITS[action]
    entry = state.get(action, {"count": 0, "window_start": now_ts()})

    elapsed = now_ts() - entry["window_start"]
    if elapsed >= period:
        entry = {"count": 0, "window_start": now_ts()}

    entry["count"] += 1
    state[action] = entry
    save_state(state)

    print(f"[rate] {action}: {entry['count']}/{max_count} nesta janela de {period}s")


def status():
    state = load_state()
    if not state:
        print("Nenhum contador ativo.")
        return

    now = now_ts()
    print(f"{'Ação':<20} {'Uso':<10} {'Limite':<10} {'Janela'}")
    print("-" * 60)
    for action, (max_count, period) in LIMITS.items():
        entry = state.get(action, {"count": 0, "window_start": now})
        elapsed = now - entry["window_start"]
        if elapsed >= period:
            count = 0
        else:
            count = entry["count"]
        remaining = max(0, int(period - elapsed))
        print(f"{action:<20} {count}/{max_count:<8} {'OK' if count < max_count else 'BLOCKED':<10} reset em {remaining}s")


def reset(action: str):
    state = load_state()
    if action in state:
        del state[action]
        save_state(state)
        print(f"[rate] Contador '{action}' resetado.")
    else:
        print(f"[rate] '{action}' sem contador ativo.")


def main():
    parser = argparse.ArgumentParser(description="Rate limiter do Jarvis")
    subparsers = parser.add_subparsers(dest="cmd")

    p_check = subparsers.add_parser("check")
    p_check.add_argument("--action", required=True)

    p_record = subparsers.add_parser("record")
    p_record.add_argument("--action", required=True)

    subparsers.add_parser("status")

    p_reset = subparsers.add_parser("reset")
    p_reset.add_argument("--action", required=True)

    args = parser.parse_args()

    if args.cmd == "check":
        result = check(args.action)
        sys.exit(0 if result == "OK" else 1)
    elif args.cmd == "record":
        record(args.action)
    elif args.cmd == "status":
        status()
    elif args.cmd == "reset":
        reset(args.action)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
