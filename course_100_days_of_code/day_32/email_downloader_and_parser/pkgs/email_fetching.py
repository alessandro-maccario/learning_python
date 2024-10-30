# --- IMPORT PACKAGES --- #
import re
import os
import sys
import json
import base64
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import PATH_SAVE_DATA_CSV, PATH_SAVE_DATA_JSON


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
            # print("RESULT IS:", results)

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
                # print("\nMESSAGE IS:\n", msg)

                # Extract the Date header from the email's headers
                headers = msg["payload"]["headers"]
                date_received = next(
                    (header["value"] for header in headers if header["name"] == "Date"),
                    "Date not found",
                )

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
                                    "utf-8"
                                )
                                email_body += (
                                    decoded_data + "\n\n"
                                )  # Append with newline for readability
                        ################################
                        # save the data to csv
                        self.save_to_csv(self.convert_to_dict(sender, email_body))
                        self.save_to_json(
                            self.convert_to_dict(
                                sender, self.clean_message_body(email_body)
                            )
                        )
                        ################################
                else:
                    # If no parts, sometimes the body is directly in the payload
                    body_data = msg.get("payload").get("body").get("data")
                    if body_data:
                        email_body = base64.urlsafe_b64decode(body_data).decode("utf-8")

                    ################################
                    # save the data to csv
                    self.save_to_csv(self.convert_to_dict(sender, email_body))
                    self.save_to_json(
                        self.convert_to_dict(
                            sender, self.clean_message_body(email_body)
                        )
                    )
                    ################################

                # Print the full email content
                # print(f"\nFull email content:\n{email_body}")

                # Print the date and a snippet of the message
                print(f"\nDate received: {date_received}")
                print(f"Message snippet: {msg['snippet']}\n")

        except HttpError as error:
            print(f"An error occurred: {error}")

    def convert_to_dict(self, sender, message) -> pd.DataFrame:
        d = {"sender": [sender], "message": [message]}
        return d

    def save_to_csv(self, sender_message: dict) -> pd.DataFrame:
        # Define file path
        file_path = PATH_SAVE_DATA_CSV

        # Check if file exists
        file_exists = os.path.isfile(file_path)

        # Create a DataFrame with the new word to append
        new_to_append = pd.DataFrame(data=sender_message)

        # If the file doesn't exist, write with header; if it does, append without header
        if not file_exists:
            new_to_append.to_csv(
                file_path, mode="w", header=["sender", "message"], index=False
            )
        else:
            new_to_append.to_csv(file_path, mode="a", header=False, index=False)

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

        # Clean the message body before saving
        # sender_message["message"] = self.clean_message_body(sender_message["message"])
        # Append the new data to the existing list
        data.append(sender_message)

        # Save the updated data back to the JSON file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def clean_message_body(self, message_body):
        # Remove newline/carriage return sequences
        message_body = re.sub(r"\r\n|\n|\r", " ", message_body)
        # Optionally, replace \u00a9 with an actual © symbol or remove it
        message_body = message_body.replace("\u00a9", "")
        return message_body
