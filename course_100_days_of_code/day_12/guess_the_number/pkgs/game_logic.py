"""
Module to store the game logic
"""

from pkgs.helper import make_a_guess, conditional_winning


def game_logic(
    number_of_attempts: int, number_to_guess: int, dict_guessing: dict
) -> None:
    """Encapsulation of the game logic where the player decides the game level difficulties
    and tries to guess the number.

    Parameters
    ----------
    number_of_attempts : int
        Number of attempts available so far
    number_to_guess : int
        Final number to guess
    dict_guessing : dict
        Dictionary containing the strings "TOO LOW" or "TOO HIGH"
    """
    while number_of_attempts > 0:
        player_guess = make_a_guess()

        # did the user guessed correctly or too low/too high?
        output = conditional_winning(player_guess, number_to_guess)
        # if output == "too_high" or output == "too_low":
        if output in dict_guessing:
            # for each wrong answer, reduce the number of attempts
            number_of_attempts -= 1
            print(f"Number guessed {dict_guessing[output]}, try again.")
            print("Number of attempts available: ", number_of_attempts)
            continue
        # if the user wins
        elif output == "winning":
            print(f"You got it! The answer was {number_to_guess}!")
            return
        # if the user loses
        else:
            print(
                f"Sorry, number of attempts are finished. The correct number was {number_to_guess}"
            )
            return
