"""Pure transformations for span-based composition notes."""

from __future__ import annotations

import math
import random
from collections import deque
from copy import copy
from dataclasses import dataclass
from typing import Iterable, Sequence

from fractmuse.core.motif import Motif


@dataclass(frozen=True)
class ExpansionOptions:
    expand_pitch: bool = True
    expand_span: bool = True
    expand_velocity: bool = True
    low: int = 0
    high: int = 87
    offset: int = 0


def _span(note) -> float:
    if note.span is None:
        return note.dur
    return note.span


def snotes_to_notes(snotes: Sequence) -> list:
    current_time = 0.0
    output = []
    for note in snotes:
        rendered = copy(note)
        rendered.time = current_time
        current_time += _span(note)
        output.append(rendered)
    return output


def snotes_to_notes_with_offset(snotes: Sequence, offset: float) -> list:
    current_time = offset
    output = []
    for note in snotes:
        rendered = copy(note)
        rendered.time = current_time
        current_time += _span(note)
        output.append(rendered)
    return output


def snotes_to_notes_tritones(snotes: Sequence) -> list:
    time_top = 0.0
    time_bottom = 0.0
    output_top = []
    output_bottom = []
    for index, note in enumerate(snotes):
        rendered = copy(note)
        if index % 2 == 0:
            rendered.time = time_top
            rendered.pitch += 6
            rendered.chan = 1
            time_top += _span(note)
            output_top.append(rendered)
        else:
            rendered.time = time_bottom
            rendered.pitch -= 6
            rendered.chan = 2
            time_bottom += _span(note)
            output_bottom.append(rendered)
    return output_top + output_bottom


def interpolate(snote_groups: Sequence[Sequence], order: Sequence[int]) -> list:
    queues = [deque(group) for group in snote_groups]
    output = []
    for group_index in order:
        try:
            output.append(copy(queues[group_index].popleft()))
        except IndexError as exc:
            raise IndexError(f"Interpolation group {group_index} is exhausted") from exc
    return output


def add_distribution(
    snotes: Sequence,
    modulus: Sequence[int],
    shift: Sequence[int],
    ascending: bool,
    inverted: bool,
    rng: random.Random | None = None,
) -> list:
    rand = rng or random
    output = []
    pitch_index = 0 if ascending else 87
    for note in snotes:
        for modulo, base in zip(modulus, shift, strict=False):
            if pitch_index % modulo == base:
                output.append(copy(note))
                break
        else:
            probability = (
                math.factorial(88)
                / (math.factorial(88 - pitch_index) * math.factorial(pitch_index))
            ) * (0.5**88) * 10
            draw = rand.random()
            if (not inverted and draw <= probability) or (inverted and draw >= probability):
                output.append(copy(note))

        pitch_index += 1 if ascending else -1
    return output


def expand_notes(snotes: Sequence, motif: Motif, options: ExpansionOptions) -> list:
    output = []
    low = options.low + options.offset
    high = options.high + options.offset
    for note in snotes:
        for pitch, span, velocity in zip(motif.pitches, motif.spans, motif.vels, strict=True):
            expanded = copy(note)
            expanded.pitch = expanded.pitch + pitch if options.expand_pitch else pitch
            expanded.span = _span(expanded) * span if options.expand_span else span
            expanded.vel = expanded.vel + velocity if options.expand_velocity else velocity
            if low <= expanded.pitch <= high:
                output.append(expanded)
    return output


def expand(snotes, motif, expPitch, expSpan, expVel, offset):
    return expand_notes(
        snotes,
        motif,
        ExpansionOptions(expPitch, expSpan, expVel, low=0, high=87, offset=offset),
    )


def _motif_from_notes(notes: Iterable) -> Motif:
    motif = Motif()
    for note in notes:
        motif.add(note.pitch, _span(note), note.vel)
    return motif


def expand_snotes(snotes: Sequence, motif_notes: Sequence, low: int, high: int) -> list:
    return expand_notes(
        snotes,
        _motif_from_notes(motif_notes),
        ExpansionOptions(True, True, False, low=low, high=high),
    )


def expand_snotes_no_span(snotes: Sequence, motif_notes: Sequence, low: int, high: int) -> list:
    return expand_notes(
        snotes,
        _motif_from_notes(motif_notes),
        ExpansionOptions(True, False, False, low=low, high=high),
    )


def expand_centered(snotes, motif, expPitch, expSpan, expVel, offset):
    if len(motif) == 0:
        return []
    average = sum(motif.pitches) // len(motif.pitches)
    centered = Motif([pitch - average for pitch in motif.pitches], motif.spans, motif.vels)
    return expand(snotes, centered, expPitch, expSpan, expVel, offset)


def expand_rand(snotes, motif, expPitch, expSpan, expVel, rand):
    output = []
    for note in snotes:
        if rand.random() < 0.7:
            output.extend(expand([note], motif, expPitch, expSpan, expVel, 0))
        else:
            output.append(note)
    return output


def rand_pois_distribution(
    snotes: Sequence,
    motif: Motif,
    rng: random.Random | None = None,
) -> list:
    rand = rng or random
    output = []
    for note in snotes:
        for pitch, span, velocity in zip(motif.pitches, motif.spans, motif.vels, strict=True):
            k = rand.randrange(0, 100)
            draw = rand.random()
            poisson = 5 * ((30**k) / math.factorial(k)) * (math.e**-30)
            if poisson >= draw:
                expanded = copy(note)
                expanded.pitch += pitch
                expanded.vel = velocity
                expanded.span = _span(expanded) * span
                output.append(expanded)
    return output


def set_mid_c(pitches: Sequence[int]) -> list[int]:
    return [pitch - 60 for pitch in pitches]


def revert_mid_c(pitches: Sequence[int]) -> list[int]:
    return [pitch + 60 for pitch in pitches]


# Historical camelCase aliases.
snotesToNotes = snotes_to_notes
snotesToNotesWithOffset = snotes_to_notes_with_offset
snotesToNotesTritones = snotes_to_notes_tritones
addDistribution = add_distribution
expandSnotes = expand_snotes
expandSnotesNoSpan = expand_snotes_no_span
expand2 = expand_centered
randPoisDistribution = rand_pois_distribution
setMidC = set_mid_c
revertMidC = revert_mid_c
