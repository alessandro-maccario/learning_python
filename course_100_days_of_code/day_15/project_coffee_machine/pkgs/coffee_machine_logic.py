"""
File to hold the logic of the coffee machine.
"""

# --- IMPORT PACKAGES --- #

from pkgs.helper import prepare_drink, give_change

from pkgs.menu import MENU
from pkgs.resources import resources


def check_resource(decision: str, menu: dict, resources: dict) -> bool:
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

        # build a dict that contains the resources availability and use it for a list comprehension
        # to check which ingredients are still available
        ingredient_availability = {
            "water": available_water,
            "milk": available_milk,
            "coffee": available_coffee,
        }

        if available_water >= 0 and available_milk >= 0 and available_coffee >= 0:
            return ingredient_availability

        else:  # grab only those ingredients that are equal to 0 or below
            missing_ingredients = [
                key
                for key in ingredient_availability
                if ingredient_availability[key] <= 0
            ]
            # create a string that contains the missing ingredients
            missing_ingredients = ", ".join(missing_ingredients)
            print(
                f"Sorry, not enough {missing_ingredients} available. \nPlease, refill the machine."
            )
            return False

    else:
        return False


def process_coin(decision: str, menu: dict) -> None:
    print()
    decision_cost = menu[decision]["cost"]  # amount of money needed to get the beverage

    current_payment = decision_cost

    print(f"Please, insert ${decision_cost}.")
    # collect the amount inserted so far
    total_amount_inserted = 0

    while current_payment > 0:
        pennies = float(input("How many pennies?: "))
        nickles = float(input("How many nickles?: "))
        dimes = float(input("How many dimes?: "))
        quarters = float(input("How many quarters?: "))

        amount_inserted = round(
            (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies), 2
        )
        total_amount_inserted += amount_inserted
        current_payment -= amount_inserted
        if current_payment > 0:
            print(
                f"Please, insert the amount of money required to complete your order. Current payment of ${total_amount_inserted}. \n"
            )
        else:
            print(f">>> Money inserted: {total_amount_inserted}")
            # if money_to_give_back is > 0, then the user will receive the money
            # back because they inserted more money than necessary.
            # Otherwise if it is 0, it means that the correct amount of money has
            # been inserted.
            money_to_give_back = round(0 - current_payment, 2)
            return (
                decision_cost,
                money_to_give_back,
            )  # the money paid by the customer will then be added to the machine's profit


def coffee_machine_working_logic(
    user_decision: str, current_resource_availability: dict, profit: float
) -> tuple[None, bool]:
    print()
    ingredient_availability = check_resource(user_decision, MENU, resources)
    # if not all the ingredients are available, close the application
    if ingredient_availability is False:
        return False
    decision_cost, payment_process = process_coin(user_decision, MENU)
    if (
        payment_process > 0
    ):  # the user will get some change in return because they paid too much
        give_change(payment_process)

    # deduct the current available resources with the one already used
    current_resource_availability.update(ingredient_availability)
    prepare_drink(user_decision)  # just a print statement
