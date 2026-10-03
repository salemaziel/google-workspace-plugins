---
name: calendar-cancel
description: "Cancel or delete a calendar event safely with confirmation using gog CLI"
---

# /calendar-cancel — Delete Event with Confirmation

Locate and cancel existing calendar events with mandatory user approval.

## Usage
- `/calendar-cancel <eventId>` — Deletes an event by its unique ID.
- `/calendar-cancel "Design Review"` — Searches for an event by name to locate ID before deleting.
- `/calendar-cancel tomorrow at 3pm` — Identifies candidate event by time.

## Execution Steps
1. Locate target event ID:
   - If ID provided directly in `{{args}}`, inspect event details with `gog calendar list --json`.
   - If search query provided, search matching events across the relevant date range.
2. Present cancellation confirmation box:
   ```markdown
   ==================================================
   ⚠️ CALENDAR EVENT CANCELLATION
   ==================================================
   Title:       Design Review
   Time:        2026-10-04 15:00 - 16:00
   Event ID:    abc123xyz
   Attendees:   alice@example.com (will receive cancellation)
   ==================================================
   ```
3. Await explicit confirmation ("yes", "delete", "cancel").
4. Execute deletion command:
   ```bash
   gog calendar delete <eventId>
   ```
5. Confirm successful removal.
