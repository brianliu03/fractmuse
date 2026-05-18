"""Scale-aware note representations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

from .notes import MidiEvent, clamp_midi_value

ScaleName = Literal["chromatic", "major", "melodic"]
Scale = tuple[ScaleName, Optional[int]]

_SCALE_INTERVALS: dict[ScaleName, list[int]] = {
    "chromatic": list(range(12)),
    "major": [0, 2, 4, 5, 7, 9, 11],
    "melodic": [0, 2, 3, 5, 7, 9, 11],
}


def pitch_for_degree(degree: int, scale: Scale) -> int:
    scale_name, root_note = scale
    root = root_note or 0
    if scale_name == "chromatic":
        return degree + root

    intervals = _SCALE_INTERVALS[scale_name]
    return intervals[degree % len(intervals)] + root + (degree // len(intervals)) * 12


@dataclass
class NoteScale:
    """A note whose pitch is interpreted as a scale degree."""

    time: Optional[float]
    dur: float
    pitch: Optional[int]
    vel: float
    chan: int = 1
    span: Optional[float] = None
    scale: Scale = ("chromatic", 60)

    def to_raws(self) -> list[MidiEvent]:
        if self.pitch is None:
            return []

        start = self.time or 0.0
        pitch = pitch_for_degree(self.pitch, self.scale)
        velocity = clamp_midi_value(self.vel)
        return [
            MidiEvent(start, True, self.chan, pitch, velocity),
            MidiEvent(start + self.dur, False, self.chan, pitch, velocity),
        ]

    @staticmethod
    def major_scale(degree: int, root_note: int) -> int:
        return pitch_for_degree(degree, ("major", root_note))

    @staticmethod
    def melodic_minor_scale(degree: int, root_note: int) -> int:
        return pitch_for_degree(degree, ("melodic", root_note))
