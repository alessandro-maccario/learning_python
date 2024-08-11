"""
Refactor the helper code
"""

# --- IMPORT PACKAGES --- #
import os
from random import sample


# CONSTANTS
HIT_OR_STAY = (
    "HIT, STAY or CLOSE the game? Insert 'y' (HIT), 's' (STAY) or 'n' (CLOSE): "
)


def draw_initial_cards(deck):
    return sample(deck, 2)


def draw_card(deck, cards: list) -> list:
    """Draw another card from the deck and add it to the other's dealer/player cards.

    Parameters
    ----------
    deck : list
        The original deck of cards
    cards : list
        Draw and append a new card from the deck to the dealer's/player's hand

    Returns
    -------
    list
        The new list of cards available either for the dealer or the user.
    """
    return cards.append(sample(deck, 1)[0])


def calculate_total_cards(cards: list) -> int:
    """Sum the values inside the card list.

    Parameters
    ----------
    cards : list
        List of cards from the dealer/player

    Returns
    -------
    int
        Return the total amount of the values inside the list of the dealer/player cards.
    """
    return sum(cards)


def winning_dealer():
    print("DEALER WINS!\n")
    print("~~~~~~~~~~~~~~~~~~~~~")


def losing_dealer():
    print("DEALER GOT BUSTED!\n")
    print("~~~~~~~~~~~~~~~~~~~~~")


def clear_screen():
    """
    The line  os.system('cls' if os.name == 'nt' else 'clear') empties the terminal screen
    at the beginning of every iteration by running cls if you're using a Windows machine and
    clear if you're using a Unix based one.
    """
    os.system("cls" if os.name == "nt" else "clear")
