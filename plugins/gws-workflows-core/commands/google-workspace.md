---
name: google-workspace
description: "Master Google Workspace CLI operations: setup diagnostics, security audit, recipe runner, and output analysis"
---

Master orchestration command for Google Workspace CLI (`gws`).

## Subcommands & Usage
- `/google-workspace setup [--json]` — Run pre-flight diagnostics and OAuth validation
- `/google-workspace audit [--services gmail,drive,calendar]` — Run security configuration audit
- `/google-workspace recipe list [--persona <role>]` — List available recipe automation templates
- `/google-workspace recipe run <name> [--dry-run]` — Execute a recipe template
- `/google-workspace auth-guide` — Interactive OAuth2 and Service Account setup wizard

## Execution Workflow
1. Locate script root using `${CLAUDE_PLUGIN_ROOT}` or relative directory traversal:
   ```bash
   SCRIPT_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}/scripts"
   ```
2. Dispatch to the appropriate Python utility:
   - For `setup`: `python3 "$SCRIPT_ROOT/gws_doctor.py" "$@"`
   - For `audit`: `python3 "$SCRIPT_ROOT/workspace_audit.py" "$@"`
   - For `recipe`: `python3 "$SCRIPT_ROOT/gws_recipe_runner.py" "$@"`
   - For `auth-guide`: `python3 "$SCRIPT_ROOT/auth_setup_guide.py" "$@"`
3. Summarize findings and format action items for the user.
