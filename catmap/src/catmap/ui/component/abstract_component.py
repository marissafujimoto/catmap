"""
Base module for UI component.

This holds an abstract class which defines a single method "build" which is used to describe how
the concrete component is built onto it's parent streamlit container.
"""
from abc import ABC, abstractmethod

from streamlit.delta_generator import DeltaGenerator


class AbstractUIComponent(ABC):  # pylint: disable=too-few-public-methods
    """Base class for UI component."""

    @abstractmethod
    def build(self, parent: DeltaGenerator):
        """
        Builds the component using the parent component (e.g. st).

        Args:
            parent (DeltaGenerator): The parent streamlit container to attach to.
            Could be a column or the root st object.
        """
        raise NotImplementedError()
