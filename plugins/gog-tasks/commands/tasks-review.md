---
name: tasks-review
description: "Run morning standup or evening daily task review using gog CLI"
---

# /tasks-review — Daily Task Prioritization & Standup

Audit overdue items, identify Top 3 Most Important Tasks (MITs) for today, and reconcile finished work.

## Usage
- `/tasks-review` — Runs full daily task audit.
- `/tasks-review morning` — Prioritizes today's focus items and clears overdue backlog.
- `/tasks-review evening` — Reconciles completions and reschedules remaining items.

## Execution Steps
1. Fetch all active tasks across lists:
   ```bash
   TASKLIST_ID=$(gog tasks lists --json | jq -r '.tasklists[0].id')
   gog tasks list "$TASKLIST_ID" --json
   ```
2. Segment tasks by priority and due dates:
   - 🔴 **Overdue / Urgent**: Items with past due dates.
   - 🟡 **Due Today**: High-priority commitments.
   - ⚪ **Upcoming**: Looking ahead 48 hours.
3. Formulate the **Top 3 Most Important Tasks (MITs)** for today:
   1. [MIT 1 - High Impact]
   2. [MIT 2 - High Impact]
   3. [MIT 3 - Routine or Quick Win]
4. Display daily executive dashboard with clear progress indicators.
