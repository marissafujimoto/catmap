"""
Module for the streamlit page showing the colon cancer data.
"""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.embedding_plotter import EmbeddingPlotter
from catmap.ui.component.select_column_dropdown import SelectColumnDropdown
from catmap.ui.component.abstract_component import AbstractUIComponent
from catmap.ui.component.info_button import InfoButton
from catmap.ui.component.return_home_button import ReturnHomeButton
from catmap.ui.component.visualization_overview_expander import VisualizationOverviewExpander
from catmap.ui.component.data_overview_expander import DataOverviewExpander


class Page2(AbstractUIComponent):  # pylint: disable=too-few-public-methods
    """Class for displaying colon cancer embeddings and information."""

    def build(self, parent: DeltaGenerator):
        """
        Sets up the components and initializes the state for the colon cancer page. Relies on
        colon cancer related session state including the selected column, dataframe, and column
        options.

        Args:
            parent (DeltaGenerator): The parent streamlit container to attach to.
            Could be a column or the root st object.
        """
        col1, col2, col3 = parent.columns([0.15, 0.7, 0.15])

        with col1:
            st.write("")

        with col2:
            parent.title("Colon Cancer Catmap")
            select_column_dropdown = SelectColumnDropdown(
                st.session_state.column_options_colon, "selected_column_colon")
            select_column_dropdown.build(parent)

            caption_text = st.session_state.colon_caption_dict[
                st.session_state.selected_column_colon]
            st.caption(caption_text)

            embedding_plotter = EmbeddingPlotter(
                st.session_state.df_colon, st.session_state.selected_column_colon, "X", "Y")
            embedding_plotter.build(parent)

            vis_overview_expander = VisualizationOverviewExpander()
            vis_overview_expander.build(parent)

            data_overview_expander = DataOverviewExpander()
            data_overview_expander.build(parent)

            home_button = ReturnHomeButton()
            home_button.build(parent)

        with col3:
            st.write("#")
            st.write("#")
            st.write("#")
            colon_info_button = InfoButton()
            colon_info_button.build(parent)
