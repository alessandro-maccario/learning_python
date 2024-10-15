# --- IMPORT PACKAGES --- #
import tkinter as tk
import secrets  # https://docs.python.org/3/library/secrets.html
import string  # https://docs.python.org/3/library/string.html#string.ascii_lowercase
# import clipboard


class GeneratePassword:
    def __init__(self, password_input_component: str) -> None:
        self.password_input_component = password_input_component
        self.generate_password()

    # --- Password generator function --- #
    def generate_password(self) -> None:
        """
        It uses the string module to get the letters and digits thath make up
        the alphabet used to generate the random characters. These
        characters are appended to the pwd string which is then assigned
        to the session_state variable [pw].

        Parameter
        ---------
        None

        Returns
        -------

        """
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet_special_chars = letters + digits + special_chars
        pwd_length = 14  # you can change it with your own decision
        pwd = ""  # empty string to start with

        for _ in range(pwd_length):
            pwd += "".join(secrets.choice(alphabet_special_chars))

        return pwd

    def fill_password_entry(self):
        """Generate a new password and"""
        # Generate a new password
        button_generated_password = self.generate_password()

        # Set the new password in the password input component
        self.password_input_component.delete(0, tk.END)  # Clear any previous text
        self.password_input_component.insert(
            0, button_generated_password
        )  # Insert the new password
