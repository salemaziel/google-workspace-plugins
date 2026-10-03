#!/usr/bin/env python3
"""
Audit Logger — Deterministically log email send events to ~/.gog-assistant/audit.log.
"""

import sys
import os
import json
import argparse
from datetime import datetime, timezone

LOG_PATH = os.path.expanduser("~/.gog-assistant/audit.log")

def main():
    parser = argparse.ArgumentParser(description="Log email send action to audit file")
    parser.add_argument("--status", choices=["success", "failure"], required=True, help="Send status")
    parser.add_argument("--to", required=True, help="Recipient address(es)")
    parser.add_argument("--subject", required=True, help="Subject line")
    parser.add_argument("--message-id", default="", help="Sent message ID")
    parser.add_argument("--error", default="", help="Error message if failed")
    args = parser.parse_args()

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "skill": "gog-email-send",
        "action": "email-send",
        "status": args.status,
        "message_id": args.message_id,
        "to": [r.strip() for r in args.to.split(",") if r.strip()],
        "subject": args.subject,
        "error": args.error
    }

    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"Logged to {LOG_PATH}")
    except Exception as e:
        print(f"Failed to write audit log: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
