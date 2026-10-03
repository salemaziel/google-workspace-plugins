---
name: clear-schedule
description: "Clear or cancel events on your calendar for a date range with mandatory preview and confirmation"
---

# /clear-schedule — Cancel Calendar Events

Remove or cancel events across a designated timeframe with mandatory preview verification.

## Usage
- `/clear-schedule today` — Lists and prepares to clear today's events.
- `/clear-schedule <eventId>` — Cancels a specific event by ID.

## Mandatory Execution Procedure
1. Identify target events across the date range.
2. Display cancellation preview box:
   ```markdown
   ==================================================
   ⚠️ CALENDAR CANCELLATION PREVIEW
   ==================================================
   Target Date: 2026-10-04
   Candidate Events:
   1. 10:00 AM - Sprint Sync (ID: ev1)
   2. 02:00 PM - Product Review (ID: ev2)
   Attendees will receive automated cancellation notices.
   ==================================================
   ```
3. Require explicit positive confirmation ("yes", "cancel").
4. Execute deletion command:
   ```bash
   gws calendar events.delete --params '{"calendarId": "primary", "eventId": "<id>"}'
   ```
5. Confirm deletion completion.
