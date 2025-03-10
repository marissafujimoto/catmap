"""Module for the catmap streamlit application."""
import importlib
import os
from pathlib import Path

import streamlit as st
import pandas as pd

from catmap.ui.component.header import Header
from catmap.ui.component.embedding_plotter import EmbeddingPlotter
from catmap.ui.component.select_column_dropdown import SelectColumnDropdown


def start():
    """Sets up the components and initializes the state."""
    _initialize_state()

    Header().build(st)

    if st.session_state.current_page == "home":
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
        page_1 = importlib.import_module("ui.pages.page1")
        page_1.show()

    elif st.session_state.current_page == "page_2":
        page_2 = importlib.import_module("ui.pages.page2")
        page_2.show()



def _initialize_state():
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home" 
    
start()

