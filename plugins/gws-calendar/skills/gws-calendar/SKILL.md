---
name: gws-calendar
description: "Manage calendars, schedule meetings, query attendee free/busy availability, and configure Google Meet calls with gws CLI."
metadata:
  version: 0.22.5
  category: "productivity"
  requires:
    bins:
      - gws
---

# gws-calendar — Google Calendar CLI Integration

Manage calendars, schedule meetings, inspect agendas, and coordinate attendee availability through the `gws` CLI.

## Quick Workflow
1. **Query Agenda**: List upcoming events across calendars with `+agenda`.
2. **Find Common Availability**: Query attendee availability via `gws calendar freebusy query` and pipe into `find_free_slots_gws.py`.
3. **Schedule**: Insert calendar events with optional automated Google Meet video links (`conferenceDataVersion=1`).

## Core Commands

```bash
# Show upcoming agenda across all calendars
gws calendar +agenda

# Check free/busy availability across multiple users
gws calendar freebusy query --json '{
  "timeMin": "2026-10-06T09:00:00Z",
  "timeMax": "2026-10-06T18:00:00Z",
  "items": [{"id": "user1@company.com"}, {"id": "user2@company.com"}]
}' | ./scripts/find_free_slots_gws.py --duration-minutes 30

# Insert a new event with automatic Google Meet conference
gws calendar events insert \
  --params '{"calendarId": "primary", "conferenceDataVersion": 1}' \
  --json '{
    "summary": "Sprint Planning",
    "start": {"dateTime": "2026-10-06T10:00:00-04:00"},
    "end": {"dateTime": "2026-10-06T11:00:00-04:00"},
    "attendees": [{"email": "colleague@example.com"}],
    "conferenceData": {"createRequest": {"requestId": "plan-1", "conferenceSolutionKey": {"type": "hangoutsMeet"}}}
  }'
```

## Safety & Best Practices
- **Conflict Prevention**: Always run free/busy queries before scheduling group meetings.
- **Explicit Confirmation**: Present proposed event time, attendees, and duration to the user before inserting.

## Progressive Disclosure & References
- **Free/Busy Calculation**: See [references/freebusy-discovery.md](references/freebusy-discovery.md) for querying attendee schedules.
- **Google Meet Integration**: See [references/meet-config.md](references/meet-config.md) for generating video conference links.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for RFC 3339 timezone handling and permission errors.
- **Free Slot Finder**: Use [scripts/find_free_slots_gws.py](scripts/find_free_slots_gws.py) to calculate open gaps between busy events.
- **Event Template**: See [templates/event-summary.md](templates/event-summary.md) for meeting notifications.
