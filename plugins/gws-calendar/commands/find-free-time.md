---
name: find-free-time
description: "Find mutual open meeting windows across team members using gws recipe"
---

# /find-free-time — Multi-Party Availability Finder

Query free/busy intervals across participants and discover open meeting windows during business hours.

## Usage
- `/find-free-time --attendees "alice@example.com,bob@example.com"`
- `/find-free-time --attendees "client@company.com" --days 5 --duration 45m`

## Execution Steps
1. Parse attendees, search horizon, and meeting duration from `{{args}}`.
2. Execute recipe:
   ```bash
   gws recipe run find-free-time --params '{"attendees": ["<email1>", "<email2>"], "days": ${DAYS:-3}, "durationMinutes": ${MINUTES:-30}}'
   ```
3. Analyze overlaps between 09:00 and 17:00 in mutual timezones.
4. Present Top 3 open slots:
   - **Slot 1**: [Date] at [Time]
   - **Slot 2**: [Date] at [Time]
   - **Slot 3**: [Date] at [Time]
5. Offer shortcut: "Type `/insert-event` to schedule one of these slots."
