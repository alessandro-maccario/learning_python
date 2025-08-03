import os
import datetime

USER_ID = "me"
TOKEN_JSON = "day_32/email_downloader_and_parser/tokens/token.json"
CLIENTID_JSON = "day_32/email_downloader_and_parser/tokens/clientID.json"
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
# PATH_SAVE_DATA_CSV = "day_32/email_downloader_and_parser/data/test_gmail.csv"
PATH_SAVE_DATA_JSON = (
    "day_32/email_downloader_and_parser/data/linkedin_gmail_email.json"
)
PATH_SAVE_DATA_JSON_CLEAN = f"day_32/email_downloader_and_parser/data/linkedin_gmail_clean_links_{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}.json"

INFO_TO_BE_REMOVED_FROM_JSON = [
    "Help",
    "LinkedIn",
    "Unsubscribe",
    "Learn why we included this.",
    "Get it on Google Play",
    "Download on the App Store",
    "Get it from Microsoft",
    "Premium icon",
    "Alessandro Maccario",
    "Premium",
    "Proton Mail",
]
