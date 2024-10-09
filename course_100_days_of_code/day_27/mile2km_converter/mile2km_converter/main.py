"""
Script to create a simple Miles to KM converter by using Python for the 100 Days of Code challenge from the Udemy course.

Problem Breakdown:
    1.
    2.


Requirements:
    -

"""

# --- IMPORT PACKAGES --- #
import tkinter

# instantiate the tkinter window
window = tkinter.Tk()
window.title("Mile2KM Converter")
# define a minimum size: if there are more elements or the user resizes the window, it is allowed
window.minsize(width=500, height=300)


"""
    Components:
        - first instantiate the component
        - define how to visualize it to show it
"""
# label component
lab = tkinter.Label(text="Label 1", font=("Arial", 15, "bold"))
lab.pack(side="left")  # pack the label on the screen and automatically center it


# keep the window on the screen and wait for user's input
window.mainloop()
