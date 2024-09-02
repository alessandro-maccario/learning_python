"""
This script will create a simple Turtle Art Paint in Python for the 100 Days of Code challenge from the Udemy course.

"""

import os
import sys
from random import randint

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- IMPORT PACKAGES --- #
from turtle import Turtle, Screen
from pkgs.move import Shape

# instanciate the turtle
turtle = Turtle()

# define the characteristics of the turtle
# turtle.shape("circle")
# turtle.color(randint(0, 255))

# --- SHAPES --- #
# instantiate the shape object
shape = Shape()

for i in range(3, 11):
    shape.geometric_shape(turtle=turtle, number_of_sides=i)

# --- LINES --- #
# shape.dashed_line(turtle=turtle)

# --- Screen and Exit --- #
# Define the screen where the turtle will draw
# instantiate the screen where the turtle will play
screen = Screen()
# once the user clicks on the window, the window will close automatically
screen.exitonclick()
