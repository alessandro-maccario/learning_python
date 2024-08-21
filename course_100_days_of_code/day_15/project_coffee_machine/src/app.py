"""
This script will create a simple Coffee Machine Project in Python for the 100 Days of Code challenge from the Udemy course.

"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.coffee_machine_logic import coffee_machine_working_logic
from pkgs.helper import display_report, user_input
from pkgs.resources import resources


# --- VARIABLES --- #
profit = 0
decision = None
current_resource_availability = resources


# --- MAIN CODE --- #
def main():
    global profit, decision, current_resource_availability  # get the global variables

    while decision != "off":
        print()
        decision = user_input()
        if decision == "espresso":
            # call the coffee machine logic
            logic = coffee_machine_working_logic(
                decision, current_resource_availability, profit
            )
            if logic is False:
                break

        elif decision == "latte":
            # call the coffee machine logic
            logic = coffee_machine_working_logic(
                decision, current_resource_availability, profit
            )
            if logic is False:
                break

        elif decision == "cappuccino":
            # call the coffee machine logic
            logic = coffee_machine_working_logic(
                decision, current_resource_availability, profit
            )
            if logic is False:
                break

        elif decision == "off":
            sys.exit("Turning off the machine...")

        else:  # the decision is report
            display_report(
                profit, current_resource_availability
            )  # show the available resources


if __name__ == "__main__":
    main()
