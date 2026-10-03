---
name: recipe
description: "Browse, filter, and run 43 Google Workspace automation recipes with dry-run support"
---

Execute automated workflow recipes across Google Workspace services.

## Usage
- `/recipe list`
- `/recipe list --persona <role>` (e.g. `pm`, `sales`, `hr`, `it`)
- `/recipe run <recipeName> --dry-run`
- `/recipe run <recipeName> --yes`

## Workflow
1. Locate `gws_recipe_runner.py` via `${CLAUDE_PLUGIN_ROOT}` or relative directory:
   ```bash
   SCRIPT_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}/scripts"
   python3 "$SCRIPT_ROOT/gws_recipe_runner.py" "$@"
   ```
2. Display matching recipe templates, parameters, and execution previews.
