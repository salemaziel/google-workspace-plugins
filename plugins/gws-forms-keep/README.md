# Google Workspace — Forms & Keep (`gws-forms-keep`)

Google Workspace Forms and Keep notes operations: survey creation, response collection, and team onboarding workflows via `gws` CLI.

## Installation

### Claude Code
```bash
claude plugin install gws-forms-keep --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gws-forms-keep@google-workspace-plugins
```

## Included Components

- **Commands**:
  - `/create-form` — Provision a new Google Form and retrieve public responder URL.
  - `/get-form` — Inspect form questions, schema, and metadata.
  - `/collect-responses` — Retrieve and summarize submitted form responses.
  - `/keep-note` — Author new notes and checklists in Google Keep.
  - `/keep-list` — List active Keep notes and task lists.
- **Agents**:
  - `hr-coordinator` — Autonomous HR operations specialist, survey creator, feedback analyst, and onboarding coordinator.
- **Skills & Recipes**:
  - `gws-forms` (core Google Forms API operations)
  - `gws-keep` (Google Keep notes and media)
  - `recipe-create-feedback-form` (form creation and Gmail distribution pipeline)
  - `recipe-collect-form-responses` (response querying and aggregation)

## License
MIT
