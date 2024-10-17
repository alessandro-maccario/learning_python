import os
import sys
import tkinter as tk

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import PINK, RED, GREEN, YELLOW, WHITE, FONT_NAME
from pkgs.save_data import Add2CSV
from pkgs.generate_password import GeneratePassword


class PasswordManagerUI:
    def __init__(self) -> None:
        self.setup_window()
        self.setup_canvas()
        self.setup_labels()
        self.setup_input_components()
        self.setup_buttons()
        self.window.mainloop()

    def setup_window(self):
        """Initializes the main window settings."""
        self.window = tk.Tk()
        # self.window.clipboard_clear()
        # self.window.clipboard_append('i can has clipboardz?')
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50, bg=WHITE)

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
        # highlightthickness=0 -> needed to remove a white border that was still there
        self.canvas = tk.Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
        self.locker_pic = tk.PhotoImage(
            file="day_29/password_manager/attachments/logo.png"
        )
        self.canvas.create_image(100, 100, image=self.locker_pic)
        self.canvas.grid(row=0, column=1)

    def setup_labels(self):
        """Creates and places labels."""
        # website label
        self.website_label = tk.Label(text="Website", bg=WHITE)
        self.website_label.grid(row=1, column=0, sticky="w")

        # email/username label
        self.email_username = tk.Label(text="Email/Username", bg=WHITE)
        self.email_username.grid(row=2, column=0, sticky="w")

        # password label
        self.password = tk.Label(text="Password", bg=WHITE)
        self.password.grid(row=3, column=0, sticky="w")

    def setup_input_components(self):
        """Creates and places input components."""
        # Input component for website
        self.website_input_component = tk.Entry(width=51)
        self.website_input_component.grid(row=1, column=1, columnspan=2)
        self.website_input_component.focus()

        # Input component for email/username
        self.email_username_input_component = tk.Entry(width=51)
        self.email_username_input_component.grid(row=2, column=1, columnspan=2)

        # Input component for password
        self.password_input_component = tk.Entry(width=32)
        self.password_input_component.grid(row=3, column=1)

    def setup_buttons(self):
        """Create the Generate password button and the Add button"""

        # instantiate the password generator class as an attribute to be able to use the output
        self.passwd_generator = GeneratePassword(
            main_window=self.window,
            password_input_component=self.password_input_component,
        )

        self.generate_passwd_button = tk.Button(
            text="Generate Password", command=self.passwd_generator.fill_password_entry
        )
        self.generate_passwd_button.grid(row=3, column=2)

        # instantiate the class Add2CSV to save the data once the add button is clicked
        save_data = Add2CSV(
            self.website_input_component,
            self.email_username_input_component,
            self.password_input_component,
        )
        # self.add_button = tk.Button(text="Add", width=43, command=save_data.save2csv)
        self.add_button = tk.Button(text="Add", width=43, command=save_data.save2json)
        self.add_button.grid(row=4, column=1, columnspan=2)
