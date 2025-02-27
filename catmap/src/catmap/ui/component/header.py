from streamlit.delta_generator import DeltaGenerator

from catmap.ui.component.abstract_component import AbstractUIComponent


class Header(AbstractUIComponent):
    def build(self, parent: DeltaGenerator) -> DeltaGenerator:
        parent.title("catmap")
