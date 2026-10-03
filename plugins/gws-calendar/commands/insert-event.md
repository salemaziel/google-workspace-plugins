---
name: insert-event
description: "Schedule a calendar event with Google Meet link and attendees using gws CLI"
---

# /insert-event — Create Calendar Event

Book a new calendar meeting with automated Google Meet video room creation and attendee invites.

## Usage
- `/insert-event --title "Sync" --start "2026-10-05T14:00:00" --duration 30m --meet`
- `/insert-event --title "Planning" --start "2026-10-06T10:00:00" --duration 1h --attendees "team@example.com"`

## Mandatory Execution Procedure
1. Parse event title, start time, duration, attendees, and Meet flag from `{{args}}`.
2. Display event creation preview:
   ```markdown
   ==================================================
   ⚠️ CALENDAR EVENT CREATION PREVIEW
   ==================================================
   Title:       Sync
   Start:       2026-10-05 14:00 (Local Time)
   Duration:    30 minutes
   Google Meet: Yes
   Attendees:   alice@example.com
   ==================================================
   ```
3. Await explicit confirmation ("yes", "create").
4. Execute insert command:
   ```bash
   gws calendar +insert --title "<title>" --start "<ISO8601>" --duration "<duration>" [--meet] [--attendees "<emails>"]
   ```
5. Return created event link and Google Meet conference URL.
