"""Module to create info button."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class InfoButton(AbstractUIComponent): # pylint: disable=too-few-public-methods
    """Class to create info button."""

    def toggle_button_state(self):
        st.session_state.button = not st.session_state.button

    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Creates the info button."""
        parent.button(":information_source:", on_click=self.toggle_button_state)
        if st.session_state.button:
            st.info("Different categories correspond to different clustering.")
