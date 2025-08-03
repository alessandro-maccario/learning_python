"""
Helper file for storing constants and small functions.
"""

# --- GLOBAL VARIABLES --- #
easy_level = 10
hard_level = 7


# --- FUNCTIONS --- #
def input_difficulty_level() -> str:
    """
    Ask the player for the difficulty level that they want to play


    Returns
    -------
    str
        Return if the user selected 'easy' or 'hard' difficulty level.
    """
    return input("Choose a difficulty. Type 'easy' or 'hard': ")


def make_a_guess() -> int:
    """
    Ask the player for a guess of the random selected number.


    Returns
    -------
    int
        Return if the number inserted is above or below the random generated number.
    """
    while True:
        try:
            return int(input("Make a guess: "))
        except TypeError:
            print("Please, provide an integer between 1 and 100.")
            continue


def conditional_winning(player_guess: int, number_to_guess: int) -> str:
    """Definition of what the output of the user interaction can be.

    Parameters
    ----------
    player_guess : int
        The integer that the user guessed
    number_to_guess : int
        The final number to be guessed

    Returns
    -------
    str
        Returns a string either winning, too low or too high.
    """
    if player_guess == number_to_guess:
        return "winning"
    elif player_guess > number_to_guess:
        return "too_high"
    elif player_guess < number_to_guess:
        return "too_low"
