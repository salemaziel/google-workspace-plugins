#!/usr/bin/env python3
import sys, json
from datetime import datetime, timezone

def filter_overdue(items):
    now = datetime.now(timezone.utc)
    overdue = []
    for item in items:
        due_str = item.get('due')
        if due_str and item.get('status') != 'completed':
            try:
                due = datetime.fromisoformat(due_str.replace('Z', '+00:00'))
                if due < now:
                    overdue.append(item)
            except Exception:
                pass
    return overdue

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        data = json.loads(raw)
        items = data.get('items', data if isinstance(data, list) else [])
        overdue = filter_overdue(items)
        print(f"Overdue Tasks ({len(overdue)}):")
        for o in overdue:
            print(f"- [{o.get('id')}] {o.get('title')} (Due: {o.get('due')})")
