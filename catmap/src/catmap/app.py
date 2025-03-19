"""
Module for the catmap streamlit application.

Contains the highest level of page layout and the state initialization.
"""
import os
from pathlib import Path

import streamlit as st
import pandas as pd

#from catmap.ui.component.header import Header
from catmap.ui.component.page_1 import Page1
from catmap.ui.component.page_2 import Page2
from catmap.ui.component.embed_results_page import EmbedResultsPage
from catmap.ui.component.homepage_header import HomePageHeader



def start():
    """Sets up the components and initializes the state."""
    _initialize_state()

    if st.session_state.current_page == "home":
        # TODO extract to home page component # pylint: disable=fixme
        HomePageHeader().build(st)
        st.markdown(
            """
            <div style='text-align: justify; text-align-last: center; width: 80%; margin: auto;'>
            <h4>
            catmap stands for ca(ncer) t(ranscriptomics) map. 
            It is a data visualization application and tool used to visualize and 
            project single cell gene expression data from cancer cells.
            </h4>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("<h3 style='text-align: center;'>Navigate to catmaps with "
        "different visualizations:</h3>", unsafe_allow_html=True)

        _, col1, _, col3 = st.columns([0.175, 0.325, 0.10, 0.40])

        with col1:
            if st.button("Non-Small-Cell-Lung Cancer"):
                st.session_state.current_page = "page_1"
                st.rerun()
        with col3:
            if st.button("Colon Cancer"):
                st.session_state.current_page = "page_2"
                st.rerun()

    elif st.session_state.current_page == "page_1":
        nsclc_page = Page1()
        nsclc_page.build(st)

    elif st.session_state.current_page == "page_2":
        other_page = Page2()
        other_page.build(st)

    elif st.session_state.current_page == "embed":
        embed_page = EmbedResultsPage()
        embed_page.build(st)


def _initialize_state():
    """Helper function to initialize the session state."""
    st.set_page_config(layout="wide")
    if "current_page" not in st.session_state:
        st.session_state.current_page = "home"

    csv_path_nsclc = os.path.join(
        Path(__file__).resolve().parent,
        "data",
        "umap_coordinates_labels_all.csv")

    csv_path_colon_cancer = os.path.join(
        Path(__file__).resolve().parent,
        "data",
        "human-colon-cancer-atlas-labels.csv")

    st.session_state.df_nsclc = pd.read_csv(csv_path_nsclc)
    columns_nsclc = st.session_state.df_nsclc.columns.tolist()
    columns_nsclc.remove('UMAP1')
    columns_nsclc.remove('UMAP2')
    st.session_state.column_options_nsclc = columns_nsclc
    st.session_state.selected_column_nsclc = columns_nsclc[0]
    st.session_state.nsclc_caption_dict = {
        "Study": "Data is grouped by the study that it originated from.", 
        "Patient": "Data is grouped by individual patients across all studies.", 
        "Cell_Cluster_level1": "Data is grouped by the high level cell type represented (9 total).", 
        "Cell_Cluster_level2": "Data is grouped by the low level cell type represented (27 total)",
        "Stage": "Data is grouped by the stage of the cancer."}

    st.session_state.df_colon = pd.read_csv(csv_path_colon_cancer)
    columns_colon = st.session_state.df_colon.columns.tolist()
    columns_colon.remove('X')
    columns_colon.remove('Y')
    st.session_state.column_options_colon = columns_colon
    st.session_state.selected_column_colon = columns_colon[0]
    st.session_state.colon_caption_dict = {
        "Patient": "Data is grouped by individual patients.", 
        "Cluster Level 1": "Data is grouped by the high level cell type represented (7 total).", 
        "Cluster Level 2": "Data is grouped by the low level cell type represented (20 total).", 
        "Cancer/Normal": "Data is grouped by classification of whether or not it is cancerous.",
        "Stage": "Data is grouped by the stage of the cancer.",
        "Lymph Node Status": "Data is grouped by classification of whether or not cancer is found "
        "in lymph nodes (N- = no, N+ = yes)",
        "MMR Status": "Data is group by MMR (mismatch repair) status (pMMR = MMR-proficient, "
        "dMMR = MMR-deficient, normal = non-cancerous)",
        "MMR MLH1": "Data is grouped by MLH1 status (a gene that encodes a protein involved in "
        "MMR)"}

    if 'button' not in st.session_state:
        st.session_state.button = False


start()
