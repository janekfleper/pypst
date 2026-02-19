from dataclasses import dataclass, field

from pypst.functional import Functional
from pypst.renderable import Renderable
from pypst.quantity import Length, Ratio
from pypst.utils import Function

POSITIONAL_FIELD_METADATA: dict[str, bool] = {"positional": True}
OPTIONAL_FIELD_METADATA: dict[str, bool] = {"keep_none": False}


@dataclass
class Place(Function):
    """
    Place content relative to the parent container.

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

    alignment: str | None = field(
        default=None,
        metadata=POSITIONAL_FIELD_METADATA,
    )
    scope: str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    float: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    clearance: Length | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    dx: Length | Ratio | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    dy: Length | Ratio | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    body: Renderable | Functional | None = field(
        default=None, metadata=POSITIONAL_FIELD_METADATA
    )
