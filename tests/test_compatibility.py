import unittest

from Note import Note
from Motif import Motif
from NoteScale import NoteScale
from algorithms.Markov_Algo import MarkovGenerator
from algorithms.algo import snotesToNotes


class CompatibilityTests(unittest.TestCase):
    def test_historical_import_paths_still_work(self):
        note = Note(None, 0.25, 0, 60, span=1)
        motif = Motif([1], [1], [1])
        scaled = NoteScale(None, 0.25, 0, 60, scale=("major", 60))
        generator = MarkovGenerator(1, 2, 1, 0)

        self.assertEqual(snotesToNotes([note])[0].time, 0.0)
        self.assertEqual(len(motif), 1)
        self.assertEqual(scaled.to_raws()[0].pitch, 60)
        self.assertEqual(generator.sizeTables, 2)


if __name__ == "__main__":
    unittest.main()
