# Google Forms & Keep Troubleshooting Guide

Common error conditions and resolutions when operating Forms and Keep with `gws`.

## 1. Disallowed Fields on `forms.create` (`400 Bad Request`)
- **Cause**: Trying to pass `description`, `items`, or `settings` in the `forms.create` payload.
- **Resolution**:
  - `forms.create` ONLY accepts `info.title` and `info.documentTitle`.
  - All questions, sections, and descriptions must be added in a subsequent `forms.batchUpdate` request.

## 2. Google Keep API Domain Access
- **Cause**: Google Keep API returns `403 Forbidden: Method not allowed for consumer accounts`.
- **Resolution**:
  - The Google Keep REST API is restricted by Google to Google Workspace Enterprise, Education, or Business organization accounts. Personal `@gmail.com` accounts cannot use the Keep REST API.

## 3. Form Response Anonymity / Missing Email
- **Cause**: `respondentEmail` is blank in `forms.responses.list`.
- **Resolution**:
  - Form must have email collection enabled via `publish_settings` or form settings.
