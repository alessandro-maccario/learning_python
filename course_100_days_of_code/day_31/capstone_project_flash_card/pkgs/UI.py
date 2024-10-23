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
    X_GERMAN_WORD_PLACE,
    Y_GERMAN_WORD_PLACE,
    X_ENGLISH_WORD_PLACE,
    Y_ENGLISH_WORD_PLACE,
)


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

    def setup_canvas(self):
        """Initializes the canvas and adds the image."""
        # instantiate a Canvas where the image will be laid out
        self.canvas = ctk.CTkCanvas(
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            highlightthickness=0,
            bg=BACKGROUND,
        )
        self.flashcard_pic = tk.PhotoImage(file=CARD_FRONT)
        self.canvas.create_image(
            CANVAS_WIDTH / 2,
            CANVAS_HEIGHT / 2,
            image=self.flashcard_pic,
        )
        self.canvas.grid(row=0, column=0, columnspan=2)

    def setup_labels(self):
        """Creates and place the translated text on the canvas."""
        # do not need to use grid, because you are already placing the text by using x and y
        self.german_word = self.canvas.create_text(
            CANVAS_WIDTH / 2, CANVAS_HEIGHT / 4, text="COD"
        )
        self.english_word = self.canvas.create_text(
            CANVAS_WIDTH / 2, CANVAS_HEIGHT / 1.5, text="COD"
        )

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
        )
        self.refuse_button.grid(row=2, column=1)
