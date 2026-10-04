---
name: recipe-share-doc-and-notify
description: "Share a Google Docs document with edit access and email collaborators the link using either gog or gws CLI."
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

# Share a Google Doc and Notify Collaborators

Share a Google Docs document with edit access and email collaborators the link using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Share Google Doc with edit privileges
gog drive share <DOC_ID> --email "reviewer@company.com" --role writer --json

# 2. Email collaborator the document link
gog gmail send \
  --to "reviewer@company.com" \
  --subject "Please review: Project Brief" \
  --body "I have shared the project brief with you: https://docs.google.com/document/d/<DOC_ID>/edit" \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Grant editor permission
gws drive permissions create \
  --params '{"fileId": "<DOC_ID>"}' \
  --json '{"role": "writer", "type": "user", "emailAddress": "reviewer@company.com"}'

# 2. Dispatch notification email
gws gmail +send \
  --to reviewer@company.com \
  --subject "Please review: Project Brief" \
  --body "I have shared the project brief with you: https://docs.google.com/document/d/<DOC_ID>/edit"
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/notify_body_gen.py](scripts/notify_body_gen.py)
