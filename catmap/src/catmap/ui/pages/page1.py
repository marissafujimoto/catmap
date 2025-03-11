import streamlit as st

import os
from pathlib import Path

import streamlit as st
import pandas as pd

from catmap.ui.component.embedding_plotter import EmbeddingPlotter
from catmap.ui.component.select_column_dropdown import SelectColumnDropdown


def show():
    """Sets up the components and initializes the state."""
    _initialize_state()

    #Header().build(st)

    
    col1, col2 = st.columns([6, 2])

    with col1:
        select_column_dropdown = SelectColumnDropdown()
        select_column_dropdown.build(st)
        

    with col2:
        if st.button("ℹ️"):
            st.info("Different categories correspond to different clustering.")
    embedding_plotter = EmbeddingPlotter()
    embedding_plotter.build(st)    
    with st.expander("About this dashboard"):
        st.write("This dashboard provides insights into catmap data.")

    if st.button("Back to Home"):
        st.session_state.current_page = "home"
        st.rerun()



def _initialize_state():
    csv_path = Path(__file__).resolve().parents[2] / "data" / "umap_coordinates_labels_all.csv"
    st.session_state.df = pd.read_csv(csv_path)
    columns = st.session_state.df.columns.tolist()
    columns.remove('UMAP1')
    columns.remove('UMAP2')
    st.session_state.column_options = columns
    st.session_state.selected_column = columns[0]



    