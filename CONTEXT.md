# Google Workspace & Google Suite Plugin Marketplace — CONTEXT

Unified Claude Code and OpenAI Codex CLI plugin marketplace packaging `gog` and `gws` Google CLI capabilities into modular, service-specific bundles.

## Contract
- **Role**: Plugin Marketplace & Component Repository
- **Clients**: Claude Code (`claude plugin marketplace add`), Codex CLI (`codex marketplace add`)
- **Version**: 1.1.0 (Agent Skills Progressive Disclosure Standard)
- **Components**: 14 Service-focused Plugins (5 `gog` CLI, 9 `gws` CLI)
- **Manifests**:
  - Claude Code: `.claude-plugin/marketplace.json`
  - OpenAI Codex: `.agents/plugins/marketplace.json`
  - Per-plugin: `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`

## Architecture Standard (v1.1.0)
Each plugin implements the Agent Skills progressive disclosure standard:
- **Lean Root `SKILL.md`**: Compact operational guide (<100 lines) with metadata and execution flow.
- **`references/`**: Domain knowledge, API discovery schemas, query syntax, error codes, and troubleshooting.
- **`scripts/`**: Executable deterministic utilities (`chmod +x`) for parsing, formatting, calculations, and dry runs.
- **`templates/`**: Structured schemas, cards, and markdown report templates.

## Plugins Overview
1. `gog-gmail`: Gmail triage, drafts, sending, and followups via `gog`. (Progressive disclosure: `triage_parser.py`, `prepare_draft.py`, `audit_logger.py`, `followup_manager.py`).
2. `gog-calendar`: Agenda, slot finding, and event creation via `gog`. (Progressive disclosure: `find_free_slots.py`, RFC 3339 schemas).
3. `gog-drive-docs-sheets`: Drive, Docs, Sheets, and Slides via `gog`. (Progressive disclosure: `drive_search_filter.py`, `csv_to_sheets_json.py`, A1-notation).
4. `gog-tasks`: Task lists and todo management via `gog`. (Progressive disclosure: `task_filter.py`, P0–P3 taxonomy).
5. `gog-suite`: Full multi-account suite orchestrator for `gog`. (Progressive disclosure: `check_accounts.py`, auth & sandbox guide).
6. `gws-gmail`: Gmail API, search, threads, triage, and customer support via `gws`. (Progressive disclosure: `verify_payload.py`, discovery schemas).
7. `gws-calendar`: Calendar events, Meet conferencing, and event coordination via `gws`. (Progressive disclosure: `find_free_slots_gws.py`, meet config).
8. `gws-drive-docs-sheets`: Storage, Docs authoring, Sheets ETL, Slides, and content creation via `gws`. (Progressive disclosure: `drive_folder_tree.py`, batchUpdate schemas).
9. `gws-tasks`: Task lists, overdue checks, and email-to-task via `gws`. (Progressive disclosure: `tasks_triage.py`, hierarchy guide).
10. `gws-chat-meet`: Chat spaces, Meet rooms, team announcements via `gws`. (Progressive disclosure: `chat_card_builder.py`, Cards v2 schemas).
11. `gws-people`: Contacts directory search and spreadsheet sync via `gws`. (Progressive disclosure: `contact_vcard_exporter.py`, personFields guide).
12. `gws-forms-keep`: Surveys, forms, and notes via `gws`. (Progressive disclosure: `form_response_analyzer.py`, 2-step form creation).
13. `gws-admin-security`: Admin reports, Apps Script, events, Model Armor via `gws`. (Progressive disclosure: `audit_log_analyzer.py`, threat vector catalog).
14. `gws-workflows-core`: System diagnostics, recipes, standup reports, and executive assistant via `gws`. (Progressive disclosure: `gws_doctor.py`, `workspace_audit.py`, `gws_recipe_runner.py`).
