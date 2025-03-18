"""
Tests for the model loader module. Includes tests for loading adata, scvi models, and scikit-learn
models.
"""

import os
import unittest
from pathlib import Path

import numpy as np
import anndata
import scvi
from sklearn.ensemble import RandomForestClassifier

from catmap.io import model_loader

TEST_ADATA_PATH = os.path.join(
    Path(__file__).resolve().parent, "data", "adata-test.h5ad")


class TestModelLoader(unittest.TestCase):  # pylint: disable=missing-class-docstring
    def test_load_adata(self):
        adata = model_loader.load_adata(TEST_ADATA_PATH)
        self.assertIsNotNone(adata)
        self.assertIsInstance(adata, anndata.AnnData)
        self.assertEqual(adata.shape, (1207, 2000))

    def test_load_adata_invalid_path(self):
        with self.assertRaises(ValueError):
            model_loader.load_adata("path-does-not-exist")

    def test_load_scvi_model(self):
        adata = model_loader.load_adata(TEST_ADATA_PATH)
        scvi_model = model_loader.load_nsclc_embedding_model(adata)
        self.assertIsNotNone(scvi_model)
        self.assertIsInstance(scvi_model, scvi.model.SCVI)
        self.assertTrue(np.array_equal(
            scvi_model.adata.X.todense(), adata.X.todense()))

    def test_load_cell_type_rfc(self):
        rfc = model_loader.load_rfc_cell_type_classifier()
        self.assertIsNotNone(rfc)
        self.assertIsInstance(rfc, RandomForestClassifier)

    def test_embed_nsclc_data(self):
        embed_df = model_loader.embed_nsclc_data(TEST_ADATA_PATH)

        self.assertIn("UMAP1", embed_df)
        self.assertIn("UMAP2", embed_df)
        self.assertIn("Predicted Cell Type", embed_df)

    def test_embed_nsclc_data_invalid_path(self):
        with self.assertRaises(ValueError):
            model_loader.embed_nsclc_data("another-invalid-path.h5ad")
