---
name: tasks-list
description: "List and filter Google Tasks by due date, list, or status with gog CLI"
---

# /tasks-list — View Active Tasks

Query tasks from Google Tasks, grouped by priority and due date.

## Usage
- `/tasks-list` — Lists open tasks from the primary task list.
- `/tasks-list --due today` — Filters tasks due today or overdue.
- `/tasks-list --list Work` — Lists tasks from a specific task list named "Work".
- `/tasks-list --all` — Includes completed tasks.

## Execution Steps
1. Discover task list ID from `{{args}}`:
   ```bash
   TASKLIST_ID=$(gog tasks lists --json | jq -r '.tasklists[0].id')
   ```
2. Query tasks:
   ```bash
   gog tasks list "$TASKLIST_ID" --json
   ```
3. Group tasks into actionable sections:
   - ⚠️ **Overdue**: Due date earlier than today.
   - 📅 **Due Today**: Due by end of today.
   - ⏳ **Upcoming**: Due in the next 7 days.
   - 📥 **No Due Date**: General backlog.
4. Render clean Markdown table:
   | Status | Priority | Title | Due Date | Task ID |
   |---|---|---|---|---|
5. Offer follow-up shortcuts:
   - "Type `done <ID>` to mark a task complete."
   - "Type `review` to prioritize today's Top 3 tasks."
