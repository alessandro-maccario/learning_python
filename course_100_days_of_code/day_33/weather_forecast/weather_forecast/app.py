import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import TIMEDELTA_DATE
from pkgs.data_fetching import DataFetching
import plotly.graph_objects as go


def main():
    df = DataFetching()
    print(df.open_weather_request())

    # # Data Plotting using graph objects in Plotly
    # fig = go.Figure(
    #     [
    #         go.Scatter(
    #             x=df.open_weather_request()["time"],
    #             y=df.open_weather_request()["temperature"],
    #         )
    #     ]
    # )

    # fig.update_layout(
    #     title=f"Temperature Forecast - Next {TIMEDELTA_DATE} days",
    #     xaxis_title="Time",
    #     yaxis_title="Temperature",
    #     font=dict(family="Courier New, monospace", size=18, color="RebeccaPurple"),
    # )

    # fig.show()


if __name__ == "__main__":
    main()
