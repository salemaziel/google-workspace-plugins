# gogcli Troubleshooting Guide

Diagnosing common setup, authentication, and execution failures with `gogcli`.

## 1. 401 Unauthorized / Token Expired
- **Symptom**: Commands fail with `invalid_grant` or token expired error.
- **Cause**: Google OAuth refresh token has expired (common in testing mode with external users after 7 days) or was revoked.
- **Resolution**:
  - In Google Cloud Console, change app Publishing Status from **Testing** to **In Production** (bypasses 7-day token expiration).
  - Refresh the token locally:
    ```bash
    gog auth add you@example.com --manual
    ```

## 2. API Not Enabled (`accessNotConfigured`)
- **Symptom**: `403 Forbidden: Gmail API has not been used in project...`
- **Resolution**:
  - Visit the Google Cloud Console API library and enable the specific service (e.g. Gmail API, Google Calendar API).

## 3. Command Blocked by Sandbox
- **Symptom**: `command rejected by GOG_ALLOWED_COMMANDS policy`.
- **Resolution**:
  - Inspect current policy: `echo $GOG_ALLOWED_COMMANDS`.
  - Add the required command to the environment variable if authorized.

## 4. Rate Limiting (429 / 403 Rate Limit Exceeded)
- **Symptom**: Repeated rapid calls trigger exponential backoff errors.
- **Resolution**:
  - Space queries across batches.
  - Implement 1-2 second delays between sequential write operations.
