---
name: gog-tasks
description: "Create, manage, and prioritize tasks and todo items with gog CLI. Supports P0-P3 taxonomy, email-to-task conversion, daily reviews, and completion tracking."
---

# gog-tasks — Task Management with gog CLI

Create, organize, and track tasks with smart prioritization (P0–P3), category bucketing, and automated daily review summaries.

## Quick Workflow
1. **Discover List**: Resolve active task list ID: `TASKLIST_ID=$(gog tasks lists --json | jq -r '.tasklists[0].id')`.
2. **Review / Triage**: Query open tasks and format priorities using `task_filter.py`.
3. **Execute**: Add new tasks with confirmation, mark completed items as done, or purge outdated tasks.

## Core Commands

```bash
# Get primary task list ID
TASKLIST_ID=$(gog tasks lists --json | jq -r '.tasklists[0].id')

# Generate structured Daily Task Review
gog tasks list "$TASKLIST_ID" --json | ./scripts/task_filter.py --review

# Add a new task (P0-P3 priority and category encoded in title/notes)
gog tasks add "$TASKLIST_ID" \
  --title "[P1][Work] Finalize Q4 Budget" \
  --notes "Priority: P1\nCategory: Work\nDue: 2026-10-15" \
  --due 2026-10-15 \
  --json

# Mark task as completed
gog tasks done "$TASKLIST_ID" <taskId> --json

# Delete a task (Requires explicit user confirmation)
gog tasks delete "$TASKLIST_ID" <taskId> --json
```

## Safety Rules & Human Confirmation
- **Confirmation Required**: Creating or deleting tasks requires explicit user approval.
- **No Auto-Completion**: Never mark tasks done without clear user instruction.
- **Preserve Provenance**: When creating tasks from emails, store the source email ID in the task notes.

## Progressive Disclosure & References
- **Priority & Categories**: Read [references/priority-taxonomy.md](references/priority-taxonomy.md) for P0–P3 definitions, category tags, and priority inflation rules.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for list resolution errors and duplicate handling.
- **Safe Testing**: Follow [references/safe-test-plan.md](references/safe-test-plan.md) to test task workflows safely.
- **Filter & Review Script**: Use [scripts/task_filter.py](scripts/task_filter.py) to parse, filter, and render daily task reviews.
- **Templates**: See [templates/daily-review.md](templates/daily-review.md) and [templates/task-proposal.md](templates/task-proposal.md) for standard schemas.
