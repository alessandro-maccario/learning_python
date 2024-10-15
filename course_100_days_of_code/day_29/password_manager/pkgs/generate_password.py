# --- IMPORT PACKAGES --- #
import tkinter as tk
import secrets  # https://docs.python.org/3/library/secrets.html
import string  # https://docs.python.org/3/library/string.html#string.ascii_lowercase
import clipboard
from pkgs.constants import SPECIAL_CHARS


class GeneratePassword:
    def __init__(self) -> None:
        pass

    # --- Password generator function --- #
    def generate_password() -> None:
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
        alphabet = letters + digits
        special_chars = string.punctuation
        pwd_length = 14  # you can change it with your own decision
        pwd = ""  # empty string to start with

        for i in range(pwd_length):
            pwd += "".join(secrets.choice(alphabet))
