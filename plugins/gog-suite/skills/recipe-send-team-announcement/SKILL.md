---
name: recipe-send-team-announcement
description: "Send a team announcement simultaneously via Gmail and a Google Chat space using either gog or gws CLI."
metadata:
  version: 1.2.0
  openclaw:
    category: "recipe"
    domain: "communication"
    requires:
      any_bin_of:
        - gog
        - gws
allowed-tools: Bash(gog:*|gws:*) Read
---

# Announce via Gmail and Google Chat

Send a team announcement simultaneously via Gmail and a Google Chat space using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Send broadcast email to team distribution list
gog gmail send \
  --to "team@company.com" \
  --subject "Important: Q2 Roadmap Alignment" \
  --body "Team, please review the finalized Q2 engineering priorities." \
  --json

# 2. Post summary alert in Google Chat space
gog chat spaces send \
  --space <SPACE_ID> \
  --message "📢 Important: Q2 Roadmap Alignment email dispatched. Please review." \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Send announcement email
gws gmail +send \
  --to team@company.com \
  --subject "Important: Q2 Roadmap Alignment" \
  --body "Team, please review the finalized Q2 engineering priorities."

# 2. Post alert in Chat space
gws chat +send \
  --space spaces/<SPACE_ID> \
  --text "📢 Important: Q2 Roadmap Alignment email dispatched. Please review." 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/format_announcement.py](scripts/format_announcement.py)
