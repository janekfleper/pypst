from collections.abc import Sequence
from dataclasses import dataclass, field

from pypst.color import Color
from pypst.functional import Functional
from pypst.quantity import Fraction, Length, Ratio
from pypst.renderable import Renderable
from pypst.stroke import Stroke
from pypst.utils import Function

POSITIONAL_FIELD_METADATA: dict[str, bool] = {"positional": True}
OPTIONAL_FIELD_METADATA: dict[str, bool] = {"keep_none": False}
VARIADIC_FIELD_METADATA: dict[str, bool] = {"variadic": True}


@dataclass
class GridCell(Function):
    """
    A cell in the grid.

    Args:
        x: The cell's column (zero-indexed).
        y: The cell's row (zero-indexed).
        colspan: The amount of columns spanned by this cell.
        rowspan: The amount of rows spanned by this cell.
        inset: The cell's inset override.
        align: The cell's alignment override.
        fill: The cell's fill override.
        stroke: The cell's stroke override.
        breakable: Whether rows spanned by this cell can be placed in different pages.
        body: The cell's body.

    Examples:
        >>> GridCell(x=2, y=3, colspan=2).render()
        '#grid.cell(x: 2, y: 3, colspan: 2)'

        >>> GridCell(x=1, fill="red", body=Content("A")).render()
        '#grid.cell(x: 1, fill: red, #[A])'
    """

    __is_function__ = "grid.cell"

    x: int | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    y: int | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    colspan: int | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    rowspan: int | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    inset: Length | Ratio | str | dict[str, str] | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    align: str | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    fill: Color | str | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    stroke: Length | Color | Stroke | str | dict[str, str] | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    breakable: bool | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    body: Renderable | Functional | None = field(
        default=None,
        metadata=POSITIONAL_FIELD_METADATA,
    )


@dataclass
class GridHorizontalLine(Function):
    """
    A horizontal line in the grid.

    Args:
        y: The row above which the horizontal line is placed (zero-indexed).
        start: The column at which the horizontal line starts (zero-indexed, inclusive).
        end: The column before which the horizontal line ends (zero-indexed, exclusive).
        stroke: The line's stroke.
        position: The position at which the line is placed ("top" or "bottom").

    Examples:
        >>> GridHorizontalLine(y=1).render()
        '#grid.hline(y: 1)'

        >>> GridHorizontalLine(y=2, start=1, end=3, stroke="2pt").render()
        '#grid.hline(y: 2, start: 1, end: 3, stroke: 2pt)'

        >>> GridHorizontalLine(y=0, position="bottom").render()
        '#grid.hline(y: 0, position: bottom)'
    """

    __is_function__ = "grid.hline"

    y: int | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    start: int | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    end: int | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    stroke: Length | Color | Stroke | str | dict[str, str] | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    position: str | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)


@dataclass
class GridVerticalLine(Function):
    """
    A vertical line in the grid.

    Args:
        x: The column at which the vertical line is placed (zero-indexed, inclusive).
        start: The row at which the vertical line starts (zero-indexed, inclusive).
        end: The row before which the vertical line ends (zero-indexed, exclusive).
        stroke: The line's stroke.
        position: The position at which the line is placed ("start" or "end").

    Examples:
        >>> GridVerticalLine(x=1).render()
        '#grid.vline(x: 1)'

        >>> GridVerticalLine(x=2, start=0, end=3, stroke="red + 1pt").render()
        '#grid.vline(x: 2, start: 0, end: 3, stroke: red + 1pt)'

        >>> GridVerticalLine(x=1, position="end").render()
        '#grid.vline(x: 1, position: end)'
    """

    __is_function__ = "grid.vline"

    x: int | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    start: int | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    end: int | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    stroke: Length | Color | Stroke | str | dict[str, str] | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    position: str | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)


@dataclass
class GridHeader(Function):
    """
    A repeatable grid header.

    Args:
        repeat: Whether this header should be repeated across pages.
        level: The level of the header.
        children: The cells and lines within the header.

    Examples:
        >>> GridHeader(children=(Content("A"), Content("B"))).render()
        '#grid.header([A], [B])'

        >>> GridHeader(repeat=True, children=(Content("A"), Content("B"))).render()
        '#grid.header(repeat: true, [A])'

        >>> GridHeader(level=2, children=(Content("X"), Content("Y"))).render()
        '#grid.header(level: 2, [X], [Y])'
    """

    __is_function__ = "grid.header"

    repeat: bool | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    level: int | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    children: Sequence[Renderable | Functional | str] = field(
        default_factory=tuple,
        metadata=VARIADIC_FIELD_METADATA,
    )


@dataclass
class GridFooter(Function):
    """
    A repeatable grid footer.

    Args:
        repeat: Whether this footer should be repeated across pages.
        children: The cells and lines within the footer.

    Examples:
        >>> GridFooter(children=(Content("A"), Content("B"))).render()
        '#grid.footer([A], [B])'
    """

    __is_function__ = "grid.footer"

    repeat: bool | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    children: Sequence[Renderable | Functional | str] = field(
        default_factory=tuple,
        metadata=VARIADIC_FIELD_METADATA,
    )


@dataclass
class Grid(Function):
    """
    Arranges content in a grid.

    Args:
        columns: The column sizes.
        rows: The row sizes.
        gutter: The gaps between rows and columns.
        column_gutter: The gaps between columns.
        row_gutter: The gaps between rows.
        inset: Padding for the cells' content.
        align: Alignment for the cells' content.
        fill: Fill style for the cells.
        stroke: Stroke style for the cells.
        children: The contents of the grid cells, plus any extra grid lines.
    """

    __is_function__ = True

    columns: (
        int
        | str
        | Fraction
        | Length
        | Ratio
        | Sequence[str | Fraction | Length | Ratio]
        | None
    ) = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    rows: (
        int
        | str
        | Fraction
        | Length
        | Ratio
        | Sequence[str | Fraction | Length | Ratio]
        | None
    ) = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    gutter: (
        int
        | str
        | Fraction
        | Length
        | Ratio
        | Sequence[str | Fraction | Length | Ratio]
        | None
    ) = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    column_gutter: (
        int
        | str
        | Fraction
        | Length
        | Ratio
        | Sequence[str | Fraction | Length | Ratio]
        | None
    ) = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    row_gutter: (
        int
        | str
        | Fraction
        | Length
        | Ratio
        | Sequence[str | Fraction | Length | Ratio]
        | None
    ) = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    inset: Length | Ratio | str | dict[str, str] | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    align: str | Sequence[str] | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    fill: Color | str | Sequence[str | Color] | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    stroke: Length | Color | Stroke | str | dict[str, str] | Sequence[str] | None = (
        field(
            default=None,
            metadata=OPTIONAL_FIELD_METADATA,
        )
    )
    children: Sequence[Renderable | Functional | str] = field(
        default_factory=tuple, metadata=VARIADIC_FIELD_METADATA
    )
