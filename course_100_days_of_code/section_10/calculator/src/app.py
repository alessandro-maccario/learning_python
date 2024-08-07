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
count_running = 0

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

while True:
    if count_running == 0:
        first_number = float(input("What is the first number?: "))
        decision_operation = input("Pick an operation amongst +, -, *, /: ")
        second_number = float(input("What is the next number?: "))

        # call the dictionary with the single operation and output the result of the function
        operation_result = operations[decision_operation](first_number, second_number)

        # in case of divide(first_number = 0, second_number = 0), not possible to perform the division
        if operation_result == float("inf"):
            operation_result = history_value
            print(
                "It has been not possible to perform the operation. Check again the input."
            )
            clear_screen()
            continue
        else:
            history_value = operation_result
            print(
                f"Current operation: {first_number} {decision_operation} {second_number} = {operation_result}"
            )

        # next decision
        decision_continuation = input(
            "Do you want to continue? Type 'y' to continue, type 'n' to start a new calculation, type 'close' to close the application entirely: "
        )

        if decision_continuation in ("y", "n"):
            if decision_continuation == "y":
                count_running += 1
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
            continue

    else:
        decision_operation = input("Pick an operation, chose between +, -, *, /: ")
        # check if the decision_operation makes sense
        while decision_operation not in ("+", "-", "*", "/"):
            decision_operation = input(
                "Please, choose a valid operator between +, -, *, /: "
            )
            continue
        next_number = float(input("What is the next number?: "))

        # call the dictionary with the single operation based on the operation_result input
        # that we got from the first iteration
        operation_result = operations[decision_operation](operation_result, next_number)

        # in case of divide(first_number = 0, second_number = 0), not possible to perform the division
        if operation_result == float("inf"):
            operation_result = history_value
            print(
                "It has been not possible to perform the operation. Check again the input."
            )
            clear_screen()
            continue
        else:
            previous_operation = history_value
            history_value = operation_result
            print(
                f"Current operation: {previous_operation} {decision_operation} {next_number} = {operation_result}"
            )

        # next decision
        decision_continuation = input(
            "Do you want to continue? Type 'y' to continue, type 'n' to start a new calculation, type 'close' to close the application entirely: "
        )

        if decision_continuation in ("y", "n"):
            if decision_continuation == "y":
                count_running += 1
                clear_screen()
                continue
            else:
                # if "n", all the possible values will be zeroed
                operation_result = 0
                previous_operation = 0
                history_value = 0
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
            continue
