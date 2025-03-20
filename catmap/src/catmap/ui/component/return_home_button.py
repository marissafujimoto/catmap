"""Module to create back to home button."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class ReturnHomeButton(AbstractUIComponent):  # pylint: disable=too-few-public-methods
    """Class to create back to home button."""

    def build(self, parent: DeltaGenerator):
        """
        Creates the back to home button.

        Args:
            parent (DeltaGenerator): The parent streamlit container to attach to.
            Could be a column or the root st object.
        """

        if parent.button("Back to Home"):
            st.session_state.current_page = "home"
            st.rerun()
