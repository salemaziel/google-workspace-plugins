#!/usr/bin/env python3
import sys, json

def parse_contacts(data):
    connections = data.get('connections', data.get('people', []))
    rows = []
    for c in connections:
        name = c.get('names', [{}])[0].get('displayName', '')
        email = c.get('emailAddresses', [{}])[0].get('value', '')
        phone = c.get('phoneNumbers', [{}])[0].get('value', '')
        if name or email:
            rows.append([name, email, phone])
    return rows

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        print(json.dumps(parse_contacts(json.loads(raw)), indent=2))
