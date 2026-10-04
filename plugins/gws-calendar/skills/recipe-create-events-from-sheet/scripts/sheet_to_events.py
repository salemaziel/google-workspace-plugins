#!/usr/bin/env python3
import sys, json

def parse_sheet_rows(json_data):
    rows = json_data.get('values', [])
    events = []
    for r in rows:
        if len(r) >= 3:
            events.append({
                'summary': r[0],
                'start': r[1],
                'end': r[2],
                'attendees': r[3] if len(r) > 3 else ''
            })
    return events

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        data = json.loads(raw)
        parsed = parse_sheet_rows(data)
        print(json.dumps(parsed, indent=2))
