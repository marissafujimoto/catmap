"""Module to create visualization overview expander."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class DataOverviewExpander(AbstractUIComponent): # pylint: disable=too-few-public-methods
    """Class to create visualization overview expander."""

    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Creates the visualization overview expander."""
        if st.session_state.current_page == "page_1":
            with parent.expander("Data Overview"):
                parent.write("Add info from Erik for Lung Cancer.")
        if st.session_state.current_page == "page_2":
            with parent.expander("Data Overview"):
                parent.write("Add info from Erik for Colon Cancer.")
