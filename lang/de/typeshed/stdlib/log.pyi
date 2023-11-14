"""Daten auf den Calliope mini V3 loggen."""
from typing import Literal, Mapping, Optional, Union, overload
MILLISECONDS = 1
"""Format des Zeitstempels in Millisekunden. (millisconds)"""
SECONDS = 10
"""Format des Zeitstempels in Sekunden."""
MINUTES = 600
"""Format des Zeitstempels in Minuten."""
HOURS = 36000
"""Format des Zeitstempels in Stunden."""
DAYS = 864000
"""Format des Zeitstempels in Tagen."""

def set_labels(*labels: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """Den Header der Protokolldatei einrichten.

Example: ``log.set_labels('X', 'Y', 'Z', timestamp=log.MINUTES)``

Ideally this function should be called a single time, before any data is
logged, to configure the data table header once.

If a log file already exists when the program starts, or if this function
is called multiple times, it will check the labels already defined in the
log file. If this function call contains any new labels not already
present, it will generate a new header row with the additional columns.

By default the first column contains a timestamp for each row. The time
unit can be selected via the timestamp argument.

:param *labels: Eine beliebige Anzahl von Positionsargumenten, die jeweils einem Eintrag im Log-Header entsprechen.
:param timestamp: Die Maßeinheit für den Zeitstempel, der automatisch als erste Spalte in jeder Zeile eingefügt wird. Zeitstempelwerte können einer der folgenden sein: ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS`` oder ``None``, um den Zeitstempel zu deaktivieren. Der Standardwert ist ``log.SECONDS``."""
    ...

@overload
def add(data_dictionary: Optional[Mapping[str, Union[str, int, float]]]) -> None:
    """Fügt dem Protokoll eine Datenzeile hinzu, indem ein Wörterbuch mit Kopfzeilen und Werten übergeben wird.

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: Die zu protokollierenden Daten in Form eines Wörterbuchs mit einem Key für jede Kopfzeile."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """Hinzufügen einer Datenzeile zum Protokoll unter Verwendung von Schlüsselwortargumenten.

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """Löscht den Inhalt des Protokolls, einschließlich der Headers.

Example: ``log.delete()``

To add the log headers again the ``set_labels`` function should to be called after this function.

There are two erase modes; “full” completely removes the data from the physical storage,
and “fast” invalidates the data without removing it.

:param full: ``True`` wählt eine "vollständige" Löschung und ``False`` wählt die "schnelle" Löschmethode."""
    ...

def set_mirroring(serial: bool):
    """Konfiguriert die Spiegelung der Datenaufzeichnungsaktivität auf die serielle Ausgabe.

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: ``True`` ermöglicht das Spiegeln von Daten an die serielle Ausgabe."""
    ...