---
name: reschedule
description: "Move a calendar event to a new time and notify attendees via gws recipe"
---

# /reschedule — Reschedule Calendar Meeting

Move an existing meeting to a new time slot and automatically update all attendees.

## Usage
- `/reschedule <eventId> --new-time "2026-10-06T15:00:00"`
- `/reschedule "Sprint Review" --to "Thursday at 2pm"`

## Execution Steps
1. Identify event ID and target new time from `{{args}}`.
2. Confirm with user:
   - Event: Sprint Review
   - Current Time: Oct 5, 10:00 AM
   - New Time: Oct 6, 03:00 PM
3. Execute reschedule recipe:
   ```bash
   gws recipe run reschedule-meeting --params '{"eventId": "<id>", "newStartTime": "<ISO8601>"}'
   ```
4. Confirm calendar updated and notifications dispatched.
