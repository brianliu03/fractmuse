"""Command-line interface for FractMuse compositions."""

from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Iterable, Sequence

from fractmuse.core.notes import Note
from fractmuse.io.midi import MidiPortConfig, play_timed_notes, write_midi_file

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
    write_midi_file(path, notes)


def _play(notes: Iterable[Note], ports: Sequence[str]) -> None:
    play_timed_notes(notes, MidiPortConfig(ports))


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
        try:
            composition = get_composition(args.name)
        except KeyError as exc:
            parser.exit(1, f"error: {exc}\n")
        context = CompositionContext(project_root=project_root, midi_file=args.midi_file)
        try:
            notes = composition.build(context)

            if args.output:
                _write_midi_file(args.output, notes)

            if not args.no_play:
                _play(notes, args.port)
        except RuntimeError as exc:
            parser.exit(1, f"error: {exc}\n")

        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
