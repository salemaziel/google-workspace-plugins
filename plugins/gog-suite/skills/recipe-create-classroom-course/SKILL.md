---
name: recipe-create-classroom-course
description: "Create a Google Classroom course and invite students using either gog or gws CLI."
metadata:
  version: 1.2.0
  openclaw:
    category: "recipe"
    domain: "education"
    requires:
      any_bin_of:
        - gog
        - gws
allowed-tools: Bash(gog:*|gws:*) Read
---

# Create a Google Classroom Course

Create a Google Classroom course and invite students using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Create a Classroom course
gog classroom courses create \
  --name "Introduction to CS" \
  --section "Period 1" \
  --room "Room 101" \
  --json

# 2. Invite student to course
gog classroom invitations create \
  --course <COURSE_ID> \
  --user "student@school.edu" \
  --role STUDENT \
  --json

# 3. List active roster
gog classroom roster <COURSE_ID> --json
```

### Option B: Using `gws` CLI
```bash
# 1. Create course via Discovery API
gws classroom courses create \
  --json '{"name": "Introduction to CS", "section": "Period 1", "room": "Room 101", "ownerId": "me"}'

# 2. Invite student
gws classroom invitations create \
  --json '{"courseId": "<COURSE_ID>", "userId": "student@school.edu", "role": "STUDENT"}'

# 3. List students
gws classroom courses students list --params '{"courseId": "<COURSE_ID>"}' --format table
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/roster_validator.py](scripts/roster_validator.py)
