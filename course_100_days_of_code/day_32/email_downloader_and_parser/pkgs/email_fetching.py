# --- IMPORT PACKAGES --- #
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class EmailFetching:
    def __init__(self) -> None:
        pass

    # NOTE: user_id should be a constant
    # NOTE: SUBJECT should be a field that is available for editing to the user
    # NOTE: if you would build an interface. The num_results as well.
    def fetch_emails_with_subject(self, creds, user_id, subject, num_results=10):
        try:
            # Build the Gmail service
            service = build("gmail", "v1", credentials=creds)

            # Search for messages with a specific subject
            query = f"subject:{subject}"
            results = (
                service.users()
                .messages()
                .list(userId=user_id, q=query, maxResults=num_results)
                .execute()
            )

            messages = results.get("messages", [])

            if not messages:
                print("No messages found with the specified subject.")
                return

            print(f"Emails with subject '{subject}':")
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

                # Print the date and a snippet of the message
                print(f"\nDate received: {date_received}")
                print(f"Message snippet: {msg['snippet']}\n")

        except HttpError as error:
            print(f"An error occurred: {error}")
