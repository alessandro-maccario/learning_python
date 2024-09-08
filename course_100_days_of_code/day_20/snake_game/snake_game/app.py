"""
Build the famous Snake game by using the Turtle package in Python for the 100 Days of Code challenge from the Udemy course.

Requirements:
    -

Steps:
    1. Create a snake body with 3 squares all lined up next to each other
    2. Move the snake
    3. Control the snake (using Up, Left, Right, Down arrow keys)
    4. Detect collisions with food: once the snake eats the food, a new food on the screen appears
    5. Create a scoreboard
    6. Detect collisions with a wall: when the game should end?
    7. Detect collisions with the snake's tail: when the game should end?

"""

import os
import sys
import time

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- IMPORT PACKAGES --- #
from turtle import Screen
from pkgs.snake_logic import Snake
from pkgs.food_logic import Food
from pkgs.scoreboard_logic import ScoreBoard

# --- CONSTANT --- #
SCREEN_WIDTH = 600
SCREE_HEIGHT = 600

# Instantiate the screen
screen = Screen()
screen.title("PySnake Game")
# setup the screen size
screen.setup(width=SCREEN_WIDTH, height=SCREE_HEIGHT)
screen.bgcolor("black")
# screen.tracer()  # turn off the tracer: Animation control section in the turtle docs

# instantiate the Snake object
snake_body = Snake()
snake_food = Food()
snake_scoreboard = ScoreBoard()

# start listening to the user's input
screen.listen()
screen.onkey(snake_body.move_up, "Up")
screen.onkey(snake_body.move_down, "Down")
screen.onkey(snake_body.move_left, "Left")
screen.onkey(snake_body.move_right, "Right")

# Continously move the segments
is_game_on = True
while is_game_on:
    # screen.update()  # update the screen only when all the segments of the body have moved forward
    time.sleep(0.3)

    # make the snake move forward
    snake_body.snake_move()

    # Detect food collision
    if snake_body.head.distance(snake_food) < 35:
        print("Delicious...")
        snake_food.refresh()
        snake_body.extend()
        snake_scoreboard.increase_score()

    # Detect wall collision
    if (
        (snake_body.head.xcor() > SCREEN_WIDTH / 2)
        or (snake_body.head.ycor() > SCREEN_WIDTH / 2)
        or (snake_body.head.xcor() < -SCREEN_WIDTH / 2)
        or (snake_body.head.ycor() < -SCREEN_WIDTH / 2)
    ):
        snake_scoreboard.game_over()
        is_game_on = False

    # Detect tail collision
    # if head collides with any segments of the tail:
    # then game_over sequence
    for body in snake_body.snake_bodies[1:]:
        if snake_body.head.distance(body) < 10:
            snake_scoreboard.game_over()
            is_game_on = False


# close the screen only when the user clicks on it
screen.exitonclick()
