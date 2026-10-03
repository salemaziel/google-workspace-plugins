# Google Workspace — Drive, Docs & Sheets (`gws-drive-docs-sheets`)

Google Workspace Drive, Docs, Sheets, and Slides operations: cloud file management, document creation, spreadsheet ETL, and slide deck generation via `gws` CLI.

## Installation

### Claude Code
```bash
claude plugin install gws-drive-docs-sheets --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gws-drive-docs-sheets@google-workspace-plugins
```

## Included Components

- **Commands**:
  - `/search` — Search Google Drive files and folders by query or MIME filter.
  - `/upload` — Upload local files to Google Drive with folder target support.
  - `/doc-create` — Provision new Google Docs with initial body text.
  - `/doc-append` — Append structured markdown/plain text to existing documents.
  - `/sheet-export` — Export tabular data to CSV or JSON.
  - `/sheet-append` — Append rows of data to Google Sheets.
  - `/sheet-read` — Read and preview cell ranges.
  - `/slide-create` — Create presentation decks in Google Slides.
  - `/shared-drive` — Provision shared drives and manage member permissions.
- **Agents**:
  - `content-creator` — Autonomous document author, presenter, and asset publisher.
  - `researcher` — Reference curator, document synthesizer, and Drive quota optimizer.
- **Skills & Recipes**:
  - Core API Skills: `gws-drive`, `gws-drive-upload`, `gws-docs`, `gws-docs-write`, `gws-sheets`, `gws-sheets-read`, `gws-sheets-append`, `gws-slides`, `google-workspace-ops`
  - Productivity Recipes:
    - `recipe-create-doc-from-template`, `recipe-draft-email-from-doc`, `recipe-share-doc-and-notify`, `recipe-save-email-to-doc`
    - `recipe-create-expense-tracker`, `recipe-sheet-export` / `recipe-backup-sheet-as-csv`, `recipe-compare-sheet-tabs`, `recipe-copy-sheet-for-new-month`, `recipe-generate-report-from-sheet`, `recipe-log-deal-update`
    - `recipe-create-presentation`
    - `recipe-create-shared-drive`, `recipe-share-folder-with-team`, `recipe-email-drive-link`, `recipe-organize-drive-folder`, `recipe-find-large-files`, `recipe-bulk-download-folder`, `recipe-watch-drive-changes`

## License
MIT
