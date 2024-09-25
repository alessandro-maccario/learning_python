"""
Build a Turtle Crossing game by using the Turtle package in Python for the 100 Days of Code challenge from the Udemy course.

Reference
    -

Problem Breakdown:
    1.
    2.

Requirements:
    - Create a Turtle screen that is 600px by 600px.
    - You need to turn off tracer(0) and use update() to refresh the screen every 0.1s.
"""

import os
import sys
from turtle import Turtle, Screen

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.player import Player


# --- CONSTANTS --- #
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# --- SCREEN --- #
# Instantiate the screen and the screen size
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)  # turn off animation so the paddle directly goes into position

# --- INSTANTIATE TURTLE --- #
turtle = Player(starting_position=(0, -200))

# start listening to the user's input
screen.listen()
# make the turtle move forward and backward
screen.onkey(turtle.move_up, "Up")  # "Up" keyboard key
# screen.onkey(turtle.move_down, "Down")  # "Down" keyboard key


# after turning off the animation, we manually have to turn constantly the animation on
game_is_on = True
while game_is_on:
    screen.update()  # after turning off the animation, you need to manually turn on the update


# let the screen on until the user clicks on it
screen.exitonclick()
