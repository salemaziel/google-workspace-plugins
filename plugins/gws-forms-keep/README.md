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

## Architecture & Components (v1.1.0)
Follows the Agent Skills progressive disclosure standard:

- **Skills & Progressive Disclosure**:
  - `gws-forms` (core Google Forms API operations)
    - References: `references/form-items-schema.md`, `references/troubleshooting.md`
    - Scripts: `scripts/form_response_analyzer.py` (executable response breakdown & percentage calculator)
    - Templates: `templates/feedback-form-spec.json`, `templates/keep-checklist.json`
  - Notes & Storage: `gws-keep` (Google Keep notes and media)
  - Recipes: `recipe-create-feedback-form`, `recipe-collect-form-responses`
- **Commands**:
  - `/create-form` — Provision a new Google Form and retrieve public responder URL.
  - `/get-form` — Inspect form questions, schema, and metadata.
  - `/collect-responses` — Retrieve and summarize submitted form responses.
  - `/keep-note` — Author new notes and checklists in Google Keep.
  - `/keep-list` — List active Keep notes and task lists.
- **Agents**:
  - `hr-coordinator` — Autonomous HR operations specialist, survey creator, feedback analyst, and onboarding coordinator.

## License
MIT
