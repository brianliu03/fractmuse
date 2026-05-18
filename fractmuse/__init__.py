"""FractMuse modernized interface."""

from .cli import main
from .compositions.registry import COMPOSITIONS, list_compositions, get_composition
from .core import Motif, Note, NoteScale

__all__ = [
    "COMPOSITIONS",
    "Motif",
    "Note",
    "NoteScale",
    "get_composition",
    "list_compositions",
    "main",
]
