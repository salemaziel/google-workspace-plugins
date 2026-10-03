# gogcli Authentication & Credential Setup Guide

Comprehensive guide for authenticating `gogcli` across desktop, server, and CI environments.

## 1. Google Cloud Console Configuration
1. Navigate to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a project (e.g. `gogcli-personal`).
3. Enable required APIs:
   - Gmail API
   - Google Calendar API
   - Google Drive API
   - Google Docs API
   - Google Sheets API
   - Google Slides API
   - Tasks API
   - People API (Contacts)
4. Configure the OAuth Consent Screen:
   - User Type: External (add your account email under Test Users) or Internal (for Google Workspace organizations).
5. Create OAuth 2.0 Client ID:
   - Application Type: **Desktop Application**
   - Download the client JSON credentials (`client_secret_....json`).

## 2. Desktop Authentication
```bash
# Register the client secret credentials
gog auth credentials ~/Downloads/client_secret_....json

# Launch local browser OAuth flow
gog auth add you@example.com

# Verify authenticated account
gog auth list
```

## 3. Headless / SSH Server Authentication
When running on remote servers without a local desktop browser:
```bash
# Run manual flow to receive authorization URL
gog auth add you@example.com --manual
```
1. Copy the displayed URL into your local computer's browser.
2. Complete Google OAuth consent.
3. Copy the authorization code and paste it into the terminal prompt.

## 4. Multi-Account Management
```bash
# Add work and personal accounts
gog auth add work@company.com
gog auth add personal@gmail.com

# Switch active account via environment variable
export GOG_ACCOUNT=work@company.com

# Or pass account per command
gog --account personal@gmail.com calendar list
```
