# Email Drafting Troubleshooting & Edge Cases

Troubleshooting guide for email drafting operations.

---

## 1. Missing Message Context / Message Not Found
- **Symptom**: `gog gmail get <id>` fails or returns `404 Not Found`.
- **Resolution**:
  1. Ask the user to confirm the email subject or search query.
  2. If the message belongs to a thread, search by thread ID: `gog gmail thread get <threadId> --json`.

## 2. Multi-Recipient & Reply-All Ambiguity
- **Symptom**: Original email has multiple stakeholders in `To` and `CC`.
- **Resolution**:
  1. Default to replying to sender only (`Reply`).
  2. Ask explicitly: "Should this reply be sent to all [N] participants or just [Sender]?"
  3. List the recipient addresses for verification.

## 3. Large Email Threads (>10 messages)
- **Symptom**: Long email chain with conflicting context.
- **Resolution**:
  1. Extract and summarize the most recent 2–3 turns.
  2. Ensure the proposed reply addresses the latest action items without repeating stale details.
