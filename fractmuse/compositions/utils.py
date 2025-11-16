"""Helper utilities for assembling compositions."""

from __future__ import annotations

from dataclasses import dataclass
from copy import copy
from typing import Iterable, List, Sequence

from algorithms.algo import (
    snotesToNotes,
    snotesToNotesTritones,
)
from Note import Note


@dataclass
class Section:
    """A block of notes to be played sequentially."""

    notes: Sequence[Note]
    pause: float = 0.0


def concatenate_sections(sections: Iterable[Section]) -> List[Note]:
    """Combine sections into a single timeline of notes."""

    timeline: List[Note] = []
    offset = 0.0
    for section in sections:
        offset += section.pause
        if not section.notes:
            continue
        section_end = max((note.time or 0.0) + note.dur for note in section.notes)
        for note in section.notes:
            new_note = copy(note)
            new_note.time = (note.time or 0.0) + offset
            timeline.append(new_note)
        offset += section_end
    return timeline


def to_notes(snotes: Sequence[Note], *, tritones: bool = False) -> List[Note]:
    """Convert span-based notes to absolute-time notes."""

    converter = snotesToNotesTritones if tritones else snotesToNotes
    return converter(list(snotes))
