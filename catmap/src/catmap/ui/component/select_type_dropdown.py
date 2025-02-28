import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent
from catmap.ui.component.embedding_plotter import EmbeddingPlotter


class SelectTypeDropdown(AbstractUIComponent):
    def build(self, parent: DeltaGenerator):
        selected = parent.multiselect(
            "Type", options=st.session_state.selected_filters, default=st.session_state.selected_filters)

        st.session_state.selected_filters = set(selected)
