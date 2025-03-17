from pathlib import Path

import streamlit as st
import pandas as pd
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.embedding_plotter import EmbeddingPlotter
from catmap.ui.component.select_column_dropdown import SelectColumnDropdown
from catmap.ui.component.abstract_component import AbstractUIComponent
from catmap.ui.component.info_button import InfoButton
from catmap.ui.component.return_home_button import ReturnHomeButton


class Page2(AbstractUIComponent):
    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Sets up the components and initializes the state."""
        col1, col2 = parent.columns([6, 2])

        with col1:
            select_column_dropdown = SelectColumnDropdown(
                st.session_state.column_options_colon, "selected_column_colon")
            select_column_dropdown.build(parent)

        with col2:
            info_button = InfoButton()
            info_button.build(parent)

        embedding_plotter = EmbeddingPlotter(
            st.session_state.df_colon, st.session_state.selected_column_colon, "X", "Y")
        embedding_plotter.build(parent)
        with parent.expander("About this dashboard"):
            # TODO: write a more informative summary of the data
            st.write("This dashboard provides insights into catmap data.")

        home_button = ReturnHomeButton()
        home_button.build(parent)
