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
    YELLOW,
)


class FlashCardUI:
    def __init__(self) -> None:
        self.setup_window()
        self.setup_canvas()
        self.setup_buttons()
        self.window.mainloop()

    def setup_window(self):
        """Initializes the main window settings."""
        self.window = tk.Tk()
        self.window.title("Flash Cards")
        self.window.config(padx=10, pady=25)
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
        self.canvas = tk.Canvas(
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
        self.canvas.grid(row=0, column=1)

    def setup_buttons(self):
        """Create the Accept and Refuse buttons"""

        # accept button
        # accept_button_image = ctk.CTkImage(Image.open(ACCEPT_BUTTON_IMAGE))

        accept_button_image = ImageTk.PhotoImage(file=ACCEPT_BUTTON_IMAGE)
        self.accept_button = ctk.CTkButton(
            master=self.window,
            image=accept_button_image,
            text="",
            fg_color="transparent",
            bg_color=BACKGROUND,
            hover_color=BACKGROUND,
        )
        self.accept_button.grid(row=3, column=2)

        # refuse button
        # refuse_button_image = ctk.CTkImage(Image.open(REFUSE_BUTTON_IMAGE))

        refuse_button_image = ImageTk.PhotoImage(file=REFUSE_BUTTON_IMAGE)
        self.refuse_button = ctk.CTkButton(
            master=self.window,
            image=refuse_button_image,
            text="",
            fg_color="transparent",
            bg_color=BACKGROUND,
            hover_color=BACKGROUND,
        )
        self.refuse_button.grid(row=3, column=0)
