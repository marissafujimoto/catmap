"""
Module for the page which shows the results of embedding new data and predicting labels.
"""
from tempfile import NamedTemporaryFile

from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.embedding_plotter import EmbeddingPlotter
from catmap.ui.component.select_column_dropdown import SelectColumnDropdown
from catmap.ui.component.abstract_component import AbstractUIComponent
from catmap.ui.component.info_button import InfoButton
from catmap.ui.component.return_home_button import ReturnHomeButton
from catmap.io.model_loader import embed_nsclc_data


class EmbedResultsPage(AbstractUIComponent):
    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Builds the embed results component"""
        col1, col2 = parent.columns([6, 2])

        with col1:
            uploaded_file = parent.file_uploader(
                "Select h5ad File", accept_multiple_files=False)
            print(uploaded_file.name)

            if uploaded_file:
                with NamedTemporaryFile(dir='.', suffix='.h5ad') as f:
                    f.write(uploaded_file.getbuffer())

                    embedding_df = embed_nsclc_data(f.name)
                    # TODO plot the embeddings

        with col2:
            pass

        with parent.expander("About Embedding"):
            # TODO: expand on this writing
            parent.write("This is placeholder writing.")

        home_button = ReturnHomeButton()
        home_button.build(parent)
