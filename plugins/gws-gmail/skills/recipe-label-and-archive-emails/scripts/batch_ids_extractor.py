#!/usr/bin/env python3
import sys, json

def get_ids(json_data):
    messages = json_data.get('messages', json_data if isinstance(json_data, list) else [])
    ids = [m.get('id') for m in messages if isinstance(m, dict) and m.get('id')]
    return ids

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        for mid in get_ids(json.loads(raw)):
            print(mid)
