# Google Slides Troubleshooting Guide

Common error conditions and resolutions when running `gog slides`.

## 1. Authentication / Permission Errors
- **Cause**: Active token lacks `slides` scope.
- **Resolution**:
  - Re-authenticate via `gog auth add you@example.com` ensuring full workspace scopes.

## 2. Invalid Title Parameter
- **Cause**: Empty or unescaped title string in shell.
- **Resolution**:
  - Ensure title argument is quoted: `gog slides create --title "Product Review"`.

## 3. Retaining Presentation ID
- **Tip**: Always create presentations with `--json` to capture `id` and `presentationUrl` in automated pipelines.
