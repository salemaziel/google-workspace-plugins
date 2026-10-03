---
name: google-workspace
description: "Google Workspace CLI operations: setup diagnostics, security audit, recipe runner, and output analysis"
---

Google Workspace CLI operations via `gws`:
Run pre-flight diagnostics, security audits, browse/execute recipes, and analyze command output.

Usage:
- `/google-workspace setup [--json]` — Run pre-flight diagnostics and auth validation
- `/google-workspace audit [--services gmail,drive,calendar]` — Run security configuration audit
- `/google-workspace recipe list [--persona <role>]` — List available recipes
- `/google-workspace recipe run <name> [--dry-run]` — Execute a recipe
