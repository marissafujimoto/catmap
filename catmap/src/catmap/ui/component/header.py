"""Module to write title."""
from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class Header(AbstractUIComponent):  # pylint: disable=too-few-public-methods
    """Class to write title."""

    def build(self, parent: DeltaGenerator):
        """
        Writes the title.

        Args:
            parent (DeltaGenerator): The parent streamlit container to attach to.
            Could be a column or the root st object.
        """
        parent.title("catmap")
