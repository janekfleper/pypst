from dataclasses import dataclass, field

from pypst.functional import Functional
from pypst.renderable import Renderable
from pypst.quantity import Length, Ratio
from pypst.utils import Function

POSITIONAL_FIELD_METADATA: dict[str, bool] = {"positional": True}
OPTIONAL_FIELD_METADATA: dict[str, bool] = {"keep_none": False}


@dataclass
class Scale(Function):
    """
    Scale content without affecting layout.

    Args:
        factor: The scaling factor for both axes.
        x: The horizontal scaling factor.
        y: The vertical scaling factor.
        origin: The origin of the transformation.
        reflow: Whether the scaling impacts the layout.
        body: The content to scale.
    """

    factor: Length | Ratio | str | None = field(
        default=None,
        metadata=POSITIONAL_FIELD_METADATA,
    )
    x: Length | Ratio | str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    y: Length | Ratio | str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    origin: str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    reflow: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    body: Renderable | Functional | None = field(
        default=None, metadata=POSITIONAL_FIELD_METADATA
    )
