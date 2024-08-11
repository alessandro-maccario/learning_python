"""
Script for creating the game hangman based on the Udemy course
"100 Days of Code: The Complete Python Pro Bootcamp".
"""

# --- Import packages --- #
import os
import sys
import random

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.ascii_art import stages, logo


def main():
    # define which char to use for empty spaces in the word
    underscore_placemark = "_"

    # generate a random word by creating a list of words from the dictionary.txt file
    with open(
        r"C:\solutions\learning_python\project_hangman\pkgs\dictionary.txt", "r"
    ) as word_dict:
        # create a random word list
        random_words = [line for line in word_dict]

    # gets a random word based on the random_words list and remove the new line char
    chosen_word = random.choice(random_words).strip("\n")
    # get as many "_" as the letters in the chosen random word
    new_string = underscore_placemark * len(chosen_word)

    # print the logo
    print(logo)

    # print the random word as a series of "_"
    print("Random word: ", new_string)

    # first convert the string to a list
    chosen_word_list = list(chosen_word)
    chosen_word_set = set(chosen_word_list)
    attempts = len(stages)  # len of the list based on the ascii hangman art

    while len(chosen_word_set) > 0:
        # if the user reached the total amounts of attempts
        if attempts == 0:
            print(
                f"Sorry, word {chosen_word.upper()} not guessed with the total amount of attempts. Try again!"
            )
            break

        # let the user guess a letter from the word
        guess = input("Guess a letter: ").lower()

        # The line  os.system('cls' if os.name == 'nt' else 'clear') empties the terminal screen
        # at the beginning of every iteration by running cls if you're using a Windows machine and
        # clear if you're using a Unix based one.
        os.system("cls" if os.name == "nt" else "clear")

        if guess in chosen_word:
            # get the indexes of the chars in the chosen word
            char_idx = [idx for idx, char in enumerate(chosen_word) if guess == char]

            # convert the string to list (why? strings are immutable!)
            string_list = list(new_string)
            # for each guessed letter that has been found in the chosen_word
            for each_idx in char_idx:
                # replace the current "_" with the guessed letter
                string_list[each_idx] = guess
            # rejoin together the list as a new string
            new_string = "".join(string_list)
            print("Updated guess: ", new_string)

            if guess in chosen_word_set:
                chosen_word_set.remove(guess)
            else:
                continue

            if len(chosen_word_set) == 0:
                print("#-#-#-#-#-#-#-#-#-#-#-#")
                print(f"Great, you correctly guessed the word {new_string.upper()}!")
                print("#-#-#-#-#-#-#-#-#-#-#-#")
                break
        else:
            attempts -= 1
            remaining_attempts = attempts
            print("\n")
            print("Remaining attempts: ", remaining_attempts)
            print(stages[attempts])
            print("Try again, wrong guess!")
            print("Updated guess: ", new_string)
            print("#-#-#-#-#-#-#-#-#-#-#-#")


if __name__ == "__main__":
    main()
