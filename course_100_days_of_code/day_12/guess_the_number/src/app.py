"""
This script will create a simple Guess the Number game in Python for the 100 Days of Code challenge from the Udemy course.
"""

# --- IMPORT PACKAGES --- #
import os
import sys
from random import randint

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.ascii_art import logo
from pkgs.helper import (
    input_difficulty_level,
    easy_level,
    hard_level,
)
from pkgs.game_logic import game_logic

# --- MAIN CODE --- #
print(logo)

wrong_guessing = {"too_low": "TOO LOW", "too_high": "TOO HIGH"}


if __name__ == "__main__":
    # create a random number to be guessed by the player
    number_to_guess = randint(1, 100)
    # ask the player for the difficulty level that they want to play
    player_difficulty_level = input_difficulty_level()

    # EASY LEVEL
    if player_difficulty_level == "easy":
        print("Number of attempts available: ", easy_level)
        while True:
            game_logic(easy_level, number_to_guess, wrong_guessing)
            break

    # HARD LEVEL
    elif player_difficulty_level == "hard":
        print("Number of attempts available: ", easy_level)
        while True:
            game_logic(hard_level, number_to_guess, wrong_guessing)
            break
