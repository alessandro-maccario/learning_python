"""
This script will create a simple Turtle Art Paint in Python for the 100 Days of Code challenge from the Udemy course.

"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- IMPORT PACKAGES --- #
from turtle import Turtle, Screen
from pkgs.move import Shape

# instanciate the turtle
turtle = Turtle()

# define the characteristics of the turtle
# turtle.shape("circle")
turtle.color("green")

# --- SHAPES --- #
# instantiate the shape object
shape = Shape()
# --- Draw a square --- #
shape.square(turtle=turtle)

# erase the screen
turtle.clear()

# --- LINES --- #
shape.dashed_line(turtle=turtle)

# --- Screen and Exit --- #
# Define the screen where the turtle will draw
# instantiate the screen where the turtle will play
screen = Screen()
# once the user clicks on the window, the window will close automatically
screen.exitonclick()
