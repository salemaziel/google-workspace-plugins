# Google Suite CLI — Tasks (`gog-tasks`)

Google Tasks management, task list synchronization, due date tracking, and task completion with the gog CLI.

## Installation

### Claude Code
```bash
claude plugin install gog-tasks --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gog-tasks@google-workspace-plugins
```

## Architecture & Components (v1.1.0)
Follows the Agent Skills progressive disclosure standard:

- **Skills**:
  - `gog-tasks` — Complete Eisenhower priority taxonomy (P0–P3), daily review cadences, and email conversion workflows.
    - References: `references/priority-taxonomy.md`, `references/troubleshooting.md`, `references/safe-test-plan.md`
    - Scripts: `scripts/task_filter.py` (executable priority bucketing & daily review engine)
    - Templates: `templates/daily-review.md`, `templates/task-proposal.md`
- **Commands**:
  - `/tasks-list` — List and filter active tasks by due date or list name.
  - `/tasks-add` — Add a prioritized task with due dates and notes.
  - `/tasks-done` — Mark tasks complete with title verification.
  - `/tasks-review` — Daily morning/evening task standup and prioritization.
  - `/tasks-delete` — Delete cancelled tasks with preview confirmation.
- **Agents**:
  - `task-organizer` — Autonomous productivity assistant for P0–P3 prioritization and backlog management.

## License
MIT
