"""
Module for the page which shows the results of embedding new data and predicting labels.
"""
from tempfile import NamedTemporaryFile

from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.embedding_plotter import EmbeddingPlotter
from catmap.ui.component.abstract_component import AbstractUIComponent
from catmap.ui.component.return_home_button import ReturnHomeButton
from catmap.io.model_loader import embed_nsclc_data


class EmbedResultsPage(AbstractUIComponent):
    def build(self, parent: DeltaGenerator):
        """
        Builds the embed results component

        Args:
            parent (DeltaGenerator): The parent container to build onto.
        """
        col1,col2,col3 = parent.columns([0.15,0.7,0.15])

        with col1:
            pass
        with col2:
            parent.write(
                "Upload an h5ad file from NSCLC to visualize clustering and predict cell types.")

            with parent.expander("Data Requirements"):
                parent.write(
                    "The h5ad file should contain raw counts (not normalized or log transformed).")
            uploaded_file = parent.file_uploader(
                "Select h5ad File", accept_multiple_files=False)

            if uploaded_file and "h5ad" != uploaded_file.name[-4:]:
                col1.error(
                    f"Uploaded file {uploaded_file.name} is not a h5ad file")

                uploaded_file = None

            if uploaded_file:
                with NamedTemporaryFile(dir='.', suffix='.h5ad') as f:
                    f.write(uploaded_file.getbuffer())

                    embedding_df = embed_nsclc_data(f.name)

                embedding_plotter = EmbeddingPlotter(
                    embedding_df, "Predicted Cell Type", "UMAP1", "UMAP2")
                embedding_plotter.build(parent)

            with parent.expander("About Embedding"):
                parent.write("This embedding uses an unsupervised model trained on the raw NSCLC data \
                            and a random forest classifier trained to classify cell types in the \
                            latent space. The final visualization is a UMAP reduction with the \
                            predicted labels superimposed.")

            home_button = ReturnHomeButton()
            home_button.build(parent)
        with col3:
            pass
