"""Mathematische Funktionen."""
from typing import Tuple

def acos(x: float) -> float:
    """Berechnung des inversen Cosinus.

Example: ``math.acos(1)``

:param x: Eine Zahl
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """Berechnung des inversen Sinus.

Example: ``math.asin(0)``

:param x: Eine Zahl
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """Berechnung des inversen Tangens.

Example: ``math.atan(0)``

:param x: Eine Zahl
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """Berechnung des Hauptwerts des inversen Tangens von ``y/x``.

Example: ``math.atan2(0, -1)``

:param y: Eine Zahl
:param x: Eine Zahl
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """Rundet eine Zahl hin zu positiver Unendlichkeit.

Example: ``math.ceil(0.1)``

:param x: Eine Zahl
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """Berechnet ``x`` mit dem Zeichen von ``y``.

Example: ``math.copysign(1, -1)``

:param x: Eine Zahl
:param y: Die Quelle des Zeichens für den Rückgabewert
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """Berechnet den Cosinus von ``x``.

Example: ``math.cos(0)``

:param x: Eine Zahl
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """Bogenmaß in Grad konvertieren.

Example: ``math.degrees(2 * math.pi)``

:param x: Ein Wert im Bogenmaß
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """Berechnet das Exponentielle von ``x``.

Example: ``math.exp(1)``

:param x: Eine Zahl
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """Gibt den absoluten Wert von ``x`` zurück.

Example: ``math.fabs(-0.1)``

:param x: Eine Zahl
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """Rundet eine Zahl hin zu negativer Unendlichkeit.

Example: ``math.floor(0.9)``

:param x: Eine Zahl
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """Berechnet den Rest von ``x/y``.

Example: ``math.fmod(10, 3)``

:param x: Der Zähler
:param y: Der Nenner"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """Zerlegt eine Gleitkommazahl in ihre Mantisse und ihren Exponenten.

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: Eine Fließkommazahl
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """Prüft, ob ein Wert endgültig ist.

Example: ``math.isfinite(float('inf'))``

:param x: Eine Zahl.
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """Prüft, ob ein Wert unendlich ist.

Example: ``math.isinf(float('-inf'))``

:param x: Eine Zahl.
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """Prüft, ob ein Wert keine Zahl (NaN ... Not A Number) ist.

Example: ``math.isnan(float('nan'))``

:param x: Eine Zahl
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """``x * (2**exp)`` berechnen.

Example: ``math.ldexp(0.5, 2)``

:param x: Eine Zahl
:param exp: Ganzzahl-Exponent
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """Berechnet den Logarithmus von ``x`` zur angegebenen Basis (Standardwert ist der natürliche Logorithmus).

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: Eine Zahl
:param base: Die zu verwendende Basis
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """Berechnung der gebrochenen und ganzzahligen Teile von ``x``.

Example: ``fractional, integral = math.modf(1.5)``

:param x: Eine Zahl
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """Gibt ``x`` in der Potenz von ``y`` zurück.

Example: ``math.pow(4, 0.5)``

:param x: Eine Zahl
:param y: Der Exponent
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """Konvertiert Grad in Bogenmaß.

Example: ``math.radians(360)``

:param x: Ein Wert in Grad
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """Berechnet den Sinus von ``x``.

Example: ``math.sin(math.pi/2)``

:param x: Eine Zahl
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """Berechnet die Quadratwurzel von ``x``.

Example: ``math.sqrt(4)``

:param x: Eine Zahl
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """Berechnung des Tangens von ``x``.

Example: ``math.tan(0)``

:param x: Eine Zahl
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """Eine Zahl auf 0 runden.

Example: ``math.trunc(-0.9)``

:param x: Eine Zahl
:return: ``x`` rounded towards zero."""
    ...
e: float
"""Basis des natürlichen Logarithmus"""
pi: float
"""Das Verhältnis des Umfangs eines Kreises zu seinem Durchmesser"""