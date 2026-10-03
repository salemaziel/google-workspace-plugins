#!/usr/bin/env python3
"""
Prepare Draft — Safely create a Gmail draft via gog CLI with temporary file cleanup.
"""

import sys
import os
import tempfile
import subprocess
import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Create a Gmail draft using gog CLI")
    parser.add_argument("--to", required=True, help="Recipient email address(es)")
    parser.add_argument("--subject", required=True, help="Email subject line")
    parser.add_argument("--cc", default="", help="CC email address(es)")
    parser.add_argument("--body", help="Body text string")
    parser.add_argument("--body-file", help="Path to file containing body text")
    args = parser.parse_args()

    body_text = args.body or ""
    if args.body_file and os.path.exists(args.body_file):
        with open(args.body_file, "r") as f:
            body_text = f.read()

    if not body_text:
        # Read from stdin if no body supplied
        if not sys.stdin.isatty():
            body_text = sys.stdin.read().strip()

    if not body_text:
        print("Error: Empty body text.", file=sys.stderr)
        sys.exit(1)

    # Create temporary file safely
    temp_file = None
    try:
        with tempfile.NamedTemporaryFile("w", delete=False, prefix="gog_draft_", suffix=".txt") as tf:
            tf.write(body_text)
            temp_file = tf.name

        cmd = [
            "gog", "gmail", "drafts", "create",
            "--to", args.to,
            "--subject", args.subject,
            "--body", temp_file,
            "--json"
        ]
        if args.cc:
            cmd.extend(["--cc", args.cc])

        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error creating draft: {result.stderr}", file=sys.stderr)
            sys.exit(result.returncode)

        print(result.stdout)
    finally:
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)

if __name__ == "__main__":
    main()
