---
name: recipe-email-drive-link
description: "Share a Google Drive file and email the link with a message to recipients using either gog or gws CLI."
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

# Email a Google Drive File Link

Share a Google Drive file and email the link with a message to recipients using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Grant read access to the recipient
gog drive share <FILE_ID> --email "client@example.com" --role reader --json

# 2. Email link to recipient
gog gmail send \
  --to "client@example.com" \
  --subject "Quarterly Performance Report" \
  --body "Hi, please review the finalized report: https://drive.google.com/open?id=<FILE_ID>" \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Share Drive file
gws drive permissions create \
  --params '{"fileId": "<FILE_ID>"}' \
  --json '{"role": "reader", "type": "user", "emailAddress": "client@example.com"}'

# 2. Email link
gws gmail +send \
  --to client@example.com \
  --subject "Quarterly Performance Report" \
  --body "Hi, please review the finalized report: https://drive.google.com/open?id=<FILE_ID>"
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/drive_url_builder.py](scripts/drive_url_builder.py)
