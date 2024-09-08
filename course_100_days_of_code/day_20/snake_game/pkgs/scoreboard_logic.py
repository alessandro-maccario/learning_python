from turtle import Turtle

# --- CONSTANTS --- #
ALIGNMENT = "center"
FONT = "Courier New"


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.score_count = 0
        self.up()
        self.color("White")
        self.goto(x=0, y=280)
        self.update_score()

    def update_score(self):
        self.write(
            f"Score:  {self.score_count}",
            align=ALIGNMENT,
            font=(FONT, 15),
        )

    def increase_score(self):
        self.score_count += 1
        self.clear()
        self.update_score()

    def game_over(self) -> bool:
        """Check if the turtle reached the end of the screen size"""
        self.home()
        self.write("Game Over", align=ALIGNMENT, font=(FONT, 15))
        return False
