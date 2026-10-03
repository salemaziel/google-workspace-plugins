#!/usr/bin/env python3
"""
Follow-up Manager — Deterministically manage pending email follow-ups in ~/.gog-assistant/followups.json.
"""

import sys
import os
import json
import argparse
from datetime import datetime, timezone, timedelta

STORE_PATH = os.path.expanduser("~/.gog-assistant/followups.json")

def load_store():
    if not os.path.exists(STORE_PATH):
        return []
    try:
        with open(STORE_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading store: {e}", file=sys.stderr)
        return []

def save_store(data):
    os.makedirs(os.path.dirname(STORE_PATH), exist_ok=True)
    with open(STORE_PATH, "w") as f:
        json.dump(data, f, indent=2)
    os.chmod(STORE_PATH, 0o600)

def main():
    parser = argparse.ArgumentParser(description="Manage email follow-up registry")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list
    list_p = subparsers.add_parser("list", help="List pending follow-ups")
    list_p.add_argument("--format", choices=["table", "json"], default="table")

    # add
    add_p = subparsers.add_parser("add", help="Add a new follow-up")
    add_p.add_argument("--email-id", required=True)
    add_p.add_argument("--person", required=True)
    add_p.add_argument("--topic", required=True)
    add_p.add_argument("--days", type=int, default=3)
    add_p.add_argument("--priority", choices=["high", "medium", "low"], default="medium")
    add_p.add_argument("--context", default="")

    # close
    close_p = subparsers.add_parser("close", help="Close a follow-up")
    close_p.add_argument("--id", required=True)

    args = parser.parse_args()
    data = load_store()

    if args.command == "list":
        pending = [item for item in data if item.get("status") == "pending"]
        if args.format == "json":
            print(json.dumps(pending, indent=2))
            return

        if not pending:
            print("No pending follow-ups.")
            return

        print(f"📋 **Pending Follow-ups**: {len(pending)}\n")
        print("| ID | Recipient | Topic | Nudge Date | Priority | Nudges |")
        print("|---|---|---|---|---|---|")
        for item in pending:
            print(f"| `{item['id']}` | {item['person']} | {item['topic']} | {item['next_nudge_date']} | {item['priority']} | {item.get('nudge_count', 0)} |")

    elif args.command == "add":
        nudge_dt = datetime.now(timezone.utc) + timedelta(days=args.days)
        entry_id = f"followup_{int(datetime.now().timestamp())}"
        entry = {
            "id": entry_id,
            "email_id": args.email_id,
            "person": args.person,
            "topic": args.topic,
            "context": args.context,
            "last_touch": datetime.now(timezone.utc).isoformat(),
            "next_nudge_date": nudge_dt.strftime("%Y-%m-%d"),
            "nudge_count": 0,
            "status": "pending",
            "priority": args.priority,
            "created_at": datetime.now(timezone.utc).isoformat()
        }
        data.append(entry)
        save_store(data)
        print(f"Added follow-up {entry_id} for {args.person} due {entry['next_nudge_date']}")

    elif args.command == "close":
        found = False
        for item in data:
            if item.get("id") == args.id or item.get("email_id") == args.id:
                item["status"] = "closed"
                item["closed_at"] = datetime.now(timezone.utc).isoformat()
                found = True
                break
        if found:
            save_store(data)
            print(f"Closed follow-up {args.id}")
        else:
            print(f"Follow-up {args.id} not found", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
