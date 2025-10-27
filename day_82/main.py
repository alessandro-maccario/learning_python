# Project day 82: Text to Morse Code Converter
# You will use what you've learnt to create a text-based (command line) program that takes any String input and converts it into Morse Code.
# You've created plenty of text-based programs in Days 1 -10, so look back at some of those projects if you don't remember what a text-base program looks like.
# To accept arguments from the command line that is values that we will pass into the programs that we call, we need to use a module called argparse.

#######################
### IMPORT PACKAGES ###
#######################
from constants import MORSE_CODE_DICT
import argparse

############
### MAIN ###
############


def text_to_morse_code(text: str) -> str:
    """Convert the input text into Morse Code.

    Parameters
    ----------
        text (str): The text to be converted into Morse code.

    Returns
    -------
        str: The Morse Code translation of the text.
    """
    output = ""
    for letter in text.upper():
        output = output + MORSE_CODE_DICT[letter]

    return output.strip()


# Define the parser object that knows how to. It reads the command-line text and converts it into Python variables.
parser = argparse.ArgumentParser(
    description="Convert any text given into Morse Code",
)

# Adding a command-line argument
parser.add_argument(
    "-t",
    "--text",
    metavar="text",
    required=True,
    help="The text to be converted to Morse Code.",
)

# Parsing the arguments. Read the arguments the user typed when running the script, and store them in args
args = parser.parse_args()

if __name__ == "__main__":
    print(text_to_morse_code(args.text))
