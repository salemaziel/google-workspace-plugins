#!/usr/bin/env python3
import sys, json

def parse_changes(data):
    changes = data.get('changes', [])
    print(f"Detected {len(changes)} Drive change events.")
    for c in changes:
        print(f"- Change on file: {c.get('fileId')} (Removed: {c.get('removed', False)})")

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        parse_changes(json.loads(raw))
