"""Utilities for interacting with MIDI devices and files."""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from typing import Iterable, List, Sequence

import rtmidi

from algorithms.algo import snotesToNotes
from Note import Raw

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class MidiPortConfig:
    """Configuration for selecting a MIDI output port."""

    preferred_names: Sequence[str]


class MidiInterface:
    """High-level wrapper around :mod:`rtmidi` with helpful defaults."""

    def __init__(self, config: MidiPortConfig):
        self._midi_out = rtmidi.MidiOut()
        self._port_index = self._resolve_port(config.preferred_names)
        self._midi_out.open_port(self._port_index)

    def _resolve_port(self, preferred_names: Sequence[str]) -> int:
        available_ports = self._midi_out.get_ports()
        if not available_ports:
            raise RuntimeError("No MIDI output ports are available")

        logger.debug("Available MIDI ports: %s", available_ports)
        if preferred_names:
            for index, name in enumerate(available_ports):
                if name in preferred_names:
                    logger.info("Using MIDI port: %s", name)
                    return index
            logger.warning(
                "None of the preferred MIDI ports %s were found; using %s",
                preferred_names,
                available_ports[0],
            )
        else:
            logger.info("No preferred MIDI ports provided; using %s", available_ports[0])
        return 0

    def close(self) -> None:
        if self._midi_out.is_port_open():
            self._midi_out.close_port()

    def __enter__(self) -> "MidiInterface":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def play_raw(self, events: Iterable[Raw]) -> None:
        ordered = sorted(events, key=lambda event: event.time)
        current_time = 0.0
        for event in ordered:
            target_time = event.time
            if target_time > current_time:
                time.sleep(target_time - current_time)
                current_time = target_time
            self._midi_out.send_message(event.to_message())

    def play_snotes(self, notes) -> None:
        self.play_notes(snotesToNotes(notes))

    def play_notes(self, notes) -> None:
        events: List[Raw] = []
        for note in notes:
            events.extend(note.to_raws())
        self.play_raw(events)

    def create_file(self, notes) -> None:
        from midiutil import MIDIFile

        midi = MIDIFile(1)
        track = 0
        channel = 0
        midi.addTempo(track, 0, 60)

        for note in notes:
            midi.addNote(track, channel, note.pitch + 21, note.time, note.dur, note.vel)

        with open("comp.mid", "wb") as output_file:
            midi.writeFile(output_file)
