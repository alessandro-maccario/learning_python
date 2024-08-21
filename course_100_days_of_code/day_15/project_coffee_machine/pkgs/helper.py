"""
Script to keep the helper functions that are not game logic related.
"""


def user_input():
    """Ask for the user's input"""
    decision = input("What would you like? Type Espresso/Latte/Cappuccino: ").lower()
    while decision not in ("espresso", "latte", "cappuccino", "report", "off"):
        print("Please, enter a valid option between espresso/latte/cappuccino.")
        decision = input(
            "What would you like? Type Espresso/Latte/Cappuccino: "
        ).lower()
    return decision


def display_report(profit: float, resources: dict) -> None:
    """Generating a report of the available resources.

    Parameters
    ----------
    profit : float
        The total amount of money collected by the coffee machine
    resources : dict
        Current resources available in the coffee machine
    """
    print("> 💧 Water:", resources["water"])
    print("> 🥛 Milk:", resources["milk"])
    print("> ☕ Coffee:", resources["coffee"])
    print("> 💲 Profit: $", profit)
    return


def prepare_drink(decision):
    """If the resources are enough, then prepare the drink."""
    print(f">>> Start pouring {decision} ☕... Enjoy 😄 !")
    return


def give_change(payment_process):
    """Print a statement when you give money back to the user"""
    print(f">>> Here is ${payment_process} dollars in change!")
