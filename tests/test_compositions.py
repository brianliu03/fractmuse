import unittest
from pathlib import Path

from fractmuse.compositions.registry import CompositionContext, get_composition, list_compositions


class CompositionTests(unittest.TestCase):
    def test_registry_lists_legacy_and_markov_compositions(self):
        names = {composition.name for composition in list_compositions()}

        self.assertIn("legacy/main3", names)
        self.assertIn("legacy/main10", names)
        self.assertIn("markov/mozart", names)

    def test_legacy_compositions_keep_expected_shape(self):
        context = CompositionContext(project_root=Path.cwd())

        main3 = get_composition("legacy/main3").build(context)
        main10 = get_composition("legacy/main10").build(context)

        self.assertEqual(len(main3), 17)
        self.assertEqual((main3[0].time, main3[0].pitch, main3[0].vel), (0.0, -29, 60))
        self.assertEqual(len(main10), 81)
        self.assertEqual((main10[0].time, main10[0].pitch, main10[0].vel), (0.0, 2, 41.0))


if __name__ == "__main__":
    unittest.main()
