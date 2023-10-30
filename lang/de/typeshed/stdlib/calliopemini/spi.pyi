"""Mit Geräten über den serielle Peripheriebus (SPI) kommunizieren."""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..calliope import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """SPI-Kommunikation initialisieren.

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: Die Geschwindigkeit der Kommunikation.
:param bits: Die Breite in Bits jeder Übertragung. Derzeit werden nur ``bits=8`` unterstützt. Dies kann sich jedoch in Zukunft ändern.
:param mode: Bestimmt die Kombination von Taktpolarität und Phase - `siehe Online-Tabelle <https://calliope.cc/programmieren/editoren/python/python-api#spiinit>`_.
:param sclk: sclk Pin (Standard 13)
:param mosi: miso Pin (Standard 15)
:param miso: miso Pin (Standard 14)"""
    ...

def read(nbytes: int) -> bytes:
    """Bytes lesen.

Example: ``spi.read(64)``

:param nbytes: Maximale Anzahl der zu lesenden Bytes.
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """Bytes in den Bus schreiben.

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: Ein Puffer, von dem Daten gelesen werden."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """Schreibt den ``out``-Puffer auf den Bus und liest jede Antwort in den ``in_``-Puffer.

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: Der Puffer, auf den jede Antwort geschrieben werden soll.
:param in_: Der Puffer aus dem Daten gelesen werden sollen."""
    ...