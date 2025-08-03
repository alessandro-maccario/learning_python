"""
Script to create a Pomodoro Technique App by using Python for the 100 Days of Code challenge from the Udemy course.

References
    1. https://docs.python.org/3/library/tk.html
    2. https://www.tcl.tk/man/tcl8.5/TkCmd/event.htm

Problem Breakdown:
    1.
    2.


Requirements:
    -

"""

# --- IMPORT PACKAGES --- #
import os
import sys
import hupper  # for interactive update of the tkinter window after every changes to the code
import tkinter as tk

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.UI import PasswordManagerUI


def start_reloader():
    """Reload the app at every changes in the code"""
    hupper.start_reloader("app.main")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


def main():
    # instantiate the class PasswordManagerApp
    ui = PasswordManagerUI()


if __name__ == "__main__":
    start_reloader()
