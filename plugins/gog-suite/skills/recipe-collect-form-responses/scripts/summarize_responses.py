#!/usr/bin/env python3
import sys, json

def summarize(data):
    responses = data.get('responses', [])
    print(f"Total responses received: {len(responses)}")

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        summarize(json.loads(raw))
