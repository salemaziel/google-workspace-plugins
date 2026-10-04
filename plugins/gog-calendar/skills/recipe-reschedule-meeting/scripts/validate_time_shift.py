#!/usr/bin/env python3
import sys
from datetime import datetime

def check_duration(start_str, end_str):
    s = datetime.fromisoformat(start_str.replace('Z', '+00:00'))
    e = datetime.fromisoformat(end_str.replace('Z', '+00:00'))
    diff = (e - s).total_seconds() / 60
    assert diff > 0, "End time must be after start time"
    print(f"Valid time window: {diff:.0f} minutes")

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        check_duration(sys.argv[1], sys.argv[2])
