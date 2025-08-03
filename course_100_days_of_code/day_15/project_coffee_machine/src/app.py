"""
This script will create a simple Coffee Machine Project in Python for the 100 Days of Code challenge from the Udemy course.

"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.coffee_machine_logic import coffee_machine_working_logic
from pkgs.helper import display_report, user_input, add_profit
from pkgs.resources import resources
from pkgs.menu import MENU


# --- VARIABLES --- #
profit = 0
machine_profit = 0
decision = None
current_resource_availability = resources


# --- MAIN CODE --- #
def main():
    global profit, decision, current_resource_availability, machine_profit  # get the global variables

    while decision != "off":
        print()
        decision = user_input()  # collect the user's input

        if decision in ("espresso", "latte", "cappuccino"):
            # if decision == "espresso":
            # call the coffee machine logic
            logic = coffee_machine_working_logic(
                decision, current_resource_availability, profit
            )
            if logic is False:
                break
            machine_profit += add_profit(decision, profit, MENU)
        elif decision == "off":
            sys.exit("Turning off the machine...")
        else:  # the decision is report
            display_report(
                machine_profit, current_resource_availability
            )  # show the available resources


if __name__ == "__main__":
    main()
