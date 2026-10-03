# Email Sending Safety Rules & Confirmation Protocols

Mandatory constraints and safeguards governing email delivery via `gog`.

---

## 1. The Strict Confirmation Protocol

Sending an email is an irreversible action. The agent must NEVER send an email without verifying that the user provided the exact uppercase confirmation phrase:

> **`YES, SEND`**

### Acceptable Confirmation Examples:
- `"YES, SEND"`
- `"YES, SEND this draft"`
- `"Approved, YES, SEND now"`

### Unacceptable Affirmations (Must Block & Reject):
- `"Yes"`, `"Sure"`, `"Go ahead"`, `"Looks good"`
- `"Please send"`, `"Send it"`
- Any conversational acknowledgement lacking the exact token sequence `"YES, SEND"`.

---

## 2. Audit Trail Requirements

Every outbound send attempt—whether successful or failed—must be appended to the local audit trail:
- Path: `~/.gog-assistant/audit.log`
- Fields:
  - `timestamp`: ISO 8601 UTC
  - `action`: `email-send`
  - `status`: `success` | `failure`
  - `recipients`: `[to_list]`
  - `subject`: `subject_line`
  - `message_id`: generated message ID (if success)
  - `error`: error details (if failure)
