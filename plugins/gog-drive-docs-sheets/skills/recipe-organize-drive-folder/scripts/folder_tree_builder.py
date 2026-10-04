#!/usr/bin/env python3
import sys

def print_tree(root, subfolders):
    print(f"📁 {root}")
    for sf in subfolders:
        print(f"  └── 📁 {sf}")

if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else 'Project Root'
    subs = sys.argv[2:] if len(sys.argv) > 2 else ['Docs', 'Assets', 'Reports']
    print_tree(r, subs)
