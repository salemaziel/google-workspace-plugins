---
name: standup
description: "Generate today's standup summary (meetings, priority tasks, blockers) via gws workflow"
---

Compile today's meetings and open tasks into a concise morning standup briefing.

## Usage
- `/standup`

## Workflow
1. Execute the cross-service standup workflow:
   ```bash
   gws workflow +standup-report
   ```
2. Parse and format the output:
   - **Today's Agenda**: Times, meeting titles, participant lists, and video links.
   - **Open Tasks**: Due dates, task titles, and priorities.
   - **Blockers & Flags**: Conflicting schedules or overdue items.
