"""
Script to create the US States Map Quiz by using Python for the 100 Days of Code challenge from the Udemy course.

Reference
    - https://www.sporcle.com/games/g/states

Problem Breakdown:
    1.

Requirements:
    - The Turtle package works only with the .gif image format.

"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- IMPORT PACKAGES --- #
from pkgs.scoreboard import ScoreBoard
from pkgs.country_name import CountryName
from turtle import Screen


# --- CONSTANTS --- #
SCREEN_WIDTH = 725
SCREEN_HEIGHT = 491
# dynamically get the absolute path to the image
IMAGE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "attachments",
    "blank_states_img.gif",
)
CSV_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "attachments",
    "50_states.csv",
)
TEXTINPUT_TITLE = "Guess Country Name"
TEXT_INPUT = "Insert the name of a US State:"
MAX_COUNT_STATES = 50

# Instantiate the screen and the screen size
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("US Map Quiz")
# now set the background to our space image
screen.bgpic(IMAGE_PATH)
# --- Instantiate the writing turtle object for the state names
country_name = CountryName()
# --- Instantiate the ScoreBoard object --- #
scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    # ask for the input user
    user_input = screen.textinput(TEXTINPUT_TITLE, TEXT_INPUT)

    # read the country name dataframe
    try:
        country_name_match = country_name.match_name(user_input=user_input)
    except IndexError:
        continue

    if country_name_match:  # if true, we have a match, therefore we have coordinates
        country_name.mark_on_map(
            x_coord=country_name_match[0],
            y_coord=country_name_match[1],
            state_name=user_input,
        )
        scoreboard.increase_score()

        if scoreboard.score_count == 1:
            scoreboard.game_end()
            game_is_on = False
            screen.exitonclick()
    else:
        continue
