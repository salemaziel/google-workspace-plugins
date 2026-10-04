#!/usr/bin/env python3
import sys

def format_ann(title, body):
    print(f"Announcement: {title}\n\n{body}")

if __name__ == '__main__':
    t = sys.argv[1] if len(sys.argv) > 1 else 'Company Update'
    b = sys.argv[2] if len(sys.argv) > 2 else 'Please see intranet for details.'
    format_ann(t, b)
