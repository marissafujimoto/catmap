"""Module to create visualization overview expander."""
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class DataOverviewExpander(AbstractUIComponent):  # pylint: disable=too-few-public-methods
    """Class to create visualization overview expander."""

    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Creates the visualization overview expander."""
        if st.session_state.current_page == "page_1":
            with parent.expander("Data Overview"):
                parent.markdown(
                    "Study: The study that collected the sample of cells.\n \n"
                    "Patient: The patient the sample is from. \n \n"
                    "Cluster Level 1: The high level type of cell (9 total).\n \n"
                    "Cluster Level 2: More specific cell types (27 total).\n \n"
                    "Stage: The stage of Cancer. Stage I is a small tumor that hasn't spread. "
                    "Stage II is cancer that has grown into nearby tissue. "
                    "Stage III is cancer that has spread to lymph nodes. "
                    "Stage IV is cancer that has spread to distant parts of the body.\n \n"
                    "https://www.nature.com/articles/s41597-023-02074-6 \n \n"
                )

        if st.session_state.current_page == "page_2":
            with parent.expander("Data Overview"):
                parent.markdown(
                    "Patient: groups the data by individual patients across all studies.\n \n"
                    "Cluster Level 1: The high level type of cell (7 total)\n \n"
                    "Cluster Level 2: More specific cell types (20 total)\n \n"
                    "Cancer/Normal: Whether the cell is cancerous or normal.\n \n"
                    "Stage: Whether the cancer is stage 4, the most advanced stage of cancer, or not.\n \n"
                    "Lymph Node Status: Whether or not at least one of the surrounding lymph nodes contain "
                    "cancer cells (N+ for yes, N- for no). This signifies the cancer cells are capable of "
                    "metastasis and can lead to cancer spreading to other parts of the body.\n \n"
                    "MMR Status: MMRd (Mismatch Repair Deficient) signifies that one or more proteins in "
                    "the MMR system of cancer cells are not functioning properly leading to a build-up of "
                    "DNA errors making it harder to provide treatment since the cells are rapidly changing. "
                    "MMRp (Mismatch Repair Proficient) signifies that the mismatch repair system is functioning "
                    "normally in the cancer cells. Normal indicates healthy cells.\n \n"
                    "MMR MLH1: MLH1 is a gene that encodes a protein involved in mismatch repair. When it is "
                    "methylated, the gene is turned off. When it is not methylated, this signifies that a change in "
                    "the DNA code is the reason for mismatch repair deficient cells. This will change the "
                    "treatment plan for the patient.\n \n"
                    "https://singlecell.broadinstitute.org/single_cell/study/SCP1162/human-colon-cancer-atlas-c295 \n \n"
                )
