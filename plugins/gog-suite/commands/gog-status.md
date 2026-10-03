---
name: gog-status
description: "Check gog CLI version, list configured accounts, and test API connectivity"
---

# /gog-status — Check CLI & Authentication Health

Verify the installation of `gog`, inspect configured accounts, and test connectivity to Google APIs.

## Usage
- `/gog-status` — Performs full environment diagnostics.
- `/gog-status --account work@company.com` — Tests connectivity for a specific account.

## Execution Steps
1. Verify CLI installation:
   ```bash
   gog --version
   ```
2. Inspect configured accounts:
   ```bash
   gog auth list --json
   ```
3. Test primary service probes:
   ```bash
   # Test Gmail API
   gog gmail labels list --json >/dev/null && echo "✅ Gmail: Connected" || echo "❌ Gmail: Failed"
   # Test Calendar API
   gog calendar list --days 1 --json >/dev/null && echo "✅ Calendar: Connected" || echo "❌ Calendar: Failed"
   # Test Drive API
   gog drive list --max 1 --json >/dev/null && echo "✅ Drive: Connected" || echo "❌ Drive: Failed"
   ```
4. Output diagnostic report:
   - **Active Account**: [Email]
   - **Configured Accounts**: [List of accounts]
   - **API Status**: Gmail (OK), Calendar (OK), Drive (OK)
   - **Guidance**: If any service fails, recommend `/gog-auth`.
