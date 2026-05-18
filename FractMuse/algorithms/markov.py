"""Markov-chain generators used by MIDI-derived compositions."""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Sequence


def _empty_table(size: int) -> list[list[float]]:
    return [[0.0 for _ in range(size)] for _ in range(size)]


def _empty_table_3d(size: int) -> list[list[list[float]]]:
    return [[[0.0 for _ in range(size)] for _ in range(size)] for _ in range(size)]


@dataclass
class MarkovGenerator:
    totalGenerations: int
    sizeTable: int
    order: int
    offset: int
    rng: random.Random = field(default_factory=random.Random)

    def __post_init__(self) -> None:
        self.sizeTables = self.sizeTable
        if self.order == 1:
            self.probabilities = _empty_table(self.sizeTable)
        elif self.order == 2:
            self.probabilities = _empty_table_3d(self.sizeTable)
        else:
            raise ValueError("Only first- and second-order Markov chains are supported")

    def _index(self, value: int) -> int:
        index = value - self.offset
        if not 0 <= index < self.sizeTable:
            raise ValueError(f"Value {value} is outside table range for offset {self.offset}")
        return index

    @staticmethod
    def _normalize_rows(table: list[list[float]]) -> None:
        for row in table:
            total = sum(row)
            if total:
                for index, value in enumerate(row):
                    row[index] = value / total

    def generateTable(self, values: Sequence[int]) -> None:
        for first, second in zip(values, values[1:], strict=False):
            self.probabilities[self._index(first)][self._index(second)] += 1
        self._normalize_rows(self.probabilities)

    def generateTableSpans(self, values: Sequence[float]) -> None:
        encoded = [int(round(value, 2) * 100) for value in values]
        self.generateTable(encoded)

    def generateTable3d(self, values: Sequence[int]) -> None:
        if self.order != 2:
            raise ValueError("generateTable3d requires order=2")

        for first, second, third in zip(values, values[1:], values[2:], strict=False):
            self.probabilities[self._index(first)][self._index(second)][self._index(third)] += 1

        for first_layer in self.probabilities:
            for row in first_layer:
                total = sum(row)
                if total:
                    for index, value in enumerate(row):
                        row[index] = value / total

    def createComp(self, start: int) -> list[int]:
        current = self._index(start)
        output = [current + self.offset]
        for _ in range(self.totalGenerations):
            next_index = self._weighted_choice(self.probabilities[current])
            if next_index is None:
                break
            output.append(next_index + self.offset)
            current = next_index
        return output

    def createComp3d(self, start: int) -> list[int]:
        if self.order != 2:
            raise ValueError("createComp3d requires order=2")

        current = self._index(start)
        output = [current + self.offset]
        previous = current
        for _ in range(self.totalGenerations):
            next_index = self._weighted_choice(self.probabilities[previous][current])
            if next_index is None:
                break
            output.append(next_index + self.offset)
            previous, current = current, next_index
        return output

    def _weighted_choice(self, probabilities: Sequence[float]) -> int | None:
        draw = self.rng.random()
        cumulative = 0.0
        for index, probability in enumerate(probabilities):
            cumulative += probability
            if draw <= cumulative:
                return index
        return None
