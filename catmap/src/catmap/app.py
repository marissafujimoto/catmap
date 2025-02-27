import streamlit as st

from catmap.ui.component import title, embedding_plotter


def start():
    title.build(st)

    left_column, right_column = st.columns(2)

    with right_column:
        embedding_plotter.build(left_column)


start()
