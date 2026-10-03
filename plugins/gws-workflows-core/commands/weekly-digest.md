---
name: weekly-digest
description: "Generate weekly briefing of schedule, priorities, and unread email volume via gws workflow"
---

Synthesize an executive summary of the week ahead.

## Usage
- `/weekly-digest`

## Workflow
1. Execute the weekly digest workflow:
   ```bash
   gws workflow +weekly-digest
   ```
2. Synthesize:
   - Total meeting count and total meeting hours for the upcoming 7 days.
   - High-impact meetings (1-on-1s, executive reviews, client calls).
   - Unread inbox volume and backlog status.
   - Project deadlines and milestone tasks due this week.
