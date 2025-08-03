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
from pkgs.config import *


# build the main logic
def main():
    player_point = 0  # points for the player (you)
    machine_point = 0  # points for the machine

    # PLAYER MOVE
    # ask the player which input wants to insert
    player_input = input("Enter rock, paper or scissor: ").lower()

    if player_input == "scissor":
        player_move = scissor
    elif player_input == "paper":
        player_move = paper
    elif player_input == "rock":
        player_move = rock
    else:
        print("Please, enter a valid choice")

    # show the move to the user
    print(f"You chose {player_input}")

    # MACHINE MOVE
    machine_input = random.randint(0, 2)

    # if-else statement for checking the random value
    if machine_input == scissor:
        print("The machine chose scissor")
    elif machine_input == paper:
        print("The machine chose paper")
    elif machine_input == rock:
        print("The machine chose rock")
    else:
        print("Please, enter a valid choice")

    if player_move > machine_input:
        player_point += 1
        print("You won this match! Congrats!")
    else:
        machine_point += 1
        print("The machine won this match, try again!")


if __name__ == "__main__":
    main()
