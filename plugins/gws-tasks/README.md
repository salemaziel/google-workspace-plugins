# Google Workspace — Tasks (`gws-tasks`)

Google Workspace Tasks operations: task list management, overdue audits, and automated email-to-task conversions via `gws` CLI.

## Installation

### Claude Code
```bash
claude plugin install gws-tasks --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gws-tasks@google-workspace-plugins
```

## Architecture & Components (v1.1.0)
Follows the Agent Skills progressive disclosure standard:

- **Skills & Progressive Disclosure**:
  - `gws-tasks` (core Google Tasks operations)
    - References: `references/task-hierarchy.md`, `references/troubleshooting.md`
    - Scripts: `scripts/tasks_triage.py` (executable overdue task parser & status formatter)
    - Templates: `templates/task-batch.json`, `templates/overdue-alert.md`
  - Cross-Service Workflows: `gws-workflow-email-to-task`
  - Recipes: `recipe-create-task-list`, `recipe-review-overdue-tasks`
- **Commands**:
  - `/list-tasks` — List tasks with completion status, due date, and tasklist filters.
  - `/add-task` — Insert a new task with due date, notes, and priority classification.
  - `/complete-task` — Mark pending tasks as completed.
  - `/create-tasklist` — Provision a new task list for projects or teams.
  - `/review-overdue` — Audit overdue tasks across lists and recommend remediation.
  - `/email-to-task` — Convert an incoming Gmail message into a Google Task.
- **Agents**:
  - `task-administrator` — Autonomous task organizer, P0–P3 priority administrator, and overdue auditor.

## License
MIT
