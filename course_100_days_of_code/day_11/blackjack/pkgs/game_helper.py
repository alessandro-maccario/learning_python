# --- IMPORT PACKAGES --- #
import os
import sys
from copy import deepcopy

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.helper import (
    draw_initial_cards,
    calculate_total_cards,
    draw_card,
    winning_dealer,
    losing_dealer,
    HIT_OR_STAY,
)


# --- CONSTANTS --- #
DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
BLACKJACK = 21

# --- GLOBAL VARIABLES --- #
number_of_player_wins = 0
number_of_games = 0


def play_game() -> str:
    """Main function to start playing the game.

    Returns
    -------
    str
        Return a string either for closing the game or continuing the game.
    """
    # give two cards to the dealer and to the player
    dealer_cards = draw_initial_cards(DECK)
    player_cards = draw_initial_cards(DECK)

    sum_dealer_card, sum_player_card = play_hand(
        dealer_cards, player_cards, hide_dealer_card=True
    )

    if sum_player_card == BLACKJACK:
        print("##### PLAYER WINS WITH A BLACKJACK, DEALER GOT BUSTED! #####\n")
        print(f"PLAYER WINS WITH A HAND OF: {player_cards} = {sum_player_card}")
        return "player_wins"
    elif sum_dealer_card == BLACKJACK:
        print("##### DEALER WINS WITH A BLACKJACK, PLAYER GOT BUSTED! #####\n")
        print(f"DEALER WINS WITH A HAND OF: {dealer_cards} = {sum_dealer_card}")
        return "dealer_wins"

    player_outcome = player_turn(dealer_cards, player_cards)
    if player_outcome == "stay":
        return dealer_turn(dealer_cards, player_cards)
    elif player_outcome == "n":
        return "n"
    elif player_outcome == "player_wins":
        return "player_wins"
    elif player_outcome == "dealer_wins":
        return "dealer_wins"


def play_hand(
    dealer_cards: list, player_cards: list, hide_dealer_card=False
) -> tuple[int, int]:
    """Play one hand and get the total value of the hand of the dealer and the player.

    Parameters
    ----------
    dealer_cards : list
        List of cards of the dealer
    player_cards : list
        List of cards of the player
    hide_dealer_card : bool, optional
        Boolean to check if the dealer's deck cards have to be shown fully or not, by default False

    Returns
    -------
    tuple[int, int]
        Return the total value of the dealer's and the player's hands.
    """
    dealer_display = deepcopy(dealer_cards)

    # calculate the total amount given by the list of cards for the dealer and the player
    total_dealer_cards = calculate_total_cards(dealer_cards)
    total_player_cards = calculate_total_cards(player_cards)

    # if True, then use the dealer_display to display and calculate the
    if hide_dealer_card:  # if TRUE
        dealer_display[0] = "*"
        print(f"Dealer's cards: {dealer_display} = {dealer_display[1]}")
        print(f"User's cards: {player_cards} = {total_player_cards}\n")
    else:
        print(f"Dealer's cards: {dealer_display} = {total_dealer_cards}")
        print(f"User's cards: {player_cards} = {total_player_cards}\n")

    return total_dealer_cards, total_player_cards


def get_player_outcome(total_player_cards):
    outcomes = {21: "player_wins"}

    # if the total_player_cards value is == 21 then the player wins
    if total_player_cards in outcomes:
        return outcomes[total_player_cards]
    # if the total_player_cards value is > 21 then the player loses and the dealer wins
    elif total_player_cards > 21:
        return "dealer_wins"
    # otherwise, we continue asking the user what they want to do
    else:
        return "continue"


def player_turn(dealer_cards: list, player_cards: list) -> str:
    """Player's turn.

    Parameters
    ----------
    dealer_cards : list
        List of cards of the dealer.
    player_cards : list
        List of cards of the player.

    Returns
    -------
    str
        Return either who won or the decision to 'stay' or to 'close' the game.
    """
    while True:
        # HIT or STAY
        decision = input(HIT_OR_STAY)
        if decision == "y":
            # add a new card to the player's hand
            draw_card(DECK, player_cards)
            # check if the total is =/>/< 21
            total_dealer_cards, total_player_cards = play_hand(
                dealer_cards, player_cards, hide_dealer_card=True
            )

            outcome = get_player_outcome(total_player_cards)

            if outcome == "player_wins":
                print("PLAYER WINS!\n")
                print("~~~~~~~~~~~~~~~~~~~~~")
                return "player_wins"
            elif outcome == "dealer_wins":
                print("PLAYER GOT BUSTED!\n")
                print("~~~~~~~~~~~~~~~~~~~~~")
                return "dealer_wins"
            elif outcome == "continue":
                continue

        elif decision == "n":
            return "n"
        elif decision == "s":
            return "stay"


def dealer_turn(dealer_cards: list, player_cards: list) -> str:
    """Dealer's turn.

    Parameters
    ----------
    dealer_cards : list
        List of cards of the dealer.
    player_cards : list
        List of cards of the player.

    Returns
    -------
    str
        Return either who won.
    """
    while True:
        # add a new card to the dealer's hand
        draw_card(DECK, dealer_cards)
        total_dealer_cards, total_player_cards = play_hand(
            dealer_cards, player_cards, hide_dealer_card=False
        )

        # if total_dealer_cards < 17 then the dealer MUST draw another card
        if total_dealer_cards < 17:
            continue
        elif total_dealer_cards > 21:
            losing_dealer()
            return "player_wins"
        elif total_dealer_cards == 21:
            winning_dealer()
            return "dealer_wins"
        elif total_dealer_cards < 21 and total_dealer_cards > total_player_cards:
            winning_dealer()
            return "dealer_wins"
        elif total_dealer_cards == 21:
            winning_dealer()
            return "dealer_wins"
