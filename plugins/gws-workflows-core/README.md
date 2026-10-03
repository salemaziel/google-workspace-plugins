# Google Workspace — Workflows & Core CLI (`gws-workflows-core`)

Google Workspace orchestration suite: pre-flight diagnostics, setup guides, recipe runner, cross-service workflows (standup report, meeting prep, weekly digest), and executive management via `gws` CLI.

## Installation

### Claude Code
```bash
claude plugin install gws-workflows-core --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gws-workflows-core@google-workspace-plugins
```

## Architecture & Components (v1.1.0)
Follows the Agent Skills progressive disclosure standard:

- **Skills & Progressive Disclosure**:
  - `gws-workflow` (cross-service pipelines)
    - References: `skills/gws-workflow/references/pipeline-patterns.md`, `skills/gws-workflow/references/troubleshooting.md`
    - Suite References: `references/gws-command-reference.md`, `references/troubleshooting.md`, `references/recipes-cookbook.md`
    - Suite Scripts: `scripts/gws_doctor.py`, `scripts/workspace_audit.py`, `scripts/gws_recipe_runner.py`, `scripts/output_analyzer.py`, `scripts/auth_setup_guide.py`
    - Templates: `templates/standup-report.md`, `templates/meeting-prep.md`, `templates/weekly-digest.md`
  - Specialized Workflow Skills: `gws-shared`, `gws-workflow-standup-report`, `gws-workflow-meeting-prep`, `gws-workflow-weekly-digest`
  - Workspace Core Skills: `google-workspace-cli`, `google-workspace-cli-concise`, `source-command-google-workspace`
- **Commands**:
  - `/doctor` — Pre-flight environment diagnostics, binary verification, and token checks.
  - `/google-workspace` — Master CLI orchestration (setup, security audit, recipe runner, auth wizard).
  - `/standup` — Daily morning briefing (calendar events + open tasks).
  - `/meeting-prep` — Pre-meeting dossier (attendees, agenda, linked docs).
  - `/weekly-digest` — Executive horizon briefing (meetings, priorities, unread volume).
  - `/recipe` — Browse, filter, and execute 43 automation templates with dry-run support.
  - `/audit` — Security, sharing policy, and configuration audit.
  - `/auth-guide` — Interactive OAuth2 and Service Account setup wizard.
- **Agents**:
  - `executive-assistant` — Autonomous executive scheduler, morning briefer, and dossier preparer.
  - `project-manager` — Cross-functional milestone tracker, backlog sync agent, and recipe executor.

## License
MIT
