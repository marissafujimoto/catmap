import streamlit as st

from catmap.ui.component.header import Header
from catmap.ui.component.embedding_plotter import EmbeddingPlotter
from catmap.ui.component.select_type_dropdown import SelectTypeDropdown


def start():
    _initialize_state()

    Header().build(st)

    select_type_dropdown = SelectTypeDropdown()
    embedding_plotter = EmbeddingPlotter()

    left_column, right_column = st.columns(2)

    with left_column:
        select_type_dropdown.build(left_column)

    with right_column:
        embedding_plotter.build(right_column)


def _initialize_state():
    st.session_state.selected_filters = {"A", "B", "C"}


start()
