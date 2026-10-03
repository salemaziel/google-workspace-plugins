---
name: gws-admin-reports
description: "Google Workspace Admin SDK: Audit activity logs, track suspicious logins, and generate security reports via gws CLI."
metadata:
  version: 0.22.5
  category: "productivity"
  requires:
    bins:
      - gws
---

# gws-admin-reports — Admin SDK Audit & Security Reports

Query organization-wide audit logs, monitor threat vectors (suspicious logins, role grants, DLP violations), and generate compliance summaries through the `gws` CLI.

## Quick Workflow
1. **Query Logs**: Query activities with `applicationName` filters (`login`, `admin`, `drive`, `token`).
2. **Analyze**: Pipe activity streams into `audit_log_analyzer.py` to identify anomalies.
3. **Report**: Format findings into executive security compliance summaries.

## Core Commands

```bash
# Query and analyze recent authentication/login events
gws admin-reports activities list \
  --params '{"userKey": "all", "applicationName": "login", "maxResults": 50}' \
  | ./scripts/audit_log_analyzer.py

# Inspect admin privilege escalations
gws admin-reports activities list \
  --params '{"userKey": "all", "applicationName": "admin", "eventName": "ASSIGN_ROLE"}'

# Export audit findings as structured JSON
gws admin-reports activities list \
  --params '{"userKey": "all", "applicationName": "drive", "maxResults": 100}' \
  | ./scripts/audit_log_analyzer.py --json > drive-audit.json
```

## Security & Best Practices
- **Super Admin Required**: Calling Admin Reports requires elevated Workspace administrative privileges.
- **Log Retention**: Events are retained for up to 180 days.

## Progressive Disclosure & References
- **Audit Log Events**: Read [references/audit-log-events.md](references/audit-log-events.md) for event names across login, admin, drive, and token applications.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for 403 administrator authorization issues and retention rules.
- **Audit Analyzer Script**: Use [scripts/audit_log_analyzer.py](scripts/audit_log_analyzer.py) to parse and flag anomalous events.
- **Templates**: See [templates/security-audit-report.md](templates/security-audit-report.md) and [templates/modelarmor-policy.json](templates/modelarmor-policy.json).
