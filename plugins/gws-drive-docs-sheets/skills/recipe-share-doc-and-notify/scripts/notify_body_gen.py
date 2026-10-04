#!/usr/bin/env python3
import sys

def message(doc_title, doc_id):
    return f"""Hello,

You have been granted edit access to '{doc_title}'.
Review URL: https://docs.google.com/document/d/{doc_id}/edit
"""

if __name__ == '__main__':
    t = sys.argv[1] if len(sys.argv) > 1 else 'Document'
    fid = sys.argv[2] if len(sys.argv) > 2 else 'DOC_ID'
    print(message(t, fid))
