"""Module for testing UI flow for the embed page"""
import os
from io import BytesIO
import unittest
from unittest import mock
from pathlib import Path

from streamlit.testing.v1 import AppTest


TEST_ADATA_PATH = os.path.join(
    Path(__file__).resolve().parent, "data", "adata-test.h5ad")


class MockFileUpload():  # pylint: disable=too-few-public-methods
    """A class for mocking a file upload result"""

    def __init__(self, name: str, backing_file_path: str):
        """
        Initializes a mock file upload.

        Args:
            name (str): the mock file name.
            backing_file_path (str): the path to the file to use as the content for the mock upload.
        """
        self.name = name
        self.backing_file_path = backing_file_path

    def getbuffer(self) -> memoryview:
        """
        Mock the result of calling getbuffer by using the backing file.

        Returns:
            memoryview: The memory view of the backing file.
        """
        with open(self.backing_file_path, "rb") as backing_file:
            return BytesIO(backing_file.read()).getbuffer()


class TestEmbedUI(unittest.TestCase):
    """Unit tests for embed UI."""

    def setUp(self):
        """Initialize a fresh app instance for the testing"""
        self.at = AppTest.from_file(
            "../src/catmap/app.py", default_timeout=20).run()

    def navigate_to_embed_page(self):
        """Helper to navigate to embed page"""
        # pylint: disable=R0801
        self.assertEqual(self.at.session_state.current_page,
                         "home")  # start on home page
        self.at.button[0].click().run()
        self.assertEqual(self.at.session_state.current_page,
                         "page_1")  # After click, move to page 1
        self.at.button[0].click().run()
        self.assertEqual(self.at.session_state.current_page,
                         "embed")  # After click, move to embed page
        # pylint: enable=R0801

    @mock.patch("catmap.ui.component.embedding_plotter.EmbeddingPlotter.__new__")
    @mock.patch("streamlit.file_uploader")
    def test_embed_with_valid_file(self, mock_upload, mock_plotter):
        """
        A user clicks to go to page 1 then clicks the embed button and then uploads a file.
        """
        mock_upload.return_value = MockFileUpload(
            "test.h5ad", TEST_ADATA_PATH)

        self.navigate_to_embed_page()

        # The last data plotted should be the predicted labels visual
        self.assertEqual(
            mock_plotter.call_args_list[-1].args[2:], ("Predicted Cell Type", "UMAP1", "UMAP2"))

    @mock.patch("catmap.ui.component.embedding_plotter.EmbeddingPlotter.__new__")
    @mock.patch("streamlit.file_uploader")
    def test_embed_with_no_file(self, mock_upload, mock_plotter):
        """
        A user clicks to go to page 1 then clicks the embed button without uploading a file.
        """
        mock_upload.return_value = None

        self.navigate_to_embed_page()

        # The last data plotted should be the first column of NSCLC
        self.assertEqual(
            mock_plotter.call_args_list[-1].args[2:], ("Study", "UMAP1", "UMAP2"))

    @mock.patch("catmap.ui.component.embedding_plotter.EmbeddingPlotter.__new__")
    @mock.patch("streamlit.file_uploader")
    def test_embed_with_invalid_file(self, mock_upload, mock_plotter):
        """
        A user clicks to go to page 1 then clicks the embed button then uploads an invalid file.
        """
        mock_upload.return_value = MockFileUpload(
            "not-an-h5ad.txt", TEST_ADATA_PATH)

        self.navigate_to_embed_page()

        # The last data plotted should be the first column of NSCLC
        self.assertEqual(
            mock_plotter.call_args_list[-1].args[2:], ("Study", "UMAP1", "UMAP2"))

        self.assertEqual(
            self.at.error[0].value, "Uploaded file not-an-h5ad.txt is not a h5ad file")
