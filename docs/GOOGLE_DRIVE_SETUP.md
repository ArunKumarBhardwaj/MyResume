# Resume Generation & Google Drive Upload Workflow

This workflow generates the resume PDF and uploads it to Google Drive, ensuring the **file link remains the same** for portfolio use.

On push to `main` (when `Arun_Kumar_Bhardwaj_CV.yaml` changes) or via manual `workflow_dispatch`, GitHub Actions:

1. Renders the PDF with RenderCV
2. Uploads/overwrites a fixed Google Drive file (stable shareable link)
3. Commits `rendercv_output/` back to the repo
4. Uploads a `resume-pdf` artifact

## Prerequisites

### 1. Create a Google Cloud Project & Service Account

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use existing)
3. Enable the **Google Drive API**:

   - Go to `APIs & Services` → `Enable APIs and Services`
   - Search for "Google Drive API" and enable it

4. Create a Service Account:

   - Go to `APIs & Services` → `Credentials`
   - Click `Create Credentials` → `Service Account`
   - Give it a name like `resume-uploader`
   - Click `Create and Continue` → `Done`

5. Create a Service Account Key:
   - Click on the service account you just created
   - Go to `Keys` tab → `Add Key` → `Create new key`
   - Choose JSON format
   - Download the JSON file (keep it safe!)

### 2. Create a Folder in Google Drive

1. Go to [Google Drive](https://drive.google.com/)
2. Create a folder called `Resume` (or any name you prefer)
3. Right-click the folder → `Share`
4. Share with the service account email (looks like: `resume-uploader@your-project.iam.gserviceaccount.com`)
5. Give **Editor** permission
6. Copy the folder ID from the URL: `https://drive.google.com/drive/folders/YOUR_FOLDER_ID`

### 3. Initial Upload (One-time Setup)

Upload your resume PDF (`Arun_Kumar_Bhardwaj_CV.pdf`) manually to the folder first, then:

1. Right-click the file → `Get Link` → `Anyone with the link`
2. Copy the file ID from the URL: `https://drive.google.com/file/d/YOUR_FILE_ID/view`
3. Save this file ID - **this is what keeps the link permanent!**

Alternatively, leave `GOOGLE_DRIVE_FILE_ID` unset on the first workflow run; the script will create the file in the folder, set anyone/reader access, and print the new `FILE_ID` in the Actions log. Add that ID to secrets afterward.

### 4. Add GitHub Secrets

Go to your GitHub repository → `Settings` → `Secrets and variables` → `Actions`:

| Secret Name                | Value                                |
| -------------------------- | ------------------------------------ |
| `GOOGLE_DRIVE_CREDENTIALS` | Entire contents of the JSON key file |
| `GOOGLE_DRIVE_FILE_ID`     | The file ID from step 3              |
| `GOOGLE_DRIVE_FOLDER_ID`   | The folder ID from step 2            |

Repo: [ArunKumarBhardwaj/MyResume](https://github.com/ArunKumarBhardwaj/MyResume)

---

## How it works

The workflow lives at [`.github/workflows/generate-and-upload-resume.yml`](../.github/workflows/generate-and-upload-resume.yml). Upload logic is in [`scripts/upload_to_drive.py`](../scripts/upload_to_drive.py):

- If `GOOGLE_DRIVE_FILE_ID` is set → **update in place** (same shareable link)
- Else → **create** in `GOOGLE_DRIVE_FOLDER_ID`, set anyone/reader, print the new file ID

Default PDF path: `rendercv_output/Arun_Kumar_Bhardwaj_CV.pdf`

---

## Your Permanent Resume Links

Once set up, your resume will always be available at:

| Format       | URL                                                           |
| ------------ | ------------------------------------------------------------- |
| **View**     | `https://drive.google.com/file/d/YOUR_FILE_ID/view`           |
| **Download** | `https://drive.google.com/uc?export=download&id=YOUR_FILE_ID` |
| **Embed**    | `https://drive.google.com/file/d/YOUR_FILE_ID/preview`        |

> **Tip:** Use the **View** link in your portfolio / README (replace `YOUR_FILE_ID` after secrets are set).

---

## Manual Trigger

To manually regenerate and upload:

1. Go to your repo → `Actions` tab
2. Select **Generate & Upload Resume PDF** workflow
3. Click `Run workflow`

---

## Troubleshooting

| Issue             | Solution                                                                 |
| ----------------- | ------------------------------------------------------------------------ |
| Permission denied | Ensure service account has **Editor** access to the folder (and file)    |
| File not found    | Double-check `GOOGLE_DRIVE_FILE_ID`; share the file with the SA email    |
| API not enabled   | Enable Google Drive API in Cloud Console                                 |
| PDF not found     | Confirm `rendercv render Arun_Kumar_Bhardwaj_CV.yaml` succeeded         |
