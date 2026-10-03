---
name: create-contact
description: "Create a new contact in Google Contacts with name, email, phone, and organization"
---

Create a new contact record.

## Usage
- `/create-contact --given-name "<first>" --family-name "<last>" --email "<email>"`
- `/create-contact --given-name "<first>" --family-name "<last>" --email "<email>" --phone "<phone>" --org "<company>"`

## Workflow
1. Parse contact properties from arguments.
2. Build JSON payload:
   ```json
   {
     "names": [{"givenName": "<first>", "familyName": "<last>"}],
     "emailAddresses": [{"value": "<email>"}],
     "phoneNumbers": [{"value": "<phone>"}],
     "organizations": [{"name": "<company>"}]
   }
   ```
3. Execute contact creation:
   ```bash
   gws people people createContact --json '<payload>'
   ```
4. Confirm creation with resource name and contact card.
