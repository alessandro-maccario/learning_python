"""
Script to create the US States Map Quiz by using Python for the 100 Days of Code challenge from the Udemy course.

Reference
    - https://www.sporcle.com/games/g/states

Problem Breakdown:
    1. Convert the guess to Title Case (in this case, both the guessed state and the state in the csv file are lowercase)
    2. Check if the guess is among the 50 states
    3. Write correct guesses on the map
    4. Use a loop to allow user to keep guessing
    5. Record the correct guesses in a list
    6. Keep track of the score

Requirements:
    - The Turtle package works only with the .gif image format.

"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- IMPORT PACKAGES --- #
from pkgs.scoreboard import ScoreBoard
from pkgs.state_name import StateName
from pkgs.constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    IMAGE_PATH,
    MAX_COUNT_STATES,
    TEXTINPUT_TITLE,
    TEXT_INPUT,
)
from turtle import Screen

# list to contain the states already guessed
state_already_seen = []

# Instantiate the screen and the screen size
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("US Map Quiz")
# now set the background to our space image
screen.bgpic(IMAGE_PATH)
# --- Instantiate the writing turtle object for the state names
country_name = StateName()
# --- Instantiate the ScoreBoard object --- #
scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    # ask for the input user
    user_input = screen.textinput(TEXTINPUT_TITLE, TEXT_INPUT)
    if user_input in state_already_seen:
        continue
    # read the country name dataframe
    try:
        country_name_match = country_name.match_name(user_input=user_input)
        state_already_seen.append(user_input)
    except IndexError:
        continue

    if country_name_match:  # if true, we have a match, therefore we have coordinates
        country_name.mark_on_map(
            x_coord=country_name_match[0],
            y_coord=country_name_match[1],
            state_name=user_input,
        )
        scoreboard.increase_score()

        if scoreboard.score_count == MAX_COUNT_STATES:
            scoreboard.game_end()
            game_is_on = False
            screen.exitonclick()
    else:
        continue
