import streamlit as st
import plotly.express as px
from streamlit.delta_generator import DeltaGenerator


from catmap.ui.component.abstract_component import AbstractUIComponent


class EmbeddingPlotter(AbstractUIComponent):
    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        fig = px.scatter(st.session_state.df, x="UMAP1",
                         y="UMAP2", color=st.session_state.selected_column)
        parent.plotly_chart(fig)
