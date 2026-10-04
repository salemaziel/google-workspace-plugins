#!/usr/bin/env python3
import sys

def human_bytes(b):
    for u in ['B', 'KB', 'MB', 'GB', 'TB']:
        if b < 1024: return f"{b:.1f} {u}"
        b /= 1024
    return f"{b:.1f} PB"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(human_bytes(int(sys.argv[1])))
