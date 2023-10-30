"""Auf Töne mit dem integrierten Mikrofon reagieren."""
from typing import Optional, Tuple
from ..calliope import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """Das letzte aufgezeichnete Tonereignis abrufen (current Event)

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """Prüft, ob seit dem letzten Anruf mindestens einmal ein Geräusch gehört wurde.

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: Das zu überprüfende Ereignis, wie z.B. ``SoundEvent.LOUD`` oder ``SoundEvent.QUIET``
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """Prüft das zuletzt erkannte Ton-Ereignis.

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: Das zu überprüfende Ereignis, wie z.B. ``SoundEvent.LOUD`` oder ``SoundEvent.QUIET``
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """Holt sich den Verlauf der Ton-Ereignisse als ein Tuple.

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """Legt den Schwellenwert für ein Ton-Ereignis fest.

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: Ein Ton-Ereignis, wie z.B. ``SoundEvent.LOUD`` oder ``SoundEvent.QUIET``.
:param value: Der Schwellenwert im Bereich 0-255."""
    ...

def sound_level() -> int:
    """Gibt den Schalldruck zurück.

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...