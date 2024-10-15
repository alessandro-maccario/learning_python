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

    def check_input_validity(self) -> tuple[str, str, str]:
        """Check the input validity"""
        website = self.website_input_component.get()
        email_username = self.email_username_input_component.get()
        password = self.password_input_component.get()

        # TODO: add a validation checker to see if the entered email contains a @
        # TODO: check this Stack: https://stackoverflow.com/questions/23718229/tkinter-entry-validation-check-for-a-valid-color-or-portion-of-a-color
        # TODO: https://stackoverflow.com/questions/4140437/interactively-validating-entry-widget-content-in-tkinter
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

        # BUG: need to move the ask confirmation right after the check_input_validity!

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
