"""Module to fill the embedding plotter window."""
import plotly.express as px
import streamlit as st

from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class EmbeddingPlotter(AbstractUIComponent):  # pylint: disable=too-few-public-methods
    """A UI component for visualizing embedding data using a scatter plot.

    This class generates a scatter plot using Plotly, where the points
    are colored based on a specified column in the DataFrame.
    """

    def __init__(self, df, column, xlab, ylab):
        """Initializes the EmbeddingPlotter

        Args:
            df (pd. DataFrame): The DataFrame containing the embedding data.
            column (str): The column name used for coloring the points.
            xlab (str): The column name to be used for the x-axis.
            ylab (str): The column name to be used for the y-axis.
        """
        self.df = df
        self.column = column
        self.xlab = xlab
        self.ylab = ylab

    def build(self, parent: DeltaGenerator):
        """
        Builds the component which plots the embedding data. Also relies on
        session_state.current_page to adjust the size of the markers for the embed page.

        Args:
            parent (DeltaGenerator): The parent streamlit container to attach to.
            Could be a column or the root st object.
        """
        fig = px.scatter(self.df, x=self.xlab,
                         y=self.ylab, color=self.column,
                         category_orders={
                             "Stage": ["I", "II", "III", "III/IV", "IV"]},
                         opacity=0.7)
        fig.update_layout(legend={'itemsizing': 'constant'})
        if st.session_state.current_page == "embed":
            fig.update_traces(marker=dict(size=10))
        else:
            fig.update_traces(marker=dict(size=1))
        fig.update_layout(width=800, height=800)
        parent.plotly_chart(fig)
