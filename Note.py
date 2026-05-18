"""Compatibility imports for historical scripts.

New code should import from :mod:`fractmuse.core.notes`.
"""

from fractmuse.core.notes import MidiEvent, Note, Raw, TimedNote

__all__ = ["MidiEvent", "Note", "Raw", "TimedNote"]
