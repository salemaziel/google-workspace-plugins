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

## Included Components
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
- **Skills**:
  - `gog-drive` — File discovery, MIME queries, and sharing permissions.
  - `gog-docs` — Document creation and markdown export.
  - `gog-sheets` — A1-notation ranges and tabular data processing.
  - `gog-slides` — Slide deck provisioning.

## License
MIT
