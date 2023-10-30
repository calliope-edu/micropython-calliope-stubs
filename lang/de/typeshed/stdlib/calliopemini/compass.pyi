"""Den eingebauten Kompass nutzen."""

def calibrate() -> None:
    """Startet den Kalibrierungsprozess.

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """Überprüft, ob der Kompass kalibriert ist.

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """Die Kalibrierung rückgängig machen, sodass der Kompass nicht mehr kalibriert ist.

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """Gibt die Stärke des magnetischen Feldes auf der ``x`` Achse zurück.

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """Gibt die Stärke des magnetischen Feldes auf der ``y`` Achse zurück.

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """Gibt die Stärke des magnetischen Feldes auf der ``z`` Achse zurück.

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """Gibt die Kompassrichtung zurück.

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """Gibt die Größe des Magnetfelds um den Calliope mini zurück.

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...