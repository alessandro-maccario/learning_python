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

Components:
        - first instantiate the component
        - define how to visualize it to show it

    Layout Manager: (Geometry Manager)
        - Decision to use Grid for its higher flexibility

"""

# --- IMPORT PACKAGES --- #
import os
import sys
import tkinter as tk

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# --- FUNCTIONS --- #
def mile2km():
    miles = float(input_component.get())
    km = miles * 1.609
    label_miles2km.config(text=km)


# --- MAIN --- #
# instantiate the tkinter window
window = tk.Tk()
window.title("Mile2KM Converter")
# define a minimum size: if there are more elements or the user resizes the window, it is allowed
window.minsize(width=200, height=100)
window.config(padx=30, pady=10)  # add space around the widgets

# Input component
input_component = tk.Entry(width=15)
input_component.grid(row=0, column=1)

# equal_to component
label_equal = tk.Label(text="is equal to", font=("Arial", 9, "bold"))
label_equal.grid(row=1, column=0)

# Miles component
label_miles = tk.Label(text="Miles", font=("Arial", 9, "bold"))
label_miles.grid(row=1, column=2)

# Current conversion component
label_miles2km = tk.Label(text="0", font=("Arial", 9, "bold"))
label_miles2km.grid(row=1, column=1)

# create a button to convert the miles into km
button = tk.Button(text="Calculate", command=mile2km)
button.grid(row=2, column=1)


# keep the window on the screen and wait for user's input
window.mainloop()
