#!/usr/bin/env python3
import sys

roles = {'organizer': 'Manager', 'fileOrganizer': 'Content Manager', 'writer': 'Contributor', 'commenter': 'Commenter', 'reader': 'Viewer'}
if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else 'writer'
    print(f"Role '{r}' maps to permissions: {roles.get(r, 'Custom')}")
