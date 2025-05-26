# Exact Steps to Create Google OAuth Credentials for Windmill (Web Console)

## 🎯 Prerequisites (Already Complete)
- ✅ Project: `sodium-lodge-414521` ("My First Project")
- ✅ APIs Enabled: Calendar, Drive, Sheets
- ✅ Ready for OAuth setup

## Step 1: Configure OAuth Consent Screen

### 1.1 Navigate to OAuth Consent Screen
**Direct Link:** https://console.cloud.google.com/apis/credentials/consent?project=sodium-lodge-414521

### 1.2 Select User Type
- **Click:** "External" (unless you have Google Workspace)
- **Click:** "Create" button

### 1.3 Fill App Information
**App Information Tab:**
- **App name:** `Windmill OAuth App` (or your preferred name)
- **User support email:** Select `alephdao@gmail.com` from dropdown
- **App logo:** (Optional - skip for now)
- **App domain:** (Optional - skip for now)
- **Authorized domains:** (Leave empty for now)
- **Developer contact information:** `alephdao@gmail.com`
- **Click:** "Save and Continue"

### 1.4 Add Scopes
**Scopes Tab:**
- **Click:** "Add or Remove Scopes"
- **Search and select these scopes:**
  - `https://www.googleapis.com/auth/calendar` (Google Calendar API)
  - `https://www.googleapis.com/auth/drive` (Google Drive API)  
  - `https://www.googleapis.com/auth/spreadsheets` (Google Sheets API)
- **Click:** "Update"
- **Click:** "Save and Continue"

### 1.5 Test Users (Optional)
**Test Users Tab:**
- **Add your email:** `alephdao@gmail.com` (click "Add Users")
- **Click:** "Save and Continue"

### 1.6 Summary
**Summary Tab:**
- **Review information**
- **Click:** "Back to Dashboard"

## Step 2: Create OAuth Client ID

### 2.1 Navigate to Credentials
**Direct Link:** https://console.cloud.google.com/apis/credentials?project=sodium-lodge-414521

### 2.2 Create Credentials
- **Click:** "Create Credentials" (blue button at top)
- **Select:** "OAuth client ID"

### 2.3 Configure OAuth Client
**Application type:** Select "Web application"

**Name:** `Windmill Web Client`

**Authorized JavaScript origins:** (Leave empty)

**Authorized redirect URIs:**
- **Click:** "Add URI"
- **Enter:** `https://app.windmill.dev/oauth/callback`
- *(Add additional URIs if you have custom Windmill instances)*

### 2.4 Create Client
- **Click:** "Create"

### 2.5 Save Credentials
**Modal will appear with:**
- **Client ID:** `1234567890-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com`
- **Client Secret:** `GOCSPX-abcdefghijklmnopqrstuvwxyz1234567890`

**IMPORTANT:** 
- **Copy both values immediately**
- **Click:** "Download JSON" (optional backup)
- **Click:** "OK"

## Step 3: Configure Windmill Resource

### 3.1 In Windmill App
**Navigate to:** Resources → Add Resource

### 3.2 Resource Configuration
**Resource Type:** `gcal` (Google Calendar OAuth)

**Configuration:**
- **Client ID:** `[paste the Client ID from Step 2.5]`
- **Client Secret:** `[paste the Client Secret from Step 2.5]`
- **Scopes:** `calendar drive spreadsheets`

### 3.3 Test Connection
- **Click:** "Save"
- **Test the OAuth flow by creating a simple script**

## Step 4: Verification & Testing

### 4.1 Test Calendar Access
```javascript
// In Windmill, create a script with gcal resource
import { Resource } from "windmill-client";

export async function main(gcal: Resource<"gcal">) {
  const response = await fetch(
    "https://www.googleapis.com/calendar/v3/users/me/calendarList",
    {
      headers: {
        Authorization: `Bearer ${gcal.token}`,
      },
    }
  );
  return await response.json();
}
```

### 4.2 Test Drive Access
```javascript
// Test Google Drive
export async function main(gcal: Resource<"gcal">) {
  const response = await fetch(
    "https://www.googleapis.com/drive/v3/files",
    {
      headers: {
        Authorization: `Bearer ${gcal.token}`,
      },
    }
  );
  return await response.json();
}
```

## 🔐 Security Notes

### Important Reminders:
- **Keep Client Secret secure** - never commit to version control
- **Limit redirect URIs** to only necessary domains
- **Monitor usage** in Google Cloud Console
- **Rotate credentials** periodically

### OAuth Consent Screen Status:
- **Testing mode:** App limited to test users you specify
- **Production mode:** Requires Google verification for public use
- **For personal/internal use:** Testing mode is sufficient

## 📋 Final Checklist

- [ ] OAuth consent screen configured
- [ ] Required scopes added (calendar, drive, spreadsheets)
- [ ] OAuth client ID created
- [ ] Client ID and Secret copied
- [ ] Windmill resource configured
- [ ] Connection tested successfully

## 🎯 Expected Results

**After completion, you'll have:**
- Working OAuth integration with Google Calendar, Drive, and Sheets
- Ability to read/write calendars, access drive files, and manipulate spreadsheets
- Full API access through Windmill scripts

**Your OAuth credentials will work for:**
- ✅ Google Calendar API
- ✅ Google Drive API (includes Google Docs)
- ✅ Google Sheets API

---

**Project:** `sodium-lodge-414521` ("My First Project")  
**Status:** Ready for web console setup  
**Estimated Time:** 10-15 minutes
