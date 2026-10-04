---
name: recipe-create-task-list
description: "Set up a new Google Tasks list with initial tasks and due dates using either gog or gws CLI."
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

# Create and Populate a Google Tasks List

Set up a new Google Tasks list with initial tasks and due dates using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Create a dedicated task list
gog tasks lists create "Q2 Product Launch" --json

# 2. Add tasks with due dates to the list
gog tasks add <TASKLIST_ID> \
  --title "Finalize Architecture Spec" \
  --due "2026-03-25T18:00:00Z" \
  --notes "Align on database partitioning" \
  --json

# 3. List active tasks
gog tasks list <TASKLIST_ID> --json
```

### Option B: Using `gws` CLI
```bash
# 1. Create task list via Discovery API
gws tasks tasklists insert --json '{"title": "Q2 Product Launch"}'

# 2. Add task entry
gws tasks tasks insert \
  --params '{"tasklist": "<TASKLIST_ID>"}' \
  --json '{
    "title": "Finalize Architecture Spec",
    "due": "2026-03-25T18:00:00.000Z",
    "notes": "Align on database partitioning"
  }'

# 3. Verify task list
gws tasks tasks list --params '{"tasklist": "<TASKLIST_ID>"}' --format table
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/task_batch_creator.py](scripts/task_batch_creator.py)
