# Google Cloud OAuth Setup for Windmill

## Overview
This guide documents how to set up Google Cloud CLI and enable full access to Google Calendar, Google Docs, and Google Sheets for use with OAuth-based applications like Windmill.

## What Was Done

### 1. Project Selection
```bash
# Switch to the target Google Cloud project
gcloud config set project sodium-lodge-414521
```

**Result:** Selected "My First Project" (Project ID: `sodium-lodge-414521`, Project Number: `436761378427`)

### 2. Enable Required APIs
```bash
# Enable Google Calendar, Drive, and Sheets APIs
gcloud services enable calendar-json.googleapis.com drive.googleapis.com sheets.googleapis.com
```

**APIs Enabled:**
- ✅ Google Calendar API (`calendar-json.googleapis.com`)
- ✅ Google Drive API (`drive.googleapis.com`) 
- ✅ Google Sheets API (`sheets.googleapis.com`)

### 3. Verify Setup
```bash
# Confirm project details
gcloud projects describe sodium-lodge-414521

# Verify enabled APIs
gcloud services list --enabled --filter="name:(calendar OR drive OR sheets)"
```

## Current Status

### ✅ Completed
- Google Cloud project configured
- All required APIs enabled
- Project ready for OAuth credential creation

### 🔧 Next Steps Required

#### 1. OAuth Consent Screen Setup
**URL:** https://console.cloud.google.com/apis/credentials/consent?project=sodium-lodge-414521

**Steps:**
- Select "External" user type
- Fill in app information:
  - App name
  - User support email
  - Developer contact information
- Add required scopes

#### 2. Create OAuth Client ID
**URL:** https://console.cloud.google.com/apis/credentials?project=sodium-lodge-414521

**Steps:**
- Click "Create Credentials" → "OAuth client ID"
- Select "Web application" 
- Add authorized redirect URI (your Windmill callback URL)
- Note the generated Client ID and Client Secret

## Required OAuth Scopes

For full access to Google Workspace services:

```
https://www.googleapis.com/auth/calendar      # Google Calendar
https://www.googleapis.com/auth/drive         # Google Drive/Docs  
https://www.googleapis.com/auth/spreadsheets  # Google Sheets
```

## Windmill Configuration

Once you have the OAuth credentials:

**Resource Type:** Google OAuth (gcal)

**Configuration:**
- **Client ID:** `[from OAuth client ID creation]`
- **Client Secret:** `[from OAuth client ID creation]` 
- **Scopes:** `calendar,drive,spreadsheets`

## Testing Access (Optional)

To test API access with your personal Google account:

```bash
# Authenticate with full scopes
gcloud auth login --scopes='https://www.googleapis.com/auth/calendar,https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/spreadsheets'

# Test Calendar API access
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  "https://www.googleapis.com/calendar/v3/users/me/calendarList"
```

## Important Notes

- **Current Token Limitation:** The default `gcloud auth print-access-token` only provides cloud-platform scopes, not Google Workspace scopes
- **Security:** Keep Client Secret secure and never commit to version control
- **Scopes:** Use the minimum required scopes for your application needs
- **Testing:** OAuth credentials created from the same Google account you want to access avoid "unverified app" warnings

## Summary

The Google Cloud infrastructure is now ready for OAuth integration. The main remaining task is creating OAuth credentials through the Google Cloud Console web interface, which cannot be automated via CLI for security reasons.

**Project:** `sodium-lodge-414521` ("My First Project")  
**Status:** ✅ Ready for OAuth credential creation  
**APIs:** ✅ Calendar, Drive, Sheets enabled
