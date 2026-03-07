from typing import Any

from pypst.binding import Binding
from pypst.block import Block
from pypst.box import Box
from pypst.cell import Cell
from pypst.color import (
    Color,
    ColorPredefined,
    ColorLuma,
    ColorOklab,
    ColorOklch,
    ColorLinearRGB,
    ColorRGB,
    ColorCMYK,
    ColorHSL,
    ColorHSV,
)
from pypst.content import Content
from pypst.document import Document
from pypst.figure import Figure
from pypst.functional import Functional
from pypst.grid import (
    Grid,
    GridCell,
    GridHorizontalLine,
    GridVerticalLine,
    GridHeader,
    GridFooter,
)
from pypst.heading import Heading
from pypst.image import Image
from pypst.itemize import Enumerate, Itemize
from pypst.place import Place
from pypst.quantity import Degree, Fraction, Length, Quantity, Radian, Ratio
from pypst.renderable import Plain, Renderable
from pypst.rotate import Rotate
from pypst.scale import Scale
from pypst.set_rule import SetRule
from pypst.show_rule import ShowRule
from pypst.skew import Skew
from pypst.stroke import Dash, Stroke
from pypst.text import Text

try:
    from pypst.table import Table  # needed to be included in code completion
except ModuleNotFoundError:
    pass


def __getattr__(name: str) -> Any:
    """Lazily import Table to check for pandas."""
    if name == "Table":
        from pypst.table import Table

        return Table
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "Binding",
    "Block",
    "Box",
    "Cell",
    "Color",
    "ColorPredefined",
    "ColorLuma",
    "ColorOklab",
    "ColorOklch",
    "ColorLinearRGB",
    "ColorRGB",
    "ColorCMYK",
    "ColorHSL",
    "ColorHSV",
    "Content",
    "Dash",
    "Degree",
    "Document",
    "Enumerate",
    "Figure",
    "Fraction",
    "Functional",
    "Grid",
    "GridCell",
    "GridFooter",
    "GridHorizontalLine",
    "GridHeader",
    "GridVerticalLine",
    "Heading",
    "Length",
    "Image",
    "Itemize",
    "Place",
    "Quantity",
    "Radian",
    "Ratio",
    "Plain",
    "Renderable",
    "Rotate",
    "Scale",
    "SetRule",
    "Skew",
    "ShowRule",
    "Stroke",
    "Table",
    "Text",
]
__version__ = "0.8.0"
