"""Compatibility wrapper for historical MIDI interface imports.

New code should import from :mod:`fractmuse.io.midi`.
"""

from __future__ import annotations

from pathlib import Path
import time
from typing import Iterable, Sequence

from fractmuse.algorithms.expand import snotes_to_notes
from fractmuse.core.notes import MidiEvent, Note
from fractmuse.io.midi import MidiPortConfig, play_timed_notes, write_midi_file


class MidiInterface:
    """Historical class API backed by the package-level MIDI adapter."""

    def __init__(self, config: MidiPortConfig):
        self.config = config

    def close(self) -> None:
        return None

    def __enter__(self) -> "MidiInterface":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def play_raw(self, events: Iterable[MidiEvent]) -> None:
        from mido import Message, get_output_names, open_output

        from fractmuse.io.midi import _resolve_output_port

        port_name = _resolve_output_port(get_output_names(), self.config.preferred_names)
        current_time = 0.0
        with open_output(port_name) as output:
            for event in sorted(events, key=lambda item: item.time):
                if event.time > current_time:
                    time.sleep(event.time - current_time)
                    current_time = event.time
                output.send(Message.from_bytes(event.to_message()))

    def play_snotes(self, notes: Sequence[Note]) -> None:
        self.play_notes(snotes_to_notes(notes))

    def play_notes(self, notes: Iterable[Note]) -> None:
        play_timed_notes(notes, self.config)

    def create_file(self, notes: Sequence[Note]) -> None:
        write_midi_file(Path("comp.mid"), notes)


__all__ = ["MidiInterface", "MidiPortConfig"]
