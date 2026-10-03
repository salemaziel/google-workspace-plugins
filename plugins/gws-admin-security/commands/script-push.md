---
name: script-push
description: "Upload local files (.gs, .js, .html, appsscript.json) to a Google Apps Script project"
---

Deploy local project files directly to Google Apps Script.

## Usage
- `/script-push --script "<scriptId>"`
- `/script-push --script "<scriptId>" --dir "<localDir>"`

## Workflow
1. Parse script ID and local directory (defaults to current working directory).
2. Validate presence of script files and `appsscript.json`.
3. Warn the user that this will overwrite all files in the Apps Script project.
4. Execute deployment:
   ```bash
   gws script +push --script "<scriptId>" --dir "${DIR:-.}"
   ```
5. Confirm updated files and project status.
