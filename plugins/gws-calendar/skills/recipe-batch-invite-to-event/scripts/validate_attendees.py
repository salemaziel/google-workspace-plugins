#!/usr/bin/env python3
import sys, re

email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def validate(emails):
    valid, invalid = [], []
    for e in emails:
        clean = e.strip()
        if email_regex.match(clean):
            valid.append(clean)
        else:
            invalid.append(clean)
    print(f"Valid ({len(valid)}): {', '.join(valid)}")
    if invalid:
        print(f"Invalid ({len(invalid)}): {', '.join(invalid)}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: validate_attendees.py email1@domain.com email2@domain.com ...")
        sys.exit(1)
    validate(sys.argv[1:])
