"""
This script will create a simple Secret Auction Program for the 100 Days of Code challenge from the Udemy course.
"""

# --- Import packages --- #
import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.ascii_art import logo
from pkgs.helper import (
    clear_screen,
    ask_name,
    ask_bid,
    ask_more_bidders,
    highest_bidder,
)


# --- MAIN FUNCTION --- #
def main():
    # print the logo secret bid auction
    print(logo)

    print("Welcome to the Secret Bid Auction.")

    # create a dictionary to store all the bids: bidder's name and the amount that has been bid
    bids = {}

    while True:
        # ask for the bidder's name
        name = ask_name()
        # ask for the bidder's bid amount
        bid = ask_bid()

        # update the dictionary based on the bid
        bids.update({name: bid})

        # are there any more bidders?
        decision = ask_more_bidders()

        if decision == "yes":
            clear_screen()
            continue
        else:
            highest_bidder_name, highest_bidder_bid = highest_bidder(bids)

            print(
                f"The highest bidder was {highest_bidder_name} with an amount of {highest_bidder_bid}."
            )
            print("Thank you for your participation.")
            return


if __name__ == "__main__":
    main()
