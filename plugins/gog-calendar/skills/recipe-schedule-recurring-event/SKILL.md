---
name: recipe-schedule-recurring-event
description: "Create a recurring Google Calendar event with attendees using either gog or gws CLI."
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

# Schedule a Recurring Meeting

Create a recurring Google Calendar event with attendees using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Create recurring weekly standup with attendees and Meet
gog calendar create primary \
  --summary "Weekly Team Standup" \
  --from "2026-03-23T09:00:00Z" \
  --to "2026-03-23T09:30:00Z" \
  --rrule "FREQ=WEEKLY;BYDAY=MO" \
  --attendees "team@company.com" \
  --with-meet \
  --json

# 2. Verify creation across next 2 weeks
gog calendar events --from "2026-03-23T00:00:00Z" --to "2026-04-06T00:00:00Z" --json
```

### Option B: Using `gws` CLI
```bash
# 1. Insert recurring event via Discovery API
gws calendar events insert \
  --params '{"calendarId": "primary"}' \
  --json '{
    "summary": "Weekly Team Standup",
    "start": {"dateTime": "2026-03-23T09:00:00Z"},
    "end": {"dateTime": "2026-03-23T09:30:00Z"},
    "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO"],
    "attendees": [{"email": "team@company.com"}]
  }'

# 2. Verify in agenda
gws calendar +agenda --days 14 --format table
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/recurrence_helper.py](scripts/recurrence_helper.py)
