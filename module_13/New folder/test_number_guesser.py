

import unittest
from number_guesser import NumberGuesser

class TestNumberGuesser(unittest.TestCase):

    def setUp(self):
        self.guesser = NumberGuesser()

    def tearDown(self):
        del self.guesser

    def test_constructor(self):
        self.assertEqual(self.guesser.guessed_list, [])

    def test_add_guess(self):
        self.guesser.add_guess(3)
        self.guesser.add_guess(7)
        self.assertEqual(self.guesser.guessed_list, [3, 7])

if __name__ == '__main__':
    unittest.main()
