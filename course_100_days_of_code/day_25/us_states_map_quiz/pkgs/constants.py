import os

# --- CONSTANTS --- #
SCREEN_WIDTH = 725
SCREEN_HEIGHT = 491
# dynamically get the absolute path to the image
IMAGE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "attachments",
    "blank_states_img.gif",
)
CSV_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "attachments",
    "50_states.csv",
)
TEXTINPUT_TITLE = "Guess Country Name"
TEXT_INPUT = "Insert the name of a US State:"
MAX_COUNT_STATES = 50
