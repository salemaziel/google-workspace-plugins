---
name: recipe-save-email-attachments
description: "Find Gmail messages with attachments and save them to a Google Drive folder using either gog or gws CLI."
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

# Save Gmail Attachments to Google Drive

Find Gmail messages with attachments and save them to a Google Drive folder using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Search emails containing attachments
gog gmail search "has:attachment from:client@example.com" --json

# 2. Download specific attachment
gog gmail attachment <MESSAGE_ID> <ATTACHMENT_ID> --out "./attachment.pdf"

# 3. Upload downloaded file to Google Drive folder
gog drive upload "./attachment.pdf" --parent <FOLDER_ID> --json
```

### Option B: Using `gws` CLI
```bash
# 1. Query messages with attachments
gws gmail users messages list \
  --params '{"userId": "me", "q": "has:attachment from:client@example.com"}' \
  --format table

# 2. Fetch message structure to identify attachmentId
gws gmail users messages get --params '{"userId": "me", "id": "<MESSAGE_ID>"}'

# 3. Download raw attachment bytes
gws gmail users messages attachments get \
  --params '{"userId": "me", "messageId": "<MESSAGE_ID>", "id": "<ATTACHMENT_ID>"}' -o attachment.pdf

# 4. Upload to Drive folder
gws drive +upload --file ./attachment.pdf --parent <FOLDER_ID>
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/find_attachments.py](scripts/find_attachments.py)
