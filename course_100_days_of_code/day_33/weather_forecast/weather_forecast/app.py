import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.data_fetching import DataFetching
from pkgs.plots import PlotlyPlot
from pkgs.constants import TIMEDELTA_DATE_FORECAST, PAST_DAYS_FORECAST


def main():
    data_fetching = DataFetching()
    df = data_fetching.open_weather_request_forecast()
    # print(df)
    df.to_csv(
        f"day_33/weather_forecast/data/forecast_past_{PAST_DAYS_FORECAST}_future_{TIMEDELTA_DATE_FORECAST}.csv",
        index=False,
    )

    # # plot the forecast up to n days
    # plotly_plot = PlotlyPlot()
    # plotly_plot.forecast_n_days(df=df)


if __name__ == "__main__":
    main()
