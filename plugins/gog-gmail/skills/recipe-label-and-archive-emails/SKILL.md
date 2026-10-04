---
name: recipe-label-and-archive-emails
description: "Apply Gmail labels to matching messages and archive them to keep your inbox clean using either gog or gws CLI."
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

# Label and Archive Gmail Threads

Apply Gmail labels to matching messages and archive them to keep your inbox clean using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Query matching messages
gog gmail search "from:notifications@service.com is:unread" --json

# 2. Apply label and archive (remove from INBOX)
gog gmail labels add <MESSAGE_ID> "Notifications" --json
gog gmail archive <MESSAGE_ID> --json

# 3. Mark message as read
gog gmail mark-read <MESSAGE_ID> --json
```

### Option B: Using `gws` CLI
```bash
# 1. Search for candidate messages
gws gmail users messages list --params '{"userId": "me", "q": "from:notifications@service.com is:unread"}' --format table

# 2. Modify message labels: add custom label and remove INBOX/UNREAD
gws gmail users messages modify \
  --params '{"userId": "me", "id": "<MESSAGE_ID>"}' \
  --json '{"addLabelIds": ["<LABEL_ID>"], "removeLabelIds": ["INBOX", "UNREAD"]}' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/batch_ids_extractor.py](scripts/batch_ids_extractor.py)
