---
name: followups
description: "Detect unanswered outgoing emails and generate follow-up reminders with gog CLI"
---

# /followups — Unanswered Thread Tracker

Analyze sent emails, identify threads that have stalled without a reply, and suggest polite follow-up nudges.

## Usage
- `/followups` — Scans sent messages from the past 14 days without a reply.
- `/followups --days 30` — Expands lookup window to the past 30 days.
- `/followups --account work@company.com` — Checks follow-ups for a specific account.

## Execution Steps
1. Parse time window `{{args}}` (default: 14 days).
2. Query outgoing messages:
   ```bash
   gog gmail search "from:me newer_than:${DAYS:-14}d" --json
   ```
3. Cross-reference thread IDs to determine whether a response was received.
4. Categorize stale threads by aging brackets:
   - ⚠️ **Critical / Overdue (7+ days)**: High urgency, requires direct check-in.
   - ⏳ **Pending Review (3–6 days)**: Ideal window for a polite, brief reminder.
   - 🕒 **Recent (1–2 days)**: Within standard response grace period; no action needed.
5. Present table with Recipient, Subject, Sent Date, Days Elapsed, and Suggested Action.
6. Provide ready-to-use 1-sentence follow-up snippets for each overdue item.
