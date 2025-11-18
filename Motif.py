"""Representation of expandable motifs."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Motif:
    pitches: List[int] = field(default_factory=list)
    spans: List[float] = field(default_factory=list)
    vels: List[float] = field(default_factory=list)

    def add(self, pitch: int, span: float, vel: int) -> None:
        self.pitches.append(pitch)
        self.spans.append(span)
        self.vels.append(vel)