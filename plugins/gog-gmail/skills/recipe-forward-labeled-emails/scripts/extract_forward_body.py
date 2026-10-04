#!/usr/bin/env python3
import sys, json

def extract_snippet(msg_json):
    snippet = msg_json.get('snippet', '')
    print(f"Message preview: {snippet}")

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        extract_snippet(json.loads(raw))
