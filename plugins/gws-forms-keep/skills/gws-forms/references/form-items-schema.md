# Google Forms Items & BatchUpdate Schema Reference

Google Forms API v1 requires a 2-step provisioning workflow:
1. `forms.create`: Allocates the form resource and assigns the title.
2. `forms.batchUpdate`: Adds questions, descriptions, page breaks, and validation rules.

## Step 1: Create Form Shell
```bash
gws forms forms create --json '{
  "info": {
    "title": "Customer Onboarding Survey",
    "documentTitle": "Customer Onboarding Survey"
  }
}'
```
Captures the generated `formId`.

## Step 2: BatchUpdate Questions
```bash
gws forms forms batchUpdate \
  --params '{"formId": "<formId>"}' \
  --json '{
    "requests": [
      {
        "createItem": {
          "item": {
            "title": "How satisfied are you with our platform?",
            "questionItem": {
              "question": {
                "required": true,
                "choiceQuestion": {
                  "type": "RADIO",
                  "options": [
                    {"value": "Very Satisfied"},
                    {"value": "Satisfied"},
                    {"value": "Neutral"},
                    {"value": "Unsatisfied"}
                  ]
                }
              }
            }
          },
          "location": {"index": 0}
        }
      },
      {
        "createItem": {
          "item": {
            "title": "What feature should we prioritize next?",
            "questionItem": {
              "question": {
                "required": false,
                "textQuestion": {
                  "paragraph": true
                }
              }
            }
          },
          "location": {"index": 1}
        }
      }
    ]
  }'
```
