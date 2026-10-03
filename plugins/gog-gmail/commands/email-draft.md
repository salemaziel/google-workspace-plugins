---
name: email-draft
description: "Prepare an email draft or reply with tone variants using gog CLI"
---

# /email-draft — Compose or Reply with Draft Variants

Generate context-aware, polished email drafts in multiple tone options. Does NOT send emails.

## Usage
- `/email-draft <messageId>` — Generates a contextual reply to a specific email thread.
- `/email-draft --to "user@example.com" --subject "Topic"` — Starts a new email draft.
- `/email-draft "reply to the last email from Alex regarding budget"` — Natural language resolution.

## Execution Steps
1. Gather context:
   - For replies: fetch thread details using `gog gmail get <messageId> --json`. Extract sender, subject, date, and key question.
   - For new messages: extract recipient, subject, and core talking points from `{{args}}`.
2. Generate 2 tone variants:
   - **Variant A (Concise & Direct)**: 2-4 sentences, immediate answer, clear call-to-action.
   - **Variant B (Warm & Collaborative)**: Friendly greeting, appreciation, comprehensive context, open-ended closing.
3. Highlight assumptions:
   - Explicitly list any facts, dates, or estimates that require user validation before sending.
4. Optionally save draft to Gmail:
   - Ask user if they want the chosen draft uploaded via `gog gmail draft create`.
   - Never trigger sending from this command; direct user to `/email-send` when ready.
