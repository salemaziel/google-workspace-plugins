---
name: review-overdue
description: "Audit overdue and impending tasks across all Google Tasks lists"
---

Scan task lists for tasks whose due dates have elapsed or are approaching within 24 hours.

## Usage
- `/review-overdue`
- `/review-overdue --tasklist <listId>`

## Workflow
1. Enumerate task lists:
   ```bash
   gws tasks tasklists list --format json
   ```
2. For each active list, query pending tasks:
   ```bash
   gws tasks tasks list --params '{"tasklist": "<tasklistId>", "showCompleted": false}' --format json
   ```
3. Compare `due` timestamps with current UTC timestamp:
   - Identify tasks with `due < now`.
   - Calculate days/hours overdue.
4. Present findings:
   - Table of overdue items ranked by lateness.
   - Interactive options: Reschedule (`gws tasks tasks patch`), Mark Completed (`gws tasks tasks patch`), or Delete (`gws tasks tasks delete`).
