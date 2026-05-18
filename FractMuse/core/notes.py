"""Core note and MIDI event models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


def clamp_midi_value(value: float | int, *, low: int = 0, high: int = 127) -> int:
    """Clamp a numeric value into the valid MIDI byte range."""

    return max(low, min(high, int(round(value))))


@dataclass(frozen=True)
class MidiEvent:
    """A low-level MIDI note-on or note-off event."""

    time: float
    on_off: bool
    chan: int
    pitch: int
    vel: int

    def to_message(self) -> list[int]:
        command = 0x90 if self.on_off else 0x80
        channel = clamp_midi_value(self.chan, low=1, high=16)
        return [
            command + channel - 1,
            clamp_midi_value(self.pitch),
            clamp_midi_value(self.vel),
        ]


Raw = MidiEvent


@dataclass
class Note:
    """A mutable composition note.

    ``span`` is the duration used when converting span-based sketches into an
    absolute timeline. ``dur`` is the MIDI note duration once rendered.
    """

    time: Optional[float]
    dur: float
    pitch: Optional[int]
    vel: float
    chan: int = 1
    span: Optional[float] = None
    root: int = 21

    def to_raws(self) -> list[MidiEvent]:
        if self.pitch is None:
            return []

        start = self.time or 0.0
        pitch = self.root + self.pitch
        velocity = clamp_midi_value(self.vel)
        return [
            MidiEvent(start, True, self.chan, pitch, velocity),
            MidiEvent(start + self.dur, False, self.chan, pitch, velocity),
        ]


TimedNote = Note
