import os
import sys
import tkinter as tk

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import PINK, RED, GREEN, YELLOW, FONT_NAME


class PasswordManagerUIOLD:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Password Manager")
        self.window.geometry("600x400")
        self.window.config(padx=120, pady=10, bg="grey")

        # instantiate a Canvas where the image will be laid out
        # highlightthickness=0 -> needed to remove a white border that was still there
        self.canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
        self.locker_pic = tk.PhotoImage(
            file="day_29/password_manager/attachments/logo.png"
        )
        self.canvas.create_image(100, 100, image=self.locker_pic)
        self.canvas.grid(row=0, column=1)

        # timer label component
        self.website_label = tk.Label(
            text="Website", font=(FONT_NAME, 11, "bold"), bg="white"
        )
        self.website_label.grid(row=1, column=0)

        # Input component
        self.website_input_component = tk.Entry(width=35)
        self.website_input_component.grid(row=1, column=1, columnspan=3)

        self.window.mainloop()


class PasswordManagerUI:
    def __init__(self) -> None:
        self.setup_window()
        self.setup_canvas()
        self.setup_labels()
        self.setup_input_components()
        self.window.mainloop()

    def setup_window(self):
        """Initializes the main window settings."""
        self.window = tk.Tk()
        self.window.title("Password Manager")
        self.window.geometry("600x400")
        self.window.config(padx=120, pady=10, bg="grey")

    def setup_canvas(self):
        """Initializes the canvas and adds the image."""
        # instantiate a Canvas where the image will be laid out
        # highlightthickness=0 -> needed to remove a white border that was still there
        self.canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
        self.locker_pic = tk.PhotoImage(
            file="day_29/password_manager/attachments/logo.png"
        )
        self.canvas.create_image(100, 100, image=self.locker_pic)
        self.canvas.grid(row=0, column=1)

    def setup_labels(self):
        """Creates and places labels."""
        # timer label component
        self.website_label = tk.Label(
            text="Website", font=(FONT_NAME, 11, "bold"), bg="white"
        )
        self.website_label.grid(row=1, column=0)

    def setup_input_components(self):
        """Creates and places input components."""
        # Input component
        self.website_input_component = tk.Entry(width=35)
        self.website_input_component.grid(row=1, column=1, columnspan=3)
