---
name: calendar-agenda
description: "View upcoming calendar events for today, tomorrow, or next N days with gog CLI"
---

# /calendar-agenda — View Upcoming Schedule

Inspect upcoming meetings, events, and daily commitments with duration and attendee details.

## Usage
- `/calendar-agenda` — Displays today's agenda.
- `/calendar-agenda tomorrow` — Shows schedule for tomorrow.
- `/calendar-agenda week` or `/calendar-agenda --days 7` — Displays upcoming 7-day schedule.
- `/calendar-agenda --account work@company.com` — Inspects calendar for a specific account.

## Execution Steps
1. Parse arguments `{{args}}`:
   - Determine target timeframe (default: 1 day).
   - If user asks for "week", set `--days 7`.
   - Identify `--account` if specified.
2. Execute command:
   ```bash
   gog calendar list --days ${DAYS:-1} ${ACCOUNT_FLAG} --json
   ```
3. Group and format events chronologically:
   - **Morning**: Events before 12:00 PM.
   - **Afternoon**: Events between 12:00 PM and 5:00 PM.
   - **Evening**: Events after 5:00 PM.
4. Highlight key attributes:
   - Time range (e.g. `10:00 AM – 10:30 AM`).
   - Title and Location / Video link (Google Meet / Zoom).
   - Attendee list and RSVP status (`accepted`, `declined`, `needsAction`).
5. Flag any overlapping events or back-to-back commitments without buffers.
