"""Composition algorithms."""

from .expand import (
    ExpansionOptions,
    add_distribution,
    expand,
    expand_notes,
    expand_rand,
    expand_snotes,
    expand_snotes_no_span,
    interpolate,
    revert_mid_c,
    set_mid_c,
    snotes_to_notes,
    snotes_to_notes_tritones,
    snotes_to_notes_with_offset,
)
from .markov import MarkovGenerator

__all__ = [
    "ExpansionOptions",
    "MarkovGenerator",
    "add_distribution",
    "expand",
    "expand_notes",
    "expand_rand",
    "expand_snotes",
    "expand_snotes_no_span",
    "interpolate",
    "revert_mid_c",
    "set_mid_c",
    "snotes_to_notes",
    "snotes_to_notes_tritones",
    "snotes_to_notes_with_offset",
]
