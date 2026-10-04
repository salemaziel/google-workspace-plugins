#!/usr/bin/env python3
import sys

def make_url(fid):
    return f"https://drive.google.com/open?id={fid}"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(make_url(sys.argv[1]))
