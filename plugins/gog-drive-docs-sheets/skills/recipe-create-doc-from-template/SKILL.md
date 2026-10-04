---
name: recipe-create-doc-from-template
description: "Copy a Google Docs template, fill in content, and share with collaborators using either gog or gws CLI."
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

# Create a Google Doc from a Template

Copy a Google Docs template, fill in content, and share with collaborators using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Duplicate template document
gog drive copy <TEMPLATE_DOC_ID> "Project Brief - Q2 Launch" --json

# 2. Append project content to the copy
gog docs write <NEW_DOC_ID> --file content.md --json

# 3. Share document with team collaborators
gog drive share <NEW_DOC_ID> --email "team@company.com" --role writer --json
```

### Option B: Using `gws` CLI
```bash
# 1. Copy template
gws drive files copy \
  --params '{"fileId": "<TEMPLATE_DOC_ID>"}' \
  --json '{"name": "Project Brief - Q2 Launch"}'

# 2. Write content
gws docs +write \
  --document-id <NEW_DOC_ID> \
  --text "## Project Brief: Q2 Launch\n\n### Goals\nDeliver high-impact features."

# 3. Share with team
gws drive permissions create \
  --params '{"fileId": "<NEW_DOC_ID>"}' \
  --json '{"role": "writer", "type": "user", "emailAddress": "team@company.com"}' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/template_vars_replacer.py](scripts/template_vars_replacer.py)
