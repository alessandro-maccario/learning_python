"""
Script to keep the helper functions that are not game logic related.
"""

# --- IMPORT PACKAGES --- #
import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.resources import resources


def display_report(money: float) -> None:
    """Generating a report of the available resources"""
    print("Water:", resources["water"])
    print("Milk:", resources["milk"])
    print("Coffee:", resources["coffee"])
    print("Money available: $", money)
    return
