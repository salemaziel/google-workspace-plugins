---
name: create-classroom
description: "Create a Google Classroom course and invite students or instructors"
---

Provision a Google Classroom course.

## Usage
- `/create-classroom "<courseName>"`
- `/create-classroom "<courseName>" --section "<sectionName>" --owner "<ownerId>"`

## Workflow
1. Parse course name, section, and owner ID.
2. Create course via `gws`:
   ```bash
   gws classroom courses create --json "{\"name\": \"<courseName>\", \"section\": \"${SECTION:-Main}\", \"ownerId\": \"${OWNER:-me}\"}"
   ```
3. Return Course ID, enrollment code, and course link.
