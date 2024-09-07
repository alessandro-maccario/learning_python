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

# --- CONSTANTS --- #
SCREEN_SIZE_WIDTH = 500
SCREEN_SIZE_HEIGH = 400

# --- MAIN --- #
screen = Screen()
# setup screen size
screen.setup(width=SCREEN_SIZE_WIDTH, height=SCREEN_SIZE_HEIGH)

# define a set of characteristics: colors and positions of the turtles
colors = ["blue", "green", "red", "purple", "yellow"]
turtle_positions = [-100, -50, 0, 50, 100]
turtle_list = []
is_race_on = False

# prompt the user to be able to guess which turtle will be the winner
guessing_winner = screen.textinput(
    title="Guess the turtle winner",
    prompt="Guess the winning turtle by typing the color:",
)
is_race_on = True

for turtle_index in range(5):
    # create the turtle instances
    new_turtle = Turtle(shape="turtle")
    # form the colors list, grab one new color per each turtle
    new_turtle.color(colors[turtle_index])

    # define a function starting_position to send all the turtles in position immediately
    turtle_movement = TurtleMovement(
        turtle=new_turtle, x_position=-200, y_position=turtle_positions[turtle_index]
    )
    # grab each turtle object and insert it into a list to be used to move each turtle afterwards
    turtle_list.append(turtle_movement)
    # send the turtles to a specific starting position
    turtle_movement.starting_position()

while is_race_on:
    for each_turtle in turtle_list:
        # print("Turtle is: ", each_turtle.turtle.color()[0])
        each_turtle.turtle_racing()
        if each_turtle.wall_checker() is False:
            is_race_on = False
            if each_turtle.turtle.color()[0] == guessing_winner:
                print(f"Congratulation, your {guessing_winner} turtle won the race!")
            else:
                print(
                    "Unfortunately, your tutle was not the fastest one. Try again next time!"
                )
                print(
                    f"The winning turtle was the {each_turtle.turtle.color()[0]} one."
                )


screen.exitonclick()
