#!/usr/bin/env python3
import sys, json

def find_parts(payload):
    parts = payload.get('parts', [])
    attachments = []
    for p in parts:
        filename = p.get('filename')
        body = p.get('body', {})
        attach_id = body.get('attachmentId')
        if filename and attach_id:
            attachments.append({'filename': filename, 'attachmentId': attach_id, 'size': body.get('size')})
    return attachments

if __name__ == '__main__':
    raw = sys.stdin.read()
    if raw.strip():
        data = json.loads(raw)
        payload = data.get('payload', data)
        print(json.dumps(find_parts(payload), indent=2))
