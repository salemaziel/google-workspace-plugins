---
name: gws-gmail
description: "Send, read, triage, and manage email using the Google Workspace CLI (gws)."
metadata:
  version: 0.22.5
  category: "productivity"
  requires:
    bins:
      - gws
---

# gws-gmail — Gmail CLI Integration

Manage Gmail messages, threads, labels, drafts, and automated streaming through the `gws` CLI.

## Quick Workflow
1. **Triage & Search**: Inspect incoming messages using `+triage` or raw queries.
2. **Read / Extract**: Fetch headers and body text using `+read`.
3. **Dispatch**: Validate payload with `verify_payload.py` and send via `+send` or `+reply`.

## Core Commands

```bash
# Triage unread messages in inbox
gws gmail +triage

# Read specific message
gws gmail +read --id <messageId>

# Validate payload before sending
./scripts/verify_payload.py --to "user@example.com" --subject "Status" --body "Everything is running smoothly."

# Send email with attachment
gws gmail +send --to "user@example.com" --subject "Status" --body "See attached" --attach ./report.pdf

# Reply to existing message in thread
gws gmail +reply --id <messageId> --body "Thank you for the update!"
```

## Safety & Best Practices
- **Dry Run**: Pass `--dry-run` to any send/reply operation to verify message headers without transmission.
- **Attachment Quotas**: Do not exceed 20MB attachments over Gmail; use Drive links for larger assets.

## Progressive Disclosure & References
- **Discovery & API Schemas**: Read [references/discovery-schemas.md](references/discovery-schemas.md) for parameter schemas and direct method calls (`gws schema gmail.users.messages.send`).
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for OAuth scopes, rate limiting, and attachment size limits.
- **Payload Validator**: Use [scripts/verify_payload.py](scripts/verify_payload.py) to validate email parameters and attachments prior to sending.
- **Templates**: See [templates/support-reply.md](templates/support-reply.md) and [templates/forward-brief.md](templates/forward-brief.md).
