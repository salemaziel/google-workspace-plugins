#!/usr/bin/env python3
"""
audit_log_analyzer.py - Parse and analyze Admin SDK activity audit logs from JSON.

Usage:
  gws admin-reports activities list --params '{"userKey": "all", "applicationName": "login"}' | ./scripts/audit_log_analyzer.py [--json]
"""

import sys
import json
import argparse
from collections import Counter

def parse_args():
    parser = argparse.ArgumentParser(description="Analyze Google Workspace Admin activity logs")
    parser.add_argument("--json", action="store_true", help="Output summary in JSON format")
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
    if not items:
        if args.json:
            print(json.dumps({"total_events": 0, "events": []}))
        else:
            print("No activity log events found.")
        return

    event_counts = Counter()
    actor_counts = Counter()
    suspicious_events = []

    for item in items:
        actor = item.get("actor", {}).get("email", "unknown")
        actor_counts[actor] += 1
        
        events = item.get("events", [])
        for ev in events:
            name = ev.get("name", "unknown")
            event_counts[name] += 1
            # Flag suspicious events
            if any(term in name.lower() for term in ["fail", "suspicious", "denied", "block", "compromise"]):
                suspicious_events.append({
                    "time": item.get("id", {}).get("time", ""),
                    "actor": actor,
                    "event": name,
                    "ip": item.get("ipAddress", "unknown")
                })

    summary = {
        "total_activities": len(items),
        "unique_actors": len(actor_counts),
        "event_types": dict(event_counts),
        "flagged_events": suspicious_events
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(f"=== Admin Audit Log Analysis ({len(items)} Events) ===")
        print(f"Unique Actors: {len(actor_counts)}")
        print("\nEvent Distribution:")
        for ev, count in event_counts.most_common(10):
            print(f"  • {ev:<35} : {count}")
            
        if suspicious_events:
            print(f"\n🚨 Flagged / Suspicious Events ({len(suspicious_events)}):")
            for s in suspicious_events[:10]:
                print(f"  ⚠️ [{s['time']}] {s['actor']} -> {s['event']} (IP: {s['ip']})")

if __name__ == "__main__":
    main()
