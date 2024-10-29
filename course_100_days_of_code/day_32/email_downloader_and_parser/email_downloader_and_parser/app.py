import os.path
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import USER_ID, TOKEN_JSON, CLIENTID_JSON, SCOPES
from pkgs.email_fetching import EmailFetching


def main():
    """Shows basic usage of the Gmail API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # TODO: the path should be moved to constants
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
            creds, user_id=USER_ID, subject="LinkedIn", num_results=10
        )

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
