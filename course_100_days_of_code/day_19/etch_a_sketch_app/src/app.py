"""
Draw a copy of the Etch-A-Sketch app by using the Turtle package in Python for the 100 Days of Code challenge from the Udemy course.

Requirements:
    - pressing W = forward
    - pressing S = backwards
    - pressing A = counter clockwise
    - pressing D = clockwise
    - pressing C = clear drawing and put turtle back in the center
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
screen.listen()  # start listening to user inputs

# instantiate a turtle object
turtle = Turtle(visible=True)
# instantiate the Movement class


def going_forwards() -> None:
    turtle.forward(10)


screen.onkey(fun=going_forwards, key="w")

# once the user clicks on the window, the window will close automatically
screen.exitonclick()
