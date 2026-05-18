"""Compatibility imports for historical scripts.

New code should import from :mod:`fractmuse.core.scales`.
"""

from fractmuse.core.scales import NoteScale, Scale, ScaleName, pitch_for_degree

__all__ = ["NoteScale", "Scale", "ScaleName", "pitch_for_degree"]
