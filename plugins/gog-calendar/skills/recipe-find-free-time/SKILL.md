---
name: recipe-find-free-time
description: "Query Google Calendar free/busy status for multiple users to find optimal meeting slots using either gog or gws CLI."
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

# Find Free Time Across Calendars

Query Google Calendar free/busy status for multiple users to find optimal meeting slots using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Query free/busy slots across target attendees
gog calendar freebusy primary "user1@company.com" "user2@company.com" \
  --from "2026-03-23T08:00:00Z" \
  --to "2026-03-23T18:00:00Z" \
  --json

# 2. Schedule meeting in identified open slot
gog calendar create primary \
  --summary "Strategy Sync" \
  --from "2026-03-23T14:00:00Z" \
  --to "2026-03-23T14:30:00Z" \
  --attendees "user1@company.com,user2@company.com" \
  --with-meet \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Query free/busy matrix
gws calendar freebusy query \
  --json '{
    "timeMin": "2026-03-23T08:00:00Z",
    "timeMax": "2026-03-23T18:00:00Z",
    "items": [{"id": "user1@company.com"}, {"id": "user2@company.com"}]
  }'

# 2. Insert event in verified free window
gws calendar +insert \
  --summary "Strategy Sync" \
  --attendee user1@company.com \
  --attendee user2@company.com \
  --start "2026-03-23T14:00:00" \
  --end "2026-03-23T14:30:00"
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/find_open_windows.py](scripts/find_open_windows.py)
