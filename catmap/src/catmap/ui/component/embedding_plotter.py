"""Module to fill the embedding plotter window."""
import random
import string

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class EmbeddingPlotter(AbstractUIComponent): # pylint: disable=too-few-public-methods
    """Class to fill the embedding plotter window."""
    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Builds the component which plots the embedding data."""
        # Create 300,000 random x and y coordinates
        x = np.random.normal(0, 100, size=150000)
        x = np.append(x, np.random.normal(1000, 50, size=150000))
        y = np.random.normal(0, 100, size=100000)
        y = np.append(y, np.random.normal(1000, 100, size=200000))

        # Add label of A, B, or C to the 300,000 coordinates
        category = random.choices(string.ascii_uppercase, weights=[
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            k=100000)
        category = np.append(category, random.choices(string.ascii_uppercase, weights=[
            0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            k=100000))
        category = np.append(category, random.choices(string.ascii_uppercase, weights=[
            0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            k=100000))

        df = pd.DataFrame({'x': x, 'y': y, "type": category})

        df = df[df["type"].isin(st.session_state.selected_filters)]

        # Plot figure based on selection
        fig = px.scatter(df, x="x", y="y", color="type")
        parent.plotly_chart(fig)
