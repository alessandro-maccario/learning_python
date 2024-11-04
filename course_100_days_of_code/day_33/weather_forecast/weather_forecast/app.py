import os
import sys
import pandas as pd

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.data_fetching import DataFetching
from pkgs.wmo_codes import WMOProcessing
from pkgs.plots import PlotlyPlot


def main():
    data_fetching = DataFetching()
    wmo_codes = WMOProcessing()
    # grab the forecast df
    df_forecast = data_fetching.open_weather_request_forecast()
    df_forecast = df_forecast.add_suffix("_forecast")
    # grab the historical df
    df_historical = data_fetching.open_weather_request_historical()
    df_historical = df_historical.add_suffix("_historical")
    # grab the wmo_codes df
    df_wmo_codes = wmo_codes.wmo_json_2_pandas()

    # join the forecast and historical with the wmo_codes
    df_forecast_historical = pd.merge(
        df_forecast, df_historical, left_on="time_forecast", right_on="time_historical"
    )[
        [
            "latitude_forecast",
            "longitude_forecast",
            "elevation_forecast",
            "time_forecast",
            "time_historical",
            "weather_code_forecast",
            "weather_code_historical",
            "temperature_average_forecast",
            "temperature_average_historical",
            "hours_sunshine_duration_forecast",
            "hours_sunshine_duration_historical",
        ]
    ]

    # merge the data with wmo_codes and rename columns by using forecast and historical suffixes
    df_forecast_historical_wmo = pd.merge(
        df_forecast_historical,
        df_wmo_codes,
        left_on="weather_code_forecast",
        right_on="wmo_code",
    )
    df_forecast_historical_wmo.rename(
        columns={
            "wmo_code": "wmo_code_forecast",
            "description": "description_forecast",
            "emoji": "emoji_forecast",
        },
        inplace=True,
    )
    df_forecast_historical_wmo_complete = pd.merge(
        df_forecast_historical_wmo,
        df_wmo_codes,
        left_on="weather_code_historical",
        right_on="wmo_code",
    )
    df_forecast_historical_wmo_complete.rename(
        columns={
            "wmo_code": "wmo_code_historical",
            "description": "description_historical",
            "emoji": "emoji_historical",
        },
        inplace=True,
    )

    df_forecast_historical_wmo_complete[
        [
            "latitude_forecast",
            "longitude_forecast",
            "elevation_forecast",
            "time_forecast",
            "time_historical",
            "weather_code_forecast",
            "weather_code_historical",
            "temperature_average_forecast",
            "temperature_average_historical",
            "hours_sunshine_duration_forecast",
            "hours_sunshine_duration_historical",
            "description_forecast",
            "description_historical",
            "wmo_code_forecast",
            "wmo_code_historical",
            "emoji_forecast",
            "emoji_historical",
        ]
    ].to_csv(
        "day_33/weather_forecast/data/forecast_historical_wmo_complete_data.csv",
        index=False,
    )

    # plot the forecast and historical data in a side-by-side bar plot
    # with related emoji for the wmo_codes
    plotly_plot = PlotlyPlot()
    plotly_plot.bar_plot_forecast_historical_emoji(
        df=df_forecast_historical_wmo_complete
    )


if __name__ == "__main__":
    main()
