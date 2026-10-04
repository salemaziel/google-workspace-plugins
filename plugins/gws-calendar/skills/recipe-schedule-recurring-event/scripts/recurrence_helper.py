#!/usr/bin/env python3
import sys

def format_rule(freq, interval=1, byday=''):
    r = f"RRULE:FREQ={freq};INTERVAL={interval}"
    if byday:
        r += f";BYDAY={byday}"
    return r

if __name__ == '__main__':
    print(format_rule('WEEKLY', 1, 'MO'))
