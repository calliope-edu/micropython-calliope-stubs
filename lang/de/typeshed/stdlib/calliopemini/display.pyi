"""Text, Bilder und Animationen auf der 5×5 LED-Matrix anzeigen."""
from ..calliope import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """Gibt die Helligkeit der LED in Spalte ``x`` und Zeile ``y`` zurück.

Example: ``display.get_pixel(0, 0)``

:param x: Die Matrix-Spalte (0..4)
:param y: Die Matrix-Zeile (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """Gibt die Helligkeit der LED in Spalte ``x`` und Zeile ``y`` zurück.

Example: ``display.set_pixel(0, 0, 9)``

:param x: Die Matrix-Spalte (0..4)
:param y: Die Matrix-Zeile (0..4)
:param value: Die Helligkeit zwischen 0 (aus) und 9 (hell)"""
    ...

def clear() -> None:
    """Setzt die Helligkeit aller LEDs auf 0 (aus).

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """Zeigt Bilder, Buchstaben oder Ziffern auf der LED-Matrix an.

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: Eine Zeichenkette, Nummer, Bild oder Liste der anzuzeigenden Bilder.
:param delay: Jeder Buchstabe, Ziffer oder Bild wird mit ``delay`` Millisekunden zwischen ihnen angezeigt.
:param wait: Wenn ``wait`` ``True`` ist, wird diese Funktion blockiert, bis die Animation beendet ist, andernfalls wird die Animation im Hintergrund stattfinden.
:param loop: Wenn ``loop`` ``True`` ist, wird die Animation für immer wiederholt.
:param clear: Wenn ``clear`` ``True`` ist, wird die Matrix gelöscht, nachdem die Sequenz beendet ist.

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """Scrollt eine Zahl oder einen Text auf der LED-Matrix.

Example: ``display.scroll('Calliope mini')``

:param text: Die zu scrollende Zeichenfolge. Wenn ``text`` eine Ganzzahl oder ein Gleitkommazahl ist, wird diese zuerst mit ``str()`` in eine Zeichenfolge (String) konvertiert.
:param delay: Der Parameter ``delay`` legt fest, wie schnell der Text scrollt.
:param wait: Wenn ``wait`` ``True`` ist, wird diese Funktion blockiert, bis die Animation beendet ist, andernfalls wird die Animation im Hintergrund stattfinden.
:param loop: Wenn ``loop`` ``True`` ist, wird die Animation für immer wiederholt.
:param monospace: Wenn ``monospace`` ``True`` ist, werden die Zeichen alle 5 Pixel-Spalten in der Breite beanspruchen, andernfalls gibt es genau 1 leere Pixelspalte zwischen jedem Zeichen, beim scrollen.

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """LED-Matrix anschalten.

Example: ``display.on()``"""
    ...

def off() -> None:
    """LED-Matrix ausschalten (Deaktivieren der Matrix erlaubt es, die GPIO-Pins für andere Zwecke zu verwenden).

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """Überprüft, ob die LED-Matrix ist.

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """Die Lichtintensität messen.

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...