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

Requirements paddle:
    - paddle: 20x100 (that means, width = 20 height=25, by 5 times)
    - x_position = 350 on the right side, in a vertical position
    - y_position = 0
    - the paddle should answer to up and down key stroke arrows and it should move by 20px
"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- IMPORT PACKAGES --- #
from turtle import Screen
from pkgs.paddle import Paddle, SCREEN_HEIGHT, SCREEN_WIDTH


# instantiate the screen and the screen size
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # turn off animation so the paddle directly goes into position

# --- Create and move a paddle --- #
player_paddle = Paddle(starting_position=(350, 0))  # right side paddle
opponent_paddle = Paddle(starting_position=(-350, 0))  # left side paddle

# start listening to the user's input
screen.listen()
# make the paddles move forward and backward
screen.onkey(player_paddle.move_up, "Up")  # "Up" keyboard key
screen.onkey(player_paddle.move_down, "Down")  # "Down" keyboard key
screen.onkey(opponent_paddle.move_up, "w")  # "w" keyboard key
screen.onkey(opponent_paddle.move_down, "s")  # "s" keyboard key


# after turning off the animation, we manually have to turn constantly the animation on
game_is_on = True
while game_is_on:
    screen.update()  # after turning off the animation, you need to manually turn on the update


# let the screen on until the user clicks on it
screen.exitonclick()
