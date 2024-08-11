"""
This script will create a simple Blackjack game in Python for the 100 Days of Code challenge from the Udemy course.
"""

# --- IMPORT PACKAGES --- #
import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.game_helper import play_game, number_of_player_wins, number_of_games
from pkgs.ascii_art import logo


if __name__ == "__main__":
    print(logo)
    while True:
        turn_outcome = play_game()
        if turn_outcome == "dealer_wins":
            number_of_games += 1
        elif turn_outcome == "player_wins":
            number_of_player_wins += 1
            number_of_games += 1
        elif turn_outcome == "n":
            try:
                total_winning = round(number_of_player_wins / number_of_games, 2) * 100
            except ZeroDivisionError:
                print("No games were played, no winning to record.")
                print("Thanks for playing with us! \nClosing the application...")
                break
            print(
                f"Results:\n\tNumber of winning games for the PLAYER: {number_of_player_wins}\n\tTotal number of game played: {number_of_games}. \nPercentage of winning games {total_winning}%\n"
            )
            print("Thanks for playing with us! \nClosing the application...")
            break
