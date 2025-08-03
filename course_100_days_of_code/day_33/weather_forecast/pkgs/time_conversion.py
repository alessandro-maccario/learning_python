import numpy as np
import pandas as pd


class TimeConversion:
    def __init__(self) -> None:
        pass

    def seconds2minutes(self, seconds: np.array) -> np.array:
        """Convert the seconds to minutes

        Parameters
        ----------
        seconds : float
            Seconds as floats

        Returns
        -------
        float
            Return the converted seconds to minutes
        """
        if seconds is None:
            pass
        else:
            seconds = seconds / 60
        return seconds

    def minutes2hours(self, minutes: float) -> float:
        """Convert the minutes to hours

        Returns
        -------
        float
            Return the converted minutes to hours
        """
        if minutes is None:
            pass
        else:
            minutes = minutes / 60
        return minutes
