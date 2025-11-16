"""Composition registry and metadata."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, List, Mapping

from Note import Note

from . import legacy


@dataclass(frozen=True)
class CompositionContext:
    project_root: Path
    midi_file: Path | None = None


@dataclass(frozen=True)
class Composition:
    name: str
    description: str
    build: Callable[[CompositionContext], List[Note]]
    requires_midi: bool = False


def _wrap(builder: Callable[[], List[Note]]) -> Callable[[CompositionContext], List[Note]]:
    def inner(context: CompositionContext) -> List[Note]:
        return builder()

    return inner


def _markov_builder(default_filename: str, start_pitch: int) -> Callable[[CompositionContext], List[Note]]:
    def inner(context: CompositionContext) -> List[Note]:
        midi_path = context.midi_file or context.project_root / "midi_files" / default_filename
        if not midi_path.exists():
            raise FileNotFoundError(f"MIDI file not found: {midi_path}")
        return legacy._markov_from_midi(midi_path, start_pitch)

    return inner


COMPOSITIONS: Mapping[str, Composition] = {
    "legacy/main": Composition(
        name="legacy/main",
        description="Original dual-sieve interpolation study.",
        build=_wrap(legacy.legacy_main),
    ),
    "legacy/main2": Composition(
        name="legacy/main2",
        description="Alternating diatonic expansions.",
        build=_wrap(legacy.legacy_main2),
    ),
    "legacy/main3": Composition(
        name="legacy/main3",
        description="Ascending sieve across a single modulus set.",
        build=_wrap(legacy.legacy_main3),
    ),
    "legacy/main4": Composition(
        name="legacy/main4",
        description="Layered sieve duet with evolving orderings.",
        build=_wrap(legacy.legacy_main4),
    ),
    "legacy/main5": Composition(
        name="legacy/main5",
        description="Self-expanding motif with stochastic layering.",
        build=_wrap(legacy.legacy_main5),
    ),
    "legacy/main6": Composition(
        name="legacy/main6",
        description="Dense expansion using modular sieves.",
        build=_wrap(legacy.legacy_main6),
    ),
    "legacy/main7": Composition(
        name="legacy/main7",
        description="Contrasting sieve passages with tritone reframing.",
        build=_wrap(legacy.legacy_main7),
    ),
    "legacy/main8": Composition(
        name="legacy/main8",
        description="Extended suite exploring offsets and interpolations.",
        build=_wrap(legacy.legacy_main8),
    ),
    "legacy/main9": Composition(
        name="legacy/main9",
        description="Motivic expansion using Comp_4 over melodic material.",
        build=_wrap(legacy.legacy_main9),
    ),
    "legacy/main10": Composition(
        name="legacy/main10",
        description="Comp_8 major-mode fractal expansion.",
        build=_wrap(legacy.legacy_main10),
    ),
    "legacy/main11": Composition(
        name="legacy/main11",
        description="Comp_7 melodic-minor exploration.",
        build=_wrap(legacy.legacy_main11),
    ),
    "legacy/main12": Composition(
        name="legacy/main12",
        description="Comp_1 motivic reduction.",
        build=_wrap(legacy.legacy_main12),
    ),
    "markov/mozart": Composition(
        name="markov/mozart",
        description="Markov chain recomposition of Mozart Sonata K311.",
        build=_markov_builder("mozart_sonata_9_1stmvt_k311_PNO.mid", start_pitch=62),
        requires_midi=True,
    ),
}


def list_compositions() -> List[Composition]:
    return list(COMPOSITIONS.values())


def get_composition(name: str) -> Composition:
    if name not in COMPOSITIONS:
        raise KeyError(f"Unknown composition: {name}")
    return COMPOSITIONS[name]
