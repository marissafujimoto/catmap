"""Module to create visualization overview expander."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class VisualizationOverviewExpander(AbstractUIComponent):  # pylint: disable=too-few-public-methods
    """Class to create visualization overview expander."""

    def build(self, parent: DeltaGenerator):
        """
        Creates the visualization overview expander.

        Args:
            parent (DeltaGenerator): The parent streamlit container to attach to.
            Could be a column or the root st object.
        """
        with parent.expander("Visualization Overview"):
            if st.session_state.current_page == "page_1":
                st.markdown("""
                    catmap stands for ca(ncer) t(ranscriptomics) map. It is a tool used to 
                            visualize and project single cell gene expression data from cancer cells.
                    
                    The plot above displays a catmap for lung cancer data. This application is meant 
                            to aid the research and understanding of patient cancer diagnoses through 
                            a visual representation of cancer types, stages, etc. 
                            
                    Interact with the filter dropdown above the plot to view the catmap with different 
                            groupings based on variables available in the data. 
                    """
                            )
            if st.session_state.current_page == "page_2":
                st.markdown("""
                    catmap stands for ca(ncer) t(ranscriptomics) map. It is a tool used to 
                            visualize and project single cell gene expression data from cancer cells.
                    
                    The plot above displays a catmap for colon cancer data. This application is meant 
                            to aid the research and understanding of patient cancer diagnoses through 
                            a visual representation of cancer types, stages, etc. 
                            
                    Interact with the filter dropdown above the plot to view the catmap with different 
                            groupings based on variables available in the data. 
                    """
                            )
