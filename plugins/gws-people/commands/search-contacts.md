---
name: search-contacts
description: "Search Google Contacts and corporate domain directory by name, email, or company"
---

Search personal contacts and organizational directory.

## Usage
- `/search-contacts "<query>"`
- `/search-contacts "<query>" --directory`

## Workflow
1. Parse query string and optional `--directory` flag.
2. If `--directory` is requested:
   ```bash
   gws people people searchDirectoryPeople --params "{\"query\": \"<query>\", \"readMask\": \"names,emailAddresses,phoneNumbers,organizations\", \"sources\": [\"DIRECTORY_SOURCE_TYPE_DOMAIN_PROFILE\"]}" --format table
   ```
   Otherwise, search personal contacts:
   ```bash
   gws people people searchContacts --params "{\"query\": \"<query>\", \"readMask\": \"names,emailAddresses,phoneNumbers,organizations\"}" --format table
   ```
3. Display structured table of results:
   - Resource Name / ID
   - Full Name
   - Primary Email
   - Phone Number
   - Organization & Job Title
