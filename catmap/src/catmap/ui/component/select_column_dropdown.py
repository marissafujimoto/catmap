"""Module to create dropdown filter of column name options that 
determines what is displayed in the plot."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class SelectColumnDropdown(AbstractUIComponent):  # pylint: disable=too-few-public-methods
    """A UI component for creating a dropdown filter to select a column

    This class generates a dropdown menu that allows users to select
    a column from a given list corresponding to the columns in the DataFrame.
    The selected column is stored in Streamlist's session state.
    """

    def __init__(self, columns, selected_column_key):
        """Initializes the SelectColumnDropdown

        Args:
            columns (list): A list of column names to be displayed in the dropdown
            selected_column_key (str): The key used to store the selected column in session state"""
        self.columns = columns
        self.selected_column_key = selected_column_key

    def build(self, parent: DeltaGenerator):
        """Builds the dropdown filter and initializes it to the first column."""
        option = parent.selectbox(
            "Column", options=self.columns, index=0)

        st.session_state[self.selected_column_key] = option
