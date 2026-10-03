---
name: triage
description: "Scan and triage unread Gmail inbox messages with gws CLI"
---

# /triage — Inbox Triage & Summary

Scan your unread inbox, group messages by priority, and identify items needing immediate action.

## Usage
- `/triage` — Scans latest 15 unread messages.
- `/triage --max 30` — Expands triage horizon to 30 messages.

## Execution Steps
1. Execute triage command:
   ```bash
   gws gmail +triage --max ${MAX:-15}
   ```
2. Classify messages into priority categories:
   - 🔴 **Urgent**: Critical alerts, customer escalations, executive requests.
   - 🟡 **Action Needed**: Requests awaiting your input or review.
   - 🟢 **Informational**: Newsletters, status digests, receipts.
3. Render structured summary:
   | Status | From | Subject | Date | Action Required |
   |---|---|---|---|---|
4. Suggest next actions:
   - "Draft reply to #1 with `/reply`?"
   - "Archive notifications with `/filter`?"
