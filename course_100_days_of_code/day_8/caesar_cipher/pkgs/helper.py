"""
Script to store the helper functions.
"""

# --- Import packages --- #
import os

# CONSTANTS
VALID_CHOICES = ("encode", "decode")
STOP_CONDITION = "stop"


def clear_screen():
    """
    The line  os.system('cls' if os.name == 'nt' else 'clear') empties the terminal screen
    at the beginning of every iteration by running cls if you're using a Windows machine and
    clear if you're using a Unix based one.
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_message():
    """Prompts the user for a message."""
    return input("Type your message:\n").lower()


def get_shift():
    """Prompts the user for a shift number and validates it."""
    while True:
        try:
            return int(input("Type the shift number:\n"))
        except ValueError:
            print("Please, insert a valid integer value.")


def ask_continue():
    """Asks the user if they want to continue or stop."""
    while True:
        decision = input(
            "Do you want to continue? Type 'yes' to continue or 'stop' to stop the application.\n"
        ).lower()
        if decision in ("yes", STOP_CONDITION):
            # once the decision is made between "yes" or "stop", the function terminates,
            # therefore the while loop is terminated.
            return decision
        print("Invalid input. Please type 'yes' or 'stop'.")


def get_user_action():
    """Prompts the user for an action (encode, decode, stop)."""
    while True:
        action = input(
            "Type 'encode' to encrypt the message, 'decode' to decrypt the message, or 'stop' to close the application.\n"
        ).lower()
        if action in VALID_CHOICES or action == STOP_CONDITION:
            return action
        print("Invalid input. Please type 'encode', 'decode', or 'stop'.")
