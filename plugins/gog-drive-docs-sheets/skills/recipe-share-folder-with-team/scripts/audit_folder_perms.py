#!/usr/bin/env python3
import sys, json

def audit(data):
    perms = data.get('permissions', data if isinstance(data, list) else [])
    print(f"Total permissions assigned: {len(perms)}")

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        audit(json.loads(raw))
