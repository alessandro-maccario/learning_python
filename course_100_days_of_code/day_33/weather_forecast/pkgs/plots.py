import os
import sys
import pandas as pd
import plotly.graph_objects as go

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import TIMEDELTA_DATE


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
            title=f"Temperature Forecast - Next {TIMEDELTA_DATE} days",
            xaxis_title="Time",
            yaxis_title="Temperature",
            font=dict(family="Courier New, monospace", size=18, color="RebeccaPurple"),
        )

        fig.show()
