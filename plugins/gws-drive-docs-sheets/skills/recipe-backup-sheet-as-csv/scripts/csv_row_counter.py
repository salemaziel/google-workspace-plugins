#!/usr/bin/env python3
import sys, csv

def count_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        print(f"Total exported rows: {len(rows)}")

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'backup.csv'
    try:
        count_csv(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
