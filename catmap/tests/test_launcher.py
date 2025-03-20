"""Test module for the catmap launcher."""
from pathlib import Path
import unittest
from unittest.mock import patch

from catmap import app
from catmap import launcher


class TestLauncher(unittest.TestCase):
    """Test class for testing the launcher."""

    @patch("streamlit.web.cli.main_run")
    def test_main(self, mock_main_run):
        """Test that the streamlit cli runner is called with the location of our app script."""
        launcher.main()

        mock_main_run.assert_called_with([str(Path(app.__file__).resolve())])
