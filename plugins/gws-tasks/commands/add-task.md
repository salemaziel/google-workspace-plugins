---
name: add-task
description: "Add a new task to Google Tasks with title, optional notes, due date, and target tasklist"
---

Create a new task in Google Tasks.

## Usage
- `/add-task "<title>"`
- `/add-task "<title>" --due "<YYYY-MM-DD>" --notes "<notes>"`
- `/add-task "<title>" --tasklist "<listId>"`

## Workflow
1. Parse title, due date, notes, and tasklist from arguments.
2. Build JSON payload. If `--due` is specified, format as RFC 3339 timestamp (e.g. `YYYY-MM-DDT17:00:00Z`).
3. Execute task creation via `gws`:
   ```bash
   gws tasks tasks insert --params '{"tasklist": "${TASKLIST:-@default}"}' --json '{"title": "<title>", "notes": "<notes>", "due": "<due-rfc3339>"}'
   ```
4. Confirm creation with Task ID, title, and assigned due date.
