"""Module to create the home page header UI component."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator


class HomePageHeader:
    """Class to write a fully centered title."""

    def build(self, parent: DeltaGenerator):
        """
        Creates a centered title and places navigation buttons below it.

        Args:
            parent (DeltaGenerator): The parent streamlit container to attach to.
            Could be a column or the root st object.
        """
        custom_html = """
        <style>
        h1 {
            font-size: 140px !important;
            font-weight: bold;
            text-align: center;
        }
        </style>
        <div>
            <h1>catmap</h1>
        </div>
        """
        parent.markdown(custom_html, unsafe_allow_html=True)
