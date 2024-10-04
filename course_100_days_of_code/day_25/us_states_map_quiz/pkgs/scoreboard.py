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
        self.goto(-140, 210)
        self.write(
            f"Score: {self.score_count}/50",
            align="center",
            font=(FONT, 20),
        )

    def increase_score(self):
        """Increase the score for the left paddle"""
        self.score_count += 1
        self.update_scoreboard()

    def game_end(self) -> bool:
        """Game over for the player either because hit by a car or they scored more then maximum amount of points"""
        self.home()
        self.write("Congrats!", align=ALIGNMENT, font=(FONT, 15))
        return
