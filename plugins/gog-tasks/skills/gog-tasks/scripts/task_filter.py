#!/usr/bin/env python3
"""
task_filter.py - Parse, categorize, and prioritize Google Tasks JSON output.

Usage:
  gog tasks list "$TASKLIST_ID" --json | ./scripts/task_filter.py [--review] [--priority P0,P1] [--category Work]
"""

import sys
import json
import re
import argparse
from datetime import datetime, timezone

def parse_args():
    parser = argparse.ArgumentParser(description="Categorize and filter Google Tasks JSON")
    parser.add_argument("--review", action="store_true", help="Generate a structured Daily Task Review in Markdown")
    parser.add_argument("--priority", help="Comma-separated priorities to filter (e.g. P0,P1)")
    parser.add_argument("--category", help="Filter by category (Work, Personal, Errands, Admin)")
    parser.add_argument("--format", choices=["table", "markdown", "json"], default="table", help="Output format")
    return parser.parse_args()

def extract_metadata(task):
    title = task.get("title", "Untitled")
    notes = task.get("notes", "") or ""
    
    # Priority extraction
    p_match = re.search(r'\[(P[0-3])\]', title) or re.search(r'Priority:\s*(P[0-3])', notes, re.IGNORECASE)
    priority = p_match.group(1).upper() if p_match else "P2"
    
    # Category extraction
    cat_match = re.search(r'\[(Work|Personal|Errands|Admin)\]', title, re.IGNORECASE) or \
                re.search(r'Category:\s*(Work|Personal|Errands|Admin)', notes, re.IGNORECASE)
    category = cat_match.group(1).capitalize() if cat_match else "Work"
    
    # Due date
    due = task.get("due")
    is_overdue = False
    due_str = "None"
    if due:
        try:
            # Format: 2026-10-03T00:00:00.000Z
            clean_due = due.replace("Z", "+00:00")
            due_dt = datetime.fromisoformat(clean_due)
            now = datetime.now(timezone.utc)
            if due_dt < now:
                is_overdue = True
            due_str = due_dt.strftime("%Y-%m-%d")
        except Exception:
            due_str = str(due)[:10]

    return {
        "id": task.get("id"),
        "title": re.sub(r'\[(P[0-3]|Work|Personal|Errands|Admin)\]', '', title).strip(),
        "raw_title": title,
        "priority": priority,
        "category": category,
        "due": due_str,
        "is_overdue": is_overdue,
        "status": task.get("status", "needsAction"),
        "notes": notes
    }

def main():
    args = parse_args()
    try:
        raw_input = sys.stdin.read().strip()
        if not raw_input:
            print("No input provided on stdin.", file=sys.stderr)
            sys.exit(1)
        data = json.loads(raw_input)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}", file=sys.stderr)
        sys.exit(1)

    items = data if isinstance(data, list) else data.get("tasks", data.get("items", []))
    parsed = [extract_metadata(t) for t in items if t.get("status") != "completed"]

    if args.priority:
        allowed_p = [p.strip().upper() for p in args.priority.split(",")]
        parsed = [t for t in parsed if t["priority"] in allowed_p]

    if args.category:
        parsed = [t for t in parsed if t["category"].lower() == args.category.lower()]

    # Sort: P0 first, then P1, etc.
    p_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    parsed.sort(key=lambda x: (p_order.get(x["priority"], 9), x["due"]))

    if args.review:
        print(f"# Daily Task Review — {datetime.now().strftime('%A, %B %d, %Y')}\n")
        
        overdue = [t for t in parsed if t["is_overdue"]]
        top_focus = parsed[:5]

        print(f"## 🔥 Top {len(top_focus)} Focus Priorities")
        for i, t in enumerate(top_focus, 1):
            print(f"{i}. **{t['title']}** ({t['priority']} | {t['category']})")
            print(f"   - Due: {t['due']} | ID: `{t['id']}`")
        print()

        if overdue:
            print(f"## ⚠️ Overdue Items ({len(overdue)})")
            for t in overdue:
                print(f"- **{t['title']}** (Was due: {t['due']}) — `{t['id']}`")
            print()

        print("## 📊 Summary by Priority")
        for p in ["P0", "P1", "P2", "P3"]:
            count = len([t for t in parsed if t["priority"] == p])
            print(f"- **{p}**: {count} open")
        return

    if args.format == "json":
        print(json.dumps(parsed, indent=2))
    else:
        print(f"{'Priority':<8} | {'Category':<10} | {'Due':<12} | {'Title'}")
        print("-" * 70)
        for t in parsed:
            print(f"{t['priority']:<8} | {t['category']:<10} | {t['due']:<12} | {t['title']}")

if __name__ == "__main__":
    main()
