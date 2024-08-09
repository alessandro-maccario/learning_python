"""
This script will create a simple Blackjack game in Python for the 100 Days of Code challenge from the Udemy course.
"""

# --- IMPORT PACKAGES --- #
import os
import sys
from random import sample

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.helper import append_new_card, reset_card_list, clear_screen

# possible card choices
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# reset the card lists
dealer_cards, user_cards = reset_card_list()


while True:
    if len(dealer_cards) == 0:
        # simplified list of available cards
        # draw two cards for the dealer
        dealer_cards = sample(cards, 2)
        # draw two cards for the user
        user_cards = sample(cards, 2)

        sum_dealer_cards = sum(dealer_cards)
        sum_user_cards = sum(user_cards)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Dealer's cards: ", dealer_cards, f"= {sum_dealer_cards}")
        print("User's cards: ", user_cards, f"= {sum_user_cards}")

        if sum_dealer_cards == 21:
            print("##### DEALER WINS, PLAYER BUSTED! #####")
            # reset the card lists
            dealer_cards, user_cards = reset_card_list()
            continue
        elif sum_user_cards == sum_dealer_cards:
            print("##### DRAW #####")
            print("Restarting the game...")
            # reset the card lists
            dealer_cards, user_cards = reset_card_list()
            continue

        # user's card calculation
        if sum_user_cards > 21:
            print("The sum of your cards is: ", sum_user_cards)
            print("##### BUSTED #####")
            decision = input(
                "Do you want to play another game? Insert 'y' to start a new game, insert 'n' to close the application."
            )
            if decision == "y":
                clear_screen()
                continue
            else:
                break
        elif sum_user_cards < 21:
            decision_more_card = input("HIT or STAY? Insert 'y' or 's': ")
            if decision_more_card == "y":
                print("#############################")
                # dealer_cards = append_new_card(cards, dealer_cards)
                user_cards = append_new_card(cards, user_cards)

                sum_dealer_cards = sum(dealer_cards)
                sum_user_cards = sum(user_cards)

                print("Dealer's cards: ", dealer_cards, f"= {sum_dealer_cards}")
                print("User's cards: ", user_cards, f"= {sum_user_cards}")

                if sum_user_cards > 21:
                    print("##### PLAYER GOT BUSTED #####")
                    decision = input(
                        "Do you want to play another game? Insert 'y' to start a new game, insert 'n' to close the application: "
                    )
                    if decision == "y":
                        clear_screen()
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        continue
                    else:
                        print("Thanks for playing with us! Come back soon!")
                        break

            # the user chose to 'stay': the dealer will get more cards until
            # they win, draw or lose
            else:
                while True:
                    dealer_cards = append_new_card(cards, dealer_cards)
                    # sum the card numbers
                    sum_dealer_cards = sum(dealer_cards)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Dealer's cards: ", dealer_cards, f"= {sum_dealer_cards}")
                    print("User's cards: ", user_cards, f"= {sum_user_cards}")

                    if sum_dealer_cards == 21:
                        print("##### DEALER WINS, PLAYER BUSTED! #####")
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break
                    elif (sum_dealer_cards > 21) and (sum_user_cards < 21):
                        print("##### PLAYER WINS, DEALER BUSTED! #####")
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break

        elif (sum_user_cards < 22) and (sum_user_cards > sum_dealer_cards):
            print("##### PLAYER WINS, DEALER BUSTED! #####")
            # reset the card lists
            dealer_cards, user_cards = reset_card_list()
            continue

    else:
        if sum_dealer_cards == 21:
            print("##### DEALER WINS, PLAYER BUSTED! #####")
            # reset the card lists
            dealer_cards, user_cards = reset_card_list()
            continue
        elif (sum_dealer_cards > 21) and (sum_user_cards < 21):
            print("##### PLAYER WINS, DEALER BUSTED! #####")
            decision = input(
                "Do you want to play another game? Insert 'y' to start a new game, insert 'n' to close the application."
            )
            if decision == "y":
                clear_screen()
                # reset the card lists
                dealer_cards, user_cards = reset_card_list()
                continue
            else:
                print("Thanks for playing with us! Come back soon!")
                break

        # user's card calculation
        if sum_user_cards == 21:
            print("##### PLAYER WINS, DEALER BUSTED! #####")
            # reset the card lists
            dealer_cards, user_cards = reset_card_list()
            continue
        elif sum_user_cards > 21:
            print("The sum of your cards is: ", sum_user_cards)
            print("##### PLAYER BUSTED #####")
            decision = input(
                "Do you want to play another game? Insert 'y' to start a new game, insert 'n' to close the application."
            )
            if decision == "y":
                clear_screen()
                # reset the card lists
                dealer_cards, user_cards = reset_card_list()
                continue
            else:
                break
        elif sum_user_cards < 21:
            decision_more_card = input("HIT or STAY? Insert 'y' or 's': ")
            if decision_more_card == "y":
                print("#############################")
                # dealer_cards = append_new_card(cards, dealer_cards)
                user_cards = append_new_card(cards, user_cards)

                # sum the card numbers
                sum_dealer_cards = sum(dealer_cards)
                sum_user_cards = sum(user_cards)

                print("Dealer's cards: ", dealer_cards, f"= {sum_dealer_cards}")
                print("User's cards: ", user_cards, f"= {sum_user_cards}")

                if sum_user_cards == sum_dealer_cards:
                    print("##### DRAW #####")
                    print("Restarting the game...")
                    # reset the card lists
                    dealer_cards, user_cards = reset_card_list()
                    continue

                elif sum_user_cards > 21:
                    print("##### PLAYER BUSTED #####")
                    decision = input(
                        "Another game? Insert 'y' to start a new game, insert 'n' to close the application: "
                    )
                    if decision == "y":
                        clear_screen()
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        continue
                    else:
                        break
            # the user chose to 'stay': the dealer will get more cards until
            # they win, draw or lose
            else:
                while True:
                    dealer_cards = append_new_card(cards, dealer_cards)
                    # sum the card numbers
                    sum_dealer_cards = sum(dealer_cards)

                    print("Dealer's cards: ", dealer_cards, f"= {sum_dealer_cards}")
                    print("User's cards: ", user_cards, f"= {sum_user_cards}")

                    if sum_dealer_cards == 21:
                        print("##### DEALER WINS, PLAYER BUSTED! #####")
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break
                    elif (sum_dealer_cards > 21) and (sum_user_cards < 21):
                        print("##### PLAYER WINS, DEALER BUSTED! #####")
                        # reset the card lists
                        dealer_cards, user_cards = reset_card_list()
                        break
                    # elif (sum_user_cards < 22) and (sum_user_cards > sum_dealer_cards):
                    #     print("##### PLAYER WINS, DEALER BUSTED! #####")
                    #     # reset the card lists
                    #     dealer_cards, user_cards = reset_card_list()
                    #     break

        elif (sum_user_cards < 22) and (sum_user_cards > sum_dealer_cards):
            print("##### PLAYER WINS, DEALER BUSTED! #####")
            # reset the card lists
            dealer_cards, user_cards = reset_card_list()
            continue

# TODO:
# Missing the 'stay' option:
# in case the user selects 'stay', then only the dealer should get more card until they BUST
# or they WIN.

# TODO:
# Convert repeated code into functions
