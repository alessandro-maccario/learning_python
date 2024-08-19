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

decision = user_input()


def process_coin(decision: str, menu: dict) -> None:
    decision_cost = menu[decision]["cost"]  # amount of money needed to get the beverage

    current_payment = decision_cost

    print(f"Please, insert ${decision_cost}.")

    while current_payment > 0:
        pennies = float(input("How many pennies?: "))
        nickles = float(input("How many nickles?: "))
        dimes = float(input("How many dimes?: "))
        quarters = float(input("How many quarters?: "))

        amount_inserted = round(
            (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies), 2
        )
        current_payment -= amount_inserted
        if current_payment > 0:
            print(
                f"Please, insert the amount of money required to complete your order. Current payment of ${current_payment}. \n"
            )
            continue

        elif current_payment == 0:
            print(f"Amount paid: {current_payment}")
            return decision_cost  # this amount will be added to the profit
        else:
            money_to_give_back = 0 - current_payment
            print(f"Money returned: {money_to_give_back}")
            return money_to_give_back


# This will be the last function needed
def prepare_drink():
    """If the resources are enough, then prepare the drink."""
    pass


if decision == "espresso":
    # TODO: define a function to deal with the espresso making
    check_resource(decision, MENU)
    process_coin(decision, MENU)
    pass
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
