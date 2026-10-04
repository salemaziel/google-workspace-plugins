---
name: recipe-batch-invite-to-event
description: "Add multiple attendees to an existing Google Calendar event and send email notifications using either gog or gws CLI."
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

# Batch Invite Attendees to Calendar Event

Add multiple attendees to an existing Google Calendar event and send email notifications using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Inspect existing event details and current attendees
gog calendar event primary <EVENT_ID> --json

# 2. Add comma-separated attendees and dispatch update emails
gog calendar update primary <EVENT_ID> \
  --add-attendee "alice@company.com,bob@company.com,carol@company.com" \
  --send-updates all \
  --json

# 3. Verify updated attendee list
gog calendar event primary <EVENT_ID> --select attendees
```

### Option B: Using `gws` CLI
```bash
# 1. Inspect existing event details
gws calendar events get --params '{"calendarId": "primary", "eventId": "<EVENT_ID>"}'

# 2. Patch attendees array and send notifications
gws calendar events patch \
  --params '{"calendarId": "primary", "eventId": "<EVENT_ID>", "sendUpdates": "all"}' \
  --json '{"attendees": [{"email": "alice@company.com"}, {"email": "bob@company.com"}, {"email": "carol@company.com"}]}'

# 3. Verify updated event
gws calendar events get --params '{"calendarId": "primary", "eventId": "<EVENT_ID>"}' --format table
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/validate_attendees.py](scripts/validate_attendees.py)
