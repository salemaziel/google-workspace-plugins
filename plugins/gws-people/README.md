# Google Workspace — Contacts & People (`gws-people`)

Google Workspace People & Contacts operations: directory search, profile lookups, and contact directory synchronization to spreadsheets via `gws` CLI.

## Installation

### Claude Code
```bash
claude plugin install gws-people --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gws-people@google-workspace-plugins
```

## Architecture & Components (v1.1.0)
Follows the Agent Skills progressive disclosure standard:

- **Skills & Progressive Disclosure**:
  - `gws-people` (core Google People API operations)
    - References: `references/person-fields.md`, `references/troubleshooting.md`
    - Scripts: `scripts/contact_vcard_exporter.py` (executable contacts to CSV / vCard exporter)
    - Templates: `templates/contact-card.json`, `templates/crm-sync-record.json`
  - Recipes: `recipe-sync-contacts-to-sheet`
- **Commands**:
  - `/search-contacts` — Search personal contacts or domain directory with `--directory`.
  - `/get-contact` — Fetch comprehensive person profile details and photos.
  - `/create-contact` — Provision new contacts with name, email, phone, and organization.
  - `/list-groups` — Display contact groups and distribution labels.
  - `/sync-contacts` — Export domain directory or personal contacts into Google Sheets.
- **Agents**:
  - `sales-ops` — Autonomous contact directory administrator, lead enricher, and spreadsheet synchronizer.

## License
MIT
