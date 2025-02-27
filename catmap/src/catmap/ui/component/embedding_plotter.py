import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random
import string
from streamlit.delta_generator import DeltaGenerator


def build(parent: DeltaGenerator) -> DeltaGenerator:
    # Create 300,000 random x and y coordinates
    x = np.random.normal(0, 100, size=150000)
    x = np.append(x, np.random.normal(1000, 50, size=150000))
    y = np.random.normal(0, 100, size=100000)
    y = np.append(y, np.random.normal(1000, 100, size=200000))

    # Add label of A, B, or C to the 300,000 coordinates
    type = random.choices(string.ascii_uppercase, weights=[
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], k=100000)
    type = np.append(type, random.choices(string.ascii_uppercase, weights=[
        0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], k=100000))
    type = np.append(type, random.choices(string.ascii_uppercase, weights=[
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], k=100000))

    df = pd.DataFrame({'x': x, 'y': y, 'type': type})

    # Plot figure based on selection
    fig = px.scatter(df, x="x", y="y", color="type")
    parent.plotly_chart(fig)
