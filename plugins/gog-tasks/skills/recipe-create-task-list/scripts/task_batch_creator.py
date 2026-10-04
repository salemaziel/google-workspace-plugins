#!/usr/bin/env python3
import sys, json

def build_tasks(titles):
    return [{'title': t.strip(), 'status': 'needsAction'} for t in titles if t.strip()]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(json.dumps(build_tasks(sys.argv[1:]), indent=2))
