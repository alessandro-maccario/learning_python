import os
import sys
import tkinter as tk
from PIL import Image
import customtkinter as ctk
from random import choice

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.constants import (
    BACKGROUND,
    CANVAS_HEIGHT,
    CANVAS_WIDTH,
    TRUE_BUTTON_IMAGE,
    FALSE_BUTTON_IMAGE,
    X_WORD_PLACE,
    Y_WORD_PLACE,
    USER_FEEDBACK_BG_TIME,
)


class TriviaQuizUI:
    def __init__(self, question_dict: dict) -> None:
        # Initialize with a list of questions
        self.questions = question_dict
        self.current_answer = None  # Store the answer for the current question
        self.score_point = 0
        self.setup_window()
        self.setup_canvas()
        self.setup_labels()
        self.setup_buttons()
        self.display_score()
        self.window.mainloop()

    def setup_window(self):
        """Initializes the main window settings."""
        self.window = tk.Tk()
        self.window.title("Trivia Quiz Game")
        self.window.configure(background=BACKGROUND, padx=20, pady=20)

        # position the Tkinter window at the center of the screen
        w = self.window.winfo_reqwidth()
        h = self.window.winfo_reqheight()
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws / 2.5) - (w / 2.5)
        y = (hs / 6) - (h / 6)
        self.window.geometry("+%d+%d" % (x, y))
        # self.flashcard_picture_front = tk.PhotoImage(file=CARD_FRONT)

    def setup_canvas(self):
        """Initializes the canvas and adds the image."""
        # instantiate a Canvas where the image will be laid out
        self.canvas = ctk.CTkCanvas(
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            highlightthickness=0,
            bg="white",
        )
        self.canvas.grid(row=1, column=0, padx=25, pady=25, columnspan=2)

    def setup_labels(self):
        """Creates and place the translated text on the canvas."""

        # delete previous displayed word/title before generating the new random one
        self.canvas.delete("tag_word")

        # Fetch a new question each time
        try:
            new_question, answer = self.pick_random_question(self.questions)
            self.current_answer = answer  # Save the current answer for validation
            # once selected the question is selected, remove it from the dictionary
            removed_value = self.questions.pop(new_question)
        except (ValueError, UnboundLocalError):
            # the number of questions are ended, therefore close the application.
            new_question = "No more card left. Thanks for playing with us!"
            # self.window.after(10000, func=exit())

        # do not need to use grid, because you are already placing the text by using x and y
        if new_question == "No more card left. Thanks for playing with us!":
            self.canvas.create_text(
                X_WORD_PLACE,
                Y_WORD_PLACE,
                text=new_question,  # add the new question as test into the canvas
                font=("Arial", 15),
                tags="tag_word",  # assign a tag to be used for deletion
                width=300,
            )
            self.accept_button.configure(
                state="disabled",
                text="",
            )
            self.refuse_button.configure(
                state="disabled",
                text="",
            )
            self.window.after(5000, func=self.window.destroy)
        else:
            self.canvas.create_text(
                X_WORD_PLACE,
                Y_WORD_PLACE,
                text=new_question,  # add the new question as test into the canvas
                font=("Arial", 15),
                tags="tag_word",  # assign a tag to be used for deletion
                width=300,
            )

    def setup_buttons(self):
        """Create the Accept and Refuse buttons"""

        # TRUE button
        true_button_image = ctk.CTkImage(
            light_image=Image.open(TRUE_BUTTON_IMAGE),
            size=(80, 80),
        )

        self.accept_button = ctk.CTkButton(
            master=self.window,
            image=true_button_image,
            # define the text to be retrieved when the button is pressed
            text="True",
            text_color=BACKGROUND,
            fg_color="transparent",
            bg_color=BACKGROUND,
            hover_color=BACKGROUND,
            # use multiple functions in sequence by clicking the button
            command=lambda: [
                self.validate_answer(self.accept_button),
                self.setup_labels(),
            ],
        )
        self.accept_button.grid(row=2, column=0)

        # FALSE button
        false_button_image = ctk.CTkImage(
            light_image=Image.open(FALSE_BUTTON_IMAGE),
            size=(80, 80),
        )

        self.refuse_button = ctk.CTkButton(
            master=self.window,
            image=false_button_image,
            # define the text to be retrieved when the button is pressed
            text="False",
            text_color=BACKGROUND,
            fg_color="transparent",
            bg_color=BACKGROUND,
            hover_color=BACKGROUND,
            # use multiple functions in sequence by clicking the button
            command=lambda: [
                self.validate_answer(self.refuse_button),
                self.setup_labels(),
            ],
        )
        self.refuse_button.grid(row=2, column=1)

    def pick_random_question(self, question_list: dict) -> str:
        """Return a random question picked from the Open Trivia API.

        Parameters
        ----------
        question_list : list
            A list of questions taken from the Open Trivia API.

        Returns
        -------
        str
            One random question picked from the list.
        """
        try:
            pick_random_question = choice(list(question_list.items()))
            return pick_random_question
        except IndexError:
            pick_random_question = ()
            return pick_random_question

    def validate_answer(self, button):
        """Validates the user's answer by comparing button text with the correct answer."""
        user_answer = button.cget("text")  # Retrieve text from button
        if user_answer == self.current_answer:
            self.correct_answer_canvas_bg("correct")
            self.window.after(USER_FEEDBACK_BG_TIME, func=self.revert_canvas_bg)
        else:
            self.correct_answer_canvas_bg("incorrect")
            self.window.after(USER_FEEDBACK_BG_TIME, func=self.revert_canvas_bg)

        # Update the score label on the window
        self.display_points.configure(text=f"Score points: {self.score_point}")

    def display_score(self):
        self.display_points = ctk.CTkLabel(
            master=self.window,
            text=f"Score points: {self.score_point}",
            bg_color=BACKGROUND,
            text_color="black",
            font=("Courier New", 15, "bold"),
        )
        self.display_points.grid(row=0, column=0, ipadx=3, sticky="n")

    def correct_answer_canvas_bg(self, answer: str) -> None:
        """If the answer is correct, then turn the Canvas background to green and score a point for the user.
        Otherwise, turn the Canvas background to red.

        Parameters
        ----------
        answer : str
            _description_
        """
        if answer == "correct":
            self.score_point += 1
            print(f"Correct! Current score is: {self.score_point}")
            self.canvas.configure(
                bg="green",
            )
        elif answer == "incorrect":
            print(f"Incorrect! Current score is: {self.score_point}")
            self.canvas.configure(
                bg="red",
            )

    def revert_canvas_bg(self) -> None:
        """Revert the Canvas background color back to white"""
        self.canvas.configure(
            bg="white",
        )
