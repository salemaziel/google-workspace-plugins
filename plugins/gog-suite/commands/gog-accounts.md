---
name: gog-accounts
description: "List, inspect, and switch active Google accounts in gog CLI"
---

# /gog-accounts — Manage Configured Google Accounts

Inspect authenticated accounts, verify primary identities, and switch default environments.

## Usage
- `/gog-accounts` — Lists all registered accounts and current default.
- `/gog-accounts switch work@company.com` — Sets default identity to the chosen account.

## Execution Steps
1. Parse command mode from `{{args}}`.
2. Query registered accounts:
   ```bash
   gog auth list --json
   ```
3. If switching account:
   - Verify requested email exists in the registered account list.
   - Instruct shell to set `export GOG_ACCOUNT="<email>"`.
   - Report: `Switched active gog account to: <email>`.
4. Output Account Overview:
   | Account | Type | Status | Active |
   |---|---|---|---|
   | personal@gmail.com | Consumer | Authorized | (Default) |
   | work@company.com | Workspace | Authorized | |
