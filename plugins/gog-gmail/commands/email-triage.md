---
name: email-triage
description: "Scan and triage unread Gmail messages with gog CLI"
---

Scan and triage unread emails:
1. Run `gog gmail search "is:unread" --max 15 --json`.
2. Categorize emails by importance and thread status.
3. Present a prioritized summary table with sender, subject, date, and suggested action.
