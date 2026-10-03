# Google Suite CLI — Full Suite (`gog-suite`)

Unified multi-account Google Suite CLI (`gog`) integration across Gmail, Calendar, Drive, Docs, Sheets, Slides, Chat, Contacts, Tasks, Keep, and Admin.

## Installation

### Claude Code
```bash
claude plugin install gog-suite --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gog-suite@google-workspace-plugins
```

## Architecture & Components (v1.1.0)
Follows the Agent Skills progressive disclosure standard:

- **Skills**:
  - `gogcli` — Unified cheatsheet, troubleshooting, and headless authentication guide.
    - References: `references/auth-guide.md`, `references/env-vars.md`, `references/troubleshooting.md`
    - Scripts: `scripts/check_accounts.py` (executable diagnostics and connectivity auditor)
    - Templates: `templates/daily-briefing.md`, `templates/gog-profile.json`
- **Commands**:
  - `/gog-briefing` — Generate an executive daily briefing (Calendar + Gmail + Tasks).
  - `/gog-status` — Check CLI binary version, list accounts, and probe API connectivity.
  - `/gog-auth` — Interactive OAuth2 setup wizard and headless authentication guide.
  - `/gog-accounts` — List, inspect, and switch active Google accounts.
- **Agents**:
  - `suite-orchestrator` — Master coordinator across all 15 Google services and multi-account setups.

## License
MIT
