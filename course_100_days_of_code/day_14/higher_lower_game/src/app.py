"""
This script will create a simple High Lower Guessing game in Python for the 100 Days of Code challenge from the Udemy course.

Reference:
- https://www.higherlowergame.com/
"""

# --- IMPORT PACKAGES --- #
import os
import sys
from random import choice
from copy import deepcopy

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.ascii_art import main_logo, vs_logo
from data.data import data
from pkgs.game_logic import compare_number_followers, print_comparison

# --- VARIABLES --- #
count_correct_answer = 0
previous_option = None


# --- MAIN CODE --- #
print(main_logo)


original_data = deepcopy(data)
already_seen = []

while True:
    if previous_option is None:
        # COMPARISON A
        # randomly choose the first element
        comparison_a = choice(data)
        # get the corresponding index. Needed to avoid picking the same element twice
        idx_comparison_a = original_data.index(comparison_a)

        # COMPARISON B
        # do not pick the same element as comparison_a for comparison_b
        # data = [x for x in data if data.index(x) != idx_comparison_a]
        already_seen.append(data.pop(idx_comparison_a))

        # randomly choose the second element
        comparison_b = choice(data)
        # get the corresponding index. Needed to avoid picking the same element twice.
        # # Need to get the index from the original list
        # idx_comparison_b = original_data.index(comparison_b)

        # print the comparison between the first and the second element
        print_comparison(comparison_a, comparison_b)

        # let the player decides which one between A and B is correct
        decision = input("Who has more followers? Type 'A' or 'B': ")
        print()

        # if compare_number_followers is None, then give previous_option count_correct_answer a
        # None value
        try:
            previous_option, count_correct_answer = compare_number_followers(
                decision,
                comparison_a,
                comparison_b,
                count_correct_answer,
                previous_option,
            )
        except TypeError:
            previous_option = None

        if previous_option is not None:
            continue
        else:
            break
    else:
        # if we are not in the first turn, comparison_a will be the previous
        comparison_a = previous_option

        # COMPARISON B
        # do not pick the same element as comparison_a for comparison_b
        # data = [x for x in data if data.index(previous_option) != idx_comparison_a]

        previous_option = None
        # randomly choose the second element
        comparison_b = None
        comparison_b = choice(data)
        # # get the corresponding index. Needed to avoid picking the same element twice
        idx_comparison_b = data.index(comparison_b)
        already_seen.append(data.pop(idx_comparison_b))

        # print the comparison between the first and the second element
        print_comparison(comparison_a, comparison_b)

        # let the player decides which one between A and B is correct
        decision = input("Who has more followers? Type 'A' or 'B': ")
        print()

        # if compare_number_followers is None, then give previous_option count_correct_answer a
        # None value
        try:
            previous_option, count_correct_answer = compare_number_followers(
                decision,
                comparison_a,
                comparison_b,
                count_correct_answer,
                previous_option,
            )
        except TypeError:
            previous_option = None
        if previous_option is not None:
            continue
        else:
            break


if count_correct_answer < 3:
    print(f"Too bad, try again! Highest score: {count_correct_answer}")
else:
    print(
        f"Above the average of 3 correct answer! Good job! Highest score: {count_correct_answer}"
    )
