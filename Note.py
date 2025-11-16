"""Core note models used across the project."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Raw:
    """A low-level MIDI message container.

    Attributes
    ----------
    time:
        Absolute time (in seconds) when the MIDI event should occur.
    on_off:
        ``True`` for note-on messages, ``False`` for note-off messages.
    chan:
        MIDI channel number (1-indexed).
    pitch:
        MIDI pitch value.
    vel:
        MIDI velocity value.
    """

    time: float
    on_off: bool
    chan: int
    pitch: int
    vel: int

    def to_message(self) -> List[int]:
        """Return the raw bytes that should be sent to the MIDI device."""

        command = 0x90 if self.on_off else 0x80
        return [command + self.chan - 1, self.pitch, self.vel]


@dataclass
class Note:
    """A musical note expressed in spans (durations) rather than timestamps."""

    time: Optional[float]
    dur: float
    pitch: Optional[int]
    vel: int
    chan: int = 1
    span: Optional[float] = None
    root: int = 21

    def to_raws(self) -> List[Raw]:
        """Convert the note into raw MIDI note-on/off events."""

        if self.pitch is None:
            return []

        pitch = self.root + self.pitch
        return [
            Raw(self.time or 0.0, True, self.chan, pitch, self.vel),
            Raw((self.time or 0.0) + self.dur, False, self.chan, pitch, self.vel),
        ]