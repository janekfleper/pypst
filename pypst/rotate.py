from dataclasses import dataclass, field

from pypst.functional import Functional
from pypst.renderable import Renderable
from pypst.quantity import Degree, Radian
from pypst.utils import Function

POSITIONAL_FIELD_METADATA: dict[str, bool] = {"positional": True}
OPTIONAL_FIELD_METADATA: dict[str, bool] = {"keep_none": False}


@dataclass
class Rotate(Function):
    """
    Rotate content without affecting the layout.

    Args:
        angle: The angle to rotate the content.
        origin: The origin of the rotation.
        reflow: Whether to reflow the content.
        body: The content to rotate.
    """

    angle: Degree | Radian = field(
        metadata=POSITIONAL_FIELD_METADATA,
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
