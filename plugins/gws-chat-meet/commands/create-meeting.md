---
name: create-meeting
description: "Provision a new Google Meet conference space and return the join link"
---

Create an open or restricted Google Meet video space.

## Usage
- `/create-meeting`
- `/create-meeting --access "<OPEN|TRUSTED|RESTRICTED>"`

## Workflow
1. Parse access policy (defaults to `OPEN`).
2. Provision space via `gws`:
   ```bash
   gws meet spaces create --json '{"config": {"accessType": "${ACCESS:-OPEN}"}}'
   ```
3. Extract `meetingUri` and space name.
4. Output join link (`https://meet.google.com/...`) and access rules.
