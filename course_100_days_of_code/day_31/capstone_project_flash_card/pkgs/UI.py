import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.constants import (
    BACKGROUND,
    CANVAS_WIDTH,
    CANVAS_HEIGHT,
    ACCEPT_BUTTON_IMAGE,
    REFUSE_BUTTON_IMAGE,
    CARD_FRONT,
    CARD_BACK,
    X_TITLE_PLACE,
    Y_TITLE_PLACE,
    X_WORD_PLACE,
    Y_WORD_PLACE,
)
from pkgs.data_reading import GermanEnglishTranslation


class FlashCardUI:
    def __init__(self) -> None:
        self.setup_window()
        self.setup_canvas()
        self.setup_labels()
        self.setup_buttons()
        self.window.mainloop()

    def setup_window(self):
        """Initializes the main window settings."""
        self.window = tk.Tk()
        self.window.title("Flash Cards")
        self.window.config(padx=50, pady=50)
        self.window.configure(background=BACKGROUND)

        # position the Tkinter window at the center of the screen
        w = self.window.winfo_reqwidth()
        h = self.window.winfo_reqheight()
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws / 4) - (w / 4)
        y = (hs / 4) - (h / 4)
        self.window.geometry("+%d+%d" % (x, y))
        self.flashcard_picture_back = tk.PhotoImage(file=CARD_BACK)

    def setup_canvas(self):
        """Initializes the canvas and adds the image."""
        # instantiate a Canvas where the image will be laid out
        self.canvas = ctk.CTkCanvas(
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            highlightthickness=0,
            bg=BACKGROUND,
        )
        self.flashcard_picture_front = tk.PhotoImage(file=CARD_FRONT)
        self.canvas.create_image(
            CANVAS_WIDTH / 2,
            CANVAS_HEIGHT / 2,
            image=self.flashcard_picture_front,
            tags=(
                "card_front"
            ),  # give a tag to be referenced when flipping to the back card
        )
        self.canvas.grid(row=0, column=0, columnspan=2)

    def setup_labels(self):
        """Creates and place the translated text on the canvas."""

        # delete previous displayed word/title before generating the new random one
        self.canvas.delete("tag_word")
        self.canvas.delete("card_title")
        # Instantiate the GermanEnglishTranslation class from where to get the random words
        german_english_translation = GermanEnglishTranslation()
        # grab the original and the translated word
        self.german_word, self.english_word = german_english_translation.dict_2_list()

        # do not need to use grid, because you are already placing the text by using x and y
        self.title_word = self.canvas.create_text(
            X_TITLE_PLACE,
            Y_TITLE_PLACE,
            text="German",
            font=("Arial", 20),
            tags=("card_title"),
        )
        self.translated_word = self.canvas.create_text(
            X_WORD_PLACE,
            Y_WORD_PLACE,
            text=f"{self.german_word}",
            font=("Arial", 50),
            tag="tag_word",  # assign a tag to be used for deletion
        )
        self.flip_card()
        self.canvas.itemconfig(
            tag_or_id="card_front", image=self.flashcard_picture_front
        )

    def flip_card(self):
        """After 3 seconds (3000ms), flip the card and show the translation"""
        self.waiting_to_flip = self.window.after(3000, func=self.show_back)

    def show_back(self):
        """Show the back side of the flashcard with the translation."""
        self.canvas.itemconfig(
            tag_or_id="card_front", image=self.flashcard_picture_back
        )
        self.canvas.itemconfig(tag_or_id="card_title", text="English", fill="white")
        self.canvas.itemconfig(
            tag_or_id="tag_word", text=f"{self.english_word}", fill="red"
        )
        # need to restart the 3 seconds counter
        self.window.after_cancel(self.waiting_to_flip)

    def setup_buttons(self):
        """Create the Accept and Refuse buttons"""

        # accept button
        accept_button_image = ctk.CTkImage(
            light_image=Image.open(ACCEPT_BUTTON_IMAGE),
            dark_image=Image.open(ACCEPT_BUTTON_IMAGE),
            size=(80, 80),
        )

        self.accept_button = ctk.CTkButton(
            master=self.window,
            image=accept_button_image,
            text="",
            fg_color="transparent",
            bg_color=BACKGROUND,
            hover_color=BACKGROUND,
            command=self.setup_labels,
        )
        self.accept_button.grid(row=2, column=0)

        # refuse button
        refuse_button_image = ctk.CTkImage(
            light_image=Image.open(REFUSE_BUTTON_IMAGE),
            dark_image=Image.open(REFUSE_BUTTON_IMAGE),
            size=(80, 80),
        )

        self.refuse_button = ctk.CTkButton(
            master=self.window,
            image=refuse_button_image,
            text="",
            fg_color="transparent",
            bg_color=BACKGROUND,
            hover_color=BACKGROUND,
            command=self.setup_labels,
        )
        self.refuse_button.grid(row=2, column=1)
