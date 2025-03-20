"""Module to create info button."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class InfoButton(AbstractUIComponent):  # pylint: disable=too-few-public-methods
    """Class to create info button."""

    def toggle_button_state(self):
        """Helper function to toggle the state of the button"""
        st.session_state.button = not st.session_state.button

    def build(self, parent: DeltaGenerator):
        """
        Creates the info button. Relies on session_state.button and session_state.current_page to
        change what information to display and draws from the column option for both pages to
        dynamically display an informative help tip.

        Args:
            parent (DeltaGenerator): The parent streamlit container to attach to.
            Could be a column or the root st object.
        """
        parent.button(":information_source:",
                      on_click=self.toggle_button_state)
        if st.session_state.button:
            if st.session_state.current_page == "page_1":
                st.info(f"Double click on a {st.session_state.selected_column_nsclc} option "
                        "in the plot legend to view data for that "
                        f"{st.session_state.selected_column_nsclc} option only. Single click on "
                        f"a {st.session_state.selected_column_nsclc} option to remove its data "
                        "from the plot.")
            if st.session_state.current_page == "page_2":
                st.info(f"Double click on a {st.session_state.selected_column_colon} option "
                        "in the plot legend to view data for that "
                        f"{st.session_state.selected_column_colon} option only. Single click on "
                        f"a {st.session_state.selected_column_colon} option to remove its data "
                        "from the plot.")
