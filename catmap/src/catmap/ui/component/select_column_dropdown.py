"""Module to create dropdown filter of column name options that 
determines what is displayed in the plot."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class SelectColumnDropdown(AbstractUIComponent):
    """Class to create dropdown filter."""

    def __init__(self, columns, selected_column_key):
        self.columns = columns
        self.selected_column_key = selected_column_key

    def build(self, parent: DeltaGenerator):
        """Builds the dropdown filter and initializes it to the first column."""
        option = parent.selectbox(
            "Column", options=self.columns, index=0)

        st.session_state[self.selected_column_key] = option
