import streamlit as st

class HomePageHeader:
    """Class to write a fully centered title and navigation buttons."""

    def build(self, parent: st.delta_generator.DeltaGenerator) -> None:
        """Creates a centered title and places navigation buttons below it."""
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
