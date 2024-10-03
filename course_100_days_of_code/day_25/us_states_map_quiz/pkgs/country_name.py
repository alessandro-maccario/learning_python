import os
import pandas as pd
from turtle import Turtle

# --- CONSTANTS --- #
ALIGNMENT = "center"
FONT = "Courier New"
CSV_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "attachments",
    "50_states.csv",
)


class CountryName(Turtle):
    def __init__(self, shape: str = "classic") -> None:
        super().__init__(shape)
        self.color("Black")
        self.penup()
        self.hideturtle()

    def match_name(self, user_input: str) -> tuple[float, float]:
        # read the file that contains the state names and the coordinates
        state_names = pd.read_csv(CSV_PATH)
        # convert lowercase column use str.lower()
        state_names["state"] = state_names["state"].str.lower()
        # convert user_input to string lower
        user_input = user_input.lower()
        # get x and y coordinates
        get_x, get_y = (
            state_names[state_names["state"] == user_input]["x"].values[0],
            state_names[state_names["state"] == user_input]["y"].values[0],
        )
        # return them as a tuple
        return get_x, get_y

    def mark_on_map(self, x_coord: float, y_coord: float, state_name: str):
        self.goto(x_coord, y_coord)
        # write the state name on the map
        self.write(state_name, align=ALIGNMENT, font=(FONT, 5))
