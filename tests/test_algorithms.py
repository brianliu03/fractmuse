import unittest

from fractmuse.algorithms.expand import expand, interpolate, snotes_to_notes
from fractmuse.algorithms.markov import MarkovGenerator
from fractmuse.core.motif import Motif
from fractmuse.core.notes import Note


class AlgorithmTests(unittest.TestCase):
    def test_snotes_to_notes_uses_spans_as_timeline(self):
        notes = [
            Note(None, 0.25, 0, 60, span=0.5),
            Note(None, 0.25, 2, 60, span=1.25),
        ]

        rendered = snotes_to_notes(notes)

        self.assertEqual([note.time for note in rendered], [0.0, 0.5])
        self.assertEqual([note.pitch for note in rendered], [0, 2])

    def test_expand_applies_motif_and_pitch_bounds(self):
        base = [Note(None, 0.25, 0, 60, span=1.0)]
        motif = Motif([1, 99], [0.5, 0.5], [10, 10])

        expanded = expand(base, motif, True, True, True, 0)

        self.assertEqual(len(expanded), 1)
        self.assertEqual(expanded[0].pitch, 1)
        self.assertEqual(expanded[0].span, 0.5)
        self.assertEqual(expanded[0].vel, 70)

    def test_interpolate_consumes_groups_in_order(self):
        group_a = [Note(None, 0.25, 1, 60, span=1)]
        group_b = [Note(None, 0.25, 2, 60, span=1), Note(None, 0.25, 3, 60, span=1)]

        output = interpolate([group_a, group_b], [1, 0, 1])

        self.assertEqual([note.pitch for note in output], [2, 1, 3])

    def test_markov_generator_has_no_numpy_dependency(self):
        generator = MarkovGenerator(totalGenerations=4, sizeTable=4, order=1, offset=0)
        generator.generateTable([0, 1, 2, 3])

        output = generator.createComp(0)

        self.assertEqual(output, [0, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()
