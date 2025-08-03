import os
import pandas as pd
from random import choice

from pkgs.constants import DE_EN_DATA, WORDS_TO_LEARN


class GermanEnglishTranslation:
    def __init__(self) -> None:
        self.df = None

    def data_reader(self) -> dict:
        """Create a dictionary from the dataframe"""
        self.df = pd.read_csv(DE_EN_DATA, sep=",")
        df_to_dict = self.df.to_dict(orient="records")
        return df_to_dict

    def random_translation_selection(self) -> dict:
        """Pick a random dictionary from the data_reader"""
        return choice(self.data_reader())

    def dict_2_list(self) -> list:
        """Take the random_translation_selection and make a list out of it"""
        return self.random_translation_selection().values()

    def words_2_learn(self, easy_words) -> None:
        """Create a words_to_learn.csv file if does not exist, otherwise append the already known words"""
        # Define file path
        file_path = WORDS_TO_LEARN

        # Check if file exists
        file_exists = os.path.isfile(file_path)

        # Create a DataFrame with the new word to append
        d = {"german": [easy_words[0]], "english": [easy_words[1]]}
        new_to_append = pd.DataFrame(data=d)

        # If the file doesn't exist, write with header; if it does, append without header
        if not file_exists:
            new_to_append.to_csv(
                file_path, mode="w", header=["german", "english"], index=False
            )
        else:
            new_to_append.to_csv(file_path, mode="a", header=False, index=False)

        # remove the word that has been considered easy and already know by the user
        self.remove_known_words(easy_words)

    def remove_known_words(self, easy_words) -> None:
        """Search for the row index of the pair and remove it if the user knows it already"""
        # Filter out the dictionary that matches random_translation_selection
        idx_to_remove = self.df[
            (
                (self.df["german"] == easy_words[0])
                & (self.df["english"] == easy_words[1])
            )
        ].index
        # remove the specific word that has been already learnt
        self.df.drop(idx_to_remove[0], inplace=True)
        # Save the updated DataFrame back to the CSV
        self.df.to_csv(DE_EN_DATA, index=False)
