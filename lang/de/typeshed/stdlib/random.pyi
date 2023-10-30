"""Zufallszahlen generieren."""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Erzeugt eine ganze Zahl mit ``n`` zufälligen Bits.

Example: ``random.getrandbits(1)``

:param n: Ein Wert zwischen 1-30 (inklusiv)."""
    ...

def seed(n: int) -> None:
    """Initialisiert den Zufallszahlengenerator.

Example: ``random.seed(0)``

:param n: Der Ganzzahlbereich

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Wählt eine zufällige ganze Zahl zwischen ``a`` und einschließlich ``b``.

Example: ``random.randint(0, 9)``

:param a: Startwert für den Bereich (inklusiv)
:param b: Endwert für den Bereich (inklusiv)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Eine zufällig ausgewählte ganze Zahl zwischen Null und bis zu (aber nicht einschließlich) ``stop``.

Example: ``random.randrange(10)``

:param stop: Endwert für den Bereich (exklusiv)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Ein zufällig ausgewähltes Element aus ``range(start, stop, step)`` wählen.

Example: ``random.randrange(0, 10)``

:param start: Der Anfang des Bereichs (inklusiv)
:param stop: Endwert für den Bereich (exklusiv)
:param step: Der Schritt."""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """Ein zufälliges Element aus der nicht leeren Folge ``seq`` auswählen.

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: Eine Sequenz.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Erzeugt eine zufällige Fließkommazahl im Bereich [0,0, 1,0].

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Gibt eine zufällige Fließkommazahl zwischen ``a`` und ``b`` einschließlich zurück.

Example: ``random.uniform(0, 9)``

:param a: Startwert für den Bereich (inklusiv)
:param b: Endwert für den Bereich (inklusiv)"""
    ...