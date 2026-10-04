---
name: recipe-save-email-to-doc
description: "Save a Gmail message body into a Google Doc for archival or reference using either gog or gws CLI."
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

# Save a Gmail Message to Google Docs

Save a Gmail message body into a Google Doc for archival or reference using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Fetch message content as JSON
gog gmail get <MESSAGE_ID> --json

# 2. Create archival Google Doc
gog docs create "Saved Email - Important Update" --json

# 3. Write email body into newly created document
gog docs write <DOC_ID> --file email_body.txt --json
```

### Option B: Using `gws` CLI
```bash
# 1. Fetch message details
gws gmail users messages get --params '{"userId": "me", "id": "<MESSAGE_ID>"}'

# 2. Create Google Doc
gws docs documents create --json '{"title": "Saved Email - Important Update"}'

# 3. Write email body into document
gws docs +write \
  --document-id <DOC_ID> \
  --text "From: client@example.com\nSubject: Important Update\n\n[Email Body]"
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/format_email_for_doc.py](scripts/format_email_for_doc.py)
