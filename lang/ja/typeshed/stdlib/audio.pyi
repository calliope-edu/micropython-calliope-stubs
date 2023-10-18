"""Play sounds using the Calliope mini (import ``audio`` for V1,V2 compatibility).
"""

# Re-export for V1,V2 compatibility.
from .calliope.audio import (
    is_playing as is_playing,
    play as play,
    stop as stop,
    AudioFrame as AudioFrame,
    SoundEffect as SoundEffect,
)
