import sys
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import (
    USER_ID,
    TOKEN_JSON,
    CLIENTID_JSON,
    SCOPES,
    PATH_SAVE_DATA_JSON,
    PATH_SAVE_DATA_JSON_CLEAN,
)
from pkgs.email_fetching import EmailFetching
from pkgs.json_cleaning import JSONCleaner


def connect_and_fetch():
    """Shows basic usage of the Gmail API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN_JSON):
        creds = Credentials.from_authorized_user_file(TOKEN_JSON, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENTID_JSON, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_JSON, "w") as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        gmail_fetching = EmailFetching()
        gmail_fetching.fetch_emails_with_subject(
            creds,
            user_id=USER_ID,
            sender="alessandro.maccario@proton.me",
            num_results=1,  # sender="linkedin.com"
        )

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


def read_and_clean():
    """Read the JSON if exists, clean it and save it back again to JSON"""
    try:
        # read the JSON if exists, clean it and save it back again
        json_cleaner = JSONCleaner()
        json_cleaner.json_cleaning(PATH_SAVE_DATA_JSON, PATH_SAVE_DATA_JSON_CLEAN)

    except FileNotFoundError:
        print("READ AND CLEAN FUNCTION: JSON file does not exists.")


if __name__ == "__main__":
    connect_and_fetch()
    read_and_clean()
