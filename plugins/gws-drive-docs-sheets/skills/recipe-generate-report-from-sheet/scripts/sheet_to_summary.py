#!/usr/bin/env python3
import sys, json

def summarize_sheet(data):
    rows = data.get('values', [])
    print(f"Synthesizing report from {len(rows)} data rows.")

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        summarize_sheet(json.loads(raw))
