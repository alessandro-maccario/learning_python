class TimeConversion:
    def __init__(self) -> None:
        pass

    def seconds2minutes(self, seconds: float) -> float:
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
        return seconds / 60

    def minutes2hours(self) -> float:
        """Convert the minutes to hours

        Returns
        -------
        float
            Return the converted minutes to hours
        """
        return self.seconds2minutes / 60
