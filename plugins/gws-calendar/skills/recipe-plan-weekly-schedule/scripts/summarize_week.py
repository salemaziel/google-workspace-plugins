#!/usr/bin/env python3
import sys, json

def summarize(events):
    print(f"Total events this week: {len(events)}")

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        data = json.loads(raw)
        items = data.get('items', data if isinstance(data, list) else [])
        summarize(items)
