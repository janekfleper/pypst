from dataclasses import dataclass

from pypst.functional import Functional
from pypst.renderable import Renderable
from pypst.utils import render


@dataclass
class Binding:
    """
    A binding of a variable or a function.

    Args:
        name: The name or signature of the binding.
        value: The value of the binding.
    """

    name: str | Renderable
    value: str | Renderable | Functional

    def render(self) -> str:
        return f"#let {render(self.name)} = {render(self.value)}"
