"""Messung der Beschleunigung des Calliope mini und die Erkennung von Gesten."""
from typing import Tuple

def get_x() -> int:
    """Ermittelt die Beschleunigungsmessung in der ``x``-Achse in milli-g.

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """Ermittelt die Beschleunigungsmessung in der ``y``-Achse in milli-g.

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """Ermittelt die Beschleunigungsmessung in der ``z``-Achse in milli-g.

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """Abrufen der Beschleunigungsmessungen in allen Achsen auf einmal als Tupel (einer geordnete Sammlung von Werten).

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """Ermittelt die Beschleunigungsmessung aller Achsen zusammen, als positive ganze Zahl. Dies ist die Pythagoras-Summe der X-, Y- und Z-Achsen.

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """Ermittelt den Namen der aktuellen Geste.

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """Prüft, ob die genannte Geste gerade aktiv ist.

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: Der Name der Geste.
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """Prüft, ob die genannte Geste seit dem letzten Aufruf aktiv war.

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: Der Name der Geste.
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """Gibt einen Tupel (eine geordnete Sammlung von Werten) der bisherigen Gesten zurück.

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`calliope.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """Legt den Empfindlichkeitsbereich des Beschleunigungssensors in g (Standardgravitation) auf die nächstliegenden Werte fest, die von der Hardware unterstützt werden, also entweder ``2``, ``4`` oder ``8`` g.

Example: ``accelerometer.set_range(8)``

:param value: Neuer Bereich für den Beschleunigungsmesser, eine ganze Zahl in ``g``."""