"""Pins, Bilder, Töne, Temperatur und Lautstärke."""
from typing import Any, Callable, List, Optional, Tuple, Union, overload
from _typeshed import ReadableBuffer
from . import accelerometer as accelerometer
from . import audio as audio
from . import compass as compass
from . import display as display
from . import i2c as i2c
from . import microphone as microphone
from . import speaker as speaker
from . import spi as spi
from . import uart as uart

def run_every(callback: Optional[Callable[[], None]]=None, days: int=0, h: int=0, min: int=0, s: int=0, ms: int=0) -> Callable[[Callable[[], None]], Callable[[], None]]:
    """Eine geplante Funktion, die in dem von den Zeitargumenten angegebenen Intervall ausgeführt wird. **V3** (alle)

Example: ``run_every(my_logging, min=5)``

``run_every`` can be used in two ways:

As a Decorator - placed on top of the function to schedule. For example::

    @run_every(h=1, min=20, s=30, ms=50)
    def my_function():
        # Do something here

As a Function - passing the callback as a positional argument. For example::

    def my_function():
        # Do something here
    run_every(my_function, s=30)

Each argument corresponds to a different time unit and they are additive.
So ``run_every(min=1, s=30)`` schedules the callback every minute and a half.

When an exception is thrown inside the callback function it deschedules the
function. To avoid this you can catch exceptions with ``try/except``.

:param callback: Funktion, die im angegebenen Intervall aufgerufen wird.
:param days: Legt die Tagesmarke für die Zeitplanung fest.
:param h: Legt die Stundenmarke für die Zeitplanung fest.
:param min: Legt die Uhrzeitmarke für die Zeitplanung fest.
:param s: Legt die Sekundenmarke für die Zeitplanung fest.
:param ms: Legt die Millisekundenmarke für die Zeitplanung fest."""

def panic(n: int) -> None:
    """Einen Panikmodus starten.

Example: ``panic(127)``

:param n: Ein beliebiger Integer <= 255, um einen Status anzuzeigen.

Requires restart."""

def reset() -> None:
    """Startet den Calliope mini neu."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """Konvertiert einen Wert aus einem Bereich in einen Ganzzahlbereich.

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: Eine zu konvertierende Zahl.
:param from_: Ein Tupel (das ist eine geordnete Sammlung von Werten), um den Bereich festzulegen, aus dem konvertiert werden soll.
:param to: Ein Tupel, um den Bereich festzulegen, zu dem konvertiert werden soll.
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """Konvertiert einen Wert von einem Bereich in einen Gleitkommabereich.

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: Eine zu konvertierende Zahl.
:param from_: Ein Tupel, um den Bereich festzulegen, aus dem konvertiert werden soll.
:param to: Ein Tupel, um den Bereich festzulegen, zu dem konvertiert werden soll.
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """Für ``n`` Millisekunden warten.

Example: ``sleep(1000)``

:param n: Die Anzahl der zu wartenden Millisekunden

One second is 1000 milliseconds, so::

    calliope.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Gibt die Laufzeit des Calliope mini zurück.

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Erhalte die Temperatur des Calliope mini in Grad Celcius."""

def set_volume(v: int) -> None:
    """Legt die Lautstärke fest.

Example: ``set_volume(127)``

:param v: ein Wert zwischen 0 (niedrig) und 255 (hoch).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """Die Klasse für die Tasten ``button_a`` und ``button_b``. (Tasten)"""

    def is_pressed(self) -> bool:
        """Überprüft, ob die Taste gedrückt wird.

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Überprüft, ob die Schaltfläche seit dem Start des Calliope mini oder beim letzten Aufruf dieser Methode gedrückt wurde.

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Ermittelt die laufende Gesamtzahl der Tastenbetätigungen und setzt diese Summe auf Null zurück, bevor es weitergeht.

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""Das ``Button`` Objekt der linken Taste."""
button_b: Button
"""Das ``Button`` Objekt der rechten Taste."""

class MicroBitDigitalPin:
    """Ein digitaler Pin. (calliopeminidigitalpin)

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Gibt den digitalen Wert des Pins zurück.

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Setzt den digitalen Wert des Pins.

Example: ``pin0.write_digital(1)``

:param value: 1, um den Pin auf high zu setzen, oder 0, um den Pin auf low zu setzen"""
        ...

    def set_pull(self, value: int) -> None:
        """Setzt den Pull-Status auf einen von drei möglichen Werten: ``PULL_UP``, ``PULL_DOWN`` oder ``NO_PULL``.

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: Der Pull-Status des entsprechenden Pins, z.B. ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Ermittelt den Pull-Zustand eines Pins.

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Gibt den Pin-Modus zurück.

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Gib ein PWM-Signal am Pin aus, bei dem das Verhältnis von An- zu Auszeit proportional zu ``Wert`` ist.

Example: ``pin0.write_analog(254)``

:param value: Eine ganze Zahl oder eine Gleitkommazahl zwischen 0 (0 % Einsatzzeit) und 1023 (100 % Einsatzzeit)."""

    def set_analog_period(self, period: int) -> None:
        """Setzt den Zeitraum des PWM-Signals, das ausgegeben wird, auf ``period`` in Millisekunden.

Example: ``pin0.set_analog_period(10)``

:param period: Der Zeitraum in Millisekunden mit einem Mindestwert von 1ms."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Setzt den Zeitraum des PWM-Signals, das ausgegeben wird, auf ``period`` in Millisekunden.

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: Der Zeitraum in Millisekunden mit einem Mindestwert von 1ms."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """Ein Pin mit analogen und digitalen Eigenschaften. (calliopeanalogdigitalpin)"""

    def read_analog(self) -> int:
        """Gibt die Spannung aus, die an dem Pin anliegt.

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """Ein Pin mit Analog-, Digital- und Touch-Funktionen. (calliopeminitouchpin)"""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Überprüft, ob der Pin berührt wird.

Example: ``pin0.is_touched()``

The default touch mode for the pins on the edge connector is ``resistive``.
The default for the logo pin **V2** is ``capacitive``.

**Resistive touch**
This test is done by measuring how much resistance there is between the
pin and ground.  A low resistance gives a reading of ``True``.  To get
a reliable reading using a finger you may need to touch the ground pin
with another part of your body, for example your other hand.

**Capacitive touch**
This test is done by interacting with the electric field of a capacitor
using a finger as a conductor. `Capacitive touch
<https://www.allaboutcircuits.com/technical-articles/introduction-to-capacitive-touch-sensing>`_
does not require you to make a ground connection as part of a circuit.

:return: ``True`` if the pin is being touched with a finger, otherwise return ``False``."""
        ...

    def set_touch_mode(self, value: int) -> None:
        """Legt den Touch-Modus für den Pin fest.

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: ``CAPACITIVE`` oder ``RESISTIVE`` von dem entsprechenden Pin."""
        ...
pin0: MicroBitTouchPin
"""Pin mit digitalen, analogen und Touch-Funktionen."""
pin1: MicroBitTouchPin
"""Pin mit digitalen, analogen und Touch-Funktionen."""
pin2: MicroBitTouchPin
"""Pin mit digitalen, analogen und Touch-Funktionen."""
pin3: MicroBitTouchPin
"""Pin mit digitalen, analogen und Touch-Funktionen."""
pin4: MicroBitAnalogDigitalPin
"""Pin mit digitalen und analogen Funktionen."""
pin5: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin6: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin7: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin8: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin9: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin10: MicroBitAnalogDigitalPin
"""Pin mit digitalen und analogen Funktionen."""
pin11: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin12: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin13: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin14: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin15: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin16: MicroBitAnalogDigitalPin
"""Pin mit digitalen Funktionen."""
pin17: MicroBitDigitalPin
"""Pin with digital features."""
pin19: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin20: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin_logo: MicroBitTouchPin
"""Ein Touch-Pin auf der Rückseite des Calliope mini, der standardmäßig auf den kapazitiven Berührungsmodus eingestellt ist."""
pin_speaker: MicroBitAnalogDigitalPin
"""Ein Pin um den Calliope mini Lautsprecher anzusprechen.

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""
pin_M0_SPEED: MicroBitDigitalPin
"""Pin with digital features."""
pin_M0_DIR: MicroBitDigitalPin
"""Pin with digital features."""
pin_M1_SPEED: MicroBitDigitalPin
"""Pin with digital features."""
pin_M1_DIR: MicroBitDigitalPin
"""Pin with digital features."""
pin_A0_SDA: MicroBitDigitalPin
"""Pin with digital features."""
pin_A0_SCL: MicroBitDigitalPin
"""Pin with digital features."""
pin_A1_RX: MicroBitDigitalPin
"""Pin with digital features."""
pin_A1_TX: MicroBitDigitalPin
"""Pin with digital features."""
pin_M_MODE: MicroBitDigitalPin
"""Pin with digital features."""

class Image:
    """Ein Bild, das auf der Calliope mini LED-Matrix angezeigt wird.

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Herz-Symbol."""
    HEART_SMALL: Image
    """Kleines Herz-Symbol."""
    HAPPY: Image
    """Happy-Symbol."""
    SMILE: Image
    """Smiley-Symbol."""
    SAD: Image
    """Trauriger-Smiley-Symbol."""
    CONFUSED: Image
    """Verwirrt-Symbol."""
    ANGRY: Image
    """Sauer-Smiley-Symbol."""
    ASLEEP: Image
    """Schlafender-Smiley-Symbol."""
    SURPRISED: Image
    """Überraschter-Smiley-Symbol."""
    SILLY: Image
    """Alberner-Smiley-Symbol."""
    FABULOUS: Image
    """Cooler-Smiley-Symbol."""
    MEH: Image
    """Gleichgültiger-Smiley-Symbol."""
    YES: Image
    """Richtig-Symbol."""
    NO: Image
    """Falsch-Symbol."""
    CLOCK12: Image
    """12 Uhr Symbol."""
    CLOCK11: Image
    """11 Uhr Symbol."""
    CLOCK10: Image
    """10 Uhr Symbol."""
    CLOCK9: Image
    """9 Uhr Symbol."""
    CLOCK8: Image
    """8 Uhr Symbol."""
    CLOCK7: Image
    """7 Uhr Symbol."""
    CLOCK6: Image
    """6 Uhr Symbol."""
    CLOCK5: Image
    """5 Uhr Symbol."""
    CLOCK4: Image
    """4 Uhr Symbol."""
    CLOCK3: Image
    """3 Uhr Symbol."""
    CLOCK2: Image
    """2 Uhr Symbol."""
    CLOCK1: Image
    """1 Uhr Symbol."""
    ARROW_N: Image
    """Pfeil, der nach Norden zeigt."""
    ARROW_NE: Image
    """Pfeil, der nach Nordosten zeigt."""
    ARROW_E: Image
    """Pfeil, der nach Osten zeigt."""
    ARROW_SE: Image
    """Pfeil, der nach Südosten zeigt."""
    ARROW_S: Image
    """Pfeil, der nach Süden zeigt."""
    ARROW_SW: Image
    """Pfeil, der nach Südwest zeigt."""
    ARROW_W: Image
    """Pfeil, der nach Westen zeigt."""
    ARROW_NW: Image
    """Pfeil, der nach Nordwesten zeigt."""
    TRIANGLE: Image
    """Symbol eines Dreiecks, das nach oben zeigt."""
    TRIANGLE_LEFT: Image
    """Symbol eines Dreiecks in der linken Ecke."""
    CHESSBOARD: Image
    """Schachbrettmuster-Symbol."""
    DIAMOND: Image
    """Diamant-Symbol."""
    DIAMOND_SMALL: Image
    """Kleines Diamant-Symbol."""
    SQUARE: Image
    """Quadrat-Symbol."""
    SQUARE_SMALL: Image
    """Kleines Quadratisches Symbol."""
    RABBIT: Image
    """Kaninchen-Symbol."""
    COW: Image
    """Kuh-Symbol."""
    MUSIC_CROTCHET: Image
    """Viertelnote-Symbol."""
    MUSIC_QUAVER: Image
    """Achtelnote-Symbol."""
    MUSIC_QUAVERS: Image
    """Pärchen-Achtelnoten-Symbol."""
    PITCHFORK: Image
    """Heugabel-Symbol."""
    XMAS: Image
    """Weihnachtsbaum-Symbol."""
    PACMAN: Image
    """Pac-Man Figur Symbol. (pac-man)"""
    TARGET: Image
    """Ziel-Symbol."""
    TSHIRT: Image
    """T-Shirt Symbol."""
    ROLLERSKATE: Image
    """Rollerskate Symbol."""
    DUCK: Image
    """Enten-Symbol."""
    HOUSE: Image
    """Haus-Symbol."""
    TORTOISE: Image
    """Schildkröten-Symbol."""
    BUTTERFLY: Image
    """Schmetterling Symbol."""
    STICKFIGURE: Image
    """Strichmännchen-Symbol."""
    GHOST: Image
    """Geister-Symbol."""
    SWORD: Image
    """Schwert-Symbol."""
    GIRAFFE: Image
    """Giraffen-Symbol."""
    SKULL: Image
    """Totenkopf-Symbol."""
    UMBRELLA: Image
    """Regenschirm-Symbol."""
    SNAKE: Image
    """Schlangen-Symbol."""
    SCISSORS: Image
    """Scheren-Symbol."""
    ALL_CLOCKS: List[Image]
    """Eine Liste mit allen Zeit Symbolen in einer Reihenfolge."""
    ALL_ARROWS: List[Image]
    """Eine Liste mit allen Pfeil-Symbolen in Reihenfolge."""

    @overload
    def __init__(self, string: str) -> None:
        """Ein Bild aus einer Zeichenkette erstellen, die beschreibt, welche LEDs leuchten.

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: Die Zeichenkette, die das Bild beschreibt."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Ein leeres Bild mit ``width`` Spalten und ``height`` Zeilen erstellen.

:param width: Optionale Breite des Bildes
:param height: Optionale Höhe des Bildes
:param buffer: Optionales Array oder Bytes von ``width``×``height`` Ganzzahlen im Bereich 0-9 zur Initialisierung des Bildes

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Gibt die Anzahl der Spalten zurück.

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Gibt die Anzahl der Zeilen zurück.

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Legt die Helligkeit eines Pixels fest.

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: Die Spaltenzahl
:param y: Die Zeilenzahl
:param value: Die Helligkeit als Ganzzahl zwischen 0 (dunkel) und 9 (hell)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """Gibt die Helligkeit eines Pixels zurück.

Example: ``my_image.get_pixel(0, 0)``

:param x: Die Spaltennummer
:param y: Die Zeilenzahl
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Erstellt ein neues Bild, indem das Bild nach links verschoben wird.

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: Die Anzahl der zu verschiebenden Spalten um
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Erstellt ein neues Bild, indem das Bild nach rechts verschoben wird.

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: Die Anzahl der zu verschiebenden Spalten um
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Erstellt ein neues Bild, indem das Bild nach oben verschoben wird.

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: Die Anzahl der zu verschiebenden Zeilen um
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Erstellt ein neues Bild, indem das Bild nach unten verschoben wird.

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: Die Anzahl der zu verschiebenden Zeilen
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Erstellt ein neues Bild durch Zuschneiden des Bildes.

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: Die Spalte für den Beschnitt
:param y: Die Zeile für den Beschnitt
:param w: Beschnittbreite
:param h: Beschnitthöhe
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Eine exakte Kopie des Bildes erstellen.

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Erstelle ein neues Bild, indem du die Helligkeit der Pixel im
Quellbild invertierst.

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Setzt die Helligkeit aller Pixel im Bild.

Example: ``my_image.fill(5)``

:param value: Die Helligkeit als Ganzzahl zwischen 0 (dunkel) und 9 (hell).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Kopiere einen Bereich von einem anderen Bild in dieses Bild.

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: Das Ausgangsbild
:param x: Versatz der Anfangsspalte im Ausgangsbild
:param y: Versatz der Startreihe im Ausgangsbild
:param w: Die Anzahl der zu kopierenden Spalten
:param h: Die Anzahl der zu kopierenden Zeilen
:param xdest: Der zu ändernde Spaltenversatz in diesem Bild
:param ydest: Der Zeilenversatz, der in diesem Bild geändert werden soll

Pixels outside the source image are treated as having a brightness of 0.

``shift_left()``, ``shift_right()``, ``shift_up()``, ``shift_down()``
and ``crop()`` can are all implemented by using ``blit()``.

For example, img.crop(x, y, w, h) can be implemented as::

    def crop(self, x, y, w, h):
        res = Image(w, h)
        res.blit(self, x, y, w, h)
        return res"""
        ...

    def __repr__(self) -> str:
        """Get a compact string representation of the image."""
        ...

    def __str__(self) -> str:
        """Ermittelt eine lesbare Zeichenkette, die das Bild darstellt."""
        ...

    def __add__(self, other: Image) -> Image:
        """Erstellt ein neues Bild, indem die Helligkeitswerte der beiden Bilder für jedes Pixel genommen werden.

Example: ``Image.HEART + Image.HAPPY``

:param other: Das zu addierende Bild."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Erstellt ein neues Bild durch Subtraktion der Helligkeitswerte des anderen Bildes von diesem Bild.

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: Das zu subtrahierende Bild."""
        ...

    def __mul__(self, n: float) -> Image:
        """Create a new image by multiplying the brightness of each pixel by
``n``.

Example: ``Image.HEART * 0.5``

:param n: Der Wert, mit dem multipliziert werden soll."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Create a new image by dividing the brightness of each pixel by
``n``.

Example: ``Image.HEART / 2``

:param n: Der Wert, durch den dividiert werden soll."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Stellt den Übergang von Schallereignissen dar, von ``quiet`` zu ``loud`` wie Klatschen oder Schreien."""
    QUIET: SoundEvent
    """Stellt den Übergang von Tonereignissen dar, von ``loud`` zu ``quiet`` wie Sprechen oder Hintergrundmusik."""

class Sound:
    """Die eingebauten Töne können mit ``audio.play(Sound.NAME)`` aufgerufen werden."""
    GIGGLE: Sound
    """Giggle-Ton."""
    HAPPY: Sound
    """Fröhlicher-Ton."""
    HELLO: Sound
    """Begrüßungs-Ton."""
    MYSTERIOUS: Sound
    """Geheimnisvoller-Ton."""
    SAD: Sound
    """Trauriger-Ton."""
    SLIDE: Sound
    """Rutschender-Ton."""
    SOARING: Sound
    """Aufsteigender-Ton."""
    SPRING: Sound
    """Frühlingsklänge."""
    TWINKLE: Sound
    """Funkelnder-Ton."""
    YAWN: Sound
    """Gähnendes-Geräusch."""