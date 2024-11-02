import os
import sys
import requests
import pandas as pd
from datetime import datetime, timedelta


# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import LAT_ARN, LONG_ARN, TIMEDELTA_DATE, GEOGRAPHICAL_COORDINATES


class DataFetching:
    def __init__(self) -> None:
        pass

    def open_weather_request(self) -> pd.DataFrame:
        """Request the data to https://open-meteo.com/en/docs.

        Returns
        -------
        pd.DataFrame
            Dataframe containing the requested data from the Weather API.
        """
        # today_date_formatted, future_date_formatted = (
        #     self.time_definition(timedelta_date=TIMEDELTA_DATE)[0],
        #     self.time_definition(timedelta_date=TIMEDELTA_DATE)[1],
        # )

        # API URL request
        # API_OSWAPI = f"https://api.open-meteo.com/v1/forecast?latitude={LAT_ARN}&longitude={LONG_ARN}&hourly=temperature_2m&timezone=Europe%2FBerlin"
        API_OSWAPI = f"https://api.open-meteo.com/v1/forecast?latitude={LAT_ARN}&longitude={LONG_ARN}&daily=weather_code,sunshine_duration,rain_sum,snowfall_sum&forecast_days={TIMEDELTA_DATE}"
        # define required parameters for the API call
        params = {
            "latitude": LAT_ARN,
            "longitude": LONG_ARN,
            # "start_date": today_date_formatted,
            # "end_date": future_date_formatted,
            "daily": [
                "weather_code",
                # "temperature_2m_mean",
                "temperature_2m_max",
                "temperature_2m_min",
                "sunshine_duration",
                "rain_sum",
                "snowfall_sum",
            ],
        }

        # send a request to the weather API
        oswapi_request = requests.get(API_OSWAPI, params=params)
        # grab the content of the request in a dict/json format
        oswapi_content = oswapi_request.json()[0]

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
        # oswapi_content_elevation = pd.Series(data_json["elevation"], name="elevation")
        # oswapi_content_time = pd.Series(data_json["hourly"]["time"], name="time")
        # oswapi_content_temperature = pd.Series(
        #     data_json["hourly"]["temperature_2m"], name="temperature"
        # )
        oswapi_content_latitude = pd.Series(data_json["latitude"], name="latitude")
        oswapi_content_longitude = pd.Series(data_json["longitude"], name="longitude")
        oswapi_content_elevation = pd.Series(data_json["elevation"], name="elevation")
        oswapi_content_time = pd.Series(data_json["daily"]["time"], name="time")
        oswapi_content_weather_code = pd.Series(
            data_json["daily"]["weather_code"], name="weather_code"
        )
        oswapi_content_temperature_max = pd.Series(
            data_json["daily"]["temperature_2m_max"],
            name="temperature_2m_max",
        )
        oswapi_content_temperature_min = pd.Series(
            data_json["daily"]["temperature_2m_min"],
            name="temperature_2m_min",
        )
        oswapi_content_sunshine_duration = pd.Series(
            data_json["daily"]["sunshine_duration"], name="sunshine_duration"
        )
        oswapi_content_rain_sum = pd.Series(
            data_json["daily"]["rain_sum"], name="rain_sum"
        )
        oswapi_content_snowfall_sum = pd.Series(
            data_json["daily"]["snowfall_sum"], name="snowfall_sum"
        )

        # create the city columns that holds the city for which you are fetching the data:
        # Take the latitude, longitude from the dataframe and search the GEOGRAPHICAL_COORDINATES dict to see if we have a key for it
        lower_bound_lat, lower_bound_long = (
            oswapi_content_latitude.values[0]
            - oswapi_content_latitude.values[0] * 0.009,
            oswapi_content_longitude.values[0]
            - oswapi_content_longitude.values[0] * 0.009,
        )
        upper_bound_lat, upper_bound_long = (
            oswapi_content_latitude.values[0]
            + oswapi_content_latitude.values[0] * 0.009,
            oswapi_content_longitude.values[0]
            + oswapi_content_longitude.values[0] * 0.009,
        )
        # check if the value[0] = lat, value[1] = long that we get from the get request is in between the lower and upper lat/long values
        city = pd.Series(
            [
                key
                for key, value in GEOGRAPHICAL_COORDINATES.items()
                if lower_bound_lat <= value[0] <= upper_bound_lat
                and lower_bound_long <= value[1] <= upper_bound_long
            ][0],
            name="city",
        )

        # combine the multiple series into one
        df = pd.concat(
            [
                oswapi_content_latitude,
                oswapi_content_longitude,
                city,
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
        # fill the nan in the columns elevation, latitude, longitude with the same contant value
        df["elevation"] = df["elevation"].fillna(data_json["elevation"])
        df["latitude"] = df["latitude"].fillna(data_json["latitude"])
        df["longitude"] = df["longitude"].fillna(data_json["longitude"])
        df["city"] = df["city"].fillna(city.values[0])

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
