"""
This script will create a simple Coffee Machine Project in Python for the 100 Days of Code challenge from the Udemy course.

"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.coffee_machine_logic import user_input, check_resource
from pkgs.helper import display_report

from pkgs.menu import MENU


# --- MAIN CODE --- #

# --- VARIABLES --- #
# TODO: once you print the resources, also the amount of profit should be displayed
profit = 0
decision = None


def process_coin(decision: str, menu: dict) -> None:
    print()
    decision_cost = menu[decision]["cost"]  # amount of money needed to get the beverage

    current_payment = decision_cost

    print(f"Please, insert ${decision_cost}.")
    # collect the amount inserted so far
    total_amount_inserted = 0

    while current_payment > 0:
        pennies = float(input("How many pennies?: "))
        nickles = float(input("How many nickles?: "))
        dimes = float(input("How many dimes?: "))
        quarters = float(input("How many quarters?: "))

        amount_inserted = round(
            (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies), 2
        )
        total_amount_inserted += amount_inserted
        current_payment -= amount_inserted
        if current_payment > 0:
            print(
                f"Please, insert the amount of money required to complete your order. Current payment of ${total_amount_inserted}. \n"
            )
        else:
            print(f"Money inserted: {total_amount_inserted}")
            # if money_to_give_back is > 0, then the user will receive the money
            # back because they inserted more money than necessary.
            # Otherwise if it is 0, it means that the correct amount of money has
            # been inserted.
            money_to_give_back = round(0 - current_payment, 2)
            return (
                decision_cost,
                money_to_give_back,
            )  # the money paid by the customer will then be added to the machine's profit


# This will be the last function needed
def prepare_drink():
    """If the resources are enough, then prepare the drink."""
    pass


while decision != "off":
    decision = user_input()
    if decision == "espresso":
        # TODO: define a function to deal with the espresso making
        check_resource(decision, MENU)
        decision_cost, payment_process = process_coin(decision, MENU)
        profit += decision_cost  # Add decision_cost to the machine's profit
        if (
            payment_process > 0
        ):  # the user will get some change in return because they paid too much
            print(f"Here is ${payment_process} dollars in change")
        print(f"Start pouring {decision} ☕...")

    elif decision == "latte":
        # TODO: define a function to deal with the latte making
        check_resource(decision, MENU)
        pass
    elif decision == "cappuccino":
        # TODO: define a function to deal with the cappuccino making
        check_resource(decision, MENU)
        pass
    elif decision == "off":
        sys.exit("Turning off the machine...")
    else:  # the decision is report
        display_report(profit)  # show the available resources


if __name__ == "__main__":
    pass
