"""Kommunikation mit Geräten über das I2C-Busprotokoll."""
from _typeshed import ReadableBuffer
from ..calliope import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """Peripherie neu initialisieren.

Example: ``i2c.init()``

:param freq: Taktfrequenz
:param sda: ``sda`` Pin (Standard 20, A0_SDA)
:param scl: ``scl`` Pin (Standard 19, A0_SCL)

On a Calliope mini V1,V2 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V3**
revision of the Calliope mini as this has `separate I²C lines <https://tech.calliope.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """Scannt den Bus nach Geräten.

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """Liest Bytes von einem Gerät.

Example: ``i2c.read(0x50, 64)``

:param addr: Die 7-Bit-Adresse des Geräts
:param n: Die Anzahl der zu lesenden Bytes
:param repeat: Wenn ``True``, wird kein Stopp-Bit gesendet
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """Schreibt Bytes auf ein Gerät.

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: Die 7-Bit-Adresse des Geräts
:param buf: Ein Puffer der die zu schreibenden Bytes enthält
:param repeat: Wenn ``True``, wird kein Stopp-Bit gesendet"""
    ...