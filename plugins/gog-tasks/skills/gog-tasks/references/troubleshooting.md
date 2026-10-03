# Google Tasks Troubleshooting Guide

Common failure modes and recovery procedures when managing tasks with `gog tasks`.

## 1. Missing Task List ID
- **Symptom**: `gog tasks list` or `gog tasks add` fails with missing argument.
- **Cause**: GOG CLI requires an explicit task list ID for all task-level mutations.
- **Resolution**:
  ```bash
  TASKLIST_ID=$(gog tasks lists --json | jq -r '.tasklists[0].id')
  ```

## 2. GOG Not Configured (`GOG_NOT_CONFIGURED`)
- **Symptom**: Command exits with authentication error or empty JSON.
- **Resolution**:
  - Run `gog auth list` to verify configured credentials.
  - Export active account: `export GOG_ACCOUNT="you@example.com"`.
  - Re-authenticate with `gog auth add you@example.com`.

## 3. Duplicate Tasks
- **Symptom**: Multiple identical tasks created across automated runs.
- **Resolution**:
  - Always query open tasks first: `gog tasks list "$TASKLIST_ID" --json`.
  - Check whether a task with a matching title or `SourceEmail` already exists before adding.

## 4. Ambiguous Priority or Due Date from Email
- **Symptom**: Email mentions action but no explicit date or urgency.
- **Resolution**:
  - Look for implicit cues ("before tomorrow's standup", "by Friday EOD").
  - If no cue exists, default to **P2 (Medium)** with due date unset or 7 days out.
  - Present the derived proposal to the user before creation.
