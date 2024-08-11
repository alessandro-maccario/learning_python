"""
This script will encode a simple Caesar Cipher for the 100 Days of Code challenge from the Udemy course.
"""

# --- Import packages --- #
import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.encode_decode import caesar
from pkgs.ascii_art import logo
from pkgs.helper import (
    clear_screen,
    get_message,
    get_shift,
    VALID_CHOICES,
    STOP_CONDITION,
    ask_continue,
    get_user_action,
)


# --- Main Function --- #
def main():
    print("-------------------------")
    print(logo)

    # Constants
    stop = False

    while stop is not True:
        # user's choice between encoding/decoding
        description = get_user_action()
        clear_screen()

        if description == STOP_CONDITION:
            print("Thanks for using the Caesar Cipher!")
            break

        print("-------------------------")
        text = get_message()  # message that you want to encode/decode
        shift = get_shift()  # integer for the number of shifts
        print("-------------------------")

        if description in VALID_CHOICES:
            # function call for the caesar cipher
            print(caesar(description, text=text, shift=shift))

            if ask_continue() == STOP_CONDITION:
                print("Thanks for using the Caesar Cipher!")
                break


if __name__ == "__main__":
    main()
