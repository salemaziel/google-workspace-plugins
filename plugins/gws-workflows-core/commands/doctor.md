---
name: doctor
description: "Run pre-flight diagnostics, binary verification, and OAuth validation for gws"
---

Run end-to-end environment diagnostics for Google Workspace CLI.

## Usage
- `/doctor`
- `/doctor --json`

## Workflow
1. Locate `gws_doctor.py` via `${CLAUDE_PLUGIN_ROOT}` or relative directory:
   ```bash
   SCRIPT_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}/scripts"
   python3 "$SCRIPT_ROOT/gws_doctor.py" "$@"
   ```
2. Checks performed:
   - CLI binary presence (`which gws`)
   - CLI version verification (`gws --version`)
   - OAuth credentials and token freshness
   - API endpoint reachability (Gmail, Drive, Calendar, Tasks)
3. Output health scorecard with remediation steps if any checks fail.
