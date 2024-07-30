"""
Script to store the helper functions.
"""

# --- Import packages --- #
import os


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
