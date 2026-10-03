---
name: gog-email-triage
description: Triage and prioritize inbox emails. Summarize unread messages, classify by urgency and category, propose actions (reply, archive, schedule, create task). Use when user wants to review inbox, process unread emails, or needs help prioritizing messages. Outputs structured summary with top priorities and suggested next actions.
compatibility: Requires gog CLI tool with email access
metadata:
  author: gog-skills
  version: "1.1"
allowed-tools: Bash(gog:*) Read
---

# Email Triage & Prioritization

Review and prioritize incoming Gmail messages into actionable urgency buckets without modifying inbox state.

> [!NOTE]
> This skill is **read-only**. It analyzes messages and suggests actions, but never deletes, archives, or sends emails without explicit confirmation.

## Workflow

### 1. Fetch Unread Messages
```bash
gog gmail search "is:unread" --max 25 --json
```
If no messages return, confirm Inbox Zero or ask if the user wants to review recent messages (`is:inbox`).

### 2. Parse & Classify Messages
Execute the bundled deterministic parser script to calculate counts and generate the summary table:
```bash
gog gmail search "is:unread" --max 25 --json | python3 "$(dirname "$0")/scripts/triage_parser.py" --format table
```
See [Classification Matrix](references/classification-matrix.md) for criteria on urgency tiers (`urgent`, `high`, `medium`, `low`) and categories (`action-required`, `meeting`, `newsletter`, `fyi`, `spam`).

### 3. Present Triage Summary
Fill the standard schema in [Triage Report Template](templates/triage-report.md) presenting:
- Header urgency metrics.
- Top 3 priorities with 1-line rationale.
- Complete message table.
- Proposed checklist of next actions.

### 4. Propose Next Steps
Ask the user which message to address first:
- To draft a reply: invoke `gog-email-draft`.
- To create a to-do item: invoke `gog-tasks`.
- To schedule a meeting: invoke `gog-calendar`.

## Resources
- **Heuristics & Criteria**: [references/classification-matrix.md](references/classification-matrix.md)
- **Troubleshooting**: [references/troubleshooting.md](references/troubleshooting.md)
- **Deterministic Parser**: [scripts/triage_parser.py](scripts/triage_parser.py)
- **Report Template**: [templates/triage-report.md](templates/triage-report.md)
