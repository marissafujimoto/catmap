"""Module to fill the embedding plotter window."""
import streamlit as st
import plotly.express as px

from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class EmbeddingPlotter(AbstractUIComponent):  # pylint: disable=too-few-public-methods
    """Class to fill the embedding plotter window."""

    def __init__(self, df, column, xlab, ylab):
        self.df = df
        self.column = column
        self.xlab = xlab
        self.ylab = ylab

    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Builds the component which plots the embedding data."""
        fig = px.scatter(self.df, x=self.xlab,
                         y=self.ylab, color=self.column)
        parent.plotly_chart(fig)
