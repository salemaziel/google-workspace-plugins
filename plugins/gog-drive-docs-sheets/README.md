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

## Architecture & Components (v1.2.0)
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
  - **Agnostic Drive, Docs, Sheets & Slides Recipes** (supports `gog` and `gws`):
    - `recipe-backup-sheet-as-csv` — Export spreadsheets directly to local CSV files.
    - `recipe-bulk-download-folder` — Batch download entire Drive folders with format conversion.
    - `recipe-compare-sheet-tabs` — Automated multi-tab delta computation and schema checks.
    - `recipe-copy-sheet-for-new-month` — Clone monthly templates with dynamic date heading.
    - `recipe-create-doc-from-template` — Duplicate standardized project briefs and replace variables.
    - `recipe-create-expense-tracker` — Scaffold structured finance spreadsheets with typed headers.
    - `recipe-create-presentation` — Provision widescreen presentation decks and configure ACLs.
    - `recipe-create-shared-drive` — Provision Team Shared Drives and manage access roles.
    - `recipe-draft-email-from-doc` — Convert Google Docs text into Gmail messages.
    - `recipe-email-drive-link` — Share Drive assets and email links to recipients.
    - `recipe-find-large-files` — Storage quota audit across large files and folders.
    - `recipe-generate-report-from-sheet` — Synthesize spreadsheet metrics into formatted Google Docs.
    - `recipe-log-deal-update` — Append sales pipeline progression events to CRM sheets.
    - `recipe-organize-drive-folder` — Provision directory hierarchies and relocate project files.
    - `recipe-share-doc-and-notify` — Grant writer access to docs and notify reviewers.
    - `recipe-share-folder-with-team` — Bulk grant team editor and stakeholder reader access.
    - `recipe-watch-drive-changes` — Track file revisions and change notification streams.
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
