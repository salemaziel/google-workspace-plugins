---
name: recipe-watch-drive-changes
description: "Track Drive file changes or subscribe to change notifications using either gog or gws CLI."
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

# Watch for Google Drive Changes

Track Drive file changes or subscribe to change notifications using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Fetch start page token for change tracking
gog drive changes start-page-token --json

# 2. Poll changes since token
gog drive changes list --page-token <PAGE_TOKEN> --json
```

### Option B: Using `gws` CLI
```bash
# 1. Create Workspace Events subscription
gws events subscriptions create \
  --json '{
    "targetResource": "//drive.googleapis.com/drives/<DRIVE_ID>",
    "eventTypes": ["google.workspace.drive.file.v1.updated"],
    "notificationEndpoint": {"pubsubTopic": "projects/PROJECT/topics/TOPIC"},
    "payloadOptions": {"includeResource": true}
  }'

# 2. List active event subscriptions
gws events subscriptions list
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/parse_change_feed.py](scripts/parse_change_feed.py)
