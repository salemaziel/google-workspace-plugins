---
name: calendar-create
description: "Schedule a calendar event with mandatory preview and confirmation using gog CLI"
---

# /calendar-create — Schedule Event with Confirmation Safeguards

Book meetings, time blocks, or calendar reminders with conflict checking and explicit confirmation.

## Usage
- `/calendar-create --title "Design Review" --start "2026-10-04T15:00:00" --duration 1h`
- `/calendar-create "sync with Sarah tomorrow at 2pm for 30m"`
- `/calendar-create --title "Standup" --start "2026-10-05T09:00:00" --attendees "team@example.com"`

## Mandatory Execution Procedure
1. Parse event details from `{{args}}`:
   - Title / Subject.
   - Start date & time in local timezone (converted to ISO 8601 string).
   - Duration (e.g. `30m`, `45m`, `1h`).
   - Attendee email addresses.
2. Conflict Pre-check:
   - Run `gog calendar list --json` to verify no existing conflicts at the target time.
3. Present verification panel to user:
   ```markdown
   ==================================================
   ⚠️ CALENDAR EVENT CREATION PREVIEW
   ==================================================
   Title:       Sprint Planning
   Start Time:  2026-10-05 10:00 AM (Local Time)
   Duration:    1 hour
   Attendees:   alice@example.com, bob@example.com
   Calendar:    default
   ==================================================
   ```
4. Require explicit user confirmation ("yes", "confirm") before scheduling.
5. Upon confirmation, execute:
   ```bash
   gog calendar create --title "<title>" --start "<ISO8601>" --duration <duration> [--attendees "<emails>"]
   ```
6. Return created event ID and confirmation summary.
