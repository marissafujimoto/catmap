"""Module to create the button which takes the user to the embedding page."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class OpenEmbeddingPageButton(AbstractUIComponent):  # pylint: disable=too-few-public-methods
    """Class to create open embedding page button."""

    def build(self, parent: DeltaGenerator):
        """
        Creates the open embedding page button which when pressed sets the current_page to embed.

        Args:
            parent (DeltaGenerator): The parent component to build onto.
        """
        if parent.button("Embed New Data"):
            st.session_state.current_page = "embed"
            st.rerun()
