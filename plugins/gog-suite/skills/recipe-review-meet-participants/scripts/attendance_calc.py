#!/usr/bin/env python3
import sys, json

def parse_attendance(data):
    participants = data.get('participants', data if isinstance(data, list) else [])
    print(f"Total participants logged: {len(participants)}")
    for p in participants:
        name = p.get('signedinUser', {}).get('displayName', 'Anonymous')
        print(f"- {name}")

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        parse_attendance(json.loads(raw))
