"""Töne mit dem Calliope mini (V3) abspielen."""
from ..calliope import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Wiedergeben eines integrierten Tons, Toneffekts oder benutzerdefinierter Audioschnipsel.

Example: ``audio.play(Sound.GIGGLE)``

:param source: Ein integrierter ``Sound`` wie ``Sound.GIGGLE``, ein ``SoundEffect`` oder Beispieldaten als Abfolge von ``AudioFrame`` Objekten.
:param wait: Wenn ``wait`` ``True``ist, wird diese Funktion blockiert, bis der Ton beendet ist.
:param pin: Ein optionales Argument zur Angabe des Ausgabepins kann verwendet werden, um den Standard von ``pin0`` zu überschreiben. Wenn kein Ton gespielt werden, kann ``pin=None`` verwendet werden.
:param return_pin: (return Pin) Bestimmt einen Pin, der an einen externen Lautsprecher anstatt an Ground angeschlossen werden soll. Dies wird bei dem Calliope mini **V3** ignoriert."""

def is_playing() -> bool:
    """Prüft, ob ein Ton abgespielt wird.

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """Audio-Wiedergabe stoppen.

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """Ein Soundeffekt, der aus einer Reihe von Parametern besteht, die über den Konstruktor oder die Attribute konfiguriert werden."""
    WAVEFORM_SINE: ClassVar[int]
    """Für den Parameter ``waveform`` verwendete Sinuswellen-Option."""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """Die Option Sägezahnwellen wird für den Parameter ``waveform`` verwendet."""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """Für den Parameter ``waveform`` verwendete Dreieckswellen-Option."""
    WAVEFORM_SQUARE: ClassVar[int]
    """Für den Parameter ``waveform`` verwendete Rechteckwellen-Option."""
    WAVEFORM_NOISE: ClassVar[int]
    """Für den Parameter ``waveform`` verwendete Rauschen-Option."""
    SHAPE_LINEAR: ClassVar[int]
    """Für den Parameter ``shape`` verwendet Option der lnearen-Interpolation."""
    SHAPE_CURVE: ClassVar[int]
    """Für den Parameter ``shape`` verwendete Option der Kurven-Interpolation."""
    SHAPE_LOG: ClassVar[int]
    """Für den Parameter ``shape`` verwendete Option der Logarithmischen-Interpolation."""
    FX_NONE: ClassVar[int]
    """Keine Effekt-Option für den Parameter ``fx`` verwendet."""
    FX_TREMOLO: ClassVar[int]
    """Tremelo-Effekt-Option, die für den Parameter ``fx`` verwendet wird."""
    FX_VIBRATO: ClassVar[int]
    """Vibrato-Effekt-Option, die für den Parameter ``fx`` verwendet wird."""
    FX_WARBLE: ClassVar[int]
    """Warble Effekt Option, die für den Parameter ``fx`` verwendet wird."""
    freq_start: int
    """Startfrequenz in Hertz (Hz), eine Zahl zwischen ``0`` und ``9999``"""
    freq_end: int
    """Endfrequenz in Hertz (Hz), eine Zahl zwischen ``0`` und ``9999``"""
    duration: int
    """Tondauer in Millisekunden, eine Zahl zwischen ``0`` und ``9999``"""
    vol_start: int
    """Startlautstärke, eine Zahl zwischen ``0`` und ``255``"""
    vol_end: int
    """Endlautstärke, eine Zahl zwischen ``0`` und ``255``"""
    waveform: int
    """Typ der Wellenformform, einer dieser Werte: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (zufällig generiertes Geräusch)"""
    fx: int
    """Effekt, dem Ton hinzuzufügen, einer der folgenden Werte: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``oder ``FX_NONE``"""
    shape: int
    """Die Art der Interpolationskurve zwischen den Anfangs- und Endfrequenzen, verschiedene Wellenformen haben unterschiedliche Frequenzänderungen. Einer der folgenden Werte: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """Einen neuen Soundeffekt erstellen.

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: Startfrequenz in Hertz (Hz), eine Zahl zwischen ``0`` und ``9999``.
:param freq_end: Endfrequenz in Hertz (Hz), eine Zahl zwischen ``0`` und ``9999``.
:param duration: Tondauer in Millisekunden, eine Zahl zwischen ``0`` und ``9999``.
:param vol_start: Startlautstärke, eine Zahl zwischen ``0`` und ``255``.
:param vol_end: Endlautstärke, eine Zahl zwischen ``0`` und ``255``.
:param waveform: Typ der Wellenformform, einer dieser Werte: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (zufällig generiertes Geräusch).
:param fx: Effekt, dem Ton hinzuzufügen, einer der folgenden Werte: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``oder ``FX_NONE``.
:param shape: Die Art der Interpolationskurve zwischen den Anfangs- und Endfrequenzen, verschiedene Wellenformen haben unterschiedliche Frequenzänderungen. Einer der folgenden Werte: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def copy(self) -> SoundEffect:
        """Erstellen einer Kopie von diesem ``SoundEffect``.

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """Ein ``AudioFrame`` Objekt ist eine Liste von 32 Samples, von denen jedes ein unsigniertes Byte
ist (ganze Zahl zwischen 0 und 255).

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """Die Daten in diesem ``AudioFrame`` mit den Daten einer anderen ``AudioFrame`` Instanz überschreiben. (copyform)

Example: ``my_frame.copyfrom(source_frame)``

:param other: ``AudioFrame`` Instanz von der die Daten kopiert werden sollen."""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...