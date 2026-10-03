---
name: list-tasks
description: "List tasks from Google Tasks lists with completion status and due dates"
---

List pending and completed tasks from Google Tasks.

## Usage
- `/list-tasks`
- `/list-tasks --tasklist <listId>`
- `/list-tasks --all` (include completed tasks)

## Workflow
1. Determine target tasklist (defaults to `@default`).
2. Fetch tasks using `gws`:
   ```bash
   gws tasks tasks list --params '{"tasklist": "${TASKLIST:-@default}", "showCompleted": ${SHOW_COMPLETED:-false}}' --format table
   ```
3. Format output:
   - Task ID
   - Status (`[ ]` or `[x]`)
   - Title
   - Due Date
   - Notes snippet
