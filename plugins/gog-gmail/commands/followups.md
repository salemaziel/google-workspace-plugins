---
name: followups
description: "Detect unanswered emails and generate followup reminders with gog CLI"
---

Track pending email followups:
1. Search sent threads without replies: `gog gmail search "from:me newer_than:14d" --json`.
2. Identify contacts who have not replied.
3. Display a list of overdue threads with last contact date and suggested followup draft.
