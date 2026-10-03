---
name: drive-upload
description: "Upload local files to Google Drive with folder targeting and confirmation using gog CLI"
---

# /drive-upload — Upload Files to Google Drive

Upload local documents, archives, images, or datasets to Google Drive with target folder support.

## Usage
- `/drive-upload ./report.pdf` — Uploads file to root Drive.
- `/drive-upload ./data.csv --folder <folderId>` — Uploads file to a specific folder.
- `/drive-upload ./deck.pptx --title "Final Presentation"` — Uploads with a custom remote title.

## Execution Steps
1. Verify local file existence and check file size from `{{args}}`.
2. Confirm target destination with the user if uploading to a shared team folder.
3. Execute upload command:
   ```bash
   gog drive upload "<localPath>" [--folder "<folderId>"] [--title "<customTitle>"] --json
   ```
4. Output upload summary:
   - **File ID**: `1a2b3c...`
   - **Title**: `report.pdf`
   - **Direct URL**: `https://drive.google.com/file/d/1a2b3c.../view`
