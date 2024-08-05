"""
Helper file that contains the four common mathematical operations to be used in the main
app.py calculator script.
"""


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
