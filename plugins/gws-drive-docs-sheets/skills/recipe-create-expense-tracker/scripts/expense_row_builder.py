#!/usr/bin/env python3
import sys, json

def build_row(date, cat, desc, amt, vendor):
    return [date, cat, desc, f"{float(amt):.2f}", vendor]

if __name__ == '__main__':
    if len(sys.argv) >= 6:
        print(json.dumps(build_row(*sys.argv[1:6])))
