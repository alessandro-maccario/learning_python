import tkinter as tk
from tkinter import messagebox
import json
import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import SAVE_PATH


class Add2CSV:
    def __init__(
        self,
        website_input_component: str,
        email_username_input_component: str,
        password_input_component: str,
    ) -> None:
        self.website_input_component = website_input_component
        self.email_username_input_component = email_username_input_component
        self.password_input_component = password_input_component

    def check_input_validity(self) -> tuple[str, str, str]:
        """Check the input validity"""
        website = self.website_input_component.get()
        email_username = self.email_username_input_component.get()
        password = self.password_input_component.get()

        if not website:
            messagebox.showerror("Invalid Input", "Please, insert website!")
            return
        elif not email_username:
            messagebox.showerror("Invalid Input", "Please, insert email/username!")
            return
        elif not password:
            messagebox.showerror("Invalid Input", "Please, insert password!")
            return
        else:
            return website, email_username, password

    def clear_entries(self):
        """Clear the entries to be able to insert new ones"""
        self.website_input_component.delete(0, tk.END)  # Clear website field
        self.email_username_input_component.delete(0, tk.END)  # Clear email field
        self.password_input_component.delete(0, tk.END)  # Clear password field

    def save2csv(self):
        """Save the input to the csv"""

        # if something has been inserted in website, email/username and password AND the confirmation is true
        if self.check_input_validity():
            # ask the user if they are sure that they want to save this data
            ask_user_confirmation = messagebox.askyesno(
                title="Saving confirmation", message="Do you want to save the data?"
            )
            if ask_user_confirmation:
                website, email_username, password = self.check_input_validity()

                # append to csv
                with open(
                    "day_29/password_manager/data/passwords.csv", "a"
                ) as pass_csv:
                    pass_csv.write(f"\n{website}, {email_username}, {password}")

                self.clear_entries()
                messagebox.showinfo("Saved", "Saved successfully!")
        else:
            pass

    def save2json(self):
        """Save the input to the json"""

        # if something has been inserted in website, email/username and password AND the confirmation is true
        if self.check_input_validity():
            # ask the user if they are sure that they want to save this data
            ask_user_confirmation = messagebox.askyesno(
                title="Saving confirmation", message="Do you want to save the data?"
            )
            if ask_user_confirmation:
                website, email_username, password = self.check_input_validity()

                # TODO: recheck the code to be sure to understand it
                # Check if the file exists and is not empty: ensures that json.load() is only called if the file has content.
                """Appending the JSON: Instead of appending directly using mode="a", you should open the file in write mode (mode="w") and overwrite it with the updated JSON. JSON needs to be written as a whole object, not appended line-by-line like in plain text files."""
                if not os.path.isfile(SAVE_PATH) or os.stat(SAVE_PATH).st_size == 0:
                    feeds = []

                else:
                    with open(SAVE_PATH, "r") as feedsjson:
                        feeds = json.load(feedsjson)  # Load existing data

                # Data to be written
                dictionary = {
                    "Website": website,
                    "Email/Username": email_username,
                    "Password": password,
                }

                # Append new entry to the feeds list
                feeds.append(dictionary)

                # Write the updated list back to the file
                with open(SAVE_PATH, mode="w") as f:
                    json.dump(feeds, f, indent=4)  # dump, not dumps, to write to a file

                self.clear_entries()
                messagebox.showinfo("Saved", "Saved successfully!")
        else:
            pass
