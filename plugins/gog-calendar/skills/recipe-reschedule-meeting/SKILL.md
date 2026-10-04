---
name: recipe-reschedule-meeting
description: "Move a Google Calendar event to a new time and automatically notify all attendees using either gog or gws CLI."
metadata:
  version: 1.2.0
  openclaw:
    category: "recipe"
    domain: "scheduling"
    requires:
      any_bin_of:
        - gog
        - gws
allowed-tools: Bash(gog:*|gws:*) Read
---

# Reschedule a Google Calendar Meeting

Move a Google Calendar event to a new time and automatically notify all attendees using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Locate the event ID
gog calendar search "Strategy Sync" --json

# 2. Update meeting time and notify participants
gog calendar update primary <EVENT_ID> \
  --from "2026-03-25T15:00:00Z" \
  --to "2026-03-25T16:00:00Z" \
  --send-updates all \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Locate event ID
gws calendar +agenda

# 2. Patch event start/end and send update notifications
gws calendar events patch \
  --params '{"calendarId": "primary", "eventId": "<EVENT_ID>", "sendUpdates": "all"}' \
  --json '{
    "start": {"dateTime": "2026-03-25T15:00:00Z"},
    "end": {"dateTime": "2026-03-25T16:00:00Z"}
  }' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/validate_time_shift.py](scripts/validate_time_shift.py)
