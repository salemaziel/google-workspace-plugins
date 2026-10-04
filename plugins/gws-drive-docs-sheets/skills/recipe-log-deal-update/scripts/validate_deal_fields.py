#!/usr/bin/env python3
import sys, re

def check_deal(date, account, stage, amount):
    assert re.match(r'^\d{4}-\d{2}-\d{2}$', date), 'Invalid date format (YYYY-MM-DD)'
    print(f"Deal validated: {account} | {stage} | {amount}")

if __name__ == '__main__':
    if len(sys.argv) >= 5:
        check_deal(*sys.argv[1:5])
