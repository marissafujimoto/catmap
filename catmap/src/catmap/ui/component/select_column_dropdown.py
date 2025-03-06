import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent

class SelectColumnDropdown(AbstractUIComponent):
    def build(self, parent: DeltaGenerator):
        option = parent.selectbox(
            "Column", options=st.session_state.column_options, index =0)

        st.session_state.selected_column = option
