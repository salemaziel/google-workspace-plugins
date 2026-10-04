#!/usr/bin/env python3
import sys, json

def manifest(title):
    return {'title': title, 'slides': ['Title Slide', 'Executive Summary', 'Architecture Roadmap', 'Q&A']}

if __name__ == '__main__':
    t = sys.argv[1] if len(sys.argv) > 1 else 'Presentation'
    print(json.dumps(manifest(t), indent=2))
