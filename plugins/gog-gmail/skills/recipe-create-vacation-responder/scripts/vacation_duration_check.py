#!/usr/bin/env python3
import sys
from datetime import datetime

def check_dates(start_str, end_str):
    s = datetime.fromisoformat(start_str.replace('Z', '+00:00'))
    e = datetime.fromisoformat(end_str.replace('Z', '+00:00'))
    days = (e - s).days
    print(f"Vacation duration configured: {days} day(s)")

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        check_dates(sys.argv[1], sys.argv[2])
