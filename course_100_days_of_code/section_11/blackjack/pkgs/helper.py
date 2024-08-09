"""
Helper file to store the main functionalities to be used in the app.py for the Blackjack Capstone Project.
"""

# --- IMPORT PACKAGES --- #
import os
from random import sample


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


def clear_screen():
    """
    The line  os.system('cls' if os.name == 'nt' else 'clear') empties the terminal screen
    at the beginning of every iteration by running cls if you're using a Windows machine and
    clear if you're using a Unix based one.
    """
    os.system("cls" if os.name == "nt" else "clear")
