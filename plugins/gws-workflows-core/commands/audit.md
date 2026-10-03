---
name: audit
description: "Audit Google Workspace security, sharing policies, and API configuration"
---

Perform a security and configuration audit across Workspace services.

## Usage
- `/audit`
- `/audit --services gmail,drive,calendar`

## Workflow
1. Locate `workspace_audit.py`:
   ```bash
   SCRIPT_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}/scripts"
   python3 "$SCRIPT_ROOT/workspace_audit.py" "$@"
   ```
2. Check security settings:
   - External sharing configurations.
   - Mail forwarding rules and SPF/DKIM verification.
   - OAuth permission scopes and app passwords.
3. Output security audit scorecard with risk ratings and remediation advice.
