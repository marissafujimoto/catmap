"""Module for the catmap streamlit application."""
import streamlit as st
import pandas as pd

from catmap.ui.component.header import Header
from catmap.ui.component.embedding_plotter import EmbeddingPlotter
from catmap.ui.component.select_column_dropdown import SelectColumnDropdown


def start():
    """Sets up the components and initializes the state."""
    _initialize_state()

    Header().build(st)

    select_column_dropdown = SelectColumnDropdown()
    embedding_plotter = EmbeddingPlotter()

    left_column, right_column = st.columns(2)

    with left_column:
        select_column_dropdown.build(left_column)

    with right_column:
        embedding_plotter.build(right_column)


def _initialize_state():
    st.session_state.df = pd.read_csv('../data/umap_coordinates_labels_all.csv')
    columns = st.session_state.df.columns.tolist()
    columns.remove('UMAP1')
    columns.remove('UMAP2')
    st.session_state.column_options = columns
    st.session_state.selected_column = columns[0]

start()
