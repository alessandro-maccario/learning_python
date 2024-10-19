import tkinter as tk
from tkinter import messagebox
import json
import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import SAVE_PATH


class FindData:
    def __init__(self, search_entry: str) -> None:
        self.search_entry = search_entry

    def find_password(self) -> None:
        """Search through the JSON to find the right entry"""
        website = self.search_entry.get()  # string
        try:
            with open(SAVE_PATH, "r") as feedsjson:
                # reading existing data
                feeds = json.load(feedsjson)
        except (ValueError, FileNotFoundError):
            # add a popup that says "Entry not found!"
            messagebox.showinfo(
                "Error",
                "No Data file found",
            )
        else:  # it will run if the try succeded
            if website in feeds:
                messagebox.showinfo(
                    f"{website}",
                    f"Email/Username:\n{feeds[website]["Email/Username"]} \n\nPassword:\n{feeds[website]["Password"]}",
                )
            else:
                messagebox.showinfo(
                    "Error",
                    f"No details for the {website} found",
                )
