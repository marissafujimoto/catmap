"""Module to fill the embedding plotter window."""
import streamlit as st
import plotly.express as px

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

    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Builds the component which plots the embedding data."""
        fig = px.scatter(self.df, x=self.xlab,
                         y=self.ylab, color=self.column)
        parent.plotly_chart(fig)
