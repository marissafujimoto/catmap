"""
Module for loading embedding models.

For now this supports a model which embeds NSCLC single cell counts into a 30 dimensional
vector.

One quirk of this model loader is that it needs to have a registered anndata file at the
time of loading the model weights. This is a limitation in SCVI. This quirk means that
the interface for loading a model also will load in anndata at the same time.
"""
import os
import tempfile

import anndata
import numpy as np
import pandas as pd
import scanpy as sc
import scvi
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_nsclc_embedding_model() -> scvi.model.SCVI:
    raise NotImplementedError()