from dataclasses import dataclass, field

from pypst.color import Color
from pypst.functional import Functional
from pypst.renderable import Renderable
from pypst.stroke import Stroke
from pypst.quantity import Fraction, Length, Ratio
from pypst.utils import Function

POSITIONAL_FIELD_METADATA: dict[str, bool] = {"positional": True}
OPTIONAL_FIELD_METADATA: dict[str, bool] = {"keep_none": False}


@dataclass
class Block(Function):
    """
    A block-level container.

    Args:
        width: The width of the block.
        height: The height of the block.
        breakable: Whether the block is breakable.
        fill: The fill color of the block.
        stroke: The stroke of the block.
        radius: The radius of the block.
        inset: The inset of the block.
        outset: The outset of the block.
        spacing: The spacing of the block.
        above: The above of the block.
        below: The below of the block.
        clip: Whether the block is clipped.
        sticky: Whether the block is sticky.
        body: The body of the block.
    """

    width: Length | Ratio | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    height: Length | Ratio | Fraction | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    breakable: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    fill: Color | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    stroke: Length | Color | Stroke | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    radius: Length | Ratio | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    inset: Length | Ratio | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    outset: Length | Ratio | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    spacing: Length | Ratio | Fraction | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    above: Length | Ratio | Fraction | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    below: Length | Ratio | Fraction | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    clip: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    sticky: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    body: Renderable | Functional | None = field(
        default=None, metadata=POSITIONAL_FIELD_METADATA
    )
