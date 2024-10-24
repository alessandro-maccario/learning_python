import pandas as pd
from random import choice

from pkgs.constants import DE_EN_DATA


class GermanEnglishTranslation:
    def __init__(self) -> None:
        pass

    def data_reader(self) -> dict:
        df = pd.read_csv(DE_EN_DATA, sep=",")
        df_to_dict = df.to_dict(orient="records")
        return df_to_dict

    def random_translation_selection(self) -> dict:
        """Pick a random dictionry from the data_reader"""
        return choice(self.data_reader())

    def dict_2_list(self) -> list:
        """Take the random_translation_selection and make a list out of it"""
        return self.random_translation_selection().values()
