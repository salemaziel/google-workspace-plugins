---
name: gog-email-draft
description: Draft email replies and compose new messages. Given email ID(s) or message context, generate professional email drafts in user's preferred tone. Offers multiple variants (concise, warmer) and includes assumptions/questions for confirmation. Use when user wants to reply to emails, compose new messages, or needs help with email writing. Does NOT send emails.
compatibility: Requires gog CLI tool with email access
metadata:
  author: gog-skills
  version: "1.1"
allowed-tools: Bash(gog:*) Read
---

# Email Drafting Assistant

Generate professional, context-aware email replies and new messages with tone variants without executing external sends.

> [!NOTE]
> This skill creates **drafts only**. It never sends messages. For sending, use `gog-email-send` which requires explicit user approval.

## Workflow

### 1. Gather Context
- **Replying**: Fetch original message context:
  ```bash
  gog gmail get <messageId> --json
  ```
- **New message**: Collect recipient email(s), subject line, and core intent.

### 2. Generate Dual Variants
Always present two distinct tone options (see [Tone Guide](references/tone-guide.md)):
- **Variant A (Concise)**: Direct, 2–4 sentences, immediate next steps.
- **Variant B (Warmer / Detailed)**: Relationship-oriented, comprehensive background.
- Highlight explicit **Assumptions** and **Questions to Confirm** before saving.

### 3. Save Draft via GOG CLI
Once approved by user, save the draft in Gmail using the bundled helper script:
```bash
python3 "$(dirname "$0")/scripts/prepare_draft.py" \
  --to "<recipient@example.com>" \
  --subject "<Subject>" \
  --body "<Draft text>"
```
Return the created `draftId` and advise user they can review in Gmail or send via `/email-send`.

## Resources
- **Tone & Drafting Guide**: [references/tone-guide.md](references/tone-guide.md)
- **Troubleshooting**: [references/troubleshooting.md](references/troubleshooting.md)
- **Draft Creation Script**: [scripts/prepare_draft.py](scripts/prepare_draft.py)
- **Boilerplate Templates**:
  - [Meeting Reply](templates/meeting-reply.md)
  - [Status Update](templates/status-update.md)
  - [Vendor Inquiry](templates/vendor-inquiry.md)
