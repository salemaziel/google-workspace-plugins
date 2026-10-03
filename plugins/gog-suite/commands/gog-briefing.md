---
name: gog-briefing
description: "Generate a unified executive briefing: Today's Calendar + Urgent Emails + Top Tasks via gog CLI"
---

# /gog-briefing — Unified Executive Briefing

Aggregate your daily schedule, unread communications, and open tasks into a single high-signal executive dashboard.

## Usage
- `/gog-briefing` — Compiles today's complete briefing.
- `/gog-briefing --account work@company.com` — Generates briefing for a specific account.

## Execution Steps
1. Fetch today's schedule:
   ```bash
   gog calendar list --days 1 --json
   ```
2. Fetch top unread messages:
   ```bash
   gog gmail search "is:unread" --max 10 --json
   ```
3. Fetch tasks due today:
   ```bash
   TASKLIST_ID=$(gog tasks lists --json | jq -r '.tasklists[0].id')
   gog tasks list "$TASKLIST_ID" --json
   ```
4. Render Executive Dashboard:
   ```markdown
   # 🌅 Morning Executive Briefing — [Date]

   ## 📅 Today's Meetings
   - **09:30 AM** — Standup (Zoom)
   - **02:00 PM** — Architecture Review (Google Meet)

   ## ✉️ Priority Inquiries (Unread)
   - [CEO] "Q3 Deliverables Update" (08:45 AM)
   - [Client] "Contract Amendment Signed" (Yesterday)

   ## 🎯 Focus Tasks (Due Today)
   - [ ] [P0] Deploy hotfix to staging
   - [ ] [P1] Review and merge Pull Request #104
   ```
5. Suggest immediate next actions:
   - "Prepare for 2:00 PM meeting?"
   - "Triage unread emails?"
