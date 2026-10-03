---
name: get-contact
description: "Retrieve comprehensive contact details by resource name or person ID"
---

Fetch and display detailed person data for a specific contact.

## Usage
- `/get-contact <resourceName>` (e.g. `people/c123456789`)
- `/get-contact me` (authenticated user profile)

## Workflow
1. Parse resource name (e.g. `people/c...` or `people/me`).
2. Retrieve profile via `gws`:
   ```bash
   gws people people get --params '{"resourceName": "<resourceName>", "personFields": "names,emailAddresses,phoneNumbers,organizations,biographies,photos"}' --format json
   ```
3. Format and display profile summary.
