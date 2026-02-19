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
class Box(Function):
    """
    An inline-level container.

    Args:
        width: The width of the box.
        height: The height of the box.
        baseline: The shift of the baseline of the box.
        fill: The fill color of the box.
        stroke: The stroke of the box.
        radius: The radius of the box.
        inset: The inset of the box.
        outset: The outset of the box.
        clip: Whether the box is clipped.
        body: The body of the box.
    """

    width: Length | Ratio | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    height: Length | Ratio | Fraction | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    baseline: Length | Ratio | Fraction | None = field(
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
    clip: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    body: Renderable | Functional | None = field(
        default=None, metadata=POSITIONAL_FIELD_METADATA
    )
