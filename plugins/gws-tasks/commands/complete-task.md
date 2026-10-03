---
name: complete-task
description: "Mark a Google Task as completed"
---

Mark a pending task as completed.

## Usage
- `/complete-task <taskId>`
- `/complete-task <taskId> --tasklist <listId>`

## Workflow
1. Parse task ID and optional tasklist ID (default `@default`).
2. Update task status to `completed`:
   ```bash
   gws tasks tasks patch --params '{"tasklist": "${TASKLIST:-@default}", "task": "<taskId>"}' --json '{"status": "completed"}'
   ```
3. Confirm completion status and updated timestamp.
