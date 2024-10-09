"""
Script to create a simple Miles to KM converter by using Python for the 100 Days of Code challenge from the Udemy course.

References
    1. https://docs.python.org/3/library/tk.html
    2. https://www.tcl.tk/man/tcl8.5/TkCmd/event.htm

Problem Breakdown:
    1.
    2.


Requirements:
    -

"""

# --- IMPORT PACKAGES --- #
import tkinter as tk

# instantiate the tkinter window
window = tk.Tk()
window.title("Mile2KM Converter")
# define a minimum size: if there are more elements or the user resizes the window, it is allowed
window.minsize(width=500, height=300)


"""
    Components:
        - first instantiate the component
        - define how to visualize it to show it
"""
# label component
lab = tk.Label(text="Label 1", font=("Arial", 15, "bold"))
lab.pack()  # pack the label on the screen and automatically center it


def button_clicked():
    lab.config(text=entry_component.get())


# create a button
button = tk.Button(text="Click me", command=button_clicked)
button.pack()


# Entry component
entry_component = tk.Entry()
entry_component.pack()

# keep the window on the screen and wait for user's input
window.mainloop()
