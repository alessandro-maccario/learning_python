"""
Script to store the helper functions.
"""

# --- Import packages --- #
import os

# CONSTANTS
VALID_CHOICES = ("yes", "no")


def clear_screen():
    """
    The line  os.system('cls' if os.name == 'nt' else 'clear') empties the terminal screen
    at the beginning of every iteration by running cls if you're using a Windows machine and
    clear if you're using a Unix based one.
    """
    os.system("cls" if os.name == "nt" else "clear")


def ask_name():
    """Ask for the bidder's name.

    Returns
    -------
    str
        The name of the bidder.
    """
    return str(input("Please, insert your name:\n"))


def ask_bid():
    """Ask for the bidder's bid.

    Returns
    -------
    str
        The bidder's bid.
    """
    while True:
        try:
            return float(input("Please, insert your bid:\n"))
        except TypeError:
            print("Please, provide a valid input!")


def ask_more_bidders():
    """Ask if there are more bidders to take into account.

    Returns
    -------
    str
        Yes or no, if there are other bidders left for the Secret Auction.
    """
    while True:
        decision = str(input("Are there any other bidders? Type 'yes' or 'no'.\n"))
        if decision in VALID_CHOICES:
            if decision == "yes":
                return decision
            else:
                return decision
        else:
            print("Please, provide a valid input, either 'yes' or 'no'.")


def highest_bidder(bid_dictionary: dict) -> tuple:
    """Return the highest bidder's name and bid.

    Parameters
    ----------
    bid_dictionary : dict
        Bid dictionary containing all the bidders and the amount bid.

    Returns
    -------
    tuple
        Bidder's name and bidder's bid.
    """
    # Sort the dictionary:
    # sort and get the first value
    highest_bidder = list(
        sorted(bid_dictionary.items(), key=lambda x: x[1], reverse=True)
    )[0]
    # get the bidder's highest paying name
    highest_bidder_name = highest_bidder[0]
    # get the bidder's highest paying bid
    highest_bidder_bid = highest_bidder[1]

    return highest_bidder_name, highest_bidder_bid
