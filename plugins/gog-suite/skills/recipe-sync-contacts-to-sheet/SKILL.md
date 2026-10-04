---
name: recipe-sync-contacts-to-sheet
description: "Export Google Contacts directory into a Google Sheets spreadsheet using either gog or gws CLI."
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

# Export Google Contacts to Sheets

Export Google Contacts directory into a Google Sheets spreadsheet using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Retrieve contacts list
gog contacts list --json

# 2. Append contact records to spreadsheet
gog sheets append <SPREADSHEET_ID> "Contacts!A1" \
  "Jane Doe" "jane@company.com" "+1-555-0100" \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Fetch directory contacts
gws people people listDirectoryPeople \
  --params '{"readMask": "names,emailAddresses,phoneNumbers", "sources": ["DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE"], "pageSize": 100}' \
  --format json

# 2. Append row to spreadsheet
gws sheets +append \
  --spreadsheet <SPREADSHEET_ID> \
  --range "Contacts" \
  --values '["Jane Doe", "jane@company.com", "+1-555-0100"]' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/contacts_to_rows.py](scripts/contacts_to_rows.py)
