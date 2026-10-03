# Email Triage Troubleshooting & Failure Modes

Troubleshooting guide for errors and edge cases encountered during email triage with `gog`.

---

## 1. GOG CLI Not Configured / Auth Expired
- **Symptom**: Command fails or dynamic context returns `GOG_NOT_CONFIGURED` / unauthorized.
- **Resolution**:
  1. Inform the user: "GOG CLI is not authenticated."
  2. Direct user to run `gog auth login` or verify `gog auth status`.
  3. Do not attempt triage until credentials are confirmed.

## 2. Empty Inbox / Zero Unread
- **Symptom**: `gog gmail search "is:unread"` returns `[]`.
- **Resolution**:
  1. Confirm Inbox Zero state: "No unread messages found."
  2. Ask if the user would like to review recent inbox emails instead:
     ```bash
     gog gmail search "is:inbox" --max 25 --json
     ```

## 3. Excessive Message Volume (>25 Unread)
- **Symptom**: User has dozens or hundreds of unread messages.
- **Resolution**:
  1. Triage in prioritized batches (e.g. `--max 25`).
  2. Offer focused filters:
     - Urgent/High only: `gog gmail search "is:unread (priority:high OR urgent)" --max 25 --json`
     - By sender/domain: `gog gmail search "is:unread from:company.com" --max 25 --json`

## 4. Metadata Ambiguity
- **Symptom**: Subject and snippet are too brief to determine urgency.
- **Resolution**:
  1. Fetch full message body: `gog gmail get <messageId> --json`.
  2. If still ambiguous, classify as `medium` urgency and `action-required`.
