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

import anndata
import numpy as np
import pandas as pd
import scanpy as sc
import torch
import scvi
from sklearn.ensemble import RandomForestClassifier
import joblib

MODEL_WEIGHTS_PATH = os.path.join(
    Path(__file__).resolve().parent.parent, "data", "nsclc-scvi-model")
CELL_TYPE_RFC_PATH = os.path.join(
    Path(__file__).resolve().parent.parent, "data", "nsclc-cell-cluster-rfc", "cc1_rfc.joblib")


def load_nsclc_embedding_model(adata: anndata.AnnData) -> scvi.model.SCVI:
    scvi_model = scvi.model.SCVI.load(MODEL_WEIGHTS_PATH, adata)
    scvi_model.is_trained = True

    return scvi_model


def load_adata(adata_path: str) -> anndata.AnnData:
    if not os.path.isfile(adata_path):
        raise ValueError(
            f"Path for adata {adata_path} does not exist or is not a file")

    adata = sc.read(adata_path)

    return adata


def load_rfc_cell_type_classifier() -> RandomForestClassifier:
    return joblib.load(CELL_TYPE_RFC_PATH)
