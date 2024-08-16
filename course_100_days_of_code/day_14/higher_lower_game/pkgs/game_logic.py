"""
Functions that include the game logic.
"""

from pkgs.ascii_art import vs_logo


def compare_number_followers(
    decision: str,
    comparison_a: int,
    comparison_b: int,
    count_correct_answer: int,
    previous_option: list,
):
    # compare number of followers
    if decision == "A":
        if comparison_a["follower_count"] > comparison_b["follower_count"]:
            print("Correct answer!")
            count_correct_answer += 1
            previous_option = None
            previous_option = comparison_a
            return previous_option, count_correct_answer
        else:
            print("Wrong answer!")
            return
    elif decision == "B":
        if comparison_b["follower_count"] > comparison_a["follower_count"]:
            print("Correct answer!")
            count_correct_answer += 1
            previous_option = None
            previous_option = comparison_b
            return previous_option, count_correct_answer
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
        f"Against comparison b: {comparison_b["name"]}, {comparison_b["description"]}, from {comparison_b["country"]}."
    )
