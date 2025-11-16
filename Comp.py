"""High level composition building blocks."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Sequence, Tuple

from algorithms.algo import expand, revertMidC, setMidC
from Motif import Motif
from Note import Note
from NoteScale import NoteScale

SpanSequence = Sequence[float]
PitchSequence = Sequence[int]


def _apply_sieve(
    motif: Motif,
    modulus: PitchSequence,
    shift: PitchSequence,
    spans: SpanSequence,
    start: int,
    end: int,
) -> None:
    """Populate ``motif`` with pitches filtered by the provided sieve."""

    step = -1 if start > end else 1
    index = start
    compare = (lambda value: value >= end) if step == -1 else (lambda value: value < end)

    while compare(index):
        for offset, modulo in enumerate(modulus):
            if index % modulo == shift[offset]:
                motif.add(index, spans[offset], 60)
                break
        index += step


@dataclass
class Notes_1:
    """Generate notes based on a sieve and expansion rules."""

    num_expansions: int
    sieve: Tuple[PitchSequence, PitchSequence]
    spans: SpanSequence
    direction: Sequence[int]
    random_seed: int = 101

    def __post_init__(self) -> None:
        modulus, shift = self.sieve
        self.motif = Motif()
        start, end = self.direction
        _apply_sieve(self.motif, modulus, shift, self.spans, start, end)
        self.motif.pitches = setMidC(self.motif.pitches)
        self.rand = random.Random(self.random_seed)

    def markovify(self, order: int, start: int) -> None:
        from algorithms.Markov_Algo import MarkovGenerator

        pitches = self.motif.pitches
        generator = MarkovGenerator(len(pitches), 88, order, 0)
        generator.generateTable(pitches)
        self.motif.pitches = generator.createComp(start)

    def run(self) -> List[Note]:
        notes: List[Note] = [Note(None, 0.25, 0, 0, span=1.0, root=81)]
        for _ in range(self.num_expansions):
            notes = expand(notes, self.motif, expPitch=True, expSpan=True, expVel=False, offset=-60)
        self.motif.pitches = revertMidC(self.motif.pitches)
        return notes


class _BaseComp:
    """Base class shared by the high-level composition helpers."""

    default_expansions: int = 1
    root: int = 60

    def __init__(self, num_expansions: int, scale: str, seed: int) -> None:
        self.num_expansions = num_expansions
        self.scale = scale
        self.seed = seed
        self.rand = random.Random(seed)
        self.motif = self._build_motif()

    def _build_motif(self) -> Motif:
        raise NotImplementedError

    def _initial_notes(self) -> List[NoteScale]:
        raise NotImplementedError

    def _expand(self, notes: List[NoteScale]) -> List[NoteScale]:
        expansions = self.num_expansions if self.num_expansions > 0 else self.default_expansions
        current = notes
        for _ in range(expansions):
            current = expand(current, self.motif, expPitch=True, expSpan=True, expVel=True, offset=-60)
        return current

    def run(self) -> List[NoteScale]:
        notes = self._initial_notes()
        return self._expand(notes)


class Comp_1(_BaseComp):
    default_expansions = 3
    root = 59

    def _build_motif(self) -> Motif:
        return Motif([-1, 5, 8, -4, 2], [1.0, 0.01, 0.5, 1.0, 0.01], [1, 0.5, 0.5, 0.5, 0.5])

    def _initial_notes(self) -> List[NoteScale]:
        return [NoteScale(None, 2.0, 0, 60, chan=2, span=1.0, scale=(self.scale, self.root))]


class Comp_4(_BaseComp):
    default_expansions = 3
    root = 59

    def _build_motif(self) -> Motif:
        return Motif([1, 4, 3, -2, 7], [0.7, 0.5, 0.7, 0.6, 0.3], [3, -10, 3, 10, -10])

    def _initial_notes(self) -> List[NoteScale]:
        return [NoteScale(None, 2.0, 0, 60, chan=2, span=1.0, scale=(self.scale, self.root))]


class Comp_7(_BaseComp):
    default_expansions = 3
    root = 64

    def _build_motif(self) -> Motif:
        return Motif([-2, 5, -4, -2, 8, 10], [0.5, 1.3, 0.75, 0.03, 0.5, 0.5], [1, 0.5, 0.5, 0.5, 0.5, 0.5])

    def _initial_notes(self) -> List[NoteScale]:
        return [NoteScale(None, 0.5, 0, 40, span=1.0, scale=(self.scale, self.root))]


class Comp_8(_BaseComp):
    default_expansions = 2
    root = 64

    def _build_motif(self) -> Motif:
        return Motif(
            [-2, 5, -10, 6, -6, 9, -9, -1, -7],
            [0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.6],
            [0.5, 20, 0.5, 20, 0.1, 0.01, 0.5, 0.5, 0.5],
        )

    def _initial_notes(self) -> List[NoteScale]:
        return [NoteScale(None, 0.1, 0, 40, span=1.0, scale=(self.scale, self.root))]
