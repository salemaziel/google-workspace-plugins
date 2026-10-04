---
name: recipe-forward-labeled-emails
description: "Find Gmail messages with a specific label and forward them to another address using either gog or gws CLI."
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

# Forward Labeled Gmail Messages

Find Gmail messages with a specific label and forward them to another address using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Search for messages with target label
gog gmail search "label:needs-review" --json

# 2. Forward message to reviewer
gog gmail forward <MESSAGE_ID> \
  --to "manager@company.com" \
  --json

# 3. Mark processed or remove review label
gog gmail labels remove <MESSAGE_ID> "needs-review" --json
```

### Option B: Using `gws` CLI
```bash
# 1. List labeled messages
gws gmail users messages list --params '{"userId": "me", "q": "label:needs-review"}' --format table

# 2. Fetch original email contents
gws gmail users messages get --params '{"userId": "me", "id": "<MESSAGE_ID>"}'

# 3. Forward message
gws gmail +send \
  --to manager@company.com \
  --subject "FW: [Original Subject]" \
  --body "Forwarding for your review: [Original Body]"
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/extract_forward_body.py](scripts/extract_forward_body.py)
