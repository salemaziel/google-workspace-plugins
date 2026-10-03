---
name: tasks-delete
description: "Delete or cancel a task safely with confirmation using gog CLI"
---

# /tasks-delete — Remove a Task with Confirmation

Cancel and remove a task from Google Tasks with mandatory verification.

## Usage
- `/tasks-delete <taskId>` — Deletes task by unique ID.
- `/tasks-delete "Obsolete task title"` — Resolves task by title, confirms, and deletes.

## Execution Steps
1. Parse task ID or title from `{{args}}`.
2. Display deletion confirmation box:
   ```markdown
   ==================================================
   ⚠️ TASK DELETION CONFIRMATION
   ==================================================
   Task Title:   Review vendor proposal
   Task ID:      xyz789
   Due Date:     2026-10-06
   List:         Work
   ==================================================
   ```
3. Await explicit user confirmation ("yes", "delete", "confirm").
4. Execute deletion command:
   ```bash
   gog tasks delete <taskId>
   ```
5. Confirm task removed.
