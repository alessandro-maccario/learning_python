import os
import sys
import pandas as pd
import plotly.graph_objects as go

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import TIMEDELTA_DATE_FORECAST


class PlotlyPlot:
    def __init__(self) -> None:
        pass
        # self.get_data = DataFetching()

    def forecast_n_days(self, df: pd.DataFrame):
        """Create a line plot to plot the forecasted data up to n days

        Parameters
        ----------
        df : pd.DataFrame
            _description_
        """
        # Data Plotting using graph objects in Plotly
        fig = go.Figure(
            [
                go.Scatter(
                    x=df["time"],
                    y=df["temperature_2m_max"],
                )
            ]
        )

        fig.update_layout(
            title=f"Temperature Forecast - Next {TIMEDELTA_DATE_FORECAST} days",
            xaxis_title="Time",
            yaxis_title="Temperature",
            font=dict(family="Courier New, monospace", size=18, color="RebeccaPurple"),
        )

        fig.show()

    def bar_plot_forecast_historical_emoji(self, df: pd.DataFrame) -> None:
        """Create a side-by-side bar plot to show the difference in the average
        temperature between forecast and historical where the markers on top
        of each bar are represented by the forecasted and historical emoji related
        to the weather condition based on the wmo_codes.

        Parameters
        ----------
        df : pd.DataFrame
            Dataframe to be plotted
        """

        # Create the plot
        fig = go.Figure()

        # Add historical temperature bars
        fig.add_trace(
            go.Bar(
                x=df["time_forecast"],
                y=df["temperature_average_historical"],
                name="Historical Temperature",
                text=df["emoji_historical"],
                textposition="outside",
                marker_color="lightgrey",
            )
        )
        # Add forecast temperature bars
        fig.add_trace(
            go.Bar(
                x=df["time_forecast"],
                y=df["temperature_average_forecast"],
                name="Forecast Temperature",
                text=df["emoji_forecast"],
                textposition="outside",
                marker_color="skyblue",
            )
        )

        # Customize layout for grouped bars and axis titles
        fig.update_layout(
            barmode="group",
            title="Forecast vs. Historical Temperatures and Weather conditions",
            xaxis_title="Date",
            yaxis_title="Temperature (°C)",
            xaxis=dict(tickformat="%Y-%m-%d"),  # Format dates on x-axis
        )

        # Show plot
        fig.show()
