"""Port of the historical entry scripts into structured builders."""

from __future__ import annotations

from pathlib import Path
from typing import List

from Motif import Motif
from Note import Note
from algorithms.algo import (
    expand,
    expandSnotes,
    expandSnotesNoSpan,
    interpolate,
    snotesToNotes,
    snotesToNotesWithOffset,
)

from .utils import Section, concatenate_sections, to_notes


def _generate_snotes(expansions, modulus, shift, spans, direction):
    from Comp import Notes_1

    return Notes_1(expansions, sieve=(modulus, shift), spans=spans, direction=direction).run()


def _markov_from_midi(midi_path: Path, start_pitch: int) -> List[Note]:
    from algorithms.Markov_Algo import MarkovGenerator
    from mido import MidiFile

    mid = MidiFile(str(midi_path), clip=True)
    motif = Motif([], [], [])

    notes = []
    times: List[float] = []
    current = 0.0
    for message in mid:
        current += message.time
        if message.type == "note_on" and getattr(message, "velocity", 0) > 0:
            notes.append(message)
            times.append(current)

    if not notes:
        return []

    offset = times[0]
    times = [time - offset for time in times]
    total_span = times[-1] - times[0]

    for index, message in enumerate(notes):
        if index == len(notes) - 1:
            span = 0
        else:
            span = total_span - times[index] - (total_span - times[index + 1])
        motif.add(message.note, span, message.velocity)

    max_span = max(motif.spans) if motif.spans else 0
    span_generator = MarkovGenerator(len(motif.spans), int(max_span * 100) + 1, 1, 0)
    span_generator.generateTableSpans(motif.spans)
    pitch_generator = MarkovGenerator(len(motif.pitches), 88, 1, 21)
    pitch_generator.generateTable(motif.pitches)
    velocity_generator = MarkovGenerator(len(motif.vels), 128, 1, 0)
    velocity_generator.generateTable(motif.vels)

    comp = Motif(
        pitch_generator.createComp(start_pitch),
        span_generator.createComp(int(round(motif.spans[0], 2)) * 100),
        velocity_generator.createComp(motif.vels[0]),
    )
    for index in range(len(comp.spans)):
        comp.spans[index] = comp.spans[index] / 100

    base = [Note(None, 1.0, 0, 0, span=1, root=0)]
    expanded = expand(base, comp, expPitch=True, expSpan=True, expVel=False, offset=21)
    return snotesToNotes(expanded)


def legacy_main() -> List[Note]:
    modulus_0 = [4, 19]
    shift_0 = [0, 0]
    spans_0 = [0.75, 0.25]
    direction_0 = [40, 70]
    modulus_1 = [14, 9]
    shift_1 = [0, 0]
    spans_1 = [0.2, 0.5]
    direction_1 = [40, 70]
    order = [
        0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1,
        1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1,
        0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1,
        1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1,
    ]
    snotes = interpolate(
        [
            _generate_snotes(3, modulus_0, shift_0, spans_0, direction_0),
            _generate_snotes(3, modulus_1, shift_1, spans_1, direction_1),
        ],
        order,
    )
    return to_notes(snotes)


def legacy_main2() -> List[Note]:
    modulus_0 = [12] * 7
    shift_0 = [0, 2, 4, 5, 7, 9, 11]
    spans_0 = [0.5] * 7
    direction_0 = [40, 60]
    modulus_1 = [12] * 7
    shift_1 = [0, 2, 4, 5, 7, 9, 11]
    spans_1 = [0.25, 0.75, 0.25, 0.75, 0.25, 0.75, 0.25]
    direction_1 = [40, 60]
    order = [0, 1] * 10
    snotes = interpolate(
        [
            _generate_snotes(2, modulus_0, shift_0, spans_0, direction_0),
            _generate_snotes(2, modulus_1, shift_1, spans_1, direction_1),
        ],
        order,
    )
    return to_notes(snotes)


def legacy_main3() -> List[Note]:
    modulus = [12, 12, 12, 12, 12, 12, 12]
    shift = [0, 1, 4, 5, 7, 10, 11]
    spans = [0.5] * 7
    direction = [30, 60]
    snotes = _generate_snotes(1, modulus, shift, spans, direction)
    return to_notes(snotes)


def legacy_main4() -> List[Note]:
    modulus_0 = [4, 14]
    shift_0 = [0, 0]
    spans_0 = [0.5, 1.25]
    direction_0 = [40, 70]
    modulus_1 = [6, 9]
    shift_1 = [0, 0]
    spans_1 = [0.75, 1.5]
    direction_1 = [40, 70]
    order = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
    order2 = [
        0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
        0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
    ]

    snotes_a = _generate_snotes(1, modulus_0, shift_0, spans_0, direction_0)
    snotes_b = _generate_snotes(1, modulus_1, shift_1, spans_1, direction_1)
    section_a = to_notes(snotes_a)
    section_b = to_notes(snotes_b)
    section_c = to_notes(interpolate([snotes_a, snotes_b], order))
    direction_0 = [44, 74]
    direction_1 = [44, 74]
    snotes_c = _generate_snotes(2, modulus_0, shift_0, spans_0, direction_0)
    snotes_d = _generate_snotes(2, modulus_1, shift_1, spans_1, direction_1)
    section_d = to_notes(interpolate([snotes_c, snotes_d], order2))
    return concatenate_sections(
        [Section(section_a), Section(section_b), Section(section_c), Section(section_d)]
    )


def legacy_main5() -> List[Note]:
    modulus_0 = [12, 4, 8, 12]
    shift_0 = [0, 3, 1, 6]
    spans_0 = [1, 0.33333, 0.25, 1.5]
    direction_0 = [48, 73]
    modulus_1 = [6, 8]
    shift_1 = [0, 0]
    spans_1 = [0.75, 0.33333]
    direction_1 = [73, 48]
    order = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]

    snotes_0 = _generate_snotes(1, modulus_0, shift_0, spans_0, direction_0)
    snotes_1 = _generate_snotes(1, modulus_1, shift_1, spans_1, direction_1)
    combined = interpolate([snotes_0, snotes_1], order)
    expanded = expandSnotes(combined, combined, -39, 39)
    return to_notes(expanded)


def legacy_main6() -> List[Note]:
    modulus_0 = [4, 5]
    shift_0 = [4, 1]
    spans_0 = [0.333, 0]
    direction_0 = [52, 62]
    modulus_1 = [6, 3]
    shift_1 = [3, 0]
    spans_1 = [0.75, 0.25]
    direction_1 = [52, 62]
    order = [1, 0, 0, 1, 1]

    snotes_0 = _generate_snotes(1, modulus_0, shift_0, spans_0, direction_0)
    snotes_1 = _generate_snotes(1, modulus_1, shift_1, spans_1, direction_1)
    combined = interpolate([snotes_0, snotes_1], order)
    expanded = expandSnotesNoSpan(combined, combined, -100, 100)
    return to_notes(expanded)


def legacy_main7() -> List[Note]:
    modulus_0 = [4, 5]
    shift_0 = [3, 2]
    spans_0 = [0.5, 1.0]
    direction_0 = [40, 60]
    modulus_1 = [6, 3]
    shift_1 = [3, 1]
    spans_1 = [0.75, 0.25]
    direction_1 = [50, 20]
    modulus_2 = [5, 7, 10]
    shift_2 = [2, 3, 5]
    spans_2 = [0.333, 0.3333, 1.25]
    direction_2 = [10, 50]
    order = [
        1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
        0, 1, 0, 1, 0, 1, 0, 0, 0, 1,
    ]

    snotes_0 = _generate_snotes(2, modulus_0, shift_0, spans_0, direction_0)
    snotes_1 = _generate_snotes(1, modulus_1, shift_1, spans_1, direction_1)
    snotes_2 = _generate_snotes(1, modulus_2, shift_2, spans_2, direction_2)
    snotes_3 = expandSnotesNoSpan(snotes_2, snotes_0, -25, 10)
    snotes_4 = interpolate([snotes_3, snotes_1], order)
    modulus_2b = [5, 7, 10]
    shift_2b = [2, 3, 5]
    spans_2b = [0.333, 0.3333, 1.0]
    direction_2b = [30, 70]
    snotes_5 = _generate_snotes(1, modulus_2b, shift_2b, spans_2b, direction_2b)

    section_a = to_notes(snotes_0, tritones=True)
    section_b = to_notes(snotes_1)
    section_c = to_notes(snotes_5, tritones=True)
    section_d = to_notes(snotes_4)
    section_e = to_notes(snotes_3) + to_notes(snotes_0, tritones=True)

    return concatenate_sections(
        [
            Section(section_a),
            Section(section_b),
            Section(section_c),
            Section(section_d, pause=0.25),
            Section(section_e),
        ]
    )


def legacy_main8() -> List[Note]:
    modulus_0 = [5, 6, 10]
    shift_0 = [2, 2, 8]
    spans_0 = [0.333, 0.3333, 0]
    modulus_1 = [6, 6, 7]
    shift_1 = [4, 7, 0]
    spans_1 = [0.75, 0.75, 0.25]

    def build_pair(direction_0, direction_1, *, tritones: bool = False) -> List[Note]:
        snotes_a = _generate_snotes(1, modulus_0, shift_0, spans_0, direction_0)
        snotes_b = _generate_snotes(1, modulus_1, shift_1, spans_1, direction_1)
        return to_notes(snotes_a, tritones=tritones) + to_notes(snotes_b, tritones=tritones)

    sections = [
        Section(build_pair([80, 26], [30, 70])),
        Section(build_pair([50, 60], [60, 50]), pause=0.6),
        Section(build_pair([30, 80], [70, 30], tritones=True)),
    ]

    # Layered textures with offsets
    snotes_0 = _generate_snotes(1, modulus_0, shift_0, spans_0, [0, 88])
    snotes_1 = _generate_snotes(1, modulus_1, shift_1, spans_1, [88, 0])
    notes_2 = to_notes(expandSnotesNoSpan(snotes_0, snotes_1, -20, 0))[:30]

    snotes_0b = _generate_snotes(1, modulus_0, shift_0, spans_0, [0, 50])
    notes_0b = to_notes(snotes_0b)
    end_time = notes_0b[-1].time + notes_0b[-1].dur
    snotes_1c = _generate_snotes(1, modulus_1, shift_1, spans_1, [20, 88])
    notes_1c = snotesToNotesWithOffset(snotes_1c, end_time)
    sections.append(Section(notes_2 + notes_0b + notes_1c))

    spans_0c = [0.75, 0.5, 1.2]
    direction_0c = [45, 55]
    spans_1c = [0.75, 0.75, 0.2]
    direction_1c = [50, 40]
    order = [0, 1, 1, 0, 1, 0, 0]
    snotes_a = _generate_snotes(1, modulus_0, shift_0, spans_0c, direction_0c)
    snotes_b = _generate_snotes(1, modulus_1, shift_1, spans_1c, direction_1c)
    snotes_c = interpolate([snotes_a, snotes_b], order)
    snotes_d = expandSnotes(snotes_c, snotes_c, -60, 60)
    snotes_d = expandSnotesNoSpan(snotes_d, snotes_c, -60, 60)
    notes_layer = to_notes(snotes_d[300:342])

    modulus_extra = [12, 12, 12]
    shift_extra = [3, 7, 10]
    spans_extra = [1, 1, 1]
    direction_extra = [3, 28]
    notes_extra = to_notes(_generate_snotes(1, modulus_extra, shift_extra, spans_extra, direction_extra))

    modulus_extra2 = [12, 12, 12]
    shift_extra2 = [7, 7, 7]
    spans_extra2 = [1, 5, 8]
    direction_extra2 = [57, 30]
    snotes_extra2 = _generate_snotes(1, modulus_extra2, shift_extra2, spans_extra2, direction_extra2)
    offset_extra = notes_extra[-1].time + notes_extra[-1].dur
    notes_extra2 = snotesToNotesWithOffset(snotes_extra2, offset_extra)

    sections.append(Section(notes_layer + notes_extra + notes_extra2))

    return concatenate_sections(sections)


def legacy_main9() -> List[Note]:
    from Comp import Comp_4

    composition = Comp_4(1, "melodic", 1001)
    return to_notes(composition.run(), tritones=True)


def legacy_main10() -> List[Note]:
    from Comp import Comp_8

    composition = Comp_8(2, "major", 1001)
    return to_notes(composition.run(), tritones=True)


def legacy_main11() -> List[Note]:
    from Comp import Comp_7

    composition = Comp_7(4, "melodic", 1001)
    return to_notes(composition.run(), tritones=True)


def legacy_main12() -> List[Note]:
    from Comp import Comp_1

    composition = Comp_1(0, "melodic", 1001)
    return to_notes(composition.run(), tritones=True)
