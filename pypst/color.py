from dataclasses import dataclass, field

from pypst.quantity import Degree, Radian, Ratio
from pypst.utils import Function

"""
The predefined colors from Typst.

https://typst.app/docs/reference/visualize/color/#predefined-colors
"""
PREDEFINED_COLORS: list[str] = [
    "black",
    "gray",
    "silver",
    "white",
    "navy",
    "blue",
    "aqua",
    "teal",
    "eastern",
    "purple",
    "fuchsia",
    "maroon",
    "red",
    "orange",
    "yellow",
    "olive",
    "green",
    "lime",
]


POSITIONAL_FIELD_METADATA: dict[str, bool] = {"positional": True}
OPTIONAL_FIELD_METADATA: dict[str, bool] = {"positional": True, "keep_none": False}


@dataclass
class Color(Function):
    """
    Base class for all colors.
    """

    pass


@dataclass
class ColorPredefined(Color):
    """
    Colors that are predefined in Typst.

    Args:
        color: The color name.
        alpha: The alpha value of the color.

    Examples:
        >>> ColorPredefined("red").render()
        'red'
        >>> ColorPredefined("blue", alpha=Ratio(0.9)).render()
        'blue.transparentize(10.0%)'
    """

    color: str
    alpha: Ratio | None = None

    def render(self) -> str:
        color = self.color
        if self.alpha is not None:
            transparency = Ratio(1 - self.alpha.value)
            color = f"{color}.transparentize({transparency.render()})"
        return color


@dataclass
class ColorLuma(Color):
    """
    Grayscale colors.

    Args:
        lightness: The lightness component.
        alpha: The alpha component.

    Examples:
        >>> ColorLuma(40).render()
        'color.luma(40)'
        >>> ColorLuma(Ratio(0.4), alpha=Ratio(0.9)).render()
        'color.luma(40.0%, 90.0%)'
    """

    __is_function__ = "color.luma"
    lightness: int | Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    alpha: Ratio | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)


@dataclass
class ColorOklab(Color):
    """
    Oklab colors.

    Args:
        lightness: The lightness component.
        a: The a ("green/red")component.
        b: The b ("blue/yellow") component.
        alpha: The alpha component.

    Examples:
        >>> ColorOklab(Ratio(0.5), Ratio(0.2), Ratio(0.3)).render()
        'color.oklab(50.0%, 20.0%, 30.0%)'
        >>> ColorOklab(Ratio(0.9), 0.2, 0.3, alpha=Ratio(0.7)).render()
        'color.oklab(90.0%, 0.2, 0.3, 70.0%)'
    """

    __is_function__ = "color.oklab"
    lightness: Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    a: float | Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    b: float | Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    alpha: Ratio | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)


@dataclass
class ColorOklch(Color):
    """
    Oklch colors.

    Args:
        lightness: The lightness component.
        chroma: The chroma component.
        hue: The hue component.
        alpha: The alpha component.

    Examples:
        >>> ColorOklch(Ratio(0.5), 0.2, Degree(30)).render()
        'color.oklch(50.0%, 20.0%, 30.0%)'
        >>> ColorOklch(Ratio(0.9), Ratio(0.2), 0.3, alpha=Ratio(0.7)).render()
        'color.oklch(90.0%, 20.0%, 30.0%, 70.0%)'
    """

    __is_function__ = "color.oklch"
    lightness: Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    chroma: float | Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    hue: Degree | Radian = field(metadata=POSITIONAL_FIELD_METADATA)
    alpha: int | Ratio | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)


@dataclass
class ColorLinearRGB(Color):
    """
    RGB colors with linear luma.

    Args:
        red: The red component.
        green: The green component.
        blue: The blue component.
        alpha: The alpha component.

    Examples:
        >>> ColorLinearRGB(Ratio(0.5), Ratio(0.6), Ratio(0.7)).render()
        'color.linear-rgb(50.0%, 60.0%, 70.0%)'
        >>> ColorLinearRGB(12, 34, 56, alpha=Ratio(0.9)).render()
        'color.linear-rgb(12, 34, 56, 90.0%)'
    """

    __is_function__ = "color.linear-rgb"
    red: int | Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    green: int | Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    blue: int | Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    alpha: int | Ratio | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)


@dataclass
class ColorRGB(Color):
    """
    RGB colors.

    Args:
        red: The red component.
        green: The green component.
        blue: The blue component.
        alpha: The alpha component.
        hex: The hex color string.

    Examples:
        >>> ColorRGB(Ratio(0.1), Ratio(0.2), Ratio(0.3)).render()
        'color.rgb(10.0%, 20.0%, 30.0%)'
        >>> ColorRGB(128, 153, 179, alpha=Ratio(0.9)).render()
        'color.rgb(128, 153, 179, 90.0%)'
        >>> ColorRGB("#ff15").render()
        'color.rgb("#ff15")'
    """

    __is_function__ = "color.rgb"
    red: int | Ratio | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    green: int | Ratio | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    blue: int | Ratio | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    alpha: int | Ratio | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
    hex: str | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)

    def render(self) -> str:
        if self.hex is not None:
            color = f"color.rgb({self.hex})"
            if self.alpha is not None:
                color += f".transparentize({Ratio(1 - self.alpha.value).render()})"
            return color

        return super().render()


@dataclass
class ColorCMYK(Color):
    """
    CMYK colors.

    Args:
        cyan: The cyan component.
        magenta: The magenta component.
        yellow: The yellow component.
        key: The key (black) component.

    Examples:
        >>> ColorCMYK(Ratio(0.1), Ratio(0.3), Ratio(0.3), Ratio(0.7)).render()
        'color.cmyk(10.0%, 30.0%, 30.0%, 70.0%)'
    """

    __is_function__ = "color.cmyk"
    cyan: Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    magenta: Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    yellow: Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    key: Ratio = field(metadata=POSITIONAL_FIELD_METADATA)


@dataclass
class ColorHSL(Color):
    """
    HSL colors.

    Args:
        hue: The hue component.
        saturation: The saturation component.
        lightness: The lightness component.
        alpha: The alpha component.

    Examples:
        >>> ColorHSL(Radian(0.1), Ratio(0.5), Ratio(0.5)).render()
        'color.hsl(0.1rad, 50.0%, 50.0%)'
        >>> ColorHSL(Degree(27), 40, 50, alpha=Ratio(0.9)).render()
        'color.hsl(27.0deg, 40, 50, 90.0%)'
    """

    __is_function__ = "color.hsl"
    hue: Degree | Radian = field(metadata=POSITIONAL_FIELD_METADATA)
    saturation: int | Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    lightness: int | Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    alpha: int | Ratio | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)


@dataclass
class ColorHSV(Color):
    """
    HSV colors.

    Args:
        hue: The hue component.
        saturation: The saturation component.
        value: The value component.
        alpha: The alpha component.

    Examples:
        >>> ColorHSV(Radian(0.1), Ratio(0.5), Ratio(0.5)).render()
        'color.hsv(0.1rad, 50.0%, 50.0%)'
        >>> ColorHSV(Degree(27), 40, 50, alpha=Ratio(0.9)).render()
        'color.hsv(27.0deg, 40, 50, 90.0%)'
    """

    __is_function__ = "color.hsv"
    hue: Degree | Radian = field(metadata=POSITIONAL_FIELD_METADATA)
    saturation: int | Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    value: int | Ratio = field(metadata=POSITIONAL_FIELD_METADATA)
    alpha: int | Ratio | None = field(default=None, metadata=OPTIONAL_FIELD_METADATA)
