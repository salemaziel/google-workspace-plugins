---
name: recipe-create-meet-space
description: "Create a Google Meet meeting space and share the join link using either gog or gws CLI."
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

# Create a Google Meet Space

Create a Google Meet meeting space and share the join link using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Create a Google Meet conference space
gog meet spaces create --json

# 2. Email the meeting link to participants
gog gmail send \
  --to "team@company.com" \
  --subject "Join Google Meet Space" \
  --body "Join the conference room here: <MEETING_URI>" \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Create meeting space via Discovery API
gws meet spaces create --json '{"config": {"accessType": "OPEN"}}'

# 2. Email join link
gws gmail +send \
  --to team@company.com \
  --subject "Join Google Meet Space" \
  --body "Join the conference room here: <MEETING_URI>"
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/extract_meet_uri.py](scripts/extract_meet_uri.py)
