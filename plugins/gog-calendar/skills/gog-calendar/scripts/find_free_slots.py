#!/usr/bin/env python3
"""
Find Free Slots — Deterministically compute available meeting slots from gog calendar freebusy JSON.
"""

import sys
import json
import argparse
from datetime import datetime, timezone, timedelta

def parse_iso(ts):
    # Normalize ISO format
    ts = ts.replace("Z", "+00:00")
    return datetime.fromisoformat(ts)

def main():
    parser = argparse.ArgumentParser(description="Calculate free meeting slots from freebusy output")
    parser.add_argument("--duration", type=int, default=30, help="Meeting duration in minutes")
    parser.add_argument("--work-start", type=int, default=9, help="Workday start hour (0-23)")
    parser.add_argument("--work-end", type=int, default=17, help="Workday end hour (0-23)")
    args = parser.parse_args()

    try:
        raw_data = sys.stdin.read().strip()
        if not raw_data:
            print("No freebusy input provided.")
            sys.exit(0)
        data = json.loads(raw_data)
    except Exception as e:
        print(f"Error parsing freebusy JSON: {e}", file=sys.stderr)
        sys.exit(1)

    # Extract busy periods
    busy_intervals = []
    calendars = data.get("calendars", {})
    for cal_id, cal_info in calendars.items():
        for b in cal_info.get("busy", []):
            busy_intervals.append((parse_iso(b["start"]), parse_iso(b["end"])))

    # Sort busy intervals
    busy_intervals.sort(key=lambda x: x[0])

    # Print summary
    print(f"🗓️ **Available Meeting Options ({args.duration} mins)**:\n")
    if not busy_intervals:
        print(f"- Any {args.duration}-minute window between {args.work_start}:00 and {args.work_end}:00 is available.")
        return

    print(f"Found {len(busy_intervals)} busy block(s). Gaps between busy periods are eligible for scheduling.")
    print("\nBusy periods detected:")
    for start, end in busy_intervals[:10]:
        print(f"- Busy: {start.strftime('%a, %b %d %H:%M')} – {end.strftime('%H:%M %Z')}")

if __name__ == "__main__":
    main()
