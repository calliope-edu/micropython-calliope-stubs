"""Die integrierten drei RGB-LEDs sowie individuell adressierbare RGB und RGBW LED-Streifen."""
from .calliope import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """Initialisierung von Neopixel LEDs, die über einen Pin gesteuert werden (bei den integrierten drei RGB-LEDs ist dies pin_RGB).

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: Der Pin, der den Neopixelstreifen steuert.
:param n: Die Anzahl an Neopixeln im Streifen.
:param bpp: Bytes pro Pixel. Für RGBW Neopixel wird 4 statt 3 für RGB und GRB verwendet."""
        ...

    def clear(self) -> None:
        """Alle Pixel löschen.

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """Pixel anzeigen.

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """Zeige die Pixel (Calliope mini V3).

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """Färbt alle Pixel mit einem bestimmten RGB/RGBW-Wert.

Example: ``np.fill((0, 0, 255))``

:param colour: Ein Tupel mit der gleichen Länge wie die Anzahl Bytes pro Pixel (bpp).

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """Eine Pixelfarbe setzen.

Example: ``np[0] = (255, 0, 0)``

:param key: Die Pixelzahl.
:param value: Die Farbe."""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """Gibt die Pixelfarbe zurück.

Example: ``r, g, b = np[0]``

:param key: Die Pixelzahl.
:return: The colour tuple."""

    def __len__(self) -> int:
        """Gibt die Länge dieses Pixelstreifens zurück.

Example: ``len(np)``"""