# --- IMPORT PACKAGES --- #
import os
import sys
import json
import base64
import pandas as pd
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import PATH_SAVE_DATA_JSON


class EmailFetching:
    def __init__(self) -> None:
        pass

    # NOTE: user_id should be a constant
    # NOTE: SUBJECT should be a field that is available for editing to the user
    # NOTE: if you would build an interface. The num_results as well.
    def fetch_emails_with_subject(self, creds, user_id, sender, num_results=10):
        try:
            # Build the Gmail service
            service = build("gmail", "v1", credentials=creds)

            # Search for messages with a specific subject
            query = f"from:{sender}"
            results = (
                service.users()
                .messages()
                .list(
                    userId=user_id, q=query, labelIds=["INBOX"], maxResults=num_results
                )
            ).execute()

            messages = results.get("messages", [])

            if not messages:
                print("No messages found with the specified subject.")
                return

            print(f"Emails with sender '{sender}':")
            for message in messages:
                # Get the message details
                msg = (
                    service.users()
                    .messages()
                    .get(userId=user_id, id=message["id"])
                    .execute()
                )

                # Extract the Date header from the email's headers
                headers = msg["payload"]["headers"]
                # in which date the message has been received?
                date_received = next(
                    (header["value"] for header in headers if header["name"] == "Date"),
                    "Date not found",
                )
                # who is the sender?
                received_from = next(
                    (header["value"] for header in headers if header["name"] == "From"),
                    "Date not found",
                )
                print("SENDER IS:", received_from, "ON", date_received)

                # Extracting the full message content
                parts = msg.get("payload").get("parts")
                email_body = ""

                if parts:
                    for part in parts:
                        mime_type = part["mimeType"]

                        # Check if it's text/plain or text/html
                        if mime_type in ["text/plain", "text/html"]:
                            data = part["body"].get("data")
                            if data:
                                decoded_data = base64.urlsafe_b64decode(data).decode(
                                    "latin-1"
                                )

                                # If it's HTML, optionally parse it to text
                                if mime_type == "text/html":
                                    # Convert HTML to readable text using BeautifulSoup
                                    soup = BeautifulSoup(decoded_data, "html.parser")
                                    # Extract only the text content
                                    decoded_data = soup.get_text(separator="\n").strip()

                                email_body += (
                                    decoded_data  # Append with newline for readability
                                )
                else:
                    # If no parts, sometimes the body is directly in the payload
                    body_data = msg.get("payload").get("body").get("data")
                    if body_data:
                        email_body = base64.urlsafe_b64decode(body_data)

                # save the data to json
                self.save_to_json(self.convert_to_dict(sender, email_body))

        except HttpError as error:
            print(f"An error occurred: {error}")

    def convert_to_dict(self, sender, message) -> pd.DataFrame:
        d = {"sender": [sender], "message": [message]}
        return d

    def save_to_json(self, sender_message: dict) -> None:
        # Define the file path for the JSON file
        file_path = PATH_SAVE_DATA_JSON

        # If the file exists, load its current content
        if os.path.isfile(file_path):
            with open(file_path, "r") as file:
                # Load existing data
                data = json.load(file)
        else:
            # Start with an empty list if file doesn't exist
            data = []

        # Append the new data to the existing list
        data.append(sender_message)

        # Save the updated data back to the JSON file
        with open(file_path, "w") as file:
            json.dump(
                data,
                file,
                indent=4,
            )
