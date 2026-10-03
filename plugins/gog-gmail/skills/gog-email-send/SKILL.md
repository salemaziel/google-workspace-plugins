---
name: gog-email-send
description: Send email messages with explicit user confirmation. Requires the exact confirmation string "YES, SEND" before executing send operations. Logs all sends to audit trail. Use ONLY when user explicitly confirms they want to send an email, never auto-invoke. This is a critical write operation requiring human approval.
compatibility: Requires gog CLI tool with email send permissions
metadata:
  author: gog-skills
  version: "1.1"
  disable-model-invocation: true
  requires-explicit-confirmation: true
allowed-tools: Bash(gog:*) Read
---

# Email Sending with Confirmation

**⚠️ CRITICAL SAFETY CONSTRAINT**: This skill sends real emails. It MUST NEVER be invoked without explicit, exact confirmation: **"YES, SEND"**.

## Workflow

### 1. Verification of Confirmation String
Check if user input contains the exact phrase:
```text
YES, SEND
```
If missing, present [Send Summary Template](templates/send-summary.md) and STOP. Do not proceed until the exact token is supplied. See [Safety Rules](references/safety-rules.md).

### 2. Execution
- **Send Existing Draft**:
  ```bash
  gog gmail drafts send <draftId> --json
  ```
- **Direct Send**:
  ```bash
  gog gmail send --to "<recipient>" --subject "<Subject>" --body "<bodyFile>" --json
  ```

### 3. Audit Logging
Deterministically append the send event to the audit trail:
```bash
python3 "$(dirname "$0")/scripts/audit_logger.py" \
  --status "success" \
  --to "<recipient>" \
  --subject "<Subject>" \
  --message-id "<messageId>"
```

### 4. Confirmation
Display sent message confirmation with timestamp and message ID.

## Resources
- **Safety Protocol**: [references/safety-rules.md](references/safety-rules.md)
- **Troubleshooting**: [references/troubleshooting.md](references/troubleshooting.md)
- **Audit Logger**: [scripts/audit_logger.py](scripts/audit_logger.py)
- **Verification Template**: [templates/send-summary.md](templates/send-summary.md)
