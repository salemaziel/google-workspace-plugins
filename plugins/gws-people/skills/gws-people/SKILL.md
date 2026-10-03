---
name: gws-people
description: "Google People & Contacts management: profiles, contact groups, vCard exports, and CRM synchronization via gws CLI."
metadata:
  version: 0.22.5
  category: "productivity"
  requires:
    bins:
      - gws
---

# gws-people — Google People & Contacts CLI Integration

Search, inspect, update, and export contacts and contact groups through the `gws` CLI.

## Quick Workflow
1. **Query Contacts**: List connections with mandatory `personFields` parameter.
2. **Export / Transform**: Convert raw contacts JSON into CSV or vCard format using `contact_vcard_exporter.py`.
3. **Mutate**: Create new contacts or update existing contact details using `updatePersonFields`.

## Core Commands

```bash
# List contacts with profile fields and pipe to table view
gws people people connections list \
  --params '{"resourceName": "people/me", "personFields": "names,emailAddresses,phoneNumbers,organizations"}' \
  | ./scripts/contact_vcard_exporter.py

# Export contacts to standard CSV
gws people people connections list \
  --params '{"resourceName": "people/me", "personFields": "names,emailAddresses,phoneNumbers,organizations"}' \
  | ./scripts/contact_vcard_exporter.py --format csv > contacts.csv

# Create a new contact
gws people people createContact \
  --json "$(cat templates/contact-card.json)"

# Search contacts (after warmup)
gws people people searchContacts \
  --params '{"query": "Alex", "readMask": "names,emailAddresses,organizations"}'
```

## Safety & Best Practices
- **Mandatory `personFields`**: Almost all GET and LIST operations require `personFields`. Omitting it triggers a `400 Bad Request`.
- **Warmup Query**: Execute an empty query warmup before searching contacts to populate API caches.

## Progressive Disclosure & References
- **Person Fields & Masks**: Read [references/person-fields.md](references/person-fields.md) for field definitions and update masks.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for 400 personFields errors, search caching, and 409 group conflicts.
- **Contact Exporter Script**: Use [scripts/contact_vcard_exporter.py](scripts/contact_vcard_exporter.py) to export connections to vCard (.vcf) or CSV.
- **Templates**: See [templates/contact-card.json](templates/contact-card.json) and [templates/crm-sync-record.json](templates/crm-sync-record.json).
