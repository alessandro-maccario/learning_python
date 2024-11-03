import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.data_fetching import DataFetching
from pkgs.plots import PlotlyPlot
from pkgs.constants import (
    TIMEDELTA_DATE_FORECAST,
    PAST_DAYS_FORECAST,
    TIMEDELTA_DATE_PAST,
)


def main():
    data_fetching = DataFetching()
    df_forecast = data_fetching.open_weather_request_forecast()
    df_historical = data_fetching.open_weather_request_historical()

    # save the data to a csv
    df_forecast.to_csv(
        "data/forecast_data.csv",
        index=False,
    )
    df_historical.to_csv(
        "data/historical_data.csv",
        index=False,
    )

    # # plot the forecast up to n days
    # plotly_plot = PlotlyPlot()
    # plotly_plot.forecast_n_days(df=df)


if __name__ == "__main__":
    main()
