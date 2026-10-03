---
name: tasks-done
description: "Mark a task complete in Google Tasks by ID or title with gog CLI"
---

# /tasks-done — Complete a Task

Mark tasks as completed in Google Tasks with verification of the task title.

## Usage
- `/tasks-done <taskId>` — Marks task complete by ID.
- `/tasks-done "Finish slide deck"` — Resolves task by title, confirms, and marks complete.

## Execution Steps
1. Parse task ID or title from `{{args}}`.
2. If title provided:
   - Query active tasks to match title and retrieve ID.
   - Display matched task: `Completing: [P1] Finish slide deck (ID: abc123)`
3. Execute completion command:
   ```bash
   gog tasks done <taskId>
   ```
4. Output completion confirmation card:
   - ✅ **Task Completed**: [Title]
   - **Timestamp**: [Local Time]
