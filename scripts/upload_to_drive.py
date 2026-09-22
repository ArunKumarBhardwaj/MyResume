#!/usr/bin/env python3
"""Upload the rendered resume PDF to Google Drive.

Updates GOOGLE_DRIVE_FILE_ID in place when set (keeping the shareable link
stable), otherwise creates the file in GOOGLE_DRIVE_FOLDER_ID and makes it
publicly readable.

Usage: python3 scripts/upload_to_drive.py [pdf_path]
Defaults: rendercv_output/Arun_Kumar_Bhardwaj_CV.pdf
"""

import json
import os
import sys
from pathlib import Path

from google.oauth2 import service_account  # type: ignore[import-not-found]
from googleapiclient.discovery import build  # type: ignore[import-not-found]
from googleapiclient.errors import HttpError  # type: ignore[import-not-found]
from googleapiclient.http import MediaFileUpload  # type: ignore[import-not-found]

DEFAULT_PDF = "rendercv_output/Arun_Kumar_Bhardwaj_CV.pdf"
SCOPES = ["https://www.googleapis.com/auth/drive"]


def main() -> int:
    pdf = Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PDF)
    if not pdf.exists():
        print(f"❌ PDF not found: {pdf}")
        return 1

    creds_dict = json.loads(os.environ["GOOGLE_DRIVE_CREDENTIALS"])

    # Print service account email for debugging
    service_email = creds_dict.get("client_email", "unknown")
    print(f"🔑 Using service account: {service_email}")

    credentials = service_account.Credentials.from_service_account_info(
        creds_dict, scopes=SCOPES
    )
    service = build("drive", "v3", credentials=credentials)

    file_id = os.environ.get("GOOGLE_DRIVE_FILE_ID")
    folder_id = os.environ.get("GOOGLE_DRIVE_FOLDER_ID")
    media = MediaFileUpload(str(pdf), mimetype="application/pdf", resumable=True)

    try:
        if file_id:
            # UPDATE existing file (keeps same link!)
            service.files().update(fileId=file_id, media_body=media).execute()
            print(f"✅ Updated existing file: https://drive.google.com/file/d/{file_id}/view")
        else:
            # CREATE new file (first time only)
            file = service.files().create(
                body={"name": pdf.name, "parents": [folder_id]},
                media_body=media,
                fields="id",
            ).execute()
            new_file_id = file.get("id")

            # Make it publicly accessible
            service.permissions().create(
                fileId=new_file_id, body={"type": "anyone", "role": "reader"}
            ).execute()

            print("✅ Created new file! Add this FILE_ID to GitHub secrets:")
            print(f"   {new_file_id}")
            print(f"📎 Shareable link: https://drive.google.com/file/d/{new_file_id}/view")
    except HttpError as e:
        if e.resp.status == 404:
            print(f"❌ ERROR: File not found (ID: {file_id})")
            print()
            print("🔧 FIX: Share the file with your service account:")
            print("   1. Go to Google Drive")
            print(f"   2. Right-click on {pdf.name} → Share")
            print(f"   3. Add: {service_email}")
            print("   4. Give 'Editor' permission")
            print("   5. Re-run this workflow")
            return 1
        raise

    return 0


if __name__ == "__main__":
    sys.exit(main())
