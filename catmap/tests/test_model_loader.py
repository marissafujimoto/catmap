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
            adata = model_loader.load_adata("path-does-not-exist")

    def test_load_scvi_model(self):
        adata = model_loader.load_adata(TEST_ADATA_PATH)
        scvi_model = model_loader.load_nsclc_embedding_model(adata)
        self.assertIsNotNone(scvi_model)
        self.assertIsInstance(scvi_model, scvi.model.SCVI)
        self.assertTrue(np.array_equal(
            scvi_model.adata.X.todense(), adata.X.todense()))
