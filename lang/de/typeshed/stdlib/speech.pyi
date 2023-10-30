"""Der Calliope mini kann sprechen, singen und andere sprachähnliche Geräusche machen."""
from typing import Optional
from .calliope import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """Englische Wörter in Laute übersetzen.

Example: ``speech.translate('hello world')``

:param words: Eine Zeichenkette aus englischen Wörtern.
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Laute aussprechen.

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: Die Zeichenkette der auszusprechenden Laute
:param pitch: Eine Zahl, die die Tonhöhe der Stimme repräsentiert
:param speed: Eine Zahl, die die Geschwindigkeit der Stimme angibt
:param mouth: Eine Zahl, welche die Mundart der Stimme repräsentiert
:param throat: Eine Zahl, welche die Stimmführung der Stimme repräsentiert
:param pin: Ein optionales Argument zur Angabe des Ausgabepins kann verwendet werden, um den Standard von ``pin0`` zu überschreiben. Wenn kein Ton gespielt werden, kann ``pin=None`` verwendet werden.

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Englische Wörter sagen.

Example: ``speech.say('hello world')``

:param words: Die Zeichenkette von Wörtern, die zu sagen sind.
:param pitch: Eine Zahl, die die Tonhöhe der Stimme repräsentiert
:param speed: Eine Zahl, die die Geschwindigkeit der Stimme angibt
:param mouth: Eine Zahl, welche die Mundart der Stimme repräsentiert
:param throat: Eine Zahl, welche die Stimmführung der Stimme repräsentiert
:param pin: Ein optionales Argument zur Angabe des Ausgabepins kann verwendet werden, um den Standard von ``pin0`` zu überschreiben. Wenn kein Ton gespielt werden, kann ``pin=None`` verwendet werden.

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Laute singen.

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: Die Zeichenkette der zu singenden Wörter.
:param pitch: Eine Zahl, die die Tonhöhe der Stimme repräsentiert
:param speed: Eine Zahl, die die Geschwindigkeit der Stimme angibt
:param mouth: Eine Zahl, welche die Mundart der Stimme repräsentiert
:param throat: Eine Zahl, welche die Stimmführung der Stimme repräsentiert
:param pin: Ein optionales Argument zur Angabe des Ausgabepins kann verwendet werden, um den Standard von ``pin0`` zu überschreiben. Wenn kein Ton gespielt werden, kann ``pin=None`` verwendet werden.

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...