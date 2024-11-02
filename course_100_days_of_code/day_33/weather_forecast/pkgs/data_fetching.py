import os
import sys
import json
import requests
import pandas as pd
from datetime import datetime, timedelta


# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import LAT_ARN, LONG_ARN, TIMEDELTA_DATE


class DataFetching:
    def __init__(self) -> None:
        pass

    def open_weather_request(self):
        API_OSWAPI = f"https://api.open-meteo.com/v1/forecast?latitude={LAT_ARN}&longitude={LONG_ARN}&hourly=temperature_2m&timezone=Europe%2FBerlin"

        today_date_formatted, future_date_formatted = (
            self.time_definition(timedelta_date=TIMEDELTA_DATE)[0],
            self.time_definition(timedelta_date=TIMEDELTA_DATE)[1],
        )
        # define required parameters for the API call
        params = {
            "latitude": LAT_ARN,
            "longitude": LONG_ARN,
            "start_date": today_date_formatted,
            "end_date": future_date_formatted,
            "daily": ["weather_code", "sunshine_duration", "rain_sum", "snowfall_sum"],
        }

        # send a request to the weather API
        oswapi_request = requests.get(API_OSWAPI, params=params)
        # grab the content of the request in a dict/json format
        oswapi_content = oswapi_request.json()

        # return the dataframe with the requested data from the API
        return self.build_dataframe(oswapi_content)

    def build_dataframe(self, data_json: dict) -> pd.DataFrame:
        """Grab the elevation, time and temperature from the JSON dict and build a df out of it

        Parameters
        ----------
        data_json : dict
            JSON dict data

        Returns
        -------
        pd.DataFrame
            Dataframe that contains the JSON data needed into a dataframe format.
        """
        oswapi_content_elevation = pd.Series(data_json["elevation"], name="elevation")
        oswapi_content_time = pd.Series(data_json["hourly"]["time"], name="time")
        oswapi_content_temperature = pd.Series(
            data_json["hourly"]["temperature_2m"], name="temperature"
        )
        # combine the multiple series into one
        df = pd.concat(
            [oswapi_content_elevation, oswapi_content_time, oswapi_content_temperature],
            axis=1,
        )
        # fill the nan in the "elevation" column to be the same value as the elevation
        df["elevation"] = df["elevation"].fillna(data_json["elevation"])

        return df

    def time_definition(self, timedelta_date: int) -> tuple[datetime, datetime]:
        """Define the start date and the end date.

        Parameters
        ----------
        timedelta_date : int
            Number of days in the future from the start date

        Returns
        -------
        tuple[datetime, datetime]
            today_date and future_date formatted to be YYY-MM-DD
        """
        today_date = datetime.today()
        future_date = timedelta(days=timedelta_date)
        today_date_formatted = today_date.strftime("%Y-%m-%d")
        future_date_formatted = (today_date + future_date).strftime("%Y-%m-%d")

        return today_date_formatted, future_date_formatted
