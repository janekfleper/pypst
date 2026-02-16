from dataclasses import dataclass, field

from pypst import utils
from pypst.color import Color
from pypst.quantity import Length

"""
The predefined dash patterns from Typst.

https://typst.app/docs/reference/visualize/stroke/#constructor-dash
"""
PREDEFINED_DASH_PATTERNS: list[str] = [
    "solid",
    "dotted",
    "densely-dotted",
    "loosely-dotted",
    "dashed",
    "densely-dashed",
    "loosely-dashed",
    "dash-dotted",
    "densely-dash-dotted",
    "loosely-dash-dotted",
]

"""
The predefined cap styles from Typst.

https://typst.app/docs/reference/visualize/stroke/#constructor-cap
"""
PREDEFINED_CAP_STYLES: list[str] = [
    "butt",
    "round",
    "square",
]

"""
The predefined join styles from Typst.

https://typst.app/docs/reference/visualize/stroke/#constructor-join
"""
PREDEFINED_JOIN_STYLES: list[str] = [
    "miter",
    "round",
    "bevel",
]

POSITIONAL_FIELD_METADATA: dict[str, bool] = {"positional": True}
OPTIONAL_FIELD_METADATA: dict[str, bool] = {"positional": True, "keep_none": False}


@dataclass
class Dash:
    """
    A dash pattern.

    Args:
        pattern: The predefined dash pattern.
        array: The array of lengths.
        phase: The phase of the dash pattern.

    Examples:
        >>> Dash(pattern="solid").render()
        'solid'
        >>> Dash(array=(Length(5, "pt"), Length(1, "em"))).render()
        '(5pt, 1em)'
        >>> Dash(array=Length((1, 3, 7), "pt"), phase=Length(0.9, "pt")).render()
        '{array: (1pt, 3pt, 7pt), phase: 0.9pt}'
    """

    pattern: str | None = None
    array: tuple[Length | str, ...] | None = None
    phase: Length | None = None

    def render(self) -> str:
        if self.pattern is None and self.array is None:
            return "none"

        if self.pattern is not None:
            return self.pattern

        if self.phase is None:
            return utils.render_sequence(self.array)
        return utils.render_mapping(dict(array=self.array, phase=self.phase.render()))


@dataclass
class Stroke:
    """
    A stroke style.

    Args:
        paint: The paint of the stroke.
        thickness: The thickness of the stroke.
        cap: The cap of the stroke.
        join: The join of the stroke.
        dash: The dash of the stroke.
        miter_limit: The miter limit of the stroke.

    Examples:
        >>> Stroke(paint=ColorPredefined("red"), thickness=Length(0.9, "pt")).render()
        'red + 0.9pt'
        >>> Stroke(dash=Dash(array=(Length((1, 2, 3, 4), "mm")), phase=Length(3, "pt"))).render()
        '(array: (1mm, 2mm, 3mm, 4mm), phase: 3pt)'
    """

    paint: Color | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    thickness: Length | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    cap: str | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    join: str | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    dash: Dash | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    miter_limit: float | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)

    def render(self) -> str:
        if (
            self.cap is None
            and self.join is None
            and self.dash is None
            and self.miter_limit is None
        ):
            if self.paint is None and self.thickness is None:
                raise ValueError("Either paint or thickness must be provided")
            if self.paint is None:
                return self.thickness.render()
            if self.thickness is None:
                return self.paint.render()
            return f"{self.paint.render()} + {self.thickness.render()}"

        stroke = {
            "paint": self.paint,
            "thickness": self.thickness,
            "cap": self.cap,
            "join": self.join,
            "dash": self.dash,
            "miter-limit": self.miter_limit,
        }
        return utils.render_mapping({k: v for k, v in stroke.items() if v is not None})
