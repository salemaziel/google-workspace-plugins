# Google Tasks Troubleshooting Guide

Common error conditions and resolutions when operating Google Tasks with `gws`.

## 1. Assigned Tasks Invalidation (`forbidden`)
- **Cause**: Trying to insert or modify tasks created from Google Docs or Google Chat Spaces.
- **Resolution**:
  - Tasks assigned from Docs or Spaces cannot be inserted or deleted directly via the Google Tasks Public API.
  - They must be managed from the origin surface (Docs comment or Chat space).

## 2. Default List Shortcut (`@default`)
- **Tip**: Instead of querying task lists every time, use `@default` for the authenticated user's primary task list:
  ```bash
  gws tasks tasks list --params '{"tasklist": "@default"}'
  ```

## 3. Due Date Formatting
- **Cause**: Rejection when setting `due`.
- **Resolution**:
  - Google Tasks expects RFC 3339 format with time component set to midnight UTC (`T00:00:00.000Z`):
    `"due": "2026-10-15T00:00:00.000Z"`.

## 4. `clear` vs `delete`
- `tasks.tasks.clear`: Hides completed tasks from default listing (soft archive).
- `tasks.tasks.delete`: Permanently destroys the task and associated subtasks.
