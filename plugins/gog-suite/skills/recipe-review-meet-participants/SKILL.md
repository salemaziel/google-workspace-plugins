---
name: recipe-review-meet-participants
description: "Review who attended a Google Meet conference and participant durations using either gog or gws CLI."
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

# Review Google Meet Attendance

Review who attended a Google Meet conference and participant durations using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. List conference records
gog meet records list --json

# 2. Inspect participants of target conference
gog meet records participants <CONFERENCE_ID> --json
```

### Option B: Using `gws` CLI
```bash
# 1. List recent conferences
gws meet conferenceRecords list --format table

# 2. List participants for conference
gws meet conferenceRecords participants list \
  --params '{"parent": "conferenceRecords/<CONFERENCE_ID>"}' \
  --format table
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/attendance_calc.py](scripts/attendance_calc.py)
