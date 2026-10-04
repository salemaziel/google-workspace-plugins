#!/usr/bin/env python3
import sys

def make_rrule(freq='WEEKLY', days='MO,TU,WE,TH,FR', count=None):
    rule = f"FREQ={freq};BYDAY={days}"
    if count:
        rule += f";COUNT={count}"
    return f"RRULE:{rule}"

if __name__ == '__main__':
    days = sys.argv[1] if len(sys.argv) > 1 else 'MO,TU,WE,TH,FR'
    print(make_rrule(days=days))
