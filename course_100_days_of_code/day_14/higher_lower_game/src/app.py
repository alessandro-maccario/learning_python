"""
This script will create a simple High Lower Guessing game in Python for the 100 Days of Code challenge from the Udemy course.

Reference:
- https://www.higherlowergame.com/
"""

# --- IMPORT PACKAGES --- #
import os
import sys
from random import shuffle

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.ascii_art import main_logo
from data.data import data
from pkgs.game_logic import (
    compare_number_followers,
    print_comparison,
    end_game_comment,
    input_decision,
)

# --- MAIN CODE --- #
print(main_logo)

# --- VARIABLES --- #
score = 0
previous_option = None


def main():
    global previous_option, score  # get the variable from the global scope

    # shuffle in place
    shuffle(data)
    data_iterator = iter(data)  # Create an iterator for the shuffled data

    while True:
        if previous_option is None:
            comparison_a = next(data_iterator)
        else:
            comparison_a = previous_option
            previous_option = None

        try:
            comparison_b = next(
                data_iterator
            )  # get the next element for the comparison with comparison_a
        except StopIteration:
            # print statement if the user is above or below score
            end_game_comment(score)
            break

        # print the comparison between the first and the second element
        print_comparison(comparison_a, comparison_b)

        # let the player decides which one between A and B is correct
        decision = input_decision()

        print()

        # if compare_number_followers is None, then give previous_option score a
        # None value
        try:
            previous_option, score = compare_number_followers(
                decision,
                comparison_a,
                comparison_b,
                score,
                previous_option,
            )
        except TypeError:
            previous_option = None

        if previous_option is None:
            break


if __name__ == "__main__":
    main()
    # print statement if the user is above or below score
    end_game_comment(score)
