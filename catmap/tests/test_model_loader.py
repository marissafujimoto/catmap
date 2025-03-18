"""
Tests for the model loader module. Includes tests for loading adata, scvi models, and scikit-learn
models.
"""

import os
import unittest

import anndata
import scvi


from catmap.io import model_loader

TEST_ADATA_PATH = os.path.join("data", "adata-test.h5ad")


class TestModelLoader(unittest.TestCase):  # pylint: disable=missing-class-docstring
    def test_load_adata(self):
        adata = model_loader.load_adata(TEST_ADATA_PATH)
        self.assertIsNotNone(adata)
        self.assertIsInstance(adata, anndata.AnnData)
        self.assertEqual(adata.shape, (1207, 2000))

    def test_load_scvi_model(self):
        adata = model_loader.load_adata(TEST_ADATA_PATH)
        scvi_model = model_loader.load_nsclc_embedding_model(adata)
        self.assertIsNotNone(scvi_model)
        self.assertisinstance(scvi_model, scvi.model.scvi)
        self.assertEqual(scvi_model.adata, adata)
