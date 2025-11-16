"""Command-line interface for FractMuse compositions."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Iterable, Sequence, TYPE_CHECKING

from Note import Note

if TYPE_CHECKING:  # pragma: no cover - imported lazily for optional dependencies
    from Midi_Interface import MidiInterface, MidiPortConfig

from .compositions.registry import CompositionContext, get_composition, list_compositions

LOGGER = logging.getLogger(__name__)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FractMuse composition runner")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List available compositions")

    run = subparsers.add_parser("run", help="Render and optionally play a composition")
    run.add_argument("name", help="Composition name (see `fractmuse list`)")
    run.add_argument("--midi-file", type=Path, help="Override MIDI source for Markov compositions")
    run.add_argument(
        "--port",
        action="append",
        default=[],
        help="Preferred MIDI output port (may be provided multiple times)",
    )
    run.add_argument("--output", type=Path, help="Write composition to MIDI file")
    run.add_argument("--no-play", action="store_true", help="Skip real-time playback")

    return parser


def _write_midi_file(path: Path, notes: Sequence[Note]) -> None:
    from midiutil import MIDIFile

    midi = MIDIFile(1)
    midi.addTempo(0, 0, 60)
    for note in notes:
        midi.addNote(0, 0, note.pitch + 21, note.time or 0.0, note.dur, note.vel)
    with path.open("wb") as handle:
        midi.writeFile(handle)
    LOGGER.info("Wrote MIDI file to %s", path)


def _play(notes: Iterable[Note], ports: Sequence[str]) -> None:
    from Midi_Interface import MidiInterface, MidiPortConfig

    config = MidiPortConfig(ports)
    with MidiInterface(config) as interface:
        interface.play_notes(notes)


def main(argv: Sequence[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO)
    parser = _build_parser()
    args = parser.parse_args(argv)

    project_root = Path(__file__).resolve().parent.parent

    if args.command == "list":
        for composition in list_compositions():
            suffix = " (requires MIDI file)" if composition.requires_midi else ""
            print(f"{composition.name}{suffix}: {composition.description}")
        return 0

    if args.command == "run":
        composition = get_composition(args.name)
        context = CompositionContext(project_root=project_root, midi_file=args.midi_file)
        notes = composition.build(context)

        if args.output:
            _write_midi_file(args.output, notes)

        if not args.no_play:
            _play(notes, args.port)

        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
