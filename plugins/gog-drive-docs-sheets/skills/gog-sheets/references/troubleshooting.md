# Google Sheets Troubleshooting Guide

Common error conditions and resolutions when running `gog sheets`.

## 1. Unable to Parse Range (`badRequest`)
- **Cause**: The `--range` string is malformed or targets a non-existent sheet tab name.
- **Resolution**:
  - Check sheet tab names exactly as they appear in the UI.
  - Wrap tab names with spaces or symbols in single quotes: `'My Sheet'!A1:B10`.
  - Validate column letters (A, B, ..., Z, AA, AB).

## 2. Invalid Values Payload (`invalidValue`)
- **Cause**: The `--values` JSON string is not a 2D array or contains non-serializable elements.
- **Resolution**:
  - Values must always be a list of lists: `[["val1", "val2"]]`.
  - Use `csv_to_sheets_json.py` to convert tabular text or CSV into valid syntax.

## 3. Cell Overwrite Warning
- **Cause**: `gog sheets write` overwrites existing data silently within the target range.
- **Resolution**:
  - Always execute `gog sheets read` first to confirm existing data before issuing a write command.
  - To add rows safely without overwriting, use `gog sheets append`.
