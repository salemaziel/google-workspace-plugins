---
name: recipe-plan-weekly-schedule
description: "Review your Google Calendar week, identify gaps, and schedule protected work blocks using either gog or gws CLI."
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

# Plan Weekly Calendar Schedule

Review your Google Calendar week, identify gaps, and schedule protected work blocks using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Inspect 7-day calendar agenda
gog calendar events \
  --from "$(date +%Y-%m-%d)" \
  --to "$(date -d '+7 days' +%Y-%m-%d 2>/dev/null || date -v+7d +%Y-%m-%d)" \
  --json

# 2. Add deep work blocks in calendar gaps
gog calendar create primary \
  --summary "Deep Work Block" \
  --from "2026-03-24T14:00:00Z" \
  --to "2026-03-24T16:00:00Z" \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Inspect weekly agenda
gws calendar +agenda --days 7

# 2. Insert work block
gws calendar +insert \
  --summary "Deep Work Block" \
  --start "2026-03-24T14:00:00" \
  --end "2026-03-24T16:00:00"
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/summarize_week.py](scripts/summarize_week.py)
