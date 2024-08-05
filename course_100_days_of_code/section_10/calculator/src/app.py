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
from pkgs.helper import clear_screen

print(logo)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

current_operation = 0
history_value = 0
temp_current_operation = 0

while True:
    first_number = float(input("What is the first number?: "))

    print("+")
    print("-")
    print("*")
    print("/")
    decision_operation = input("Pick an operation: ")
    second_number = float(input("What is the next number?: "))

    temp_current_operation = current_operation
    # possible to convert this if-else with a function and reduce the code
    if decision_operation == "+":
        current_operation += add(
            first_number,
            second_number,
        )
        # save the current, valid, current_operation value
        if current_operation != float("inf"):
            history_value = current_operation
    elif decision_operation == "-":
        current_operation -= subtract(
            first_number,
            second_number,
        )
        # save the current, valid, current_operation value
        if current_operation != float("inf"):
            history_value = current_operation
    elif decision_operation == "*":
        current_operation *= multiply(
            first_number,
            second_number,
        )
        # save the current, valid, current_operation value
        if current_operation != float("inf"):
            history_value = current_operation
    elif decision_operation == "/":
        current_operation /= divide(
            first_number,
            second_number,
        )
        # save the current, valid, current_operation value
        if current_operation != float("inf"):
            history_value = current_operation

    # in case of divide(first_number = 0, second_number = 0), not possible to perform the division
    if current_operation == float("inf"):
        current_operation = history_value
        print(
            "It has been not possible to perform the operation. Check again the input."
        )
        clear_screen()
        continue
    else:
        print(
            f"Current operation: {temp_current_operation} {decision_operation} ({first_number} {decision_operation} {second_number}) = {current_operation}"
        )

    # next decision
    decision_continuation = input(
        "Do you want to continue? Type 'y' to continue, type 'n' to start a new calculation, type 'close' to close the application entirely: "
    )

    if decision_continuation in ("y", "n"):
        if decision_continuation == "y":
            clear_screen()
            continue
        else:
            current_operation = 0
            clear_screen()
            continue
    elif decision_continuation == "close":
        # close the application
        print("Closing the calculator...")
        break
    else:
        print(
            "Please, provide a valid choice between: 'y' to continue, 'n' to start a new calculation, 'close' to close the application."
        )
