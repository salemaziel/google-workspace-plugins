---
name: focus-time
description: "Block recurring focus time on Google Calendar using gws recipe"
---

# /focus-time — Block Deep Work Hours

Create recurring focus time blocks on your calendar to protect uninterrupted deep work.

## Usage
- `/focus-time --start "09:00" --duration 2h` — Blocks 2 hours every weekday morning.
- `/focus-time --days "Mon,Wed,Fri" --start "14:00" --duration 3h`

## Execution Steps
1. Parse focus time parameters from `{{args}}`.
2. Preview focus block schedule with user.
3. Execute recipe:
   ```bash
   gws recipe run block-focus-time --params '{"startTime": "<time>", "durationHours": <hours>}'
   ```
4. Confirm recurring focus blocks scheduled on primary calendar.
