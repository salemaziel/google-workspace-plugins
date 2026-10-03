# Google Suite CLI — Drive & Docs (`gog-drive-docs-sheets`)

Google Drive file management, markdown Docs export, Sheets tabular read/write, and Slides creation using the gog CLI.

## Installation

### Claude Code
```bash
claude plugin install gog-drive-docs-sheets --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gog-drive-docs-sheets@google-workspace-plugins
```

## Architecture & Components (v1.1.0)
Each skill follows the Agent Skills progressive disclosure standard:

- **Skills**:
  - `gog-drive` — File discovery, MIME queries, and sharing permissions.
    - References: `references/query-syntax.md`, `references/troubleshooting.md`
    - Scripts: `scripts/drive_search_filter.py`
    - Templates: `templates/share-notification.md`
  - `gog-docs` — Document creation and markdown export.
    - References: `references/export-formats.md`, `references/troubleshooting.md`
    - Templates: `templates/meeting-notes.md`, `templates/project-spec.md`
  - `gog-sheets` — A1-notation ranges and tabular data processing.
    - References: `references/a1-notation.md`, `references/troubleshooting.md`
    - Scripts: `scripts/csv_to_sheets_json.py`
    - Templates: `templates/table-schema.json`, `templates/metric-log.json`
  - `gog-slides` — Slide deck provisioning.
    - References: `references/presentation-guidelines.md`, `references/troubleshooting.md`
    - Templates: `templates/pitch-deck-outline.md`, `templates/executive-briefing.md`
- **Commands**:
  - `/drive-search` — Search files and folders with keyword and MIME filters.
  - `/drive-upload` — Upload local files to Google Drive.
  - `/drive-share` — Share Drive assets with teammates by email and role.
  - `/docs-export` — Export Google Docs as Markdown, plain text, or PDF.
  - `/docs-create` — Provision a new Google Doc and return edit link.
  - `/sheets-read` — Query Google Sheets tabular ranges into Markdown or JSON.
  - `/sheets-write` — Write or append data into spreadsheets with confirmation preview.
  - `/slides-create` — Generate a new Google Slides presentation deck.
- **Agents**:
  - `document-analyst` — Autonomous analyst for cross-document synthesis and data workflows.

## License
MIT
