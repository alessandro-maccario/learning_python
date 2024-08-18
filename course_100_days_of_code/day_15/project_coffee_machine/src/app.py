"""
This script will create a simple Coffee Machine Project in Python for the 100 Days of Code challenge from the Udemy course.

"""

# --- IMPORT PACKAGES --- #
import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.coffee_machine_logic import user_input


# --- MAIN CODE --- #

decision = user_input()
while decision not in ("espresso", "latte", "cappuccino"):
    print("Please, enter a valid option between espresso/latte/cappuccino.")
    continue

if decision == "espresso":
    pass
elif decision == "latte":
    pass
else:  # the decision is then the cappuccino
    pass
