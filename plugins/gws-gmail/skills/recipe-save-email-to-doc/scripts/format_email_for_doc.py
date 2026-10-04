#!/usr/bin/env python3
import sys, json

def format_doc(msg_json):
    headers = {h.get('name'): h.get('value') for h in msg_json.get('payload', {}).get('headers', [])}
    subject = headers.get('Subject', 'No Subject')
    from_hdr = headers.get('From', 'Unknown')
    date_hdr = headers.get('Date', '')
    snippet = msg_json.get('snippet', '')
    
    return f"""# {subject}

- **From**: {from_hdr}
- **Date**: {date_hdr}

---

{snippet}
"""

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        print(format_email_for_doc(json.loads(raw)))
