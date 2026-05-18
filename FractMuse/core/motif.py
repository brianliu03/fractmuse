"""Motif model used by expansion algorithms."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Motif:
    pitches: list[int] = field(default_factory=list)
    spans: list[float] = field(default_factory=list)
    vels: list[float] = field(default_factory=list)

    def __post_init__(self) -> None:
        lengths = {len(self.pitches), len(self.spans), len(self.vels)}
        if len(lengths) > 1:
            raise ValueError("Motif pitches, spans, and velocities must have equal lengths")

    def add(self, pitch: int, span: float, vel: float) -> None:
        self.pitches.append(pitch)
        self.spans.append(span)
        self.vels.append(vel)

    def __len__(self) -> int:
        return len(self.pitches)
