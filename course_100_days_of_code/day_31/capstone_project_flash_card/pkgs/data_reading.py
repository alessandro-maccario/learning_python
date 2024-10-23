import pandas as pd


class GermanEnglishTranslation:
    def __init__(self) -> None:
        pass

    def data_reader(self):
        df = pd.read_csv(
            "day_31/capstone_project_flash_card/data/de_100_words.txt", sep=","
        )
        return df
