"""
Draw a copy of the Hirst painting by using the Turtle package in Python for the 100 Days of Code challenge from the Udemy course.

Requirements:
    - The number of rows and columns must be 10x10. That means, 10 dots per row, per 10 rows
    - Each dot must be 20px in size
    - Each dot must be spaced apart by 50px
"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- IMPORT PACKAGES --- #
from turtle import Turtle, Screen

# Define the screen where the turtle will draw
# instantiate the screen where the turtle will play
screen = Screen()

# instantiate a turtle object
turtle = Turtle(visible=False)

# once the user clicks on the window, the window will close automatically
screen.exitonclick()
