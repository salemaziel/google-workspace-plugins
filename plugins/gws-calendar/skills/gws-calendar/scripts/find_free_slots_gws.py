#!/usr/bin/env python3
"""
find_free_slots_gws.py - Parse freebusy JSON from `gws calendar freebusy query` and compute open slots.

Usage:
  gws calendar freebusy query --json '...' | ./scripts/find_free_slots_gws.py [--duration-minutes 30] [--work-start 09:00] [--work-end 17:00]
"""

import sys
import json
import argparse
from datetime import datetime, time, timedelta, timezone

def parse_args():
    parser = argparse.ArgumentParser(description="Find open meeting slots from freebusy query output")
    parser.add_argument("--duration-minutes", type=int, default=30, help="Meeting duration in minutes")
    parser.add_argument("--work-start", default="09:00", help="Day start time (HH:MM)")
    parser.add_argument("--work-end", default="17:00", help="Day end time (HH:MM)")
    parser.add_argument("--json", action="store_true", help="Output free slots as JSON")
    return parser.parse_args()

def parse_iso(dt_str):
    clean = dt_str.replace("Z", "+00:00")
    return datetime.fromisoformat(clean)

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

    cals = data.get("calendars", {})
    busy_intervals = []
    for cal_id, cal_data in cals.items():
        for b in cal_data.get("busy", []):
            try:
                st = parse_iso(b["start"])
                en = parse_iso(b["end"])
                busy_intervals.append((st, en))
            except Exception:
                continue

    if not busy_intervals:
        print("✅ No busy intervals found. The entire queried window is free.")
        return

    # Sort intervals by start
    busy_intervals.sort(key=lambda x: x[0])
    
    # Merge overlapping busy intervals
    merged = []
    for cur in busy_intervals:
        if not merged:
            merged.append(cur)
        else:
            last_st, last_en = merged[-1]
            if cur[0] <= last_en:
                merged[-1] = (last_st, max(last_en, cur[1]))
            else:
                merged.append(cur)

    # Compute gaps between busy intervals
    free_slots = []
    min_dur = timedelta(minutes=args.duration_minutes)
    for i in range(len(merged) - 1):
        gap_start = merged[i][1]
        gap_end = merged[i+1][0]
        if gap_end - gap_start >= min_dur:
            free_slots.append({
                "start": gap_start.isoformat(),
                "end": gap_end.isoformat(),
                "duration_minutes": int((gap_end - gap_start).total_seconds() / 60)
            })

    if args.json:
        print(json.dumps(free_slots, indent=2))
    else:
        if not free_slots:
            print("❌ No open slots of requested duration found between busy intervals.")
        else:
            print(f"=== Found {len(free_slots)} Open Slot(s) ===")
            for s in free_slots:
                print(f"  📅 {s['start']}  -->  {s['end']} ({s['duration_minutes']} min)")

if __name__ == "__main__":
    main()
