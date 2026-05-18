"""MIDI file and playback adapters."""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

from fractmuse.core.notes import MidiEvent, Note, clamp_midi_value

LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True)
class MidiPortConfig:
    preferred_names: Sequence[str] = ()


def write_midi_file(path: Path, notes: Sequence[Note], *, tempo: int = 60) -> None:
    try:
        from mido import Message, MetaMessage, MidiFile, MidiTrack, bpm2tempo, second2tick
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "MIDI file output requires the `mido` package. Run `pip install -e .`."
        ) from exc

    ticks_per_beat = 480
    midi = MidiFile(ticks_per_beat=ticks_per_beat)
    track = MidiTrack()
    midi.tracks.append(track)
    track.append(MetaMessage("set_tempo", tempo=bpm2tempo(tempo), time=0))

    events = sorted(_notes_to_mido_events(notes), key=lambda event: event.time)
    current_time = 0.0
    for event in events:
        delta_seconds = max(0.0, event.time - current_time)
        delta_ticks = int(round(second2tick(delta_seconds, ticks_per_beat, bpm2tempo(tempo))))
        track.append(
            Message(
                "note_on" if event.on_off else "note_off",
                note=clamp_midi_value(event.pitch),
                velocity=clamp_midi_value(event.vel),
                channel=clamp_midi_value(event.chan - 1, low=0, high=15),
                time=delta_ticks,
            )
        )
        current_time = event.time

    path.parent.mkdir(parents=True, exist_ok=True)
    midi.save(path)
    LOGGER.info("Wrote MIDI file to %s", path)


def read_note_on_events(path: Path) -> tuple[list, list[float]]:
    try:
        from mido import MidiFile
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "MIDI file input requires the `mido` package. Run `pip install -e .`."
        ) from exc

    midi = MidiFile(str(path), clip=True)
    messages = []
    times: list[float] = []
    current = 0.0
    for message in midi:
        current += message.time
        if message.type == "note_on" and getattr(message, "velocity", 0) > 0:
            messages.append(message)
            times.append(current)
    return messages, times


def play_timed_notes(notes: Iterable[Note], config: MidiPortConfig) -> None:
    try:
        import mido
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "MIDI playback requires mido with a port backend. Run `pip install -e .[playback]`."
        ) from exc

    port_name = _resolve_output_port(mido.get_output_names(), config.preferred_names)
    with mido.open_output(port_name) as output:
        current_time = 0.0
        for event in sorted(_notes_to_midi_events(notes), key=lambda item: item.time):
            if event.time > current_time:
                time.sleep(event.time - current_time)
                current_time = event.time
            output.send(_to_mido_message(event))


def _resolve_output_port(available_ports: Sequence[str], preferred_names: Sequence[str]) -> str:
    if not available_ports:
        raise RuntimeError("No MIDI output ports are available")

    for preferred in preferred_names:
        for port in available_ports:
            if preferred in port:
                return port

    if preferred_names:
        LOGGER.warning(
            "None of the preferred MIDI ports %s were found; using %s",
            preferred_names,
            available_ports[0],
        )
    return available_ports[0]


def _notes_to_midi_events(notes: Iterable[Note]) -> list[MidiEvent]:
    events: list[MidiEvent] = []
    for note in notes:
        events.extend(note.to_raws())
    return events


def _notes_to_mido_events(notes: Iterable[Note]) -> list[MidiEvent]:
    return _notes_to_midi_events(notes)


def _to_mido_message(event: MidiEvent):
    from mido import Message

    return Message.from_bytes(event.to_message())
