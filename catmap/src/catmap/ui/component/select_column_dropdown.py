"""Module to create dropdown filter of column name options that 
determines what is displayed in the plot."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent

class SelectColumnDropdown(AbstractUIComponent):
    """Class to create dropdown filter."""
    def build(self, parent: DeltaGenerator):
        """Builds the dropdown filter and initializes it to the first column."""
        option = parent.selectbox(
            "Column", options=st.session_state.column_options, index=0)

        st.session_state.selected_column = option
