#!/usr/bin/env python3
import sys, re

email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate_roster(emails):
    valid = [e.strip() for e in emails if email_regex.match(e.strip())]
    print(f"Valid student emails ({len(valid)}): {', '.join(valid)}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        validate_roster(sys.argv[1:])
