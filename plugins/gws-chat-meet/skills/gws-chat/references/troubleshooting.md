# Google Chat & Meet Troubleshooting Guide

Common error conditions and resolutions when operating Chat and Meet with `gws`.

## 1. Space Not Found (`404 NOT_FOUND`)
- **Cause**: The space ID (format `spaces/AAAAAAAAAAA`) does not exist, or the authenticated account has not been added as a member.
- **Resolution**:
  - Run `gws chat spaces list` to retrieve all spaces the authenticated account belongs to.
  - Group chats and direct messages do not appear in `spaces list` until at least one message has been sent.

## 2. Organization Policy Restriction (`403 Forbidden`)
- **Cause**: External guest joining is blocked by Google Workspace organizational administrator policy, or Chat Apps are restricted.
- **Resolution**:
  - Verify that the calling account is within the organization domain.
  - Check with Workspace Admin for chat space external permissions.

## 3. Meet Transcript or Recording Access Denied
- **Cause**: Querying `gws meet conferenceRecords transcripts` before the recording/transcript has finalized processing.
- **Resolution**:
  - Google Meet transcripts may take 5–15 minutes post-meeting to finalize in Drive and become queryable via API.
