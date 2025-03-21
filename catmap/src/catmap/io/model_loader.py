"""
Module for loading embedding models.

For now this supports a model which embeds NSCLC single cell counts into a 30 dimensional
vector.

One quirk of this model loader is that it needs to have a registered anndata file at the
time of loading the model weights. This is a limitation in SCVI. This quirk means that
the interface for loading a model also will need the anndata at the same time.
"""
import os
from pathlib import Path

import pandas as pd
import anndata
import scanpy as sc
import scvi
from sklearn.ensemble import RandomForestClassifier
import joblib

MODEL_WEIGHTS_PATH = os.path.join(
    Path(__file__).resolve().parent.parent, "data", "nsclc-scvi-model")
CELL_TYPE_RFC_PATH = os.path.join(
    Path(__file__).resolve().parent.parent, "data", "nsclc-cell-cluster-rfc", "cc1_rfc.joblib")


def load_nsclc_embedding_model(adata: anndata.AnnData) -> scvi.model.SCVI:
    """
    Load the trained NSCLC embedding model.

    Args:
        adata (AnnData): The anndata object containing raw counts that this model will embed with.

    Returns:
        scvi_model (scvi.model.SCVI): The scvi model object
    """
    scvi_model = scvi.model.SCVI.load(MODEL_WEIGHTS_PATH, adata)
    scvi_model.is_trained = True

    return scvi_model


def load_adata(adata_path: str) -> anndata.AnnData:
    """
    Load adata from a given path.

    Args:
        adata_path (str): The path to the adata file.

    Returns:
        adata (AnnData): The loaded anndata object.

    Raises:
        ValueError: If the path does not exist or is not a file
    """
    if not os.path.isfile(adata_path):
        raise ValueError(
            f"Path for adata {adata_path} does not exist or is not a file")

    adata = sc.read(adata_path)

    return adata


def load_rfc_cell_type_classifier() -> RandomForestClassifier:
    """
    Load the random forest classifier for NSCLC to classify cell type from NSCLC embeddings. This
    model should be used in conjunction with the model loaded from load_nsclc_embedding_model.

    Returns:
        rfc (RandomForestClassifier): The random forest classifier object.
    """
    return joblib.load(CELL_TYPE_RFC_PATH)


def embed_nsclc_data(adata_path: str) -> pd.DataFrame:
    """
    Calculates embedding vectors for a given adata. The adata should have the same genes as the
    nsclc embedding model loaded from load_nsclc_embedding_model. Then calculates the predicted
    cell types using a random forest classifier.

    Args:
        adata_path (str): The path to the adata file.

    Returns:
        embed_df (pd.DataFrame): A pandas dataframe containing the UMAP coordinates as columns
        "UMAP1" and "UMAP2" and the predicted cell type in the "Predicted Cell Type" column.

    Raises:
        ValueError: If the path does not exist or is not a file.
    """
    if not os.path.isfile(adata_path):
        raise ValueError(
            f"Path for adata {adata_path} does not exist or is not a file")

    adata = load_adata(adata_path)
    scvi_model = load_nsclc_embedding_model(adata)
    rfc = load_rfc_cell_type_classifier()

    print("Getting Latent Representation")
    latent = scvi_model.get_latent_representation(adata)

    print("Predicting Cell Types")
    predicted_cell_type = rfc.predict(latent)

    print("Calculating UMAP")
    adata.obsm["X_scVI"] = latent
    sc.pp.neighbors(adata, n_neighbors=15, use_rep="X_scVI")
    sc.tl.umap(adata)

    print("Embedding Done")

    embed_df = pd.DataFrame()

    embed_df["UMAP1"] = adata.obsm["X_umap"][:, 0]
    embed_df["UMAP2"] = adata.obsm["X_umap"][:, 1]
    embed_df["Predicted Cell Type"] = predicted_cell_type

    return embed_df
