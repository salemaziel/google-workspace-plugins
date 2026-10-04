#!/usr/bin/env python3
import sys, json

def diff_files(f1, f2):
    with open(f1) as a, open(f2) as b:
        d1 = json.load(a).get('values', [])
        d2 = json.load(b).get('values', [])
    print(f"Comparing {len(d1)} rows vs {len(d2)} rows:")
    diffs = 0
    for i in range(max(len(d1), len(d2))):
        r1 = d1[i] if i < len(d1) else []
        r2 = d2[i] if i < len(d2) else []
        if r1 != r2:
            diffs += 1
            print(f"Row {i+1} difference: {r1} != {r2}")
    if diffs == 0:
        print("Tabs are identical.")

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        diff_files(sys.argv[1], sys.argv[2])
