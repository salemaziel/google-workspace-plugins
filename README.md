# Google Workspace & Google Suite Plugin Marketplace

[![Claude Code Marketplace](https://img.shields.io/badge/Claude%20Code-Marketplace-blueviolet)](https://github.com/salemaziel/google-workspace-plugins)
[![Codex Marketplace](https://img.shields.io/badge/OpenAI%20Codex-Marketplace-black)](https://github.com/salemaziel/google-workspace-plugins)
[![Antigravity CLI](https://img.shields.io/badge/Antigravity%20CLI-Plugins-4285F4)](https://github.com/salemaziel/google-workspace-plugins)
[![Version: 1.2.0](https://img.shields.io/badge/Version-1.2.0-brightgreen.svg)](https://github.com/salemaziel/google-workspace-plugins)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A unified, production-grade plugin marketplace for **Claude Code**, **OpenAI Codex CLI**, and **Antigravity CLI (`agy`)**, packaging the complete suites of **Google Suite CLI (`gog`)** and **Google Workspace CLI (`gws`)** into 14 modular, service-specific plugins.

All 14 plugins follow the **Agent Skills Progressive Disclosure Standard (v1.2.0)**:
- **Lean Root `SKILL.md`**: Compact operational guides (<100 lines) with clear decision flows and metadata.
- **Deep Reference Docs (`references/`)**: Exhaustive API schemas, full-text query syntax, priority taxonomies, and troubleshooting guides.
- **Executable Automation Scripts (`scripts/`)**: Deterministic calculations, free-slot algorithms, payload validators, CSV converters, and log parsers.
- **Boilerplate Templates (`templates/`)**: Reusable incident alerts, daily standups, meeting dossiers, and PRD specifications.

---

## Quick Start & Installation

### Claude Code

1. Add the marketplace:
```bash
claude plugin marketplace add salemaziel/google-workspace-plugins
```

2. Install any service bundle:
```bash
# GOG CLI plugins
claude plugin install gog-gmail --marketplace google-workspace-plugins
claude plugin install gog-calendar --marketplace google-workspace-plugins
claude plugin install gog-drive-docs-sheets --marketplace google-workspace-plugins
claude plugin install gog-tasks --marketplace google-workspace-plugins
claude plugin install gog-suite --marketplace google-workspace-plugins

# Google Workspace (gws) CLI plugins
claude plugin install gws-gmail --marketplace google-workspace-plugins
claude plugin install gws-calendar --marketplace google-workspace-plugins
claude plugin install gws-drive-docs-sheets --marketplace google-workspace-plugins
claude plugin install gws-tasks --marketplace google-workspace-plugins
claude plugin install gws-chat-meet --marketplace google-workspace-plugins
claude plugin install gws-people --marketplace google-workspace-plugins
claude plugin install gws-forms-keep --marketplace google-workspace-plugins
claude plugin install gws-admin-security --marketplace google-workspace-plugins
claude plugin install gws-workflows-core --marketplace google-workspace-plugins
```

Some plugins declare `dependencies` and install the plugins their agents need automatically: `gws-workflows-core` and `gws-forms-keep` pull in `gws-gmail`, `gws-calendar`, `gws-drive-docs-sheets` and `gws-chat-meet`; `gws-people` and `gws-admin-security` pull in `gws-gmail`, `gws-calendar` and `gws-drive-docs-sheets`. To disable one of those four, disable the plugins that depend on it first.

---

### OpenAI Codex CLI

1. Register the marketplace:
```bash
codex marketplace add google-workspace-plugins https://github.com/salemaziel/google-workspace-plugins.git
```

2. Install any service bundle:
```bash
codex plugin install gog-gmail@google-workspace-plugins
codex plugin install gws-gmail@google-workspace-plugins
codex plugin install gws-workflows-core@google-workspace-plugins
```

Codex has no plugin dependency mechanism, so install the dependencies yourself. For the cross-service workflows in `gws-workflows-core`, `gws-forms-keep`, `gws-people` and `gws-admin-security`, also install `gws-gmail`, `gws-calendar`, `gws-drive-docs-sheets` and `gws-chat-meet`. Codex plugins cannot ship agents, so the `agents/` folders are Claude Code and Antigravity only.

---

### Antigravity CLI (`agy`)

Each plugin has a root `plugin.json` (Antigravity manifest). Clone the repo and install plugins from their local paths:
```bash
git clone https://github.com/salemaziel/google-workspace-plugins.git
cd google-workspace-plugins
agy plugin install ./plugins/gws-gmail
agy plugin install ./plugins/gws-workflows-core
agy plugin list
```

Antigravity converts each plugin's `commands/` into skills, so they work as slash commands. It has no plugin dependencies either; install `gws-gmail`, `gws-calendar`, `gws-drive-docs-sheets` and `gws-chat-meet` alongside the plugins that use them (same list as Codex above).

---

## Plugin Catalog (All 14 Plugins — v1.2.0)

### 1. `gog` CLI Plugins (Google Suite CLI)

| Plugin | Service | Commands | Agents | Progressive Disclosure Components |
|---|---|---|---|---|
| [`gog-gmail`](plugins/gog-gmail) | Gmail | `/email-triage`, `/email-draft`, `/email-send`, `/followups` | `inbox-manager` | `triage_parser.py`, `prepare_draft.py`, `audit_logger.py`, `followup_manager.py`, classification matrix, tone guides, templates |
| [`gog-calendar`](plugins/gog-calendar) | Calendar | `/calendar-agenda`, `/calendar-create`, `/calendar-freebusy`, `/calendar-cancel` | `schedule-coordinator` | `find_free_slots.py`, RFC 3339 schemas, conflict resolution, agenda/proposal templates |
| [`gog-drive-docs-sheets`](plugins/gog-drive-docs-sheets) | Drive, Docs, Sheets, Slides | `/drive-search`, `/drive-upload`, `/drive-share`, `/docs-export`, `/docs-create`, `/sheets-read`, `/sheets-write`, `/slides-create` | `document-analyst` | `drive_search_filter.py`, `csv_to_sheets_json.py`, A1-notation reference, presentation guidelines, templates |
| [`gog-tasks`](plugins/gog-tasks) | Google Tasks | `/tasks-list`, `/tasks-add`, `/tasks-done`, `/tasks-review`, `/tasks-delete` | `task-organizer` | `task_filter.py` (P0–P3 bucketing), safe test plan, daily standup review templates |
| [`gog-suite`](plugins/gog-suite) | Complete Suite | `/gog-briefing`, `/gog-status`, `/gog-auth`, `/gog-accounts` | `suite-orchestrator` | `check_accounts.py`, OAuth headless guide, `GOG_ALLOWED_COMMANDS` sandbox, briefing templates |

---

### 2. `gws` CLI Plugins (Google Workspace CLI)

| Plugin | Service | Commands | Agents | Progressive Disclosure Components |
|---|---|---|---|---|
| [`gws-gmail`](plugins/gws-gmail) | Gmail | `/search`, `/triage`, `/send`, `/reply`, `/forward`, `/vacation`, `/filter` | — | `verify_payload.py` (pre-flight payload validator), discovery schemas, support reply templates |
| [`gws-calendar`](plugins/gws-calendar) | Calendar | `/get-schedule`, `/insert-event`, `/clear-schedule`, `/find-free-time`, `/focus-time`, `/reschedule`, `/batch-invite` | — | `find_free_slots_gws.py` (freebusy gap calculator), Meet conference config, event summary templates |
| [`gws-drive-docs-sheets`](plugins/gws-drive-docs-sheets) | Drive, Docs, Sheets, Slides | `/search`, `/upload`, `/doc-create`, `/doc-append`, `/sheet-export`, `/sheet-append`, `/sheet-read`, `/slide-create`, `/shared-drive` | — | `drive_folder_tree.py` (ASCII folder visualizer), batchUpdate Docs/Slides schemas, PRD spec templates |
| [`gws-tasks`](plugins/gws-tasks) | Google Tasks | `/list-tasks`, `/add-task`, `/complete-task`, `/create-tasklist`, `/review-overdue`, `/email-to-task` | `task-administrator` | `tasks_triage.py` (overdue auditor), subtask hierarchy reference, batch task templates |
| [`gws-chat-meet`](plugins/gws-chat-meet) | Chat & Meet | `/list-spaces`, `/send-message`, `/create-meeting`, `/team-announce`, `/post-mortem`, `/review-participants` | — | `chat_card_builder.py` (Cards v2 generator), incident war room templates, standup templates |
| [`gws-people`](plugins/gws-people) | Contacts & Directory | `/search-contacts`, `/get-contact`, `/create-contact`, `/list-groups`, `/sync-contacts` | `sales-ops` | `contact_vcard_exporter.py` (CSV/vCard exporter), `personFields` guide, CRM sync schema |
| [`gws-forms-keep`](plugins/gws-forms-keep) | Forms & Keep | `/create-form`, `/get-form`, `/collect-responses`, `/keep-note`, `/keep-list` | `hr-coordinator` | `form_response_analyzer.py` (tally & percentage analyzer), 2-step form creation, checklist templates |
| [`gws-admin-security`](plugins/gws-admin-security) | Admin, Script & Security | `/audit-reports`, `/sanitize-prompt`, `/sanitize-response`, `/script-push`, `/events-subscribe`, `/create-classroom` | `it-admin` | `audit_log_analyzer.py` (suspicious login & privilege anomaly detector), Model Armor policies |
| [`gws-workflows-core`](plugins/gws-workflows-core) | Workflows & CLI Core | `/doctor`, `/google-workspace`, `/standup`, `/meeting-prep`, `/weekly-digest`, `/recipe`, `/audit`, `/auth-guide` | `executive-assistant`, `project-manager`, `customer-support`, `event-coordinator`, `team-lead`, `content-creator`, `researcher` | Suite scripts (`gws_doctor.py`, `workspace_audit.py`, `gws_recipe_runner.py`), command references, cross-service templates |

---

## 41 CLI-Agnostic Recipe Workflows (v1.2.0)

All 41 canonical productivity recipes are engineered to be **CLI-agnostic** (running seamlessly with either `gog` or `gws` CLI) and follow the Agent Skills progressive disclosure standard (`SKILL.md` <80 lines, `references/cli-mapping.md`, `scripts/*.py`, `templates/`):

- **Calendar Workflows (8)**: `recipe-batch-invite-to-event`, `recipe-block-focus-time`, `recipe-create-events-from-sheet`, `recipe-find-free-time`, `recipe-plan-weekly-schedule`, `recipe-reschedule-meeting`, `recipe-schedule-recurring-event`, `recipe-share-event-materials` (in `gws-calendar` & `gog-calendar`).
- **Gmail Workflows (6)**: `recipe-create-gmail-filter`, `recipe-create-vacation-responder`, `recipe-forward-labeled-emails`, `recipe-label-and-archive-emails`, `recipe-save-email-attachments`, `recipe-save-email-to-doc` (in `gws-gmail` & `gog-gmail`).
- **Drive, Docs, Sheets & Slides Workflows (17)**: `recipe-backup-sheet-as-csv`, `recipe-bulk-download-folder`, `recipe-compare-sheet-tabs`, `recipe-copy-sheet-for-new-month`, `recipe-create-doc-from-template`, `recipe-create-expense-tracker`, `recipe-create-presentation`, `recipe-create-shared-drive`, `recipe-draft-email-from-doc`, `recipe-email-drive-link`, `recipe-find-large-files`, `recipe-generate-report-from-sheet`, `recipe-log-deal-update`, `recipe-organize-drive-folder`, `recipe-share-doc-and-notify`, `recipe-share-folder-with-team`, `recipe-watch-drive-changes` (in `gws-drive-docs-sheets` & `gog-drive-docs-sheets`).
- **Tasks Workflows (2)**: `recipe-create-task-list`, `recipe-review-overdue-tasks` (in `gws-tasks` & `gog-tasks`).
- **Cross-Service Workflows (8)**: `recipe-create-meet-space`, `recipe-post-mortem-setup`, `recipe-review-meet-participants`, `recipe-send-team-announcement`, `recipe-collect-form-responses`, `recipe-create-feedback-form`, `recipe-sync-contacts-to-sheet`, `recipe-create-classroom-course` (in corresponding `gws-*` & `gog-suite`).

---

## Directory Architecture

```
google-workspace-plugins/
├── .claude-plugin/
│   └── marketplace.json          # Claude Code Marketplace Manifest (v1.2.0)
├── .agents/
│   └── plugins/
│       └── marketplace.json      # OpenAI Codex Marketplace Manifest (v1.2.0)
├── plugins/
│   ├── gog-gmail/
│   ├── gog-calendar/
│   ├── gog-drive-docs-sheets/
│   ├── gog-tasks/
│   ├── gog-suite/
│   ├── gws-gmail/
│   ├── gws-calendar/
│   ├── gws-drive-docs-sheets/
│   ├── gws-tasks/
│   ├── gws-chat-meet/
│   ├── gws-people/
│   ├── gws-forms-keep/
│   ├── gws-admin-security/
│   └── gws-workflows-core/
├── CONTEXT.md
└── README.md
```

Each plugin follows the standardized progressive disclosure structure:
```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Claude Code plugin manifest (v1.2.0)
├── .codex-plugin/
│   └── plugin.json          # Codex plugin manifest (v1.2.0)
├── plugin.json              # Antigravity CLI plugin manifest (name, description only)
├── commands/                 # Slash commands (.md with YAML frontmatter)
├── agents/                   # Autonomous subagents (.md with YAML frontmatter)
├── skills/                   # Modular agent skills (subdirectories with lean SKILL.md)
│   └── skill-name/
│       ├── SKILL.md          # Lean operational guide (<100 lines)
│       ├── references/       # In-depth schemas, query syntax, troubleshooting
│       ├── scripts/          # Deterministic executable CLI tools (chmod +x)
│       └── templates/        # Reusable schemas, cards, and markdown reports
└── README.md
```

---

## Author & Maintainer

Maintained by **salemaziel** (`mymainemail0501@gmail.com`).

Licensed under the MIT License.
