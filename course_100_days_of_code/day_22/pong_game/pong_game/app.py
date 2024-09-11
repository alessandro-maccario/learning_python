"""
Build the famous Pong game by using the Turtle package in Python for the 100 Days of Code challenge from the Udemy course.

Reference
    - https://en.wikipedia.org/wiki/Pong

Problem Breakdown:
    1. Create the Screen
    2. Create and move the paddle
    3. Create another paddle to have a two player game
    4, Create the ball and make it move constantly across the screen
    5. Detect collision with wall and bounce the ball back
    6. Detect collision with a paddle to know when to bounce the ball back
    7. Detect when paddle misses the ball and score a point for one of the user
    8. Keep score using a Scoreboard as done in the Snake Game
"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- IMPORT PACKAGES --- #
from turtle import Screen, Turtle

# --- CONSTANTS --- #
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# instantiate the screen and the screen size
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")

# --- Create and move a paddle --- #


# let the screen on until the user clicks on it
screen.exitonclick()
