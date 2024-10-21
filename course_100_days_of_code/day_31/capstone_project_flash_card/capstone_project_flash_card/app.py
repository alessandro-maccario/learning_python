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
import tkinter as tk

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
