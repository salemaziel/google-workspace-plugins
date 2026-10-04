# Google Suite CLI — Gmail (`gog-gmail`)

Gmail inbox management, message triage, draft preparation, sending with confirmation, and thread followup tracking using the `gog` CLI.

## Installation

### Claude Code
```bash
claude plugin install gog-gmail --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gog-gmail@google-workspace-plugins
```

## Architecture & Components

- **Commands** (`commands/`):
  - `/email-triage` — Analyze unread messages and generate priority breakdown.
  - `/email-draft` — Compose contextual email replies with dual tone variants.
  - `/email-send` — Send email with strict `"YES, SEND"` confirmation.
  - `/followups` — Track waiting email threads and schedule reminders.
- **Agents** (`agents/`):
  - `inbox-manager` — Autonomous inbox triage, SLA monitoring, and draft coordinator.
- **Modular Skills** (`skills/`):
  - `gog-email-triage` — Progressive disclosure with `references/classification-matrix.md`, deterministic `scripts/triage_parser.py`, and `templates/triage-report.md`.
  - `gog-email-draft` — Progressive disclosure with `references/tone-guide.md`, safe temporary draft builder `scripts/prepare_draft.py`, and boilerplate templates.
  - `gog-email-send` — Progressive disclosure with `references/safety-rules.md`, audit logger `scripts/audit_logger.py`, and verification templates.
  - `gog-followups` — Progressive disclosure with `references/nudge-strategy.md`, local store manager `scripts/followup_manager.py`, and reminder templates.
  - **Agnostic Gmail Recipes** (supports `gog` and `gws`):
    - `recipe-create-gmail-filter` — Automated email routing, labeling, and star/archive rules.
    - `recipe-create-vacation-responder` — OOO auto-replies with date windows and domain scoping.
    - `recipe-forward-labeled-emails` — Triage queue review and automated dispatch to managers.
    - `recipe-label-and-archive-emails` — Bulk cleanup rules for automated notifications and newsletters.
    - `recipe-save-email-attachments` — Ingest inbound message attachments into Google Drive.
    - `recipe-save-email-to-doc` — Convert critical email threads into structured Google Docs records.

## License
MIT
