---
name: auth-guide
description: "Interactive setup and troubleshooting guide for Google Workspace CLI authentication"
---

Step-by-step setup guide for OAuth2 client credentials and Service Account authorization.

## Usage
- `/auth-guide`

## Workflow
1. Locate `auth_setup_guide.py`:
   ```bash
   SCRIPT_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}/scripts"
   python3 "$SCRIPT_ROOT/auth_setup_guide.py"
   ```
2. Interactive walkthrough:
   - Creating Google Cloud project and enabling APIs.
   - Configuring OAuth consent screen.
   - Downloading client secret JSON or Service Account key.
   - Initializing `gws auth login`.
