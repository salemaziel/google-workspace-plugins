---
name: recipe-create-vacation-responder
description: "Enable a Gmail out-of-office auto-reply with a custom message and date range using either gog or gws CLI."
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

# Set Up a Gmail Vacation Responder

Enable a Gmail out-of-office auto-reply with a custom message and date range using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Enable vacation responder with dates and subject
gog gmail settings vacation update \
  --enable \
  --subject "Out of Office: March 2026" \
  --body "I am currently out of office. For urgent queries, contact support@company.com." \
  --start "2026-03-23T00:00:00Z" \
  --end "2026-03-30T23:59:59Z" \
  --json

# 2. Verify active vacation responder configuration
gog gmail settings vacation get --json
```

### Option B: Using `gws` CLI
```bash
# 1. Update vacation settings via Discovery API
gws gmail users settings updateVacation \
  --params '{"userId": "me"}' \
  --json '{
    "enableAutoReply": true,
    "responseSubject": "Out of Office: March 2026",
    "responseBodyPlainText": "I am currently out of office. For urgent queries, contact support@company.com.",
    "restrictToContacts": false,
    "restrictToDomain": false
  }'

# 2. Verify configuration
gws gmail users settings getVacation --params '{"userId": "me"}' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/vacation_duration_check.py](scripts/vacation_duration_check.py)
