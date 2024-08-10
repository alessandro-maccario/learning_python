"""
Helper file to store the main functionalities to be used in the app.py for the Blackjack Capstone Project.
"""

# --- IMPORT PACKAGES --- #
import os
from random import sample

# CONSTANTS
DEALER_WINS = "##### DEALER WINS, PLAYER GOT BUSTED! #####"
PLAYER_WINS = "##### PLAYER WINS, DEALER GOT BUSTED! #####"
RESTART_APPLICATION = "Another game? Insert 'y' to start a new game, insert 'n' to close the application: "
HIT_OR_STAY = "HIT or STAY? Insert 'y' or 's': "
DRAW = "##### DRAW ##### \n Restarting the game..."
CHEERS = "Thanks for playing with us! Come back soon!"


def append_new_card(original_card_list: list, player_list: list) -> list:
    """Append a new card to the user list (player, dealer)

    Parameters
    ----------
    original_card_list : list
        List of possible cards to be drawn
    player_list : list
        List of cards of the player, where the player could be the player or the dealer

    Returns
    -------
    list
        Player's list with an additional card
    """
    player_list.append(sample(original_card_list, 1)[0])
    # append one card from the original deck to the card_list
    return player_list


def reset_card_list() -> tuple[list, list]:
    """Return a tuple of the two empty lists for the player and the dealer.

    Returns
    -------
    tuple[list, list]
        Return the tuple of the two empty lists for the player and the dealer.
    """
    dealer_cards = list()
    user_cards = list()

    return dealer_cards, user_cards


def player_lose(sum_user_cards: int) -> str:
    """The sum value of the player's card is over 21, therefore they lose.

    Parameters
    ----------
    sum_user_cards : int
        The sum value of the player's cards.

    Returns
    -------
    str
        Decision of the user if continue with the game or not.
    """
    print("The sum of your cards is: ", sum_user_cards)
    print(DEALER_WINS)
    decision = input(RESTART_APPLICATION)

    return decision


def stop_game(number_of_player_wins: int, number_of_games: int) -> str:
    """If the user stops the game, the number of winning games over the number of games,
    and a cheer message is returned.

    Parameters
    ----------
    number_of_player_wins : int
        Number of wins for the player
    number_of_games : int
        Number of games played until the game stops

    Returns
    -------
    str
        A cheerful message
    """
    print(
        "Number of player's wins:",
        number_of_player_wins,
        "over",
        number_of_games,
    )
    return CHEERS


def clear_screen():
    """
    The line  os.system('cls' if os.name == 'nt' else 'clear') empties the terminal screen
    at the beginning of every iteration by running cls if you're using a Windows machine and
    clear if you're using a Unix based one.
    """
    os.system("cls" if os.name == "nt" else "clear")
