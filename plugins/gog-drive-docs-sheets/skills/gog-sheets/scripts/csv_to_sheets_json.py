#!/usr/bin/env python3
"""
csv_to_sheets_json.py - Convert CSV or TSV data into a 2D JSON array suitable for `gog sheets write/append --values '...'`.

Usage:
  cat data.csv | ./scripts/csv_to_sheets_json.py
  ./scripts/csv_to_sheets_json.py data.csv [--delimiter ","]
"""

import sys
import csv
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Convert CSV data to Google Sheets 2D JSON array")
    parser.add_argument("file", nargs="?", help="Input CSV file (reads from stdin if omitted)")
    parser.add_argument("--delimiter", default=",", help="Delimiter character (default: ,)")
    return parser.parse_args()

def parse_val(v):
    v = v.strip()
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False
    try:
        if "." in v:
            return float(v)
        return int(v)
    except ValueError:
        return v

def main():
    args = parse_args()
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=args.delimiter)
            rows = [[parse_val(cell) for cell in row] for row in reader]
    else:
        reader = csv.reader(sys.stdin, delimiter=args.delimiter)
        rows = [[parse_val(cell) for cell in row] for row in reader]

    print(json.dumps(rows))

if __name__ == "__main__":
    main()
