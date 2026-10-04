---
name: recipe-compare-sheet-tabs
description: "Read data from two tabs in a Google Sheet to compare and identify differences using either gog or gws CLI."
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

# Compare Two Google Sheets Tabs

Read data from two tabs in a Google Sheet to compare and identify differences using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Read first tab data
gog sheets get <SPREADSHEET_ID> "January!A1:D50" --json > jan.json

# 2. Read second tab data
gog sheets get <SPREADSHEET_ID> "February!A1:D50" --json > feb.json

# 3. Compute delta between tabs
python3 scripts/diff_tabs.py jan.json feb.json
```

### Option B: Using `gws` CLI
```bash
# 1. Read first tab
gws sheets +read --spreadsheet <SPREADSHEET_ID> --range "January!A1:D50" > jan.txt

# 2. Read second tab
gws sheets +read --spreadsheet <SPREADSHEET_ID> --range "February!A1:D50" > feb.txt

# 3. Diff tables
diff -u jan.txt feb.txt
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/diff_tabs.py](scripts/diff_tabs.py)
