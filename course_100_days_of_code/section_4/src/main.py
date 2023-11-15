"""
    This Section 4 is dedicated to the project game "Rock, Paper, Scissor".

    References:
    World Rock-Paper-Scissor Association:
        - https://wrpsa.com/

    Rules:
        - rock BEATS scissors
        - paper BEATS rock
        - scissor BEATS paper
"""

# import packages
import random
from ..utils.constants import *


# build the main logic
def main():
    # if-else statement for checking the random value
    if random.randint(0, 2) == scissor:
        print("scissor")
    elif random.randint(0, 2) == paper:
        print("paper")
    else:
        print("rock")
