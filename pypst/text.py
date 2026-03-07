from dataclasses import dataclass, field
from collections.abc import Sequence

from pypst.color import Color
from pypst.functional import Functional
from pypst.renderable import Renderable
from pypst.stroke import Stroke
from pypst.quantity import Length, Ratio
from pypst.utils import Function

POSITIONAL_FIELD_METADATA: dict[str, bool] = {"positional": True}
OPTIONAL_FIELD_METADATA: dict[str, bool] = {"keep_none": False}


@dataclass
class Text(Function):
    """
    Customizes the look and layout of text.

    Corresponds to the Typst ``text`` function.
    https://typst.app/docs/reference/text/text/

    Args:
        font: A font family name or priority list of font family descriptors.
        fallback: Whether to allow last resort font fallback.
        style: The desired font style ("normal", "italic", or "oblique").
        weight: The desired thickness of the font's glyphs (100-900 or name).
        stretch: The desired width of the glyphs.
        size: The size of the glyphs.
        fill: The glyph fill paint.
        stroke: How to stroke the text.
        tracking: Space added between characters.
        spacing: Space between words.
        cjk_latin_spacing: Whether to auto-insert spacing between CJK and Latin.
        baseline: Amount to shift the text baseline by.
        overhang: Whether certain glyphs can hang over into the margin.
        top_edge: The top end of the conceptual frame around the text.
        bottom_edge: The bottom end of the conceptual frame around the text.
        lang: An ISO 639-1/2/3 language code.
        region: An ISO 3166-1 alpha-2 region code.
        script: The OpenType writing script.
        dir: The dominant direction for text and inline objects.
        hyphenate: Whether to hyphenate text to improve line breaking.
        costs: Cost overrides for layout choices (hyphenation, runt, widow, orphan).
        kerning: Whether to apply kerning.
        alternates: Whether to apply stylistic alternates.
        stylistic_set: Which stylistic sets to apply (1-20).
        ligatures: Whether standard ligatures are active.
        discretionary_ligatures: Whether discretionary ligatures are active.
        historical_ligatures: Whether historical ligatures are active.
        number_type: Which kind of numbers to select ("lining" or "old-style").
        number_width: The width of numbers ("proportional" or "tabular").
        slashed_zero: Whether to have a slash through the zero glyph.
        fractions: Whether to turn numbers into fractions.
        features: Raw OpenType features to apply.
        body: Content in which all text is styled according to the other arguments.
    """

    font: str | Sequence[str | dict[str, str]] | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    fallback: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    style: str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    weight: int | str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    stretch: Ratio | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    size: Length | None = field(
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
    tracking: Length | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    spacing: Length | Ratio | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    cjk_latin_spacing: str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    baseline: Length | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    overhang: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    top_edge: Length | str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    bottom_edge: Length | str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    lang: str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    region: str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    script: str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    dir: str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    hyphenate: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    costs: dict[str, Ratio] | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    kerning: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    alternates: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    stylistic_set: int | Sequence[int] | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    ligatures: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    discretionary_ligatures: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    historical_ligatures: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    number_type: str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    number_width: str | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    slashed_zero: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    fractions: bool | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    features: Sequence[str] | dict[str, int] | None = field(
        default=None,
        metadata=OPTIONAL_FIELD_METADATA,
    )
    body: Renderable | Functional | None = field(
        default=None, metadata=POSITIONAL_FIELD_METADATA
    )
