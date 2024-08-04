"""
This script will create a simple Calculator in Python for the 100 Days of Code challenge from the Udemy course.
"""

# --- Import packages --- #
import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.ascii_art import logo
from pkgs.operations import add, subtract, multiply, divide

print(logo)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

first_operation = 0
current_operation = 0

while True:
    first_number = int(input("What is the first number?: "))
    print("+")
    print("-")
    print("*")
    print("/")
    decision_operation = input("Pick an operation: ")
    next_number = int(input("What is the next number?"))

    # possible to convert this if-else with a function and reduce the code
    if decision_operation == "+":
        first_operation += add(
            first_number,
            next_number,
        )
    elif decision_operation == "-":
        first_operation += subtract(
            first_number,
            next_number,
        )
    elif decision_operation == "*":
        first_operation += multiply(
            first_number,
            next_number,
        )
    elif decision_operation == "/":
        first_operation += divide(
            first_number,
            next_number,
        )

    # fetch the first value to be taken for following operations, if necessary
    current_operation = first_operation

    decision_continuation = input(
        "Do you want to continue? Type 'y' to continue, type 'n' to start a new calculation, type 'close' to close the application entirely."
    )

    if decision_continuation in ("y", "n"):
        # do something in a function
        pass
    elif decision_continuation == "close":
        # close the application
        break
    else:
        print(
            "Please, provide a valid choice between: 'y' to continue, 'n' to start a new calculation, 'close' to close the application."
        )
