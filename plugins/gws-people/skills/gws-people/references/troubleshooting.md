# Google People API Troubleshooting Guide

Common error conditions and resolutions when operating Contacts through `gws people`.

## 1. 400 Bad Request: `personFields` Missing
- **Cause**: Attempting to call `people.get` or `connections.list` without specifying `personFields`.
- **Resolution**:
  - Always include `--params '{"personFields": "names,emailAddresses"}'` in request parameters.

## 2. Search Warmup Requirement
- **Cause**: Search returns empty or fails immediately on first call.
- **Resolution**:
  - According to Google People API specification, clients should execute a lightweight warmup query before searching:
    ```bash
    gws people people searchContacts --params '{"query": "", "readMask": "names"}'
    ```

## 3. Duplicate Contact Group Name (`409 Conflict`)
- **Cause**: Attempting to create a contact group with a name that already exists for the user.
- **Resolution**:
  - Query existing groups with `gws people contactGroups list` prior to creation.

## 4. ETag Mismatch on Update (`412 Precondition Failed`)
- **Cause**: The contact record was modified concurrently since the initial GET.
- **Resolution**:
  - Re-fetch the person record to acquire the fresh `etag` string before updating.
