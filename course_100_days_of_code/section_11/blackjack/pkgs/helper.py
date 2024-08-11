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
    return cards.append(sample(deck, 1)[0])


def calculate_total_cards(cards):
    return sum(cards)


def clear_screen():
    """
    The line  os.system('cls' if os.name == 'nt' else 'clear') empties the terminal screen
    at the beginning of every iteration by running cls if you're using a Windows machine and
    clear if you're using a Unix based one.
    """
    os.system("cls" if os.name == "nt" else "clear")
