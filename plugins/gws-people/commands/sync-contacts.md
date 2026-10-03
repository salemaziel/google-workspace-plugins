---
name: sync-contacts
description: "Export Google Contacts directory into a Google Sheets spreadsheet"
---

Export domain directory or personal contacts into a structured Google Sheet.

## Usage
- `/sync-contacts --sheet "<spreadsheetId>"`
- `/sync-contacts --sheet "<spreadsheetId>" --range "Contacts"`

## Workflow
1. Parse spreadsheet ID and optional tab range name.
2. Fetch directory contacts via `gws`:
   ```bash
   gws people people listDirectoryPeople --params '{"readMask": "names,emailAddresses,phoneNumbers,organizations", "sources": ["DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE"], "pageSize": 100}' --format json
   ```
3. Initialize sheet headers if empty:
   ```bash
   gws sheets +append --spreadsheet "<spreadsheetId>" --range "${RANGE:-Contacts}" --values "Full Name,Email,Phone,Organization,Job Title"
   ```
4. Transform contacts into tabular rows and append them:
   ```bash
   gws sheets +append --spreadsheet "<spreadsheetId>" --range "${RANGE:-Contacts}" --json-values '<rows-json>'
   ```
5. Confirm total synced records and provide link to the Google Sheet.
