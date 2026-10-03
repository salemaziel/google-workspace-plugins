#!/usr/bin/env python3
"""
check_accounts.py - Audit gogcli authentication, active accounts, and service availability.

Usage:
  ./scripts/check_accounts.py [--json]
"""

import sys
import subprocess
import json
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Check gogcli account health and service reachability")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    return parser.parse_args()

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
        return res.returncode == 0, res.stdout.strip(), res.stderr.strip()
    except Exception as e:
        return False, "", str(e)

def main():
    args = parse_args()
    
    # Check if gog binary exists
    installed, _, _ = run_cmd(["which", "gog"])
    if not installed:
        res = {"status": "error", "message": "gog CLI binary not found in PATH."}
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print("❌ gog CLI is not installed or not in PATH.")
        sys.exit(1)

    # Check auth list
    ok, auth_out, auth_err = run_cmd(["gog", "auth", "list", "--json"])
    accounts = []
    if ok and auth_out:
        try:
            parsed = json.loads(auth_out)
            accounts = parsed if isinstance(parsed, list) else parsed.get("accounts", [])
        except json.JSONDecodeError:
            pass

    current_account = os.environ.get("GOG_ACCOUNT", "default")
    allowed_cmds = os.environ.get("GOG_ALLOWED_COMMANDS", "all")

    # Quick ping services
    services_status = {}
    
    # Gmail test
    gm_ok, _, _ = run_cmd(["gog", "gmail", "labels", "list", "--max", "1", "--json"])
    services_status["gmail"] = "OK" if gm_ok else "UNREACHABLE / NOT_CONFIGURED"

    # Calendar test
    cal_ok, _, _ = run_cmd(["gog", "calendar", "list", "--days", "1", "--json"])
    services_status["calendar"] = "OK" if cal_ok else "UNREACHABLE / NOT_CONFIGURED"

    # Drive test
    drv_ok, _, _ = run_cmd(["gog", "drive", "list", "--max", "1", "--json"])
    services_status["drive"] = "OK" if drv_ok else "UNREACHABLE / NOT_CONFIGURED"

    data = {
        "binary_installed": True,
        "active_account": current_account,
        "allowed_commands": allowed_cmds,
        "accounts_found": len(accounts),
        "services": services_status
    }

    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print("=== gogcli Suite Diagnostics ===")
        print(f"Active Account     : {current_account}")
        print(f"Allowed Commands   : {allowed_cmds}")
        print(f"Configured Accounts: {len(accounts)}")
        print("\nService Connectivity:")
        for s, status in services_status.items():
            icon = "✅" if status == "OK" else "⚠️"
            print(f"  {icon} {s:<10} : {status}")

if __name__ == "__main__":
    main()
