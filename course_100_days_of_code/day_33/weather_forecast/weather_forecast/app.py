import os
import sys
import pandas as pd

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.data_fetching import DataFetching
from pkgs.wmo_codes import WMOProcessing
from pkgs.plots import PlotlyPlot
from pkgs.constants import (
    TIMEDELTA_DATE_FORECAST,
    PAST_DAYS_FORECAST,
    TIMEDELTA_DATE_PAST,
)


def main():
    data_fetching = DataFetching()
    wmo_codes = WMOProcessing()
    # grab the forecast df
    df_forecast = data_fetching.open_weather_request_forecast()
    # grab the historical df
    df_historical = data_fetching.open_weather_request_historical()
    # grab the wmo_codes df
    df_wmo_codes = wmo_codes.wmo_json_2_pandas()

    # join the forecast and historical with the wmo_codes
    df_forecast_wmo = pd.merge(
        df_forecast, df_wmo_codes, left_on="weather_code", right_on="wmo_code"
    )
    df_historical_wmo = pd.merge(
        df_historical, df_wmo_codes, left_on="weather_code", right_on="wmo_code"
    )

    # save the data to a csv
    df_forecast_wmo.to_csv(
        "data/forecast_data.csv",
        index=False,
    )
    df_historical_wmo.to_csv(
        "data/historical_data.csv",
        index=False,
    )

    # # plot the forecast up to n days
    # plotly_plot = PlotlyPlot()
    # plotly_plot.forecast_n_days(df=df)


if __name__ == "__main__":
    main()
