"""Module which allows running the streamlit app with our own script ingress."""
import os
from pathlib import Path

from streamlit.web import cli


def main():
    """Starts the streamlit app."""
    cli.main_run([os.path.join(Path(__file__).resolve().parent, "app.py")])
