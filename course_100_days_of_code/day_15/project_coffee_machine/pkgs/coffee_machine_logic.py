"""
File to hold the logic of the coffee machine.
"""

# --- IMPORT PACKAGES --- #
from pkgs.resources import resources


def user_input():
    """Ask for the user's input"""
    decision = input("What would you like? Type Espresso/Latte/Cappuccino: ").lower()
    while decision not in ("espresso", "latte", "cappuccino", "report", "off"):
        print("Please, enter a valid option between espresso/latte/cappuccino.")
        decision = input(
            "What would you like? Type Espresso/Latte/Cappuccino: "
        ).lower()
    return decision


def check_resource(decision: str, menu: dict) -> bool:
    """
    Based on the user decision, the function checks if the resources are
    enough to prepare the drink.

    Parameters
    ----------
    decision : str
        The drink chosen by the user.
    menu : dict
        The menu containing all the available drinks, ingredients and costs.
    """
    if decision in menu:
        water, milk, coffee = (
            menu[decision]["Ingredients"]["water"],
            menu[decision]["Ingredients"]["milk"],
            menu[decision]["Ingredients"]["coffee"],
        )

        # pull the available resources
        res_water, res_milk, res_coffee = resources.values()

        available_water = res_water - water
        available_milk = res_milk - milk
        available_coffee = res_coffee - coffee

        # build a dict that contains the availability and use it for a list comprehension
        # to check which ingredients are still available
        ingredient_availability = {
            "water": available_water,
            "milk": available_milk,
            "coffee": available_coffee,
        }

        if available_water > 0 and available_milk > 0 and available_coffee > 0:
            print(f"Start pouring {decision} ☕...")
            return True

        else:
            missing_ingredients = [
                key
                for key in ingredient_availability
                if ingredient_availability[key] <= 0
            ]
            # create a string that contains the missing ingredients
            missing_ingredients = ", ".join(missing_ingredients)
            print(f"Sorry, not enough {missing_ingredients} available.")
            return False

    else:
        return False
