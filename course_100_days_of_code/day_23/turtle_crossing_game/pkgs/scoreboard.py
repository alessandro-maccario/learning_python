import time
from turtle import Turtle

# --- CONSTANTS --- #
ALIGNMENT = "center"
FONT = "Courier New"


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.score_count = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Creating the turtle to write the score on the screen"""
        self.clear()
        # draw the score
        self.goto(0, 260)
        self.write(
            f"{self.score_count}",
            align="center",
            font=(FONT, 30),
        )

    def increase_score(self):
        """Increase the score for the left paddle"""
        self.score_count += 1
        self.update_scoreboard()

    def game_over(self) -> bool:
        """Game over for the player either because hit by a car or they scored more then maximum amount of points"""
        self.home()
        self.write("Game Over", align=ALIGNMENT, font=(FONT, 15))
        return
