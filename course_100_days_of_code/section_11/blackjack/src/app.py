"""
This script will create a simple Blackjack game in Python for the 100 Days of Code challenge from the Udemy course.
"""

# --- IMPORT PACKAGES --- #
import os
import sys
from copy import deepcopy
from random import sample

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.helper import (
    draw_card,
    reset_card_list,
    player_lose,
    clear_screen,
    stop_game,
    DEALER_WINS,
    PLAYER_WINS,
    RESTART_APPLICATION,
    HIT_OR_STAY,
    DRAW,
)

# possible card choices
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# reset the card lists
dealer_cards, user_cards = reset_card_list()
number_of_player_wins = 0
number_of_games = 0

while True:
    if len(dealer_cards) == 0:
        # simplified list of available cards
        # draw two cards for the dealer
        dealer_cards = sample(deck, 2)
        # draw two cards for the user
        user_cards = sample(deck, 2)

        sum_dealer_cards = sum(dealer_cards)
        sum_user_cards = sum(user_cards)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # make a copy of the dealer cards and sum up values using this list
        original_dealer_cards = deepcopy(dealer_cards)
        hide_dealer_cards = deepcopy(original_dealer_cards)
        # hide the first element of the dealer cards
        hide_dealer_cards[0] = "*"

        print(f"Dealer's cards: {hide_dealer_cards} = {dealer_cards[1]}")
        print(f"User's cards: {user_cards} = {sum_user_cards}")

        if sum_user_cards > 21:
            decision = player_lose(sum_user_cards)
            if decision == "y":
                number_of_games += 1
                clear_screen()
                # reset the card lists
                dealer_cards, user_cards = reset_card_list()
                continue
            else:
                stop_game(number_of_player_wins, number_of_games)
                break
        elif sum_user_cards < 21:
            decision_more_card = input(HIT_OR_STAY)
            if decision_more_card == "y":
                print("#############################")
                user_cards = draw_card(deck, user_cards)

                sum_dealer_cards = sum(dealer_cards)
                sum_user_cards = sum(user_cards)

                print(f"Dealer's cards: {hide_dealer_cards} = {dealer_cards[1]}")
                print(f"User's cards: {user_cards} = {sum_user_cards}")

                if sum_user_cards > 21:
                    decision = player_lose(sum_user_cards)
                    if decision == "y":
                        number_of_games += 1
                        clear_screen()
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        continue
                    else:
                        stop_game(number_of_player_wins, number_of_games)
                        break

            # the user chose to 'stay': the dealer will get more cards until
            # they win, draw or lose
            else:
                while True:
                    if sum_dealer_cards == 21:
                        print(DEALER_WINS)
                        print(f"Dealer's cards: {dealer_cards} = {sum_dealer_cards}")
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break
                    elif sum_user_cards == sum_dealer_cards:
                        print(DRAW)
                        print(f"Dealer's cards: {dealer_cards} = {sum_dealer_cards}")
                        number_of_games += 1
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break
                    elif (sum_dealer_cards > sum_user_cards) and sum_dealer_cards < 21:
                        print(DEALER_WINS)
                        print(f"Dealer's cards: {dealer_cards} = {sum_dealer_cards}")
                        number_of_games += 1
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break

                    dealer_cards = draw_card(deck, dealer_cards)
                    # sum the card numbers
                    sum_dealer_cards = sum(dealer_cards)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(f"Dealer's cards: {dealer_cards} = {sum_dealer_cards}")
                    print(f"User's cards: {user_cards} = {sum_user_cards}")

                    if sum_dealer_cards == 21:
                        print(DEALER_WINS)
                        print(f"Dealer's cards: {dealer_cards} = {sum_dealer_cards}")
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break
                    elif (sum_dealer_cards > 21) and (sum_user_cards < 21):
                        print(PLAYER_WINS)
                        number_of_player_wins += 1
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break

        elif (sum_user_cards == 21) and (sum_user_cards > sum_dealer_cards):
            print(PLAYER_WINS)
            number_of_player_wins += 1
            number_of_games += 1
            # reset the card lists
            dealer_cards, user_cards = reset_card_list()
            continue

    else:
        if sum_dealer_cards == 21:
            print(DEALER_WINS)
            # reset the card lists
            dealer_cards, user_cards = reset_card_list()
            continue
        elif (sum_dealer_cards > 21) and (sum_user_cards < 21):
            print(PLAYER_WINS)
            number_of_player_wins += 1
            decision = input(RESTART_APPLICATION)
            if decision == "y":
                number_of_games += 1
                clear_screen()
                # reset the card lists
                dealer_cards, user_cards = reset_card_list()
                continue
            else:
                number_of_games += 1
                stop_game(number_of_player_wins, number_of_games)
                break

        # user's card calculation
        if sum_user_cards == 21:
            print(PLAYER_WINS)
            number_of_player_wins += 1
            number_of_games += 1
            # reset the card lists
            dealer_cards, user_cards = reset_card_list()
            continue
        elif sum_user_cards > 21:
            decision = player_lose(sum_user_cards)
            if decision == "y":
                number_of_games += 1
                clear_screen()
                # reset the card lists
                dealer_cards, user_cards = reset_card_list()
                continue
            else:
                break
        elif sum_user_cards < 21:
            decision_more_card = input(HIT_OR_STAY)
            if decision_more_card == "y":
                print("#############################")
                user_cards = draw_card(deck, user_cards)

                # sum the card numbers
                sum_dealer_cards = sum(dealer_cards)
                sum_user_cards = sum(user_cards)

                print(f"Dealer's cards: {hide_dealer_cards} = {dealer_cards[1]}")
                print(f"User's cards: {user_cards} = {sum_user_cards}")

                if sum_user_cards == sum_dealer_cards:
                    print(DRAW)
                    print(f"Dealer's cards: {dealer_cards} = {sum_dealer_cards}")
                    number_of_games += 1
                    # reset the card lists
                    dealer_cards, user_cards = reset_card_list()
                    continue

                elif sum_user_cards > 21:
                    print(DEALER_WINS)
                    print(f"Dealer's cards: {dealer_cards} = {sum_dealer_cards}")
                    decision = input(RESTART_APPLICATION)
                    if decision == "y":
                        number_of_games += 1
                        clear_screen()
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        continue
                    else:
                        number_of_games += 1
                        stop_game(number_of_player_wins, number_of_games)
                        break
            # the user chose to 'stay': the dealer will get more cards until
            # they win, draw or lose
            else:
                while True:
                    if sum_dealer_cards == 21:
                        print(DEALER_WINS)
                        print(f"Dealer's cards: {dealer_cards} = {sum_dealer_cards}")
                        number_of_games += 1
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break
                    elif sum_user_cards == sum_dealer_cards:
                        print(DRAW)
                        print(f"Dealer's cards: {dealer_cards} = {sum_dealer_cards}")
                        number_of_games += 1
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break

                    dealer_cards = draw_card(deck, dealer_cards)
                    # sum the card numbers
                    sum_dealer_cards = sum(dealer_cards)

                    print(f"Dealer's cards: {dealer_cards} = {sum_dealer_cards}")
                    print(f"User's cards: {user_cards} = {sum_user_cards}")

                    if sum_dealer_cards == 21:
                        print(DEALER_WINS)
                        number_of_games += 1
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break
                    elif sum_dealer_cards > sum_user_cards:
                        print(DEALER_WINS)
                        number_of_games += 1
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break
                    elif (sum_dealer_cards > 21) and (sum_user_cards < 21):
                        print(PLAYER_WINS)
                        number_of_player_wins += 1
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break

        elif (sum_user_cards < 22) and (sum_user_cards > sum_dealer_cards):
            print(PLAYER_WINS)
            number_of_player_wins += 1
            number_of_games += 1
            # reset the card lists
            dealer_cards, user_cards = reset_card_list()
            continue

# TODO:
# Convert repeated code into functions
