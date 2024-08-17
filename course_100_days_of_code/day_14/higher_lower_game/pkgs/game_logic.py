"""
Functions that include the game logic.
"""

from pkgs.ascii_art import vs_logo


def correct_answer(higher_follower_value: str, score: int) -> tuple[str, int]:
    """_summary_

    Parameters
    ----------
    higher_follower_value : str
        Either comparison_a or comparison_b, depending who has more followers
    score : int
        Current number of correct answers from the player

    Returns
    -------
    tuple[str, int]
        Returns previous_option and score
    """
    print("Correct answer!")
    score += 1
    previous_option = None
    previous_option = higher_follower_value
    return previous_option, score


def compare_number_followers(
    decision: str,
    comparison_a: int,
    comparison_b: int,
    score: int,
    previous_option: list,
):
    # compare number of followers
    if decision == "A":
        if comparison_a["follower_count"] > comparison_b["follower_count"]:
            previous_option, score = correct_answer(comparison_a, score)
            return previous_option, score
        else:
            print("Wrong answer!")
            return
    elif decision == "B":
        if comparison_b["follower_count"] > comparison_a["follower_count"]:
            previous_option, score = correct_answer(comparison_b, score)
            return previous_option, score
        else:
            print("Wrong answer!")
            return


def print_comparison(comparison_a: dict, comparison_b: dict) -> None:
    """Print the information about the comparison_a and comparison_b dicts.

    Parameters
    ----------
    comparison_a : dict
        Contains the information about the first value to compare against the second
    comparison_b : dict
        Contains the information about the second value to compare against the first
    """

    print(
        f"Comparison A: {comparison_a["name"]}, {comparison_a["description"]}, with {comparison_a["follower_count"]} followers, from {comparison_a["country"]}."
    )
    print(vs_logo)
    print(
        f"Against comparison B: {comparison_b["name"]}, {comparison_b["description"]}, from {comparison_b["country"]}."
    )


def end_game_comment(count_correct_answer) -> None:
    """Return a comment in case the average count_correct_score is above or below the average."""
    if count_correct_answer <= 3:
        print(f"Too bad, try again! Highest score: {count_correct_answer}")
        return
    else:
        print(
            f"Above the average of 3 correct answer! Good job! Highest score: {count_correct_answer}"
        )
        return


def input_decision():
    # let the player decides which one between A and B is correct
    decision = input("Who has more followers? Type 'A' or 'B': ").upper()
    while decision not in ("a", "A", "b", "B"):
        print("Please, provide a valid input, type 'a', 'A' or 'b', 'B'.")
        decision = input("Who has more followers? Type 'A' or 'B': ").upper()
        continue

    return decision
