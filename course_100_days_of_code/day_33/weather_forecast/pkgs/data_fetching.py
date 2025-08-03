import os
import sys
import requests
import openmeteo_requests
import pandas as pd
from datetime import datetime, timedelta


# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import (
    LAT_ARN,
    LONG_ARN,
    LAT_KL,
    LONG_KL,
    LAT_VIH,
    LONG_VIH,
    TIMEDELTA_DATE_PAST,
)
from pkgs.time_conversion import TimeConversion


class DataFetching:
    def __init__(self) -> None:
        self.time_converter = TimeConversion()

    def open_weather_request_forecast(self) -> pd.DataFrame:
        """Request the data to https://open-meteo.com/en/docs regarding future data.

        Returns
        -------
        pd.DataFrame
            Dataframe containing the requested data from the Weather API about the forecasts.
        """

        # API URL request
        API_OSWAPI = "https://api.open-meteo.com/v1/forecast"
        # define required parameters for the API call
        params = {
            "latitude": [LAT_KL],
            "longitude": [LONG_KL],
            "daily": [
                "weather_code",
                "temperature_2m_max",
                "temperature_2m_min",
                "sunshine_duration",
                "rain_sum",
                "snowfall_sum",
            ],
            "timezone": "auto",
            "past_days": 31,
        }

        # send a request to the weather API
        oswapi_request = requests.get(API_OSWAPI, params=params)
        if len(params["latitude"]) > 1:
            # grab the content of the request in a dict/json format
            oswapi_content = oswapi_request.json()[0]
        else:
            # grab the content of the request in a dict/json format
            oswapi_content = [oswapi_request.json()]

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
        # grab the data from the JSON dict and construct pd.Series and then the final dataframe

        oswapi_content_latitude = pd.Series(
            [location["latitude"] for location in data_json], name="latitude"
        )
        oswapi_content_longitude = pd.Series(
            [location["longitude"] for location in data_json], name="longitude"
        )
        oswapi_content_elevation = pd.Series(
            [location["elevation"] for location in data_json], name="elevation"
        )
        oswapi_content_time = pd.Series(
            [location["daily"]["time"] for location in data_json], name="time"
        )
        oswapi_content_weather_code = pd.Series(
            [location["daily"]["weather_code"] for location in data_json],
            name="weather_code",
        )
        oswapi_content_temperature_max = pd.Series(
            [location["daily"]["temperature_2m_max"] for location in data_json],
            name="temperature_2m_max",
        )
        oswapi_content_temperature_min = pd.Series(
            [location["daily"]["temperature_2m_min"] for location in data_json],
            name="temperature_2m_min",
        )
        oswapi_content_sunshine_duration = pd.Series(
            [location["daily"]["sunshine_duration"] for location in data_json],
            name="sunshine_duration",
        )
        oswapi_content_rain_sum = pd.Series(
            [location["daily"]["rain_sum"] for location in data_json], name="rain_sum"
        )
        oswapi_content_snowfall_sum = pd.Series(
            [location["daily"]["snowfall_sum"] for location in data_json],
            name="snowfall_sum",
        )

        # TODO: to add the city information you can tap into openstreetmap to fetch the city name
        # TODO: based on the coordinates that the request gives you back

        # combine the multiple series into one
        df = pd.concat(
            [
                oswapi_content_latitude,
                oswapi_content_longitude,
                oswapi_content_elevation,
                oswapi_content_time,
                oswapi_content_weather_code,
                oswapi_content_temperature_max,
                oswapi_content_temperature_min,
                oswapi_content_sunshine_duration,
                oswapi_content_rain_sum,
                oswapi_content_snowfall_sum,
            ],
            axis=1,
        )

        # explode the dataframe so each row gets its own result
        df = df.explode(
            column=[
                "time",
                "weather_code",
                "sunshine_duration",
                "temperature_2m_min",
                "temperature_2m_max",
                "rain_sum",
                "snowfall_sum",
            ]
        ).reset_index(drop=True)

        # add the average temperature for each row based on max and min
        df["temperature_average"] = df[
            ["temperature_2m_min", "temperature_2m_max"]
        ].mean(axis=1)

        # convert sunshine_duration from seconds to minutes and to hours and add it to the dataframe
        df["minutes_sunshine_duration"] = df["sunshine_duration"].apply(
            self.time_converter.seconds2minutes
        )
        df["hours_sunshine_duration"] = df["minutes_sunshine_duration"].apply(
            self.time_converter.minutes2hours
        )

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
        past_date = timedelta(days=timedelta_date)
        today_date_formatted = today_date.strftime("%Y-%m-%d")
        past_date_formatted = (today_date - past_date).strftime("%Y-%m-%d")

        return today_date_formatted, past_date_formatted

    def open_weather_request_historical(self) -> pd.DataFrame:
        """Request the data to https://open-meteo.com/en/docs/historical-weather-api regarding historical data.

        Returns
        -------
        pd.DataFrame
            Dataframe containing the requested data from the Weather API about the past.
        """

        today_date_formatted, past_date_formatted = (
            self.time_definition(timedelta_date=TIMEDELTA_DATE_PAST)[0],
            self.time_definition(timedelta_date=TIMEDELTA_DATE_PAST)[1],
        )

        # API URL request
        API_OSWAPI_HISTORICAL = "https://archive-api.open-meteo.com/v1/archive"

        params = {
            "latitude": [LAT_KL],
            "longitude": [LONG_KL],
            "start_date": past_date_formatted,  # from date
            "end_date": today_date_formatted,  # to date
            "daily": [
                "weather_code",
                "temperature_2m_max",
                "temperature_2m_min",
                "sunshine_duration",
                "rain_sum",
                "snowfall_sum",
            ],
            "timezone": "auto",
        }

        # send a request to the weather API
        oswapi_request = requests.get(API_OSWAPI_HISTORICAL, params=params)
        # print the full URL with all parameters
        # URL = oswapi_request.url

        if len(params["latitude"]) > 1:
            # grab the content of the request in a dict/json format
            oswapi_content_historical = oswapi_request.json()[0]
        else:
            # grab the content of the request in a dict/json format
            oswapi_content_historical = [oswapi_request.json()]

        # return the dataframe with the requested data from the API
        return self.build_dataframe(oswapi_content_historical)
