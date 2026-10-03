# Google Workflows Troubleshooting Guide

Common error conditions and resolutions when operating cross-service workflows with `gws`.

## 1. Multiple Service Scope Failures
- **Cause**: A workflow crossing Calendar, Gmail, Drive, and Tasks fails halfway through due to missing permissions on one service.
- **Resolution**:
  - Run `gws doctor` or `auth_setup_guide.py` to check permission coverage across all required services before launching composite workflows.

## 2. Empty Intermediate Payloads
- **Cause**: Calendar event has no attendees or no attached document links.
- **Resolution**:
  - Defensive fallback: render "No attached docs" rather than failing the entire pipeline.
