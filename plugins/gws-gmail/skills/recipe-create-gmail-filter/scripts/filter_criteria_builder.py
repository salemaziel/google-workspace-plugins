#!/usr/bin/env python3
import sys, json

def build_filter(from_addr=None, to_addr=None, subject=None, has_attach=False):
    criteria = {}
    if from_addr: criteria['from'] = from_addr
    if to_addr: criteria['to'] = to_addr
    if subject: criteria['subject'] = subject
    if has_attach: criteria['hasAttachment'] = True
    return criteria

if __name__ == '__main__':
    from_arg = sys.argv[1] if len(sys.argv) > 1 else 'notifications@domain.com'
    print(json.dumps(build_filter(from_addr=from_arg), indent=2))
