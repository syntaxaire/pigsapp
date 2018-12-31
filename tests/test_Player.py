import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import Player  # noqa: E402


class rollTests(unittest.TestCase):
    def test_Player(self):
        p1 = Player.Player(100)
        p2 = Player.Player(100)
        p1.reg_opponent(p2)
        p2.reg_opponent(p1)
        for i in range(4):
            self.assertFalse(p1.process_roll(['dot', 'snouter']) == 'win')
            self.assertFalse(p1.process_roll(['pink', 'snouter']) == 'win')
        self.assertEqual(p1.process_roll(['trotter', 'trotter']), 'win')
        p1.__init__(200)
        p2.__init__(200)
        self.assertEqual(p1.score, 0)
        self.assertEqual(p1.to_score, 200)
        self.assertEqual(p2.to_score, 200)
        for i in range(3):
            self.assertFalse(p2.process_roll(['jowler', 'jowler']) == 'win')
        self.assertEqual(p2.process_roll(['jowler', 'jowler']), 'win')
        self.assertEqual(p1.opponent.score, 240)
