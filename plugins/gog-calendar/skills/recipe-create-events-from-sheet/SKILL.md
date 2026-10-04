---
name: recipe-create-events-from-sheet
description: "Read event schedules from a Google Sheets spreadsheet and create Google Calendar entries using either gog or gws CLI."
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

# Create Calendar Events from Google Sheets

Read event schedules from a Google Sheets spreadsheet and create Google Calendar entries using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Read event rows from spreadsheet
gog sheets get <SPREADSHEET_ID> "Events!A2:E" --json

# 2. Iterate and create calendar events for each entry
gog calendar create primary \
  --summary "Team Standup" \
  --from "2026-03-23T09:00:00Z" \
  --to "2026-03-23T09:30:00Z" \
  --attendees "alice@company.com,bob@company.com" \
  --with-meet \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Read tabular event data
gws sheets +read --spreadsheet <SPREADSHEET_ID> --range "Events!A2:E"

# 2. Insert event for each row
gws calendar +insert \
  --summary "Team Standup" \
  --start "2026-03-23T09:00:00" \
  --end "2026-03-23T09:30:00" \
  --attendee alice@company.com \
  --attendee bob@company.com
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/sheet_to_events.py](scripts/sheet_to_events.py)
