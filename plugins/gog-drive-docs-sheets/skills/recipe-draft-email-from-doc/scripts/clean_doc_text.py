#!/usr/bin/env python3
import sys

def clean_text(raw):
    lines = [l.strip() for l in raw.splitlines() if l.strip()]
    return '\n\n'.join(lines)

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        print(clean_text(raw))
