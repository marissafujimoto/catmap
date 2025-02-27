import streamlit as st

from catmap.ui.component.header import Header
from catmap.ui.component.embedding_plotter import EmbeddingPlotter


def start():
    Header().build(st)

    embedding_plotter = EmbeddingPlotter()

    left_column, right_column = st.columns(2)

    with right_column:
        embedding_plotter.build(left_column)


start()
