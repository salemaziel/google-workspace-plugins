---
name: audit-reports
description: "Run Google Workspace Admin audit and activity reports for login, admin, or drive events"
---

Query domain activity logs and audit security events.

## Usage
- `/audit-reports`
- `/audit-reports --app "<login|admin|drive>"`
- `/audit-reports --user "<userKey>" --app "<appName>"`

## Workflow
1. Parse application name (defaults to `login` or `admin`) and target user (defaults to `all`).
2. Query activity reports via `gws`:
   ```bash
   gws admin-reports activities list --params "{\"userKey\": \"${USER:-all}\", \"applicationName\": \"${APP:-login}\"}" --format table
   ```
3. Display event timestamps, IP addresses, actor emails, and action names.
