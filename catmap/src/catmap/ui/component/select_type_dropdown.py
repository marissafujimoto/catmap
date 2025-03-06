"""Module to build the filter selection dropdown."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class SelectTypeDropdown(AbstractUIComponent): # pylint: disable=too-few-public-methods
    """Class to build the filter selection dropdown."""
    def build(self, parent: DeltaGenerator):
        """Builds the filter selection dropdown."""
        selected = parent.multiselect(
            "Type", options=st.session_state.selected_filters, 
            default=st.session_state.selected_filters)

        st.session_state.selected_filters = set(selected)
