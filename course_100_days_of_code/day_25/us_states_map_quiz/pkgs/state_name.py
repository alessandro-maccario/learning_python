import pandas as pd
from turtle import Turtle
from pkgs.constants import CSV_PATH

# --- CONSTANTS --- #
ALIGNMENT = "center"
FONT = "Courier New"


class StateName(Turtle):
    def __init__(self, shape: str = "classic") -> None:
        super().__init__(shape)
        self.color("Black")
        self.penup()
        self.hideturtle()

    def match_name(self, user_input: str) -> tuple[float, float]:
        """Check if the state name inserted by the user exists in the dataframe.

        Parameters
        ----------
        user_input : str
            The state that the user wants to guess.

        Returns
        -------
        tuple[float, float]
            Grab the x_coord and the y_coord.
        """
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
        """Mark on the map the state name.

        Parameters
        ----------
        x_coord : float
            Coordinate for the x value.
        y_coord : float
            Coordinate for the y value.
        state_name : str
            Name of the guessed state.
        """
        self.goto(x_coord, y_coord)
        # write the state name on the map
        self.write(state_name, align=ALIGNMENT, font=(FONT, 8))
