# Email Sending Troubleshooting & Recovery

Failure analysis and remediation for outbound email issues.

---

## 1. Authentication Failure / Invalid Token
- **Symptom**: `gog gmail drafts send` or `gog gmail send` exits with HTTP 401/403.
- **Resolution**:
  1. Halt execution immediately.
  2. Direct user to refresh OAuth token: `gog auth login`.
  3. Ensure the draft remains safely saved in Gmail so it can be sent after authentication.

## 2. Invalid Recipient Syntax
- **Symptom**: CLI returns malformed email address error.
- **Resolution**:
  1. Validate email structure (`user@domain.tld`).
  2. Point out the malformed address and request correction.
  3. Require fresh `"YES, SEND"` confirmation once corrected.

## 3. Network Disconnect During Send
- **Symptom**: Command times out or socket breaks.
- **Resolution**:
  1. Inspect the sent folder before retrying:
     ```bash
     gog gmail search "in:sent" --max 1 --json
     ```
  2. If the message appears in Sent, confirm delivery and do NOT resend.
