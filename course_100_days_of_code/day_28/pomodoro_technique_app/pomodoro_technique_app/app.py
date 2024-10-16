"""
Script to create a Pomodoro Technique App by using Python for the 100 Days of Code challenge from the Udemy course.

References
    1. https://docs.python.org/3/library/tk.html
    2. https://www.tcl.tk/man/tcl8.5/TkCmd/event.htm

"""

# --- IMPORT PACKAGES --- #
import os
import sys
import tkinter as tk

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import (
    PINK,
    RED,
    GREEN,
    YELLOW,
    FONT_NAME,
    WORK_MIN,
    SHORT_BREAK_MIN,
    LONG_BREAK_MIN,
)

# --- GLOBAL VARIABLES --- #
repetitions = 0
after_id = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """Reset the timer and stop the countdown."""
    global after_id, repetitions

    if after_id:
        window.after_cancel(after_id)  # Cancel the ongoing countdown
    after_id = None

    # Reset the timer display
    canvas.itemconfig(text_timer_label, text="00:00")
    # Reset the checkmarks
    checkmark_label.config(
        text="",
        fg=GREEN,
        bg=YELLOW,
        font=(FONT_NAME, 15),
    )
    # Reset the timer label
    timer_label.config(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
    # Reset repetitions so that when the "Start" button is pressed again it increases from the beginning
    repetitions = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_countdown():
    """This function is called by the button "Start" to start the countdown"""
    global repetitions, complete_work
    # update the reps to mirror the amount of repetitions passed
    repetitions += 1

    # convert from minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # convert the WORK_MIN in minutes
    if repetitions % 8 == 0:
        # take a long break
        countdown(long_break_sec)
        # update the TIMER label to be RED
        timer_label.config(
            text="Break", font=(FONT_NAME, 32, "bold"), fg=RED, bg=YELLOW
        )
    elif repetitions % 2 == 0:
        # take a short break
        countdown(short_break_sec)
        # update the TIMER label to be PINK
        timer_label.config(
            text="Break", font=(FONT_NAME, 32, "bold"), fg=PINK, bg=YELLOW
        )
    else:
        # working time
        countdown(work_sec)
        # update the TIMER label to be GREEN
        timer_label.config(
            text="Work", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW
        )
        print("Repetitions:", repetitions)
        mark = ""
        work_session = repetitions // 2
        for i in range(work_session):
            # add the counter to the label again with the increase completed work
            mark += "✓"
            checkmark_label.config(
                text=f"{mark}",
                fg=GREEN,
                bg=YELLOW,
                font=(FONT_NAME, 15),
            )


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """Recursive function to create a countdown.

    Parameters
    ----------
    count : int
        Number of seconds from which you cound down
    """
    global after_id  # Reference the global variable

    # convert seconds to minutes
    minutes, seconds = divmod(count, 60)
    minutes = int(minutes)
    seconds = round(seconds, 2)
    print(minutes, seconds)

    if len(str(seconds)) == 1:
        seconds = f"0{str(seconds)}"

    # need to change the time that is in the Canvas
    canvas.itemconfig(text_timer_label, text=f"{minutes}:{seconds}")
    if count > 0:
        after_id = window.after(1000, countdown, count - 1)
    else:
        start_countdown()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# instantiate a Canvas where the image will be laid out
canvas = tk.Canvas(
    width=200, height=224, bg=YELLOW, highlightthickness=0
)  # highlightthickness=0 -> needed to remove a white border that was still there
tomato_pic = tk.PhotoImage(file="day_28/pomodoro_technique_app/attachments/tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
text_timer_label = canvas.create_text(
    102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)

# timer label component
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# create the start button
start_button = tk.Button(text="Start", font=FONT_NAME, command=start_countdown)
start_button.grid(row=3, column=0)

# create the reset button
reset_button = tk.Button(text="Reset", font=FONT_NAME, command=reset_timer)
reset_button.grid(row=3, column=3)

# checkmark component
checkmark_label = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
checkmark_label.grid(row=3, column=1)


# keep the window open
window.mainloop()
