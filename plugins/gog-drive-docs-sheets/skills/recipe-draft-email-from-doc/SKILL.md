---
name: recipe-draft-email-from-doc
description: "Read content from a Google Doc and dispatch it as an email using either gog or gws CLI."
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

# Draft Email from Google Docs Content

Read content from a Google Doc and dispatch it as an email using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Export Google Doc text
gog docs cat <DOC_ID> > draft.txt

# 2. Send email with document contents
gog gmail send \
  --to "team@company.com" \
  --subject "Weekly Project Update" \
  --body-file draft.txt \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Export document content
gws drive files export \
  --params '{"fileId": "<DOC_ID>", "mimeType": "text/plain"}' -o draft.txt

# 2. Dispatch email
gws gmail +send \
  --to team@company.com \
  --subject "Weekly Project Update" \
  --body "$(cat draft.txt)"
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/clean_doc_text.py](scripts/clean_doc_text.py)
