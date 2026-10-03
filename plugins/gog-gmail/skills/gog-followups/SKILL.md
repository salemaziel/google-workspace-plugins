---
name: gog-followups
description: Track follow-ups from sent emails, detect stale threads, and generate reminder drafts. Maintains local store of pending follow-ups with nudge dates. Identifies emails awaiting responses and suggests gentle reminder messages. Use when user wants to track responses, follow up on sent emails, or review what's waiting for replies. Requires confirmation before updating follow-up store.
compatibility: Requires gog CLI tool with email access
metadata:
  author: gog-skills
  version: "1.1"
allowed-tools: Bash(gog:*) Read Write
---

# Follow-up & Nudge Tracking

Track unanswered email threads, monitor nudge dates, and generate timely reminder drafts via `gog`.

## Follow-up Store
Tracked locally at `~/.gog-assistant/followups.json` (chmod 600).

## Workflow

### 1. Track New Follow-up
When a user sends or references an email awaiting a response:
```bash
python3 "$(dirname "$0")/scripts/followup_manager.py" add \
  --email-id "<messageId>" \
  --person "<recipient@example.com>" \
  --topic "<Subject>" \
  --days 3 \
  --priority "high"
```

### 2. Review Pending Follow-ups
Display items awaiting responses:
```bash
python3 "$(dirname "$0")/scripts/followup_manager.py" list --format table
```
Highlight any items where `next_nudge_date` is today or overdue.

### 3. Generate Nudge Draft
When a nudge is due, draft a gentle or direct reminder (see [Nudge Template](templates/nudge-draft.md) and [Nudge Strategy](references/nudge-strategy.md)):
- Fetch previous thread: `gog gmail get <emailId> --json`.
- Present Gentle vs Direct draft variants.
- Once approved, send via `gog-email-send` ("YES, SEND").

### 4. Close Follow-up
When a response is received or tracking is complete:
```bash
python3 "$(dirname "$0")/scripts/followup_manager.py" close --id "<followupId>"
```

## Resources
- **Nudge Strategy & Timing**: [references/nudge-strategy.md](references/nudge-strategy.md)
- **Troubleshooting**: [references/troubleshooting.md](references/troubleshooting.md)
- **Store Manager Script**: [scripts/followup_manager.py](scripts/followup_manager.py)
- **Nudge Draft Template**: [templates/nudge-draft.md](templates/nudge-draft.md)
