"""Kommunikation zwischen mehreren Calliope mini über das integrierte Radio."""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""Konstante zeigt einen Durchsatz von 1 MBit pro Sekunde an."""
RATE_2MBIT: int
"""Konstante zeigt einen Durchsatz von 2 MBit pro Sekunde an."""

def on() -> None:
    """Startet die Funkverbindung.

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """Schaltet die Funkverbindung aus, dies spart Energie und Speicher.

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """Konfiguriert die Funkverbindung.

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (default=32) legt die maximale Länge einer Nachricht in Bytes fest.
Sie kann bis zu 251 Bytes lang sein (254 - 3 Bytes für S0, LENGTH und S1 Präamble).
:param queue: (default=3) gibt die Anzahl der Nachrichten an, die in der Warteschlange gespeichert werden können.
Wenn keine Leerzeichen in der Warteschlange für eingehende Nachrichten übrig sind, wird die eingehende Nachricht gelöscht.
:param channel: (default=7) ein ganzzahliger Wert von 0 bis 83 (inklusiv), der einen beliebigen "Kanal" definiert, auf den Funk eingestellt ist.
Nachrichten werden über diesen Kanal gesendet und nur Nachrichten, die über diesen Kanal empfangen werden, werden in die Warteschlange der eingehenden Nachrichten aufgenommen. Jeder Schritt ist 1MHz breit, bei 2400MHz.
:param power: (default=6) ist ein ganzzahliger Wert von 0 bis 7 (inklusive), der die Stärke des Signals angibt, das bei der Übertragung einer Nachricht verwendet wird.
Je höher der Wert, desto stärker das Signal, aber desto mehr Leistung wird vom Gerät verbraucht. Die Nummerierung übersetzt sich in Positionen in der folgenden Liste der dBm (dezibel milliwatt) Werte: -30, -20, -16, -12, -8, -4, 0, 4.
:param address: (default=0x75626974) ein beliebiger Name, ausgedrückt als 32-Bit-Adresse, der verwendet wird, um eingehende Pakete auf der Hardware-Ebene zu filtern und nur diejenigen zu behalten, die mit der festgelegten Adresse übereinstimmen. Die von anderen Calliope-mini-Plattformen verwendete Standardeinstellung ist die hier verwendete Standardeinstellung.
:param group: (default=0) ein 8-Bit-Wert (0-255), der mit dem ``address`` beim Filtern von Nachrichten verwendet wird.
Konzeptionell ist "Adresse" wie eine Haus- oder Büroadresse und "Gruppe" ist wie die Person an der Adresse, an die eine Nachricht gesendet werden soll.
:param data_rate: (default=``radio.RATE_1MBIT``) zeigt die Geschwindigkeit an, mit der der Datendurchsatz stattfindet.
Kann eine der folgenden Konstanten im ``radio`` Modul sein: ``RATE_250KBIT``, ``RATE_1MBIT`` oder ``RATE_2MBIT``.

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """Setzt die Einstellungen auf ihre Standardwerte zurück.

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """Sendet eine Nachricht die Bytes enthält.

Example: ``radio.send_bytes(b'hello')``

:param message: Die zu sendenden Bytes."""
    ...

def receive_bytes() -> Optional[bytes]:
    """Empfangen der nächsten eingehenden Nachricht in der Nachrichtenwarteschlange.

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """Kopiert die nächste eingehende Nachricht in der Nachrichtenwarteschlange in einen Puffer.

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: Der Zielpuffer. Die Nachricht wird abgeschnitten, wenn sie größer als der Puffer ist.
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """Sendet eine Zeichenkette als Nachricht.

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the Calliope mini).

:param message: Die zu sendende Zeichenkette."""
    ...

def receive() -> Optional[str]:
    """Funktioniert genauso wie ``receive_bytes``, gibt aber zurück, was gesendet wurde.

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the Calliope mini).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """Gibt einen Tupel zurück, der drei Werte enthält, welche die nächste eingehende Nachricht in der Nachrichtenwarteschlange darstellen.

Example: ``radio.receive_full()``

If there are no pending messages then ``None`` is returned.

The three values in the tuple represent:

- the next incoming message on the message queue as bytes.
- the RSSI (signal strength): a value between 0 (strongest) and -255 (weakest) as measured in dBm.
- a microsecond timestamp: the value returned by ``time.ticks_us()`` when the message was received.

For example::

    details = radio.receive_full()
    if details:
        msg, rssi, timestamp = details

This function is useful for providing information needed for triangulation
and/or trilateration with other Calliope mini devices.

:return: ``None`` if there is no message, otherwise a tuple of length three with the bytes, strength and timestamp values."""
    ...