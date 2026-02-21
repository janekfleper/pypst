from dataclasses import dataclass, field

from pypst.functional import Functional
from pypst.renderable import Renderable
from pypst.quantity import Degree, Radian
from pypst.utils import Function

POSITIONAL_FIELD_METADATA: dict[str, bool] = {"positional": True}
OPTIONAL_FIELD_METADATA: dict[str, bool] = {"keep_none": False}


@dataclass
class Skew(Function):
    """
    Skew content.

    Args:
        ax: The horizontal skewing angle.
        ay: The vertical skewing angle.
        origin: The origin of the skew transformation.
        reflow: Whether the skew transformation impacts the layout.
        body: The content to skew.
    """

    ax: Degree | Radian | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    ay: Degree | Radian | None = field(
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
