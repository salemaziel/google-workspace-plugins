# Google People API `personFields` & UpdateMask Reference

Understanding mandatory parameters and field schemas for Google People API v1 via `gws people`.

## Mandatory `personFields` Parameter
The People API requires `personFields` in almost all GET and LIST operations:
```bash
gws people people get \
  --params '{"resourceName": "people/me", "personFields": "names,emailAddresses,phoneNumbers,organizations"}'
```

### Supported Person Fields
- `names`: Display name, family name, given name, prefixes.
- `emailAddresses`: Email strings and labels (work, home, other).
- `phoneNumbers`: Phone numbers and labels.
- `organizations`: Job title, company name, department.
- `biographies`: Notes and descriptions.
- `userDefined`: Custom key-value pairs.
- `memberships`: Contact group memberships (`contactGroupMembership`).

## Updating Contacts with `updatePersonFields`
When modifying an existing contact with `gws people people updateContact`:
1. Retrieve the contact first to acquire the current `etag`.
2. Supply `updatePersonFields` to indicate which specific fields should be overwritten:
```bash
gws people people updateContact \
  --params '{"resourceName": "people/c12345", "updatePersonFields": "names,emailAddresses"}' \
  --json '{
    "etag": "<currentEtag>",
    "names": [{"givenName": "Jane", "familyName": "Doe"}],
    "emailAddresses": [{"value": "jane.doe@example.com", "type": "work"}]
  }'
```
