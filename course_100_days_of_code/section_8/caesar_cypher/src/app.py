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
from pkgs.helper import clear_screen, get_message, get_shift


# --- Main Function --- #
def main():
    print("-------------------------")
    print(logo)

    # Constants
    stop = False
    VALID_CHOICES = ("encode", "decode")
    STOP_CONDITION = "stop"

    while stop is not True:
        # user's choice between encoding/decoding
        description = input(
            "Type 'encode' to encrypt the message, type 'decode' to decrypt the message. Type 'stop' to close the application.\n"
        )

        clear_screen()

        if description.lower() == STOP_CONDITION:
            print("Thanks for using the Caesar Cypher!")
            stop = True
            break
        elif description.lower() not in VALID_CHOICES:
            print(
                "Please, type 'encode' or 'decode'. If you want to stop the execution, type 'stop'."
            )
            continue
        else:
            print("-------------------------")
            text = get_message()  # message that you want to encode/decode
            shift = get_shift()  # integer for the number of shifts
            print("-------------------------")

            if description in VALID_CHOICES:
                print(caesar(description, text=text, shift=shift))

                waiting_user_decision = True
                while waiting_user_decision:
                    # continue or stop the application
                    user_decision = input(
                        "Do you want to continue? Type 'yes' to continue, type 'stop' to stop the application.\n"
                    )
                    if user_decision == "stop":
                        stop = True
                        waiting_user_decision = False
                        print("Thanks for using the Caesar Cypher!")
                        break
                    elif user_decision == "yes":
                        waiting_user_decision = False
                        break
                    print("------------")
                    print("Invalid input. Please type 'encode', 'decode', or 'stop'.\n")


if __name__ == "__main__":
    main()
