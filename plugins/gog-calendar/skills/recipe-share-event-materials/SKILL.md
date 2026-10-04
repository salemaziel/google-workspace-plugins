---
name: recipe-share-event-materials
description: "Share Google Drive files with all attendees of a Google Calendar event using either gog or gws CLI."
metadata:
  version: 1.2.0
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      any_bin_of:
        - gog
        - gws
allowed-tools: Bash(gog:*|gws:*) Read
---

# Share Files with Meeting Attendees

Share Google Drive files with all attendees of a Google Calendar event using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Fetch event details and attendee list
gog calendar event primary <EVENT_ID> --json

# 2. Grant read access to target attendees on Drive file
gog drive share <FILE_ID> \
  --email "attendee@company.com" \
  --role reader \
  --json

# 3. Verify active permissions on the document
gog drive permissions <FILE_ID> --json
```

### Option B: Using `gws` CLI
```bash
# 1. Get event attendees
gws calendar events get --params '{"calendarId": "primary", "eventId": "<EVENT_ID>"}'

# 2. Share Drive file with attendee
gws drive permissions create \
  --params '{"fileId": "<FILE_ID>"}' \
  --json '{"role": "reader", "type": "user", "emailAddress": "attendee@company.com"}'

# 3. List active permissions
gws drive permissions list --params '{"fileId": "<FILE_ID>"}' --format table
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/extract_attendees.py](scripts/extract_attendees.py)
