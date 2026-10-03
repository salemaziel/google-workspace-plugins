#!/usr/bin/env python3
"""
tasks_triage.py - Parse and triage tasks from `gws tasks tasks list` JSON output.

Usage:
  gws tasks tasks list --params '{"tasklist": "@default"}' | ./scripts/tasks_triage.py [--overdue-only] [--json]
"""

import sys
import json
import argparse
from datetime import datetime, timezone

def parse_args():
    parser = argparse.ArgumentParser(description="Triage Google Tasks JSON output")
    parser.add_argument("--overdue-only", action="store_true", help="Only show tasks that are past due")
    parser.add_argument("--json", action="store_true", help="Output triaged tasks in JSON")
    return parser.parse_args()

def main():
    args = parse_args()
    try:
        raw = sys.stdin.read().strip()
        if not raw:
            print("No JSON input provided on stdin.", file=sys.stderr)
            sys.exit(1)
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}", file=sys.stderr)
        sys.exit(1)

    items = data if isinstance(data, list) else data.get("items", [])
    now = datetime.now(timezone.utc)

    triaged = []
    for item in items:
        if item.get("status") == "completed":
            continue
        due_str = item.get("due")
        is_overdue = False
        due_formatted = "No Due Date"
        if due_str:
            try:
                due_dt = datetime.fromisoformat(due_str.replace("Z", "+00:00"))
                is_overdue = due_dt < now
                due_formatted = due_dt.strftime("%Y-%m-%d")
            except Exception:
                due_formatted = str(due_str)[:10]

        if args.overdue_only and not is_overdue:
            continue

        triaged.append({
            "id": item.get("id"),
            "title": item.get("title", "Untitled"),
            "due": due_formatted,
            "is_overdue": is_overdue,
            "notes": item.get("notes", "")
        })

    if args.json:
        print(json.dumps(triaged, indent=2))
    else:
        if not triaged:
            print("✅ No open tasks found matching criteria.")
            return

        print(f"{'Status':<10} | {'Due Date':<12} | {'Task Title'}")
        print("-" * 65)
        for t in triaged:
            status = "⚠️ OVERDUE" if t["is_overdue"] else "OPEN"
            print(f"{status:<10} | {t['due']:<12} | {t['title']}")

if __name__ == "__main__":
    main()
