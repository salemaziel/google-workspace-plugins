---
name: recipe-block-focus-time
description: "Create recurring focus time blocks on Google Calendar to protect deep work hours using either gog or gws CLI."
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

# Block Focus Time on Google Calendar

Create recurring focus time blocks on Google Calendar to protect deep work hours using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Create a native Focus Time block with auto-decline and DND
gog calendar focus-time \
  --summary "Focus Time" \
  --from "2026-03-23T09:00:00Z" \
  --to "2026-03-23T11:00:00Z" \
  --auto-decline all \
  --decline-message "Declined: In protected deep work focus time." \
  --chat-status doNotDisturb \
  --rrule "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR" \
  --json

# 2. Verify upcoming focus time entries
gog calendar events --today --json
```

### Option B: Using `gws` CLI
```bash
# 1. Insert recurring focus event with opaque transparency
gws calendar events insert \
  --params '{"calendarId": "primary"}' \
  --json '{
    "summary": "Focus Time",
    "description": "Protected deep work block",
    "start": {"dateTime": "2026-03-23T09:00:00Z"},
    "end": {"dateTime": "2026-03-23T11:00:00Z"},
    "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"],
    "transparency": "opaque"
  }'

# 2. Verify agenda
gws calendar +agenda --days 7
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/generate_rrule.py](scripts/generate_rrule.py)
