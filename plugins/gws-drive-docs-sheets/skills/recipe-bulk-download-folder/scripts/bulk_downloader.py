#!/usr/bin/env python3
import sys, json

def extract_downloads(data):
    files = data.get('files', data if isinstance(data, list) else [])
    print(f"Discovered {len(files)} file(s) for bulk download:")
    for f in files:
        print(f"- [{f.get('id')}] {f.get('name')} ({f.get('mimeType')})")

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        extract_downloads(json.loads(raw))
