# Google Sheets A1-Notation Syntax Reference

Detailed syntax specification for specifying cell ranges in `gog sheets read` and `gog sheets write/append`.

## Range Types and Notations

| Range Format | Target Scope | Example Use Case |
|---|---|---|
| `Sheet1!A1:D10` | Specific rectangular matrix (bounded) | Read fixed table or write explicit block |
| `Sheet1!A:D` | Entire columns A through D | Query all records across 4 columns |
| `Sheet1!5:10` | Entire rows 5 through 10 | Inspect specific records across all columns |
| `Sheet1!A1` | Single cell | Read / update single scalar value or append anchor |
| `'Q3 Budget'!B2:F20` | Sheet with spaces in sheet name | Quoting required if tab name contains spaces |
| `A1:B10` | First tab in workbook | Omission of sheet name targets index 0 tab |

## Quoting Rules
- If the sheet name contains spaces, hyphens, or special characters, wrap it in single quotes: `'2026-Q3 Metrics'!A1:B5`.
- In shell commands (`bash`), ensure outer quotes do not conflict with single quotes:
  ```bash
  gog sheets read <id> --range "'Q3 Forecast'!A1:D20"
  ```

## 2D Matrix Values Schema
When writing or appending values with `--values`, the payload must be a JSON array of row arrays:
```json
[
  ["Column 1", "Column 2", "Column 3"],
  ["Row 1 Val 1", 123.45, true],
  ["Row 2 Val 1", 678.90, false]
]
```
