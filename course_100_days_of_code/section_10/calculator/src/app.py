"""
This script will create a simple Calculator in Python for the 100 Days of Code challenge from the Udemy course.
"""

# --- Import packages --- #
import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.ascii_art import logo
from pkgs.operations import add, subtract, multiply, divide, calculator

print(logo)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

current_operation = 0
history_value = 0
count_running = 0

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
first_number = float(input("What is the first number?: "))

if __name__ == "__main__":
    calculator(first_number, history_value)
