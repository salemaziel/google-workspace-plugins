#!/usr/bin/env python3
"""
Triage Parser — Deterministically parse, classify, and format Gmail messages from gog CLI.
"""

import sys
import json
import argparse
from typing import List, Dict, Any

URGENT_KEYWORDS = ["urgent", "asap", "emergency", "immediately", "outage", "blocker", "critical"]
ACTION_KEYWORDS = ["action required", "please review", "approval needed", "feedback requested", "status update"]
MEETING_KEYWORDS = ["invitation", "reschedule", "calendar", "meeting", "sync", "demo"]

def classify_message(msg: Dict[str, Any]) -> Dict[str, str]:
    subject = (msg.get("subject") or "").lower()
    snippet = (msg.get("snippet") or "").lower()
    sender = (msg.get("from") or "").lower()
    text = f"{subject} {snippet}"

    # Urgency heuristic
    if any(k in text for k in URGENT_KEYWORDS):
        urgency = "urgent"
    elif any(k in text for k in ACTION_KEYWORDS):
        urgency = "high"
    elif any(k in text for k in MEETING_KEYWORDS):
        urgency = "high"
    elif "newsletter" in text or "unsubscribe" in text or "noreply" in sender:
        urgency = "low"
    else:
        urgency = "medium"

    # Category heuristic
    if any(k in text for k in MEETING_KEYWORDS):
        category = "meeting"
        action = "schedule-meeting"
    elif "newsletter" in text or "unsubscribe" in text:
        category = "newsletter"
        action = "archive"
    elif urgency in ["urgent", "high"]:
        category = "action-required"
        action = "reply"
    else:
        category = "fyi"
        action = "review"

    return {
        "id": msg.get("id", "")[-6:] or msg.get("id", ""),
        "full_id": msg.get("id", ""),
        "from": msg.get("from", "Unknown"),
        "subject": (msg.get("subject") or "No Subject")[:45],
        "urgency": urgency,
        "category": category,
        "action": action
    }

def main():
    parser = argparse.ArgumentParser(description="Parse and triage gog email JSON payload")
    parser.add_argument("--format", choices=["table", "json"], default="table", help="Output format")
    args = parser.parse_args()

    try:
        raw_data = sys.stdin.read().strip()
        if not raw_data:
            print("No input provided.")
            sys.exit(0)
        messages = json.loads(raw_data)
        if isinstance(messages, dict):
            messages = messages.get("messages", [])
    except Exception as e:
        print(f"Error reading JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    classified = [classify_message(m) for m in messages]
    counts = {"urgent": 0, "high": 0, "medium": 0, "low": 0}
    for item in classified:
        counts[item["urgency"]] = counts.get(item["urgency"], 0) + 1

    if args.format == "json":
        print(json.dumps({"counts": counts, "messages": classified}, indent=2))
        return

    # Print markdown table format
    print(f"📧 **Total Messages**: {len(classified)}")
    print(f"⚠️  **Urgent**: {counts['urgent']} | 🔴 **High**: {counts['high']} | 🟡 **Medium**: {counts['medium']} | 🟢 **Low**: {counts['low']}\n")
    print("| ID | From | Subject | Urgency | Category | Action |")
    print("|---|---|---|---|---|---|")
    for item in classified:
        print(f"| `{item['id']}` | {item['from']} | {item['subject']} | {item['urgency']} | {item['category']} | {item['action']} |")

if __name__ == "__main__":
    main()
