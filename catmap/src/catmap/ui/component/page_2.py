from pathlib import Path

import streamlit as st
import pandas as pd
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.embedding_plotter import EmbeddingPlotter
from catmap.ui.component.select_column_dropdown import SelectColumnDropdown
from catmap.ui.component.abstract_component import AbstractUIComponent


class Page2(AbstractUIComponent):
    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Sets up the components and initializes the state."""
        col1, col2 = parent.columns([6, 2])

        with col1:
            select_column_dropdown = SelectColumnDropdown()
            select_column_dropdown.build(parent)

        with col2:
            def click_button():
                st.session_state.button = not st.session_state.button

            col2.button(":information_source:", on_click=click_button)

            if st.session_state.button:
                st.info("Different categories correspond to different clustering.")

        embedding_plotter = EmbeddingPlotter()
        embedding_plotter.build(parent)
        with parent.expander("About this dashboard"):
            st.write("This dashboard provides insights into catmap data.")

        if parent.button("Back to Home"):
            st.session_state.current_page = "home"
