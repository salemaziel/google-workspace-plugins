# Follow-ups Troubleshooting & Storage Management

Troubleshooting guide for the local follow-up registry.

---

## 1. Store Location & File Permissions
- Follow-ups are tracked locally in:
  ```text
  ~/.gog-assistant/followups.json
  ```
- File permissions must be set to `0600` for user privacy:
  ```bash
  chmod 600 ~/.gog-assistant/followups.json
  ```

## 2. Corrupted JSON Recovery
- **Symptom**: `jq parse error` or malformed JSON syntax.
- **Resolution**:
  1. Create immediate timestamped backup:
     ```bash
     cp ~/.gog-assistant/followups.json ~/.gog-assistant/followups.json.bak-$(date +%s)
     ```
  2. Re-initialize empty or repaired array `[]`.

## 3. Large Overdue Backlog (>10 items)
- **Symptom**: User is overwhelmed with overdue follow-up alerts.
- **Resolution**:
  1. Filter by priority: focus exclusively on `high` priority items first.
  2. Ask user whether stale items (>30 days) should be batch-closed.
