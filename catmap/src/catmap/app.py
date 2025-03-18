"""
Module for the catmap streamlit application.

Contains the highest level of page layout and the state initialization.
"""
import os
from pathlib import Path

import streamlit as st
import pandas as pd

from catmap.ui.component.header import Header
from catmap.ui.component.page_1 import Page1
from catmap.ui.component.page_2 import Page2


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
        other_page = Page2()
        other_page.build(st)


def _initialize_state():
    """Helper function to initialize the session state."""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"

    csv_path_nsclc = os.path.join(
        Path(__file__).resolve().parent,
        "data",
        "umap_coordinates_labels_all.csv")

    csv_path_colon_cancer = os.path.join(
        Path(__file__).resolve().parent,
        "data",
        "human-colon-cancer-atlas-labels.csv")

    st.session_state.df_nsclc = pd.read_csv(csv_path_nsclc)
    columns_nsclc = st.session_state.df_nsclc.columns.tolist()
    columns_nsclc.remove('UMAP1')
    columns_nsclc.remove('UMAP2')
    st.session_state.column_options_nsclc = columns_nsclc
    st.session_state.selected_column_nsclc = columns_nsclc[0]

    st.session_state.df_colon = pd.read_csv(csv_path_colon_cancer)
    columns_colon = st.session_state.df_colon.columns.tolist()
    columns_colon.remove('X')
    columns_colon.remove('Y')
    st.session_state.column_options_colon = columns_colon
    st.session_state.selected_column_colon = columns_colon[0]

    if 'button' not in st.session_state:
        st.session_state.button = False


start()
