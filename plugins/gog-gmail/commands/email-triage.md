---
name: email-triage
description: "Scan and prioritize Gmail inbox messages using gog CLI with optional filters"
---

# /email-triage — Scan and Prioritize Messages

Scan unread or matching Gmail messages, group them by priority, and suggest immediate next actions.

## Usage
- `/email-triage` — Scans latest 20 unread messages in the default account.
- `/email-triage --max 50` — Scans up to 50 unread messages.
- `/email-triage "from:client@domain.com"` — Triages messages matching a custom search query.
- `/email-triage --account work@company.com` — Triages inbox for a specific configured account.

## Execution Steps
1. Parse arguments `{{args}}`:
   - Identify query filter (defaults to `is:unread` if no query is given).
   - Identify `--max` count (defaults to `20`).
   - Identify `--account` if specified.
2. Execute the scan command:
   ```bash
   gog gmail search "${QUERY:-is:unread}" --max ${MAX:-20} ${ACCOUNT_FLAG} --json
   ```
3. Format output in a structured triage table:
   | # | Priority | From | Subject | Date | Recommended Action |
   |---|---|---|---|---|---|
   | 1 | 🔴 Urgent | CEO / Client | Q3 Delivery Delay | Today 09:15 | Draft reply acknowledging fix |
   | 2 | 🟡 Action | Team Lead | Code Review Request | Yesterday | Review PR & reply |
   | 3 | 🟢 FYI | GitHub | New Release v2.4 | Oct 2 | Archive / mark read |

4. Offer interactive follow-up shortcuts:
   - "Type `reply 1` to draft a response to email #1."
   - "Type `followups` to review unanswered sent threads."
