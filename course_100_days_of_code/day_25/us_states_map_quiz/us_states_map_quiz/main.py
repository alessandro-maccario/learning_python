"""
Script to create the US States Map Quiz by using Python for the 100 Days of Code challenge from the Udemy course.

Reference
    - https://www.sporcle.com/games/g/states

Problem Breakdown:
    1.

Requirements:
    - The Turtle package works only with the .gif image format.

"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- IMPORT PACKAGES --- #
from turtle import Turtle, Screen


# --- CONSTANTS --- #
SCREEN_WIDTH = 725
SCREEN_HEIGHT = 491


# Instantiate the screen and the screen size
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("US Map Quiz")
# now set the background to our space image
screen.bgpic("day_25/us_states_map_quiz/attachments/blank_states_img.gif")


# let the screen on until the user clicks on it
screen.exitonclick()
