"""
Script that contains the coffee machine logic with a focus on OOP.
"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.oop_menu import Menu, MenuItem
from pkgs.oop_money_machine import MoneyMachine
from pkgs.oop_coffee_maker import CoffeeMaker

# --- Variables --- #
is_on = True  # is the coffee machine on?

# print the resources
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_on:
    options = menu.get_items()  # all the options will be saved here
    choice = input(f"What would you like? {options}")  # user choice

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
