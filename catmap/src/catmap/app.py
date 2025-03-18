"""Module for the catmap streamlit application."""
import os
import sys
from pathlib import Path

import streamlit as st
import pandas as pd

from catmap.ui.component.header import Header
from catmap.ui.component.embedding_plotter import EmbeddingPlotter
from catmap.ui.component.select_column_dropdown import SelectColumnDropdown
from catmap.ui.component.page_1 import Page1
from catmap.ui.component.page_2 import Page2
from catmap.ui.component.embed_results_page import EmbedResultsPage


def start():
    """Sets up the components and initializes the state."""
    _initialize_state()

    Header().build(st)

    if st.session_state.current_page == "home":
        # TODO extract to home page component
        st.write("Navigate to other pages:")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Go to Page 1"):
                st.session_state.current_page = "page_1"
                st.rerun()

        with col2:
            if st.button("Go to Page 2"):
                st.session_state.current_page = "page_2"
                st.rerun()

    elif st.session_state.current_page == "page_1":
        nsclc_page = Page1()
        nsclc_page.build(st)

    elif st.session_state.current_page == "page_2":
        other_page = Page1()
        other_page.build(st)

    elif st.session_state.current_page == "embed":
        embed_page = EmbedResultsPage()
        embed_page.build(st)


def _initialize_state():
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"

    csv_path = os.path.join(
        Path(__file__).resolve().parent,
        "data",
        "umap_coordinates_labels_all.csv")
    st.session_state.df = pd.read_csv(csv_path)
    columns = st.session_state.df.columns.tolist()
    columns.remove('UMAP1')
    columns.remove('UMAP2')
    st.session_state.column_options = columns
    st.session_state.selected_column = columns[0]

    if 'button' not in st.session_state:
        st.session_state.button = False


start()
