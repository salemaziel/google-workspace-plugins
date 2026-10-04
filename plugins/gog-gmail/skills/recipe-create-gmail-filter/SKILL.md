---
name: recipe-create-gmail-filter
description: "Create a Gmail filter to automatically label, star, or categorize incoming messages using either gog or gws CLI."
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

# Create a Gmail Filter

Create a Gmail filter to automatically label, star, or categorize incoming messages using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Inspect existing filters
gog gmail settings filters list --json

# 2. Create automated filter matching criteria
gog gmail settings filters create \
  --from "receipts@example.com" \
  --add-label "Receipts" \
  --archive \
  --json

# 3. Verify created filter
gog gmail settings filters list --json
```

### Option B: Using `gws` CLI
```bash
# 1. List existing labels to obtain LABEL_ID
gws gmail users labels list --params '{"userId": "me"}' --format table

# 2. Create the filter rule
gws gmail users settings filters create \
  --params '{"userId": "me"}' \
  --json '{
    "criteria": {"from": "receipts@example.com"},
    "action": {"addLabelIds": ["<LABEL_ID>"], "removeLabelIds": ["INBOX"]}
  }'

# 3. Verify active filters
gws gmail users settings filters list --params '{"userId": "me"}' --format table
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/filter_criteria_builder.py](scripts/filter_criteria_builder.py)
