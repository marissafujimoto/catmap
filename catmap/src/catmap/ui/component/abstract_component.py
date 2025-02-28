from abc import ABC, abstractmethod

from streamlit.delta_generator import DeltaGenerator


class AbstractUIComponent(ABC):
    @abstractmethod
    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        raise NotImplementedError()
