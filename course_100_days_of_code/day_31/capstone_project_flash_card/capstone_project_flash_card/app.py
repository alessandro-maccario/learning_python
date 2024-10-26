"""
Script to create the Capstone Project Flashcard App by using Python for the 100 Days of Code challenge from the Udemy course.

Problem Breakdown:
    1.
    2.


Requirements:
    1.
    2.

References
    1. https://docs.python.org/3/library/tk.html
    2. https://www.tcl.tk/man/tcl8.5/TkCmd/event.htm
    3. https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists
    4. https://github.com/hermitdave/FrequencyWords/tree/master/content/2018
    5. https://www.opensubtitles.org/en/search/subs

"""

# --- IMPORT PACKAGES --- #
import os
import sys

# import hupper  # for interactive update of the tkinter window after every changes to the code
import hupper  # for interactive update of the tkinter window after every changes to the code

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.UI import FlashCardUI


def start_reloader():
    """Reload the app at every changes in the code"""
    hupper.start_reloader("app.main")


def main():
    # instantiate the class PasswordManagerApp
    ui = FlashCardUI()


if __name__ == "__main__":
    # main()
    start_reloader()
