import os
import sys
import tkinter as tk
from PIL import ImageTk
import customtkinter as ctk

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.constants import BACKGROUND


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
        self.window.config(padx=50, pady=50)
        self.window.configure(background=BACKGROUND)

        # position the Tkinter window at the center of the screen
        w = self.window.winfo_reqwidth()
        h = self.window.winfo_reqheight()
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws / 2.5) - (w / 2.5)
        y = (hs / 4) - (h / 4)
        self.window.geometry("+%d+%d" % (x, y))

    def setup_canvas(self):
        """Initializes the canvas and adds the image."""
        # instantiate a Canvas where the image will be laid out
        self.canvas = tk.Canvas(width=350, height=250, highlightthickness=0)
        self.flashcard_pic = tk.PhotoImage(
            file="day_31/capstone_project_flash_card/images/card_front.png"
        )
        self.canvas.create_image(100, 100, image=self.flashcard_pic)
        self.canvas.grid(row=0, column=1)

    def setup_buttons(self):
        """Create the Accept and Refuse buttons"""

        # accept button
        accept_button_image = ImageTk.PhotoImage(
            file="day_31/capstone_project_flash_card/images/right.png"
        )
        self.accept_button = ctk.CTkButton(self.window, image=accept_button_image)
        self.accept_button.grid(row=3, column=2)

        # refuse button
        refuse_button_image = ImageTk.PhotoImage(
            file="day_31/capstone_project_flash_card/images/wrong.png"
        )
        self.refuse_button = ctk.CTkButton(self.window, image=refuse_button_image)
        self.refuse_button.grid(row=3, column=0)
