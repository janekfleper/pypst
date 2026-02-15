from dataclasses import dataclass
from collections.abc import Mapping, Sequence

import numpy as np
from pypst import utils


@dataclass
class Quantity:
    """
    A quantity with a value and a unit.

    This class takes care of scaling, rounding and applying the unit.

    Args:
        value: The value of the quantity.
        unit: The unit of the quantity.
        scale: The scale of the quantity.
        digits: The number of digits to round the quantity to.

    Examples:
        >>> Quantity(1, "mm").render()
        '1mm'
        >>> Quantity(0.9, "fr").render()
        '0.9fr'
        >>> Quantity(1, "m", digits=2).render()
        '1.00m'
    """

    value: int | float | Sequence[int | float] | Mapping[str, int | float]
    unit: str
    scale: int | float | None = None
    digits: int | None = 3

    def render(self) -> str:
        scale = 1 if self.scale is None else self.scale
        unit = "" if self.unit is None else self.unit

        if isinstance(self.value, (int, float, np.integer, np.floating)):
            scaled = self.value * scale
            if self.digits is not None:
                scaled = round(scaled, self.digits)
            return f"{scaled}{unit}"

        if isinstance(self.value, Mapping):
            keys = self.value.keys()
            values = self.value.values()
        else:
            keys = None
            values = self.value

        scaled = [v * scale for v in values]
        if self.digits is not None:
            scaled = [round(v, self.digits) for v in scaled]
        values = [f"{v}{unit}" for v in scaled]

        if keys is None:
            return utils.render_sequence(values)
        return utils.render_mapping(dict(zip(keys, values)))


@dataclass
class Fraction(Quantity):
    """
    A quantity for relative layout spacing.

    Args:
        value: The value of the fraction.
        digits: The number of digits to round the value to.

    Examples:
        >>> Fraction(0.9).render()
        '0.9fr'
    """

    unit: str = "fr"
    scale: int = 1


@dataclass
class Degree(Quantity):
    """
    A quantity for angles in degree.

    Args:
        value: The value of the angle in degree.
        digits: The number of digits to round the value to.

    Examples:
        >>> Degree(27).render()
        '27deg'
    """

    unit: str = "deg"
    scale: int = 1

    @classmethod
    def from_radian(cls, radian: float, digits: int | None = None) -> "Degree":
        return cls(radian * (180 / np.pi), digits=digits)


@dataclass
class Radian(Quantity):
    """
    A quantity for angles in radian.

    Args:
        value: The value of the angle in radian.
        digits: The number of digits to round the value to.

    Examples:
        >>> Radian(27).render()
        '0.9rad'
    """

    unit: str = "rad"
    scale: int = 1

    @classmethod
    def from_degree(cls, degree: float, digits: int | None = None) -> "Radian":
        return cls(degree * np.pi / 180, digits=digits)


@dataclass
class Ratio(Quantity):
    """
    A quantity for ratios in percent.

    Args:
        value: The value of the ratio.
        digits: The number of digits to round the value to.

    Examples:
        >>> Ratio(0.27).render()
        '27%'
    """

    unit: str = "%"
    scale: int = 100
