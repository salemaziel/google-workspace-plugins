---
name: gws-tasks
description: "Google Tasks management: task lists, hierarchies, subtask trees, and overdue task triage via gws CLI."
metadata:
  version: 0.22.5
  category: "productivity"
  requires:
    bins:
      - gws
---

# gws-tasks — Google Tasks CLI Integration

Create, organize, prioritize, and triage Google Tasks and subtasks through the `gws` CLI.

## Quick Workflow
1. **List / Triage**: Inspect active tasks using `@default` list and pipe into `tasks_triage.py`.
2. **Add / Move**: Insert new tasks or position them into subtask hierarchies via `parent` and `previous`.
3. **Resolve**: Mark tasks completed or clear soft-archived items.

## Core Commands

```bash
# Triage open and overdue tasks in primary tasklist
gws tasks tasks list --params '{"tasklist": "@default"}' | ./scripts/tasks_triage.py

# Filter only overdue tasks
gws tasks tasks list --params '{"tasklist": "@default"}' | ./scripts/tasks_triage.py --overdue-only

# Insert a new task with due date (Midnight UTC RFC 3339)
gws tasks tasks insert \
  --params '{"tasklist": "@default"}' \
  --json '{
    "title": "Review security audit logs",
    "notes": "Verify external sharing permissions on Drive",
    "due": "2026-10-15T00:00:00.000Z"
  }'

# Complete a task
gws tasks tasks patch \
  --params '{"tasklist": "@default", "task": "<taskId>"}' \
  --json '{"status": "completed"}'

# Clear completed tasks from view
gws tasks tasks clear --params '{"tasklist": "@default"}'
```

## Progressive Disclosure & References
- **Hierarchy & Subtasks**: Read [references/task-hierarchy.md](references/task-hierarchy.md) for subtask positioning rules and quota limits.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for RFC 3339 due dates and assigned task constraints.
- **Triage Script**: Use [scripts/tasks_triage.py](scripts/tasks_triage.py) to flag overdue items and format task status tables.
- **Templates**: See [templates/task-batch.json](templates/task-batch.json) and [templates/overdue-alert.md](templates/overdue-alert.md).
