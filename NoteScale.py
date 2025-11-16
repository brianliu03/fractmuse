"""Scale-aware note representations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple

from Note import Raw

Scale = Tuple[str, Optional[int]]


@dataclass
class NoteScale:
    """A note that maps degrees of a scale to absolute MIDI pitches."""

    time: Optional[float]
    dur: float
    pitch: Optional[int]
    vel: int
    chan: int = 1
    span: Optional[float] = None
    scale: Scale = ("chromatic", 60)

    def to_raws(self) -> List[Raw]:
        if self.pitch is None:
            return []

        scale_type, param = self.scale
        if scale_type == "chromatic":
            temp = self.pitch + (param or 0)
        elif scale_type == "major":
            temp = self.major_scale(self.pitch, param or 0)
        elif scale_type == "melodic":
            temp = self.melodic_minor_scale(self.pitch, param or 0)
        else:
            raise ValueError(f"Unknown scale type: {scale_type}")

        start_time = self.time or 0.0
        return [
            Raw(start_time, True, self.chan, temp, self.vel),
            Raw(start_time + self.dur, False, self.chan, temp, self.vel),
        ]

    @staticmethod
    def major_scale(degree: int, root_note: int) -> int:
        major_to_midi = [0, 2, 4, 5, 7, 9, 11]
        return major_to_midi[degree % 7] + root_note + (degree // 7) * 12

    @staticmethod
    def melodic_minor_scale(degree: int, root_note: int) -> int:
        melodic_to_midi = [0, 2, 3, 5, 7, 9, 11]
        return melodic_to_midi[degree % 7] + root_note + (degree // 7) * 12