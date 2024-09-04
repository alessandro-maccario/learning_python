"""
This script will create a simple Turtle Art Paint in Python for the 100 Days of Code challenge from the Udemy course.

"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- IMPORT PACKAGES --- #
from turtle import Turtle, Screen
from pkgs.move import Shape, random_walk

# instanciate the turtle
turtle = Turtle(visible=False)

# define the characteristics of the turtle
# turtle.shape("circle")
# turtle.color(randint(0, 255))

# --- SHAPES --- #
# instantiate the shape object
shape = Shape()

# Draw all the shapes based on the number of sides input
# for i in range(3, 11):
#     shape.geometric_shape(turtle=turtle, number_of_sides=i)

# --- Define a random walk for the turtle --- #
# random_walk(turtle=turtle, number_of_steps=200)
shape.spirograph(turtle=turtle, radius=50, angle_head=10)

# --- LINES --- #
# shape.dashed_line(turtle=turtle)

# --- Screen and Exit --- #
# Define the screen where the turtle will draw
# instantiate the screen where the turtle will play
screen = Screen()
screen.colormode(255)
# once the user clicks on the window, the window will close automatically
screen.exitonclick()
