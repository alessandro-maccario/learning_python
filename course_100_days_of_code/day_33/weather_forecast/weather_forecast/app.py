import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.data_fetching import DataFetching
from pkgs.plots import PlotlyPlot


def main():
    data_fetching = DataFetching()
    df = data_fetching.open_weather_request_forecast()
    print(df)
    df.to_csv("day_33/weather_forecast/data/out.csv", index=False)

    # # plot the forecast up to n days
    # plotly_plot = PlotlyPlot()
    # plotly_plot.forecast_n_days(df=df)


if __name__ == "__main__":
    main()
