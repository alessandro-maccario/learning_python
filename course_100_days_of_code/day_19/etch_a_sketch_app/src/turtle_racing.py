"""
Build a turtle race game by using the Turtle package in Python for the 100 Days of Code challenge from the Udemy course.

Requirements:

"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- IMPORT PACKAGES --- #
from turtle import Turtle, Screen
from pkgs.racing import TurtleMovement

# --- MAIN --- #
screen = Screen()
# setup screen size
screen.setup(width=500, height=400)

# prompt the user to be able to guess which turtle will be the winner
guessing_winner = screen.textinput(
    title="Guess the turtle winner",
    prompt="Guess the winning turtle by typing the color:",
)


colors = ["blue", "green", "red", "purple", "yellow"]
turtle_positions = [-100, -50, 0, 50, 100]

for turtle_index in range(5):
    # create the turtle instances
    new_turtle = turtle = Turtle(shape="turtle")
    # form the colors list, grab one new color per each turtle
    new_turtle.color(colors[turtle_index])

    # define a function starting_position to send all the turtles in position immediately
    turtle_movement = TurtleMovement(
        turtle=new_turtle, x_position=-200, y_position=turtle_positions[turtle_index]
    )
    turtle_movement.starting_position()


screen.exitonclick()
