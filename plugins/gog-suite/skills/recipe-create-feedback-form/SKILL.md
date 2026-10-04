---
name: recipe-create-feedback-form
description: "Create a Google Form for feedback and share it via Gmail using either gog or gws CLI."
metadata:
  version: 1.2.0
  openclaw:
    category: "recipe"
    domain: "productivity"
    requires:
      any_bin_of:
        - gog
        - gws
allowed-tools: Bash(gog:*|gws:*) Read
---

# Create and Share a Google Form

Create a Google Form for feedback and share it via Gmail using either gog or gws CLI.

> [!TIP]
> This recipe is **CLI-agnostic**. Execute with either `gog` (idiomatic Unix) or `gws` (Google Discovery API).

## Execution Options

### Option A: Using `gog` CLI (Recommended)
```bash
# 1. Create a new Google Form
gog forms create --title "Customer Feedback Q1" --json

# 2. Add question to the form
gog forms add-question <FORM_ID> --title "Rate your satisfaction (1-5)" --json

# 3. Email the form respondent link
gog gmail send \
  --to "attendees@company.com" \
  --subject "Please share your feedback" \
  --body "Please take 2 minutes to complete our survey: <RESPONDER_URI>" \
  --json
```

### Option B: Using `gws` CLI
```bash
# 1. Create form
gws forms forms create \
  --json '{"info": {"title": "Customer Feedback Q1", "documentTitle": "Customer Feedback"}}'

# 2. Email form responder link
gws gmail +send \
  --to attendees@company.com \
  --subject "Please share your feedback" \
  --body "Please take 2 minutes to complete our survey: <RESPONDER_URI>" 
```

## Progressive Disclosure & Resources
- **Reference & Parameters**: [references/cli-mapping.md](references/cli-mapping.md)
- **Helper Script**: [scripts/form_question_scaffold.py](scripts/form_question_scaffold.py)
