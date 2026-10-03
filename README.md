# Google Workspace & Google Suite Plugin Marketplace

[![Claude Code Marketplace](https://img.shields.io/badge/Claude%20Code-Marketplace-blueviolet)](https://github.com/salemaziel/google-workspace-plugins)
[![Codex Marketplace](https://img.shields.io/badge/OpenAI%20Codex-Marketplace-black)](https://github.com/salemaziel/google-workspace-plugins)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A unified plugin marketplace for **Claude Code** and **OpenAI Codex CLI**, packaging the complete suites of **Google Suite CLI (`gog`)** and **Google Workspace CLI (`gws`)** into modular, service-specific plugins.

Each plugin includes native **Slash Commands** (`commands/`), specialized **Subagents** (`agents/`), and modular **Agent Skills** (`skills/`) structured according to the open standards for Claude Code and Codex CLI.

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

---

## Plugin Catalog

### 1. `gog` CLI Plugins (Google Suite CLI)

| Plugin | Service | Commands | Agents | Description |
|---|---|---|---|---|
| [`gog-gmail`](plugins/gog-gmail) | Gmail | `/email-triage`, `/email-draft`, `/email-send`, `/followups` | `inbox-manager` | Email triage, composition with safeguards, draft review, and unanswered thread followup tracking. |
| [`gog-calendar`](plugins/gog-calendar) | Calendar | `/calendar-agenda`, `/calendar-create`, `/calendar-freebusy`, `/calendar-cancel` | `schedule-coordinator` | Agenda inspection, attendee availability query, conflict-free meeting creation, and event cancellation. |
| [`gog-drive-docs-sheets`](plugins/gog-drive-docs-sheets) | Drive, Docs, Sheets, Slides | `/drive-search`, `/drive-upload`, `/drive-share`, `/docs-export`, `/docs-create`, `/sheets-read`, `/sheets-write`, `/slides-create` | `document-analyst` | Drive searches, uploads, asset sharing, markdown doc exports/creation, spreadsheet reading/writing, and slide decks. |
| [`gog-tasks`](plugins/gog-tasks) | Google Tasks | `/tasks-list`, `/tasks-add`, `/tasks-done`, `/tasks-review`, `/tasks-delete` | `task-organizer` | Task list synchronization, P0–P3 prioritization, due date tracking, and daily standup review. |
| [`gog-suite`](plugins/gog-suite) | Complete Suite | `/gog-briefing`, `/gog-status`, `/gog-auth`, `/gog-accounts` | `suite-orchestrator` | Master cross-service briefing, multi-account management, OAuth2 configuration, and full suite diagnostics. |

---

### 2. `gws` CLI Plugins (Google Workspace CLI)

| Plugin | Service | Commands | Agents | Description |
|---|---|---|---|---|
| [`gws-gmail`](plugins/gws-gmail) | Gmail | `/search`, `/triage`, `/send`, `/reply`, `/forward`, `/vacation`, `/filter` | `customer-support` | Gmail API operations, search, sending with dry-run, draft composition, NDJSON mailbox change streams, and customer support. |
| [`gws-calendar`](plugins/gws-calendar) | Calendar | `/get-schedule`, `/clear-schedule`, `/find-free-time` | `event-coordinator` | Calendar agenda, Meet conferencing, batch invites, focus blocks, and schedule coordination. |
| [`gws-drive-docs-sheets`](plugins/gws-drive-docs-sheets) | Drive, Docs, Sheets, Slides | `/search`, `/upload`, `/sheet-export` | `content-creator`, `researcher` | Cloud storage operations, template instantiation, tabular data manipulation, and slide presentations. |
| [`gws-tasks`](plugins/gws-tasks) | Google Tasks | `/list-tasks`, `/add-task`, `/review-overdue` | `task-administrator` | Task list inspection, overdue audits, and automated email-to-task conversions. |
| [`gws-chat-meet`](plugins/gws-chat-meet) | Chat & Meet | `/send-message`, `/create-meeting` | `team-lead` | Space messaging, video room provisioning, incident post-mortems, and team announcements. |
| [`gws-people`](plugins/gws-people) | Contacts & Directory | `/search-contacts`, `/sync-contacts` | `sales-ops` | Corporate directory search, profile lookups, and contact directory sync to Google Sheets. |
| [`gws-forms-keep`](plugins/gws-forms-keep) | Forms & Keep | `/create-form`, `/collect-responses` | `hr-coordinator` | Feedback forms, survey response aggregation, and team onboarding notes. |
| [`gws-admin-security`](plugins/gws-admin-security) | Admin, Script & Security | `/audit-reports`, `/sanitize-prompt` | `it-admin` | Admin audit logs, Apps Script deployments, Workspace event subscriptions, and Model Armor safety filters. |
| [`gws-workflows-core`](plugins/gws-workflows-core) | Workflows & CLI Core | `/google-workspace`, `/standup`, `/meeting-prep`, `/weekly-digest`, `/doctor` | `executive-assistant`, `project-manager` | Pre-flight diagnostics, security audits, recipe runner, cross-service workflows, and executive orchestration. |

---

## Directory Architecture

```
google-workspace-plugins/
├── .claude-plugin/
│   └── marketplace.json          # Claude Code Marketplace Manifest
├── .agents/
│   └── plugins/
│       └── marketplace.json      # OpenAI Codex Marketplace Manifest
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

Each plugin follows the standardized structure:
```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Claude Code plugin manifest
├── .codex-plugin/
│   └── plugin.json          # Codex plugin manifest
├── commands/                 # Slash commands (.md with YAML frontmatter)
├── agents/                   # Autonomous subagents (.md with YAML frontmatter)
├── skills/                   # Modular agent skills (subdirectories with SKILL.md)
└── README.md
```

---

## Author & Maintainer

Maintained by **salemaziel** (`mymainemail0501@gmail.com`).

Licensed under the MIT License.
