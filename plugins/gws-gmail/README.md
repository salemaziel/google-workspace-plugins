# Google Workspace — Gmail (`gws-gmail`)

Google Workspace Gmail automation: search, threads, draft composition, labels, NDJSON mailbox change streams, and automated triage via `gws` CLI.

## Installation

### Claude Code
```bash
claude plugin install gws-gmail --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gws-gmail@google-workspace-plugins
```

## Included Components
- **Commands**:
  - `/search` — Search Gmail messages by query, sender, or label.
  - `/triage` — Inbox triage and priority classification.
  - `/send` — Safe email sending with dry-run payload verification.
  - `/reply` — Contextual threaded email replies.
  - `/forward` — Forward email conversations preserving attribution.
  - `/vacation` — Configure out-of-office vacation autoreponder.
  - `/filter` — Automated Gmail filter and labeling rules.
- **Agents**:
  - `customer-support` — Autonomous customer support and client communication agent.
- **Skills & Recipes**:
  - `gws-gmail` (core API operations)
  - `gws-gmail-send`, `gws-gmail-read`, `gws-gmail-reply`, `gws-gmail-reply-all`, `gws-gmail-forward`, `gws-gmail-triage`, `gws-gmail-watch`
  - `recipe-create-gmail-filter`, `recipe-create-vacation-responder`, `recipe-forward-labeled-emails`, `recipe-label-and-archive-emails`, `recipe-save-email-attachments`, `recipe-save-email-to-doc`

## License
MIT
