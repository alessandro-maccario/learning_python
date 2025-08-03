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
from pkgs.hirst_paint import HirstPaint

# --- CONSTANTS --- #
# change the size of the turtle
DOT_SIZE = 20
SPACING = 50
X_AXIS_POSITION = -240.00
y_axis_position = -200.00

# Define the screen where the turtle will draw
# instantiate the screen where the turtle will play
screen = Screen()

# instantiate a turtle object
turtle = Turtle(visible=False)

# change the shape of the turtle
turtle.shape("circle")
# slowest speed to see what is happenign
turtle.speed("fastest")

# send the turtle to the bottom right of the canvas
turtle.penup()
turtle.goto(X_AXIS_POSITION, y_axis_position)
turtle.pendown()
turtle.showturtle()

paint = HirstPaint(
    turtle=turtle,
    DOT_SIZE=DOT_SIZE,
    SPACING=SPACING,
    X_AXIS_POSITION=X_AXIS_POSITION,
    y_axis_position=y_axis_position,
    number_of_loops=10,
)
paint.hirst_paint()

# --- Screen and Exit --- #
screen.colormode(255)
# once the user clicks on the window, the window will close automatically
screen.exitonclick()
