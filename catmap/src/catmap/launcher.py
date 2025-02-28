import os
from pathlib import Path

from streamlit.web import cli


def main():
    cli.main_run([os.path.join(Path(__file__).resolve().parent, "app.py")])
