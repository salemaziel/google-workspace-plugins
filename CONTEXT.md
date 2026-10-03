# Google Workspace & Google Suite Plugin Marketplace — CONTEXT

Unified Claude Code and OpenAI Codex CLI plugin marketplace packaging `gog` and `gws` Google CLI capabilities into modular, service-specific bundles.

## Contract
- **Role**: Plugin Marketplace & Component Repository
- **Clients**: Claude Code (`claude plugin marketplace add`), Codex CLI (`codex marketplace add`)
- **Components**: 14 Service-focused Plugins (5 `gog` CLI, 9 `gws` CLI)
- **Manifests**:
  - Claude Code: `.claude-plugin/marketplace.json`
  - OpenAI Codex: `.agents/plugins/marketplace.json`
  - Per-plugin: `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`

## Plugins Overview
1. `gog-gmail`: Gmail triage, drafts, sending, and followups via `gog`.
2. `gog-calendar`: Agenda, slot finding, and event creation via `gog`.
3. `gog-drive-docs-sheets`: Drive, Docs, Sheets, and Slides via `gog`.
4. `gog-tasks`: Task lists and todo management via `gog`.
5. `gog-suite`: Full multi-account suite orchestrator for `gog`.
6. `gws-gmail`: Gmail API, search, threads, triage, and customer support via `gws`.
7. `gws-calendar`: Calendar events, Meet conferencing, and event coordination via `gws`.
8. `gws-drive-docs-sheets`: Storage, Docs authoring, Sheets ETL, Slides, and content creation via `gws`.
9. `gws-tasks`: Task lists, overdue checks, and email-to-task via `gws`.
10. `gws-chat-meet`: Chat spaces, Meet rooms, team announcements via `gws`.
11. `gws-people`: Contacts directory search and spreadsheet sync via `gws`.
12. `gws-forms-keep`: Surveys, forms, and notes via `gws`.
13. `gws-admin-security`: Admin reports, Apps Script, events, Model Armor via `gws`.
14. `gws-workflows-core`: System diagnostics, recipes, standup reports, and executive assistant via `gws`.
