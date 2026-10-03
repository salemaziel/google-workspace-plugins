# Google Workspace — Admin & Security (`gws-admin-security`)

Google Workspace Admin reports, Classroom courses, Apps Script deployment, Workspace events, and Model Armor safety filters via `gws` CLI.

## Installation

### Claude Code
```bash
claude plugin install gws-admin-security --marketplace google-workspace-plugins
```

### Codex CLI
```bash
codex plugin install gws-admin-security@google-workspace-plugins
```

## Architecture & Components (v1.1.0)
Follows the Agent Skills progressive disclosure standard:

- **Skills & Progressive Disclosure**:
  - `gws-admin-reports` (core security audit logs)
    - References: `references/audit-log-events.md`, `references/troubleshooting.md`
    - Scripts: `scripts/audit_log_analyzer.py` (executable Admin SDK log analyzer & anomaly detector)
    - Templates: `templates/security-audit-report.md`, `templates/modelarmor-policy.json`
  - Safety & Integration Skills:
    - `gws-modelarmor`, `gws-modelarmor-create-template`, `gws-modelarmor-sanitize-prompt`, `gws-modelarmor-sanitize-response`
    - `gws-script`, `gws-script-push`
    - `gws-events`, `gws-events-subscribe`, `gws-events-renew`
    - `gws-classroom`, `recipe-create-classroom-course`
- **Commands**:
  - `/audit-reports` — Run Admin audit logs and login/drive activity reports.
  - `/sanitize-prompt` — Sanitize inbound prompts with Google Model Armor templates.
  - `/sanitize-response` — Sanitize outbound model responses for toxicity and data leakage.
  - `/script-push` — Upload local files (.gs, .js, .html, appsscript.json) to Apps Script.
  - `/events-subscribe` — Subscribe to real-time Workspace events via Cloud Pub/Sub.
  - `/create-classroom` — Provision Google Classroom courses and sections.
- **Agents**:
  - `it-admin` — Autonomous IT administrator, security auditor, Apps Script deployer, and policy enforcer.

## License
MIT
