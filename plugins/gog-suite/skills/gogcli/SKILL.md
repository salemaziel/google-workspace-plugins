---
name: "Google Suite CLI (gogcli)"
description: "Cross-service CLI orchestrator for Gmail, Calendar, Drive, Docs, Sheets, Slides, Contacts, and Tasks. Use when managing accounts, sandboxing permissions, or synthesizing multi-service briefings."
---

# Google Suite CLI (`gogcli`) — Multi-Service Orchestrator

Unified interface for orchestrating operations across Google Workspace services using the `gog` CLI.

## Quick Workflow
1. **Health & Connectivity**: Run `./scripts/check_accounts.py` to audit tokens and service reachability.
2. **Account Switching**: Select the target identity using `export GOG_ACCOUNT=user@company.com`.
3. **Execution & Sandboxing**: Execute commands across Gmail, Calendar, Drive, Docs, Sheets, and Tasks with optional command allowlists.

## Core Multi-Service Commands

```bash
# Verify authentication and connectivity
./scripts/check_accounts.py

# Switch active account
export GOG_ACCOUNT="you@company.com"

# Synthesize daily briefing across services
gog calendar list --days 1 --json
gog gmail search "is:unread is:important" --max 5 --json
gog tasks list <tasklistId> --json

# Restrict subagent to safe read-only execution
export GOG_ALLOWED_COMMANDS="gmail search,calendar list,drive search,tasks list"
```

## Security & Best Practices
- **JSON Standard**: Always use `--json` for structured agent interoperability.
- **Account Sandboxing**: Set `GOG_ALLOWED_COMMANDS` in autonomous environments to prevent unintended writes or deletions.

## Progressive Disclosure & References
- **Authentication Guide**: Read [references/auth-guide.md](references/auth-guide.md) for Google Cloud project setup, consent screens, and headless/SSH flows.
- **Environment Variables**: See [references/env-vars.md](references/env-vars.md) for `GOG_ACCOUNT`, `GOG_ALLOWED_COMMANDS`, and path overrides.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for 401 token refresh loops and rate limits.
- **Diagnostics Script**: Run [scripts/check_accounts.py](scripts/check_accounts.py) for instant connection and authentication audits.
- **Templates**: See [templates/daily-briefing.md](templates/daily-briefing.md) and [templates/gog-profile.json](templates/gog-profile.json).
