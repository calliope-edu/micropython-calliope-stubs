"""Packen und Entpacken primitiver Datentypen."""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """Ermittelt die Anzahl der Bytes, die zum Speichern des angegebenen ``fmt`` benötigt werden.

Example: ``struct.calcsize('hf')``

:param fmt: Eine Formatzeichenfolge.
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """Werte gemäß einer Formatzeichenfolge packen.

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: Die Formatzeichenfolge.
:param v1: Der erste Wert.
:param *vn: Die verbleibenden Werte.
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """Werte gemäß einer Formatzeichenfolge packen.

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: Die Formatzeichenfolge.
:param buffer: Der Puffer, in den geschrieben wird.
:param offset: Der Offset in dem Puffer. Kann negativ sein, um vom Ende des Puffers aus zu zählen.
:param v1: Der erste Wert.
:param *vn: Die verbleibenden Werte."""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """Werte gemäß einer Formatzeichenfolge entpacken.

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: Die Formatzeichenfolge.
:param data: Die Daten.
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """Werte gemäß einer Formatzeichenfolge aus einem Puffer entpacken.

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: Die Formatzeichenfolge.
:param buffer: Der Quellpuffer, aus dem gelesen werden soll.
:param offset: Der Offset in dem Puffer. Kann negativ sein, um vom Ende des Puffers aus zu zählen.
:return: A tuple of the unpacked values."""
    ...