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
from random import randrange
from turtle import Turtle, Screen

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.player import Player
from pkgs.car import Car
from pkgs.scoreboard import ScoreBoard
from pkgs.helper import random_color


# --- CONSTANTS --- #
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CAR_NUMBER = 15

# define a set of characteristics: colors and positions of the turtles
colors = [random_color() for _ in range(0, CAR_NUMBER)]
# get 10 values between -200 and 200 completely randomly generator
turtle_positions = [randrange(-200, 200, 30) for _ in range(0, CAR_NUMBER)]
turtle_list = []


# --- SCREEN --- #
# Instantiate the screen and the screen size
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)  # turn off animation so the paddle directly goes into position

# --- INSTANTIATE PLAYER TURTLE --- #
player = Player(starting_position=(0, -200))
# --- INSTANTIATE THE SCOREBOARD --- #
score = ScoreBoard()

# start listening to the user's input
screen.listen()
# make the turtle move forward and backward
screen.onkey(player.move_up, "Up")  # "Up" keyboard key

for turtle_index in range(len(colors)):
    # create the turtle instances
    new_turtle = Car(
        x_position=-280,
        y_position=randrange(-300, 300, 30),
    )
    # form the colors list, grab one new color per each turtle
    new_turtle.color(colors[turtle_index])

    # grab each turtle object and insert it into a list to be used to move each turtle afterwards
    turtle_list.append(new_turtle)
    # send the turtles to a specific starting position
    new_turtle.starting_position()


# after turning off the animation, we manually have to turn constantly the animation on
game_is_on = True
while game_is_on:
    screen.update()  # after turning off the animation, you need to manually turn on the update
    for each_turtle in turtle_list:
        # move the car forward
        each_turtle.turtle_racing()

        # if the turtle goes off screen at the top without being hit by a car, then end the game with a win
        if player.ycor() > SCREEN_HEIGHT / 2:
            score.increase_score()
            player.player_restart()
            for each_turtle in turtle_list:
                each_turtle.car_restart()

        # if the car goes out of the screen on the right, then push it back to the left side of the screen
        if each_turtle.wall_checker(SCREEN_WIDTH):
            each_turtle.car_flow()


# TODO: add game_over whenever a car hit the turtle

# let the screen on until the user clicks on it
screen.exitonclick()
