"""Kommunikation mit einem Gerät über eine serielle Schnittstelle."""
from _typeshed import WriteableBuffer
from ..calliope import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""Ungerade Parität"""
EVEN: int
"""Gleiche Parität"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """Serielle Kommunikation initialisieren.

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: Die Geschwindigkeit der Kommunikation.
:param bits: Die Größe der Bytes, die übertragen wird. Calliope mini unterstützt nur 8.
:param parity: Wie Parität überprüft wird, ``None``, ``uart.ODD`` oder ``uart.EVEN``.
:param stop: Die Anzahl der Stopp-Bits, muss für den Calliope mini 1 sein.
:param tx: Sendender Pin.
:param rx: Empfangender Pin.

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """Prüfen, ob Daten warten.

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """Bytes lesen.

Example: ``uart.read()``

:param nbytes: Wenn ``nbytes`` angegeben ist, werden maximal so viele Bytes gelesen, andernfalls werden so viele Bytes wie möglich gelesen
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """Bytes in den ``buf`` lesen.

Example: ``uart.readinto(input_buffer)``

:param buf: Der Puffer, in den geschrieben wird.
:param nbytes: Wenn ``nbytes`` angegeben ist, werden höchstens so viele Bytes gelesen, andernfalls ``len(buf)`` Bytes.
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """Liest eine Zeile, die mit einem Zeilenumbruch endet.

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """Schreibt einen Puffer auf den Bus.

Example: ``uart.write('hello world')``

:param buf: Ein Byte-Objekt oder eine Zeichenkette (String).
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...