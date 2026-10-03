---
name: collect-responses
description: "Retrieve and summarize submitted responses from a Google Form"
---

Query submitted responses and compile a structured summary.

## Usage
- `/collect-responses <formId>`

## Workflow
1. Parse form ID from arguments.
2. Query responses via `gws`:
   ```bash
   gws forms forms responses list --params '{"formId": "<formId>"}' --format json
   ```
3. Calculate:
   - Total number of responses
   - Submission timestamps
   - Frequency breakdown of multiple choice answers
   - Key highlights from open-text answers
4. Format output into an executive summary table.
