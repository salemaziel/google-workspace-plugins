---
name: gog-auth
description: "Interactive OAuth2 authentication and credential setup guide for gog CLI"
---

# /gog-auth — Setup and Authorize Google Accounts

Configure OAuth2 credentials from Google Cloud Console and authenticate accounts in the `gog` CLI.

## Usage
- `/gog-auth` — Displays step-by-step interactive setup wizard.
- `/gog-auth --add "user@example.com"` — Initiates OAuth flow for a specific account.
- `/gog-auth --credentials ./client_secret.json` — Stores OAuth client secrets.
- `/gog-auth --manual` — Prints a manual authorization URL for headless/remote servers.

## Execution Steps
1. Parse arguments `{{args}}`:
2. **Step 1: Client Secret Registration** (one-time):
   If `client_secret.json` is provided:
   ```bash
   gog auth credentials <path-to-client-secret.json>
   ```
3. **Step 2: Account Authorization**:
   ```bash
   # Standard local browser flow
   gog auth add <email>

   # Headless / SSH remote flow
   gog auth add <email> --manual
   ```
4. **Step 3: Set Default Identity**:
   ```bash
   export GOG_ACCOUNT=<email>
   ```
5. Verify setup by running `/gog-status`.
