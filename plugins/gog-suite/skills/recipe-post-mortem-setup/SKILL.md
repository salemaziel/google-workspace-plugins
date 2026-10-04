---
name: recipe-post-mortem-setup
description: "Create a Google Docs post-mortem, schedule a review meeting, and broadcast to Google Chat using either gog or gws CLI."
metadata:
  version: 1.2.0
  openclaw:
    category: "recipe"
    domain: "engineering"
    requires:
      any_bin_of:
        - gog
        - gws
allowed-tools: Bash(gog:*|gws:*) Read
---

# Set Up Incident Post-Mortem

Create a Google Docs post-mortem, schedule a review meeting, and broadcast to Google Chat using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Create incident post-mortem Google Doc
gog docs create "Post-Mortem: [INCIDENT_NAME]" --json

# 2. Schedule post-mortem review meeting on Calendar
gog calendar create primary \
  --summary "Post-Mortem Review: [INCIDENT_NAME]" \
  --from "2026-03-27T15:00:00Z" \
  --to "2026-03-27T16:00:00Z" \
  --attendees "team@company.com" \
  --with-meet \
  --json

# 3. Broadcast notification to Google Chat space
gog chat spaces send \
  --space <SPACE_ID> \
  --message "Incident Post-Mortem doc created and review meeting scheduled." \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Create document
gws docs +write \
  --title "Post-Mortem: [INCIDENT_NAME]" \
  --body "## Summary\n\n## Timeline\n\n## Root Cause\n\n## Action Items"

# 2. Schedule review meeting
gws calendar +insert \
  --summary "Post-Mortem Review: [INCIDENT_NAME]" \
  --attendee team@company.com \
  --start "2026-03-27T15:00:00" \
  --end "2026-03-27T16:00:00"

# 3. Notify Chat space
gws chat +send \
  --space spaces/<SPACE_ID> \
  --text "Incident Post-Mortem doc created and review meeting scheduled." 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/postmortem_scaffold.py](scripts/postmortem_scaffold.py)
