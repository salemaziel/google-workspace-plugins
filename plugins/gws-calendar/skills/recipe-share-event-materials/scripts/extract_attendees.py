#!/usr/bin/env python3
import sys, json

def get_emails(event_json):
    attendees = event_json.get('attendees', [])
    emails = [a.get('email') for a in attendees if a.get('email')]
    return emails

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        data = json.loads(raw)
        emails = get_emails(data)
        for e in emails:
            print(e)
