import tkinter as tk
from tkinter import messagebox


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

    # TODO: create another method to actually save the data to a csv
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

    def save2csv(self):
        """Save the input to the csv"""

        if (
            self.check_input_validity()
        ):  # if something has been inserted in website, email/username and password
            website, email_username, password = self.check_input_validity()

            # append to csv
            with open("day_29/password_manager/data/passwords.csv", "a") as pass_csv:
                pass_csv.write(website + "," + email_username + "," + password)
