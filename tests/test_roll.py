import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import roll  # noqa: E402


class rollTests(unittest.TestCase):
    def test_roll(self):
        for i in range(1000):
            pigs = roll.roll()
            self.assertEqual(len(pigs), 2)
            sides = ('pink', 'dot', 'razorback',
                     'trotter', 'snouter', 'jowler',)
            self.assertTrue(all(pig in sides for pig in pigs))

    def test_is_bust(self):
        self.assertTrue(roll.is_bust(['pink', 'dot']))
        self.assertTrue(roll.is_bust(['dot', 'pink']))

    def test_calculate(self):
        tests = [(['pink', 'pink'], 1),
                 (['dot', 'dot'], 1),
                 (['pink', 'razorback'], 5),
                 (['trotter', 'dot'], 5),
                 (['pink', 'snouter'], 10),
                 (['jowler', 'dot'], 15),
                 ]
        for test in tests:
            pigs, score = test[0], test[1]
            self.assertEqual(roll.calculate(pigs), score)
