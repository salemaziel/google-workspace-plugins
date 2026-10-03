#!/usr/bin/env python3
"""
drive_search_filter.py - Filter and format Google Drive JSON search output.

Usage:
  gog drive search "quarterly" --json | ./scripts/drive_search_filter.py [--mime-type TYPE] [--owner EMAIL] [--limit N]
"""

import sys
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Filter and format Google Drive JSON output")
    parser.add_argument("--mime-type", help="Filter by MIME type or shorthand (doc, sheet, slide, pdf)")
    parser.add_argument("--owner", help="Filter by owner email substring")
    parser.add_argument("--limit", type=int, default=20, help="Maximum number of files to return")
    parser.add_argument("--format", choices=["table", "json", "links"], default="table", help="Output format")
    return parser.parse_args()

MIME_ALIASES = {
    "doc": "application/vnd.google-apps.document",
    "sheet": "application/vnd.google-apps.spreadsheet",
    "slide": "application/vnd.google-apps.presentation",
    "folder": "application/vnd.google-apps.folder",
    "pdf": "application/pdf"
}

def main():
    args = parse_args()
    try:
        raw_input = sys.stdin.read().strip()
        if not raw_input:
            print("No input provided on stdin.", file=sys.stderr)
            sys.exit(1)
        data = json.loads(raw_input)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON from stdin: {e}", file=sys.stderr)
        sys.exit(1)

    files = data if isinstance(data, list) else data.get("files", [data] if "id" in data else [])

    target_mime = MIME_ALIASES.get(args.mime_type, args.mime_type) if args.mime_type else None

    filtered = []
    for f in files:
        if target_mime and f.get("mimeType") != target_mime:
            continue
        if args.owner:
            owners = [o.get("emailAddress", "") for o in f.get("owners", [])]
            if not any(args.owner.lower() in o.lower() for o in owners):
                continue
        filtered.append(f)

    filtered = filtered[:args.limit]

    if args.format == "json":
        print(json.dumps(filtered, indent=2))
    elif args.format == "links":
        for f in filtered:
            name = f.get("name", "Untitled")
            link = f.get("webViewLink", f.get("id", ""))
            print(f"- [{name}]({link})")
    else:
        # Table format
        if not filtered:
            print("No matching files found.")
            return
        print(f"{'ID':<30} | {'MIME Type':<35} | {'Name'}")
        print("-" * 90)
        for f in filtered:
            fid = f.get("id", "")[:28]
            mtype = f.get("mimeType", "").replace("application/vnd.google-apps.", "")
            name = f.get("name", "Untitled")
            print(f"{fid:<30} | {mtype:<35} | {name}")

if __name__ == "__main__":
    main()
