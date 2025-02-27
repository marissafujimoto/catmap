from streamlit.delta_generator import DeltaGenerator


def build(parent: DeltaGenerator) -> DeltaGenerator:
    parent.title("catmap")
