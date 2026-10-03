# Security & Access Audit Report

**Audited Domain**: {{DOMAIN}}  
**Time Window**: {{START_TIME}} to {{END_TIME}}  
**Auditor**: {{AUDITOR}}  

---

## 1. Executive Summary
Overview of organizational activity, authentication failures, and permission escalations during the audited timeframe.

## 2. Authentication Anomalies
- **Failed Logins**: {{FAILED_LOGIN_COUNT}}
- **Suspicious IP Geolocation Alerts**: {{SUSPICIOUS_LOGIN_COUNT}}

## 3. Privilege Escalations
- **Role Assignments**: {{ADMIN_ASSIGNMENTS}}
- **Service Settings Changes**: {{SETTING_CHANGES}}

## 4. Drive External Data Exposure
- **Files Shared Outside Domain**: {{EXTERNAL_SHARE_COUNT}}
- **Public Link Shares**: {{PUBLIC_LINK_COUNT}}

## 5. Remediation Actions
1. Revoke unauthorized third-party OAuth app tokens.
2. Enforce 2-Step Verification for flagged accounts.
