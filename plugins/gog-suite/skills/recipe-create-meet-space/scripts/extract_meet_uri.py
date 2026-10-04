#!/usr/bin/env python3
import sys, json

def parse_meet(data):
    uri = data.get('meetingUri', data.get('uri', ''))
    code = data.get('meetingCode', '')
    print(f"Meeting URI: {uri} (Code: {code})")

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        parse_meet(json.loads(raw))
