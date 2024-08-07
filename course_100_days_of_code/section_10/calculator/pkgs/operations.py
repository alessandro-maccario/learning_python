"""
Helper file that contains the four common mathematical operations to be used in the main
app.py calculator script.
"""

# --- IMPORT PACKAGES --- #
from pkgs.helper import clear_screen


def add(first_number: float, second_number: float) -> float:
    """Add two numbers.

    Parameters
    ----------
    first_number : _type_
        _description_
    second_number : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    return float(first_number) + float(second_number)


def subtract(first_number: float, second_number: float) -> float:
    """Subtract two numbers.

    Parameters
    ----------
    first_number : _type_
        _description_
    second_number : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    return float(first_number) - float(second_number)


def multiply(first_number: float, second_number: float) -> float:
    """Multiply two numbers.

    Parameters
    ----------
    first_number : _type_
        _description_
    second_number : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    return float(first_number) * float(second_number)


def divide(first_number: float, second_number: float) -> float:
    # TODO
    # catch DivisionErrors, e.g.: n/0
    """Divide two numbers.

    Parameters
    ----------
    first_number : _type_
        _description_
    second_number : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    try:
        return float(first_number) / float(second_number)
    except ZeroDivisionError:
        print("Cannot divide by 0!")
        return float("inf")


#########################################
########### TESTING RECURSION ###########
#########################################


def calculator(first_number: float, history_value: float) -> None:
    """Calculator function that performs the very basic operations,

    Parameters
    ----------
    first_number : float
        First number to be inserted by the user or, in following steps, the current value.
    history_value : float
        Previous value inserted. In case of 0/0, the history value will be used to maintain the
        previous value intacted.
    """
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    decision_operation = input("Pick an operation amongst +, -, *, /: ")
    while decision_operation not in ("+", "-", "*", "/"):
        decision_operation = input(
            "Please, choose a valid operator between +, -, *, /: "
        )
        continue
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
        calculator(operation_result, history_value)
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
            clear_screen()
            calculator(history_value, second_number)
        else:
            # if "n", all the possible values will be zeroed
            operation_result = 0
            # previous_operation = 0
            history_value = 0
            clear_screen()
            calculator(operation_result, history_value)
    elif decision_continuation == "close":
        print("Closing the calculator...")
        # close the application
        return
    else:
        print(
            "Please, provide a valid choice between: 'y' to continue, 'n' to start a new calculation, 'close' to close the application."
        )
        calculator(history_value, second_number)
