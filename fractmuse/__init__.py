"""FractMuse modernized interface."""

from .cli import main
from .compositions.registry import COMPOSITIONS, list_compositions, get_composition

__all__ = ["COMPOSITIONS", "list_compositions", "get_composition", "main"]
