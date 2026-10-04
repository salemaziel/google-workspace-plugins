---
name: recipe-review-overdue-tasks
description: "Find Google Tasks that are past due and need attention using either gog or gws CLI."
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

# Review Overdue Google Tasks

Find Google Tasks that are past due and need attention using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. List active task lists
gog tasks lists list --json

# 2. Retrieve pending tasks from list
gog tasks list <TASKLIST_ID> --json | python3 scripts/filter_overdue.py

# 3. Mark completed task
gog tasks done <TASKLIST_ID> <TASK_ID> --json
```

### Option B: Using `gws` CLI
```bash
# 1. List task lists
gws tasks tasklists list --format table

# 2. List uncompleted tasks
gws tasks tasks list \
  --params '{"tasklist": "<TASKLIST_ID>", "showCompleted": false}' \
  --format json | python3 scripts/filter_overdue.py

# 3. Mark completed task
gws tasks tasks patch \
  --params '{"tasklist": "<TASKLIST_ID>", "task": "<TASK_ID>"}' \
  --json '{"status": "completed"}' 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/filter_overdue.py](scripts/filter_overdue.py)
