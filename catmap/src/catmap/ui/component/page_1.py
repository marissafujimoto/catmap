"""
Module for the streamlit page showing the NSCLC data.
"""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.embedding_plotter import EmbeddingPlotter
from catmap.ui.component.select_column_dropdown import SelectColumnDropdown
from catmap.ui.component.abstract_component import AbstractUIComponent
from catmap.ui.component.info_button import InfoButton
from catmap.ui.component.return_home_button import ReturnHomeButton


class Page1(AbstractUIComponent):  # pylint: disable=too-few-public-methods
    """Class for displaying NSCLC embeddings and information."""

    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Sets up the components and initializes the state."""
        col1, col2 = parent.columns([6, 2])

        with col1:
            select_column_dropdown = SelectColumnDropdown(
                st.session_state.column_options_nsclc, "selected_column_nsclc")
            select_column_dropdown.build(parent)

        with col2:
            nsclc_info_button = InfoButton()
            nsclc_info_button.build(parent)

        caption_text = st.session_state.nsclc_caption_dict[st.session_state.selected_column_nsclc]
        st.caption(caption_text)

        embedding_plotter = EmbeddingPlotter(
            st.session_state.df_nsclc, st.session_state.selected_column_nsclc, "UMAP1", "UMAP2")
        embedding_plotter.build(parent)
        with parent.expander("Visualization Overview"):
            # TODO: write a more informative summary of the data
            parent.write("This dashboard provides insights into NSCLC data.")
        with parent.expander("Data Overview"):
            # TODO: write a more informative summary of the data
            parent.write("This dashboard provides insights into NSCLC data.")

        home_button = ReturnHomeButton()
        home_button.build(parent)
