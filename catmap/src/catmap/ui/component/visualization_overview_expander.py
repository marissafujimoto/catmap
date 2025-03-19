"""Module to create visualization overview expander."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class VisualizationOverviewExpander(AbstractUIComponent): # pylint: disable=too-few-public-methods
    """Class to create visualization overview expander."""

    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Creates the visualization overview expander."""
        with parent.expander("Visualization Overview"):
                st.markdown("""
                    The plot above displays a cancer transcriptomics map (catmap). This tool is meant to aid the research 
                            and understanding of patient cancer diagnoses through a visual representation of cancer types, 
                            stages, etc. 
                            
                    Interact with the filter dropdown above the plot to view the catmap with different groupings based on
                            variables included in the data. 
                    """
                )
