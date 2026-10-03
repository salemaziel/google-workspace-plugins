#!/usr/bin/env python3
"""
verify_payload.py - Validate email parameters before invoking `gws gmail +send`.

Usage:
  ./scripts/verify_payload.py --to user@example.com --subject "Subject" --body "Body" [--attach file.pdf]
"""

import sys
import re
import os
import argparse
import json

def parse_args():
    parser = argparse.ArgumentParser(description="Validate email parameters before dispatch")
    parser.add_argument("--to", required=True, help="Recipient email address(es)")
    parser.add_argument("--subject", required=True, help="Email subject line")
    parser.add_argument("--body", required=True, help="Email body text or path to body file")
    parser.add_argument("--attach", action="append", default=[], help="File attachments")
    parser.add_argument("--json", action="store_true", help="Output validation result in JSON")
    return parser.parse_args()

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def main():
    args = parse_args()
    errors = []
    warnings = []

    # Validate recipients
    recipients = [r.strip() for r in args.to.split(",") if r.strip()]
    if not recipients:
        errors.append("No valid recipient specified in --to.")
    for r in recipients:
        if not re.match(EMAIL_REGEX, r):
            errors.append(f"Invalid recipient email format: '{r}'")

    # Validate subject
    if not args.subject.strip():
        errors.append("Email subject line cannot be empty.")

    # Validate body
    body_content = args.body
    if os.path.exists(args.body):
        with open(args.body, "r", encoding="utf-8") as f:
            body_content = f.read()

    if not body_content.strip():
        errors.append("Email body cannot be empty.")

    # Validate attachments
    total_size = 0
    for att in args.attach:
        if not os.path.exists(att):
            errors.append(f"Attachment file not found: '{att}'")
        else:
            sz = os.path.getsize(att)
            total_size += sz

    # Check 20MB limit (safety margin under 25MB)
    if total_size > 20 * 1024 * 1024:
        errors.append(f"Total attachment size ({total_size / (1024*1024):.2f}MB) exceeds 20MB safety limit.")

    result = {
        "valid": len(errors) == 0,
        "recipients": recipients,
        "subject": args.subject,
        "attachment_count": len(args.attach),
        "total_attachment_bytes": total_size,
        "errors": errors,
        "warnings": warnings
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if errors:
            print("❌ Validation Failed:")
            for err in errors:
                print(f"  - {err}")
            sys.exit(1)
        else:
            print(f"✅ Payload Valid: {len(recipients)} recipient(s), subject: '{args.subject}'")

if __name__ == "__main__":
    main()
