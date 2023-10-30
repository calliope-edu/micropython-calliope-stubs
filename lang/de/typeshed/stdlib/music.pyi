"""Melodien erstellen und abspielen."""
from typing import Optional, Tuple, Union, List
from .calliope import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""Melodie: die Eröffnung zu Beethovens 5. Sinfonie in C Moll."""
ENTERTAINER: Tuple[str, ...]
"""Melodie: Das Eröffnungsfragment von Scott Joplins Ragtime Klassiker "The Entertainer"."""
PRELUDE: Tuple[str, ...]
"""Melodie: Beginn des ersten Präludiums in C-Dur der 48 Präludien und Fugen von J.S. Bach."""
ODE: Tuple[str, ...]
"""Melodie: Das Thema „Ode an die Freude“ von Beethovens 9. Sinfonie in D Moll."""
NYAN: Tuple[str, ...]
"""Melodie: Das Nyan Cat Thema (http://www.nyan.cat/).

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""Melodie: Etwas, das wie ein Klingelton eines Mobiltelefons klingt.

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""Melodie: Eine funkige Basslinie für Geheimagenten und kriminelle Superhirne."""
BLUES: Tuple[str, ...]
"""Melodie: Ein 12-taktiger Boogie-Woogie-Blues mit Walking Bass."""
BIRTHDAY: Tuple[str, ...]
"""Melodie: "Happy Birthday to You..."

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""Melodie: Der Brautchchor von Wagners Oper "Lohengrin"."""
FUNERAL: Tuple[str, ...]
"""Melodie: der "Trauermarsch", auch bekannt als Frédéric Chopins Klaviersonate Nr. 2 in b♭-Moll, op. 35."""
PUNCHLINE: Tuple[str, ...]
"""Melodie: Ein lustiges Fragment, das anzeigt, dass ein Scherz gemacht worden ist."""
PYTHON: Tuple[str, ...]
"""Melody: John Philip Sousas Marsch „Liberty Bell“ aka, das Thema „Monty Pythons Flying Circus“ (nach dem die Programmiersprache Python benannt ist)."""
BADDY: Tuple[str, ...]
"""Melodie: Auftritt eines Bösewichts in der Stummfilmzeit."""
CHASE: Tuple[str, ...]
"""Melodie: Verfolgungsszene aus der Stummfilmzeit."""
BA_DING: Tuple[str, ...]
"""Melodie: ein kurzes Signal, um darauf hinzuweisen, dass etwas passiert ist."""
WAWAWAWAA: Tuple[str, ...]
"""Melodie: Eine sehr traurige Posaune. (wawawawawa)"""
JUMP_UP: Tuple[str, ...]
"""Melodie: Zur Verwendung in einem Spiel, das eine Aufwärtsbewegung anzeigt."""
JUMP_DOWN: Tuple[str, ...]
"""Melodie: Zur Verwendung in einem Spiel, das eine Abwärtsbewegung anzeigt. (jump up)"""
POWER_UP: Tuple[str, ...]
"""Melodie: Eine Fanfare, die anzeigt, dass ein Erfolg freigeschaltet wurde."""
POWER_DOWN: Tuple[str, ...]
"""Melodie: Eine traurige Fanfare, die anzeigt, dass ein Erfolg verloren wurde."""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """Legt das ungefähre Tempo für die Wiedergabe fest.

Example: ``music.set_tempo(bpm=120)``

:param ticks: Die Anzahl der Ticks, die einen Beat ausmachen.
:param bpm: Eine Ganzzahl, welche die Schläge pro Minute bestimmt.

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """Gibt das aktuelle Tempo als ein Tupel von Ganzzahlen zurück: ``(ticks, bpm)``.

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """Spielt Musik ab.

Example: ``music.play(music.NYAN)``

:param music: Musik in einer `speziellen Notation <https://calliope.cc/programmieren/editoren/python/python-api#musicalnotation>`_ angegeben
:param pin: Der Ausgabepin für den Einsatz mit einem externen Lautsprecher (Standard ``pin0``), ``None`` für keinen Klang.
:param wait: Wenn ``wait`` auf ``True`` gesetzt ist, blockiert diese Funktion.
:param loop: Wenn ``loop`` auf ``True`` gesetzt ist, wird die Melodie wiederholt, bis ``stop`` aufgerufen oder der blockierende Aufruf unterbrochen wird.

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """Eine Note spielen.

Example: ``music.pitch(185, 1000)``

:param frequency: Eine Ganzzahl-Frequenz
:param duration: Eine Millisekundendauer. Wenn negativ, dann wird der Ton bis zum nächsten Aufruf oder ``stop`` fortgesetzt.
:param pin: Optionaler Ausgabepin (Standard ``pin0``).
:param wait: Wenn ``wait`` auf ``True`` gesetzt ist, blockiert diese Funktion.

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Stoppt die gesamte Musikwiedergabe auf dem eingebauten Lautsprecher und jedem Pin mit Tonausgabe.

Example: ``music.stop()``

:param pin: Ein optionales Argument kann zur Angabe eines Pins mitgegeben werden, z.B. ``music.stop(pin1)``."""

def reset() -> None:
    """Setzt Ticks, bpm, Dauer und Oktave auf ihre Standardwerte zurück.

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...