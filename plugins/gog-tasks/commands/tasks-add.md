---
name: tasks-add
description: "Add a new task to Google Tasks with priority, due date, and notes using gog CLI"
---

# /tasks-add — Create a New Task

Insert a prioritized task with optional due date, notes, and list targeting.

## Usage
- `/tasks-add "Finish slide deck" --due tomorrow`
- `/tasks-add "[P1] Submit monthly expense report" --due "2026-10-15"`
- `/tasks-add "Buy server cables" --list Personal`

## Execution Steps
1. Parse task title, due date, and notes from `{{args}}`.
   - Normalize relative dates (`today`, `tomorrow`, `monday`) to ISO `YYYY-MM-DD`.
2. Discover target task list ID:
   ```bash
   TASKLIST_ID=$(gog tasks lists --json | jq -r '.tasklists[0].id')
   ```
3. Execute creation command:
   ```bash
   gog tasks add "$TASKLIST_ID" "<title>" [--due "<YYYY-MM-DD>"] [--notes "<notes>"] --json
   ```
4. Output creation confirmation:
   - **Task**: [Title]
   - **Due Date**: [Date]
   - **List**: [ListName]
   - **Task ID**: [TaskID]
