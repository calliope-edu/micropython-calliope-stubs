"""Low-Level-Dienstprogramme."""
from typing import Any
from .calliope import MicroBitDigitalPin

def unique_id() -> bytes:
    """Liefert eine Byte-Zeichenkette mit einem eindeutigen Bezeichner für ein Board.

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """Der Calliope mini wird auf ähnliche Weise zurückgesetzt, als ob man die externe RESET-Taste drücken würde.

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """Ermitteln der CPU-Frequenz in Hertz.

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """Interrupt-Anfragen deaktivieren.

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """Interrupt-Anfragen wieder aktivieren.

Example: ``machine.enable_irq(interrupt_state)``

:param state: Der Wert, der vom letzten Aufruf an die Funktion ``disable_irq`` zurückgegeben wurde."""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """Einen Impuls an einem Pin zeitlich festlegen.

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: Der zu verwendende Pin
:param pulse_level: 0 für einen niedrigen Impuls oder 1 für einen hohen Impuls zu timen
:param timeout_us: Ein Mikrosekunden-Timeout
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """Die Klasse der ``mem8``, ``mem16`` und ``mem32`` Speicheransichten."""

    def __getitem__(self, address: int) -> int:
        """Zugriff auf einen Wert vom Speicher.

:param address: Die Speicheradresse.
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """Setzt einen Wert an der angegebenen Adresse.

:param address: Die Adresse im Speicher.
:param value: Der einzustellende Ganzzahlwert."""
        ...
mem8: mem
"""8-bit (Byte) Ansicht des Speichers."""
mem16: mem
"""16-Bit-Ansicht des Speichers."""
mem32: mem
"""32-Bit-Ansicht des Speichers."""