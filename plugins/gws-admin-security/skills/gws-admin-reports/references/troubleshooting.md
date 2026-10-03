# Google Workspace Admin Reports Troubleshooting Guide

Common error conditions and resolutions when operating Admin SDK with `gws`.

## 1. 403 Forbidden: Not an Administrator
- **Cause**: The authenticated account is a regular user without delegated Google Workspace administrative privileges.
- **Resolution**:
  - The Admin SDK Reports API requires either **Super Admin** or a delegated admin role with **Reports** privilege.
  - Verify account identity: `gws auth list`.

## 2. Invalid `userKey` Parameter
- **Cause**: Omitting `userKey`.
- **Resolution**:
  - To query events across the entire organization, specify `"userKey": "all"`.
  - For a specific individual, pass their primary email: `"userKey": "employee@company.com"`.

## 3. Data Retention Limits
- Activities are retained for a maximum of **180 days**. Queries with `startTime` exceeding 180 days will return an error or empty result set.
