"""Base module for UI component."""
from abc import ABC, abstractmethod

from streamlit.delta_generator import DeltaGenerator


class AbstractUIComponent(ABC): # pylint: disable=too-few-public-methods
    """Base class for UI component."""
    @abstractmethod
    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        """Builds the component using the parent component."""
        raise NotImplementedError()
