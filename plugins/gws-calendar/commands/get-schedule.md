---
name: get-schedule
description: "Show your schedule for today, tomorrow, or a specified date range using gws CLI"
---

# /get-schedule — Display Calendar Agenda

Query your Google Calendar agenda with chronological grouping, Google Meet links, and attendee details.

## Usage
- `/get-schedule` — Shows today's schedule.
- `/get-schedule tomorrow` — Displays tomorrow's agenda.
- `/get-schedule --week` — Displays full 7-day schedule.
- `/get-schedule --date "2026-10-15"` — Displays agenda for a specific date.

## Execution Steps
1. Parse date parameters from `{{args}}` (defaults to today).
2. Execute agenda command:
   ```bash
   gws calendar +agenda --date "${DATE:-today}" [--week] --format "${FORMAT:-table}"
   ```
3. Format events chronologically:
   | Time | Event Title | Location / Meet Link | Attendees | Status |
   |---|---|---|---|---|
4. Highlight any schedule overlaps or zero-minute transitions.
