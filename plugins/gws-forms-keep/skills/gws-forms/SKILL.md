---
name: gws-forms
description: "Google Forms creation, question batchUpdate, and response analytics with gws CLI."
metadata:
  version: 0.22.5
  category: "productivity"
  requires:
    bins:
      - gws
---

# gws-forms — Google Forms CLI Integration

Create Google Forms surveys, manage question items with `batchUpdate`, and analyze respondent feedback through the `gws` CLI.

## Quick Workflow
1. **Create Shell**: Initialize empty form via `gws forms forms create` with title only.
2. **Add Questions**: Append questions and choice options using `forms.batchUpdate`.
3. **Analyze**: Query submissions with `forms.responses.list` and pipe into `form_response_analyzer.py`.

## Core Commands

```bash
# 1. Create a new form container
gws forms forms create --json '{"info": {"title": "Team Survey", "documentTitle": "Team Survey"}}'

# 2. Add question items via batchUpdate
gws forms forms batchUpdate \
  --params '{"formId": "<formId>"}' \
  --json '{
    "requests": [{
      "createItem": {
        "item": {
          "title": "Rate the workshop",
          "questionItem": {
            "question": {
              "required": true,
              "choiceQuestion": {"type": "RADIO", "options": [{"value": "5 - Excellent"}, {"value": "4 - Good"}]}
            }
          }
        },
        "location": {"index": 0}
      }
    }]
  }'

# 3. Analyze form responses with summary report
gws forms forms responses list --params '{"formId": "<formId>"}' | ./scripts/form_response_analyzer.py
```

## Progressive Disclosure & References
- **Form Items Schema**: Read [references/form-items-schema.md](references/form-items-schema.md) for 2-step creation rules and choice/text question structures.
- **Troubleshooting**: See [references/troubleshooting.md](references/troubleshooting.md) for create payload restrictions and Google Keep enterprise domain access.
- **Response Analyzer**: Use [scripts/form_response_analyzer.py](scripts/form_response_analyzer.py) to aggregate submission metrics.
- **Templates**: See [templates/feedback-form-spec.json](templates/feedback-form-spec.json) and [templates/keep-checklist.json](templates/keep-checklist.json).
